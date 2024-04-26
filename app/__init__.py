''' This file serves as the initialization module for the Serenaid-Backend Flask application.

It creates and configures the Flask application by registering blueprints and setting up necessary configurations.

The Flask application can be created by calling the `create_app()` function.

Example:
    app = create_app()

Contributors:
    - Sam Sui
'''

# Package Modules
from app.routes import music_bp
from app.routes import health_bp

# Third-party libraries
from flask import Flask

def create_app():
    ''' Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    '''
    
    app = Flask(__name__)

    app.register_blueprint(music_bp, url_prefix='/api')
    app.register_blueprint(health_bp, url_prefix='/api')

    return app
