import logging


class LogGeneration:
    
    @staticmethod
    def loggen():

        logging.basicConfig(filename=".\\Logs\\execution.txt",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
