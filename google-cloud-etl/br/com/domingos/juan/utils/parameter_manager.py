import logging

class ParameterManager:
    
    def __init__(self, args):
        self.__LOGGER = logging.getLogger('ParameterManager')
        self.__LOGGER.info("Getting application parameters")

        for argument in args:
            name = argument.split(":")[0]
            value = argument.split(":")[1]

            setattr(self, name, value)

        pass

    def get(self, parameter):
        try:
            return getattr(self, parameter.value)
        except:
            return None
