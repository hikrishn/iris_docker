
import logging
import yaml
import sys

class ConfigHolder:

    configMap = None
    def __init__(self, configFile):
        global configMap
        try:
            with open(configFile, 'r') as file:
                self.configMap = yaml.safe_load(file)
                sys.stdout.write("configMap: {}\n".format(self.configMap))
                file.close()
        except yaml.YAMLError as exc:
            if hasattr(exc, 'problem_mark'):
                if exc.context != None:
                    sys.stdout.write("Error1")
                else:
                    sys.stdout.write("Error2")
            else:
                sys.stdout.write("Error3")

