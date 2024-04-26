''' This file serves as the entry point for the Serenaid Backend application.

It imports the create_app function from the app module and defines the main function as the entry point of the application.

Contributors:
    - Sam Sui
'''

from app import create_app
from config import DevelopmentConfig

app = create_app()
app.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
