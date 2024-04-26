''' This module contains the routes related to music generation in the Serenaid backend application.

The routes defined in this module handle the generation of music based on the provided JSON data.

Contributors:
    - Sam Sui
'''

# Package Modules
from app.controllers import MusicController

# Third-party libraries
from flask import Blueprint, request

music_controller = MusicController()
music_bp = Blueprint('music_bp', __name__)

@music_bp.route('/music', methods=['POST'])
def handle_music_generation():
    ''' Handle the generation of music based on the provided JSON data.

    This function is responsible for generating music based on the JSON data
    provided in the request body. It calls the `generate_music` function from
    the `music_controller` module to perform the actual music generation.

    Returns:
        The generated music as a response.

    Raises:
        None.
    '''
    
    return music_controller.generate_music(request.json)