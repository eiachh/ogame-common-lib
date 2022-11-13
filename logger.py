from cgi import print_arguments
import platform
import requests

class OBLC_Logger:
    logLevel = 'Info'

    def __init__(self, loglevel, componentName):
        self.componentName = componentName
        if(loglevel == 'Info' or loglevel == 'Debug' or loglevel == 'Init'):
            self.logLevel = loglevel
        else:
            self.logLevel = 'Info'
            self.log(f'Set log level was invalid {loglevel} using default value: {self.logLevel}', 'Warning')

    def setLogLevel(self, loglevel):
        self.logLevel = loglevel

    def getLogLevel(self):
        return self.logLevel

    def shouldBeLogged(self, loglevel):
        if(loglevel == 'Debug' and self.logLevel == 'Info'):
            return False
        return True

    def logMinorInfo(self, message):
        if(self.shouldBeLogged('Minor')):
            self.logConsoleImplementation(message, 'Minor')

    def logMainInfo(self, message):
        if(self.shouldBeLogged('Main')):
            self.logConsoleImplementation(message, 'Main')
            self.logDiscordImplementation(message, 'Main')
        
    def logWarn(self, message):
        if(self.shouldBeLogged('Warn')):
            self.logConsoleImplementation(message, 'Warn')
            self.logDiscordImplementation(message, 'Warn')

    def logError(self, message):
        if(self.shouldBeLogged('Error')):
            self.logConsoleImplementation(message, 'Error')
            self.logDiscordImplementation(message, 'Error')

    def getLogHeaders(self, messageLogLevel):
        return f'[{self.componentName}][{messageLogLevel}]: '

    def logConsoleImplementation(self, message, loglevel):
        print(f'{self.getLogHeaders(loglevel)} {message}')

    def logDiscordImplementation(self, message, loglevel):
        actualMessageToSend = f'{self.getLogHeaders(loglevel)} {message}'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        currPlatform = platform.platform()
        if( not ("Windows" in currPlatform)):
            requests.post("http://modularis.default.svc.cluster.local:5000/RestModuleCall/TargetedCall", data=actualMessageToSend, headers=headers)
        