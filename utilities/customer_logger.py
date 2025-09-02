import logging
import inspect
import os


class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',
        'INFO': '\033[92m',
        'WARNING': '\033[93m',
        'ERROR': '\033[91m',
        'CRITICAL': '\033[95m',
        'ENDC': '\033[0m'
    }

    def format(self, record):
        log_level = record.levelname
        msg = super().format(record)
        return f"{self.COLORS.get(log_level, '')}{msg}{self.COLORS['ENDC']}"


class LogGen:
    @staticmethod
    def loggen():
        current_file_name = inspect.stack()[1].filename
        current_file_name = os.path.splitext(os.path.basename(current_file_name))[0]
        logger = logging.getLogger(current_file_name)

        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        log_dir = os.path.join(os.path.dirname(__file__), 'C:\\Users\\hp\\PycharmProjects\\CallTest\\Logs')

        if not os.path.exists(log_dir):
            os.makedev(log_dir)

        log_file_path = os.path.join(log_dir, 'call.log')
        filehandler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :"
                                      "%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        coloured_formatter = ColoredFormatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        console_handler.setFormatter(coloured_formatter)
        logger.addHandler(console_handler)
        return logger
