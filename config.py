''' Configuration settings for the application.

This module defines the configuration settings for the application. It defines a base configuration class and a development configuration class.

Attributes:
    Config (class): Base configuration class.
    DevelopmentConfig (class): Configuration class for the development environment.

Contributors:
    - Sam Sui
'''

class Config(object):
    ''' Base configuration class.

    This class defines the base configuration settings for the application.

    Attributes:
        DEBUG (bool): Flag indicating whether debug mode is enabled or not.
    '''
    
    DEBUG = True

class DevelopmentConfig(Config):
    ''' Configuration class for the development environment.

    This class defines the configuration settings specific to the development environment.
    It inherits from the base `Config` class.

    Attributes:
        DEBUG (bool): Flag indicating whether debug mode is enabled or not.
    '''

    DEBUG = True