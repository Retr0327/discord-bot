from logging import Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL, LogRecord


class CustomFormatter(Formatter):
    """
    The CustomFormatter object adds color to log messages.
    """

    colors = {
        DEBUG: "\x1b[40;1m",
        INFO: "\x1b[34;1m",
        WARNING: "\x1b[33;1m",
        ERROR: "\x1b[31m",
        CRITICAL: "\x1b[41m",
    }

    default_color = colors[DEBUG]
    fmt = "\x1b[30;1m%(asctime)s\x1b[0m {color}%(levelname)-8s\x1b[0m \x1b[35m%(name)s\x1b[0m -> %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    def __init__(self) -> None:
        super().__init__(fmt=self.fmt, datefmt=self.datefmt)

    def format(self, record: LogRecord) -> str:
        """The format function fromats the log record into a string.

        Returns:
            a str
        """
        color = self.colors.get(record.levelno, self.default_color)
        self._style._fmt = self.fmt.format(color=color)

        if record.exc_info:
            text = self.formatException(record.exc_info)
            record.exc_text = f"\x1b[31m{text}\x1b[0m"

        output = super().format(record)

        # Remove the cache layer
        record.exc_text = None
        return output
