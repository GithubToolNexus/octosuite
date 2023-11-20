def on_call():
    from datetime import datetime

    from . import __version__
    from .coreutils import args, log
    from .executor import Executor
    from .masonry import Masonry
    from .messages import message

    start_time = datetime.now()
    tree_masonry = Masonry()
    executor = Executor(arguments=args, tree_masonry=tree_masonry)

    print(
        """
┏┓    ┏┓  •   
┃┃┏╋┏┓┗┓┓┏┓╋┏┓
┗┛┗┗┗┛┗┛┗┻┗┗┗ """
    )

    try:
        if args.target:
            log.info(
                message(
                    message_type="info",
                    message_key="program_started",
                    program_name="OctoSuite",
                    program_version=__version__,
                    start_time=start_time,
                )
            )
            tree_masonry.api.get_updates()

        executor.execute_cli_arguments()
    except KeyboardInterrupt:
        log.warning(message(message_type="warning", message_key="user_interruption"))
    except Exception as error:
        log.error(
            message(
                message_type="error",
                message_key="unknown_error",
                error_message=error,
            )
        )
    finally:
        log.info(
            message(
                message_type="info",
                message_key="program_stopped",
                run_time=datetime.now() - start_time,
            )
        )
