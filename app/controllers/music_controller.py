''' This module contains the MusicController class, which is responsible for generating music based on provided description and duration.

The MusicController class has the following attributes:
- musicgen_service (MusicGenService): An instance of the MusicGenService class.

The MusicController class has the following methods:
- generate_music(params: dict): Generates music based on the provided description and duration.
- _sanitize_description(description: str): Sanitizes the provided description by removing special characters and replacing spaces with underscores.

Contributors:
    - Sam Sui
'''

# Package Modules
from app.services import MusicGenService

# Standard library
import io
import re

# Third-party libraries
from flask import send_file
import scipy

class MusicController:
    ''' Controller class for generating music based on provided description and duration.

    Attributes:
        musicgen_service (MusicGenService): An instance of the MusicGenService class.

    Methods:
        generate_music: Generates music based on the provided description and duration.
        _sanitize_description: Sanitizes the provided description by removing special characters and replacing spaces with underscores.
    '''

    def __init__(self):
        self.musicgen_service = MusicGenService()

    def generate_music(self, params: dict):
        ''' Generates music based on the provided description and duration.

        Args:
            params (dict): A dictionary containing the request parameters.

        Returns:
            dict: A dictionary containing the generated music file as a response or an error message.

        Raises:
            ValueError: If the description is not provided or if the duration is not a positive integer.
            Exception: If there is an error while generating the audio file.
        '''

        # Check if the description is provided
        if 'description' not in params:
            return {"error": "Description is required."}, 400
        
        description = params['description']
        sanitized_description = self._sanitize_description(description)

        # Check if a duration is provided
        duration = params.get('duration', 30)
        if not isinstance(duration, int) or duration < 1:
            return {"error": "Duration must be a positive integer."}, 400

        try:
            audio_buffer = io.BytesIO() # Create a buffer to store the audio file
            audio_values, sampling_rate = self.musicgen_service.generate_audio(description, duration)
            scipy.io.wavfile.write(
                audio_buffer, 
                rate=sampling_rate, 
                data=audio_values[0, 0].numpy()
            )
            audio_buffer.seek(0) # Reset the buffer position
        except Exception as e:
            print(e)
            return {"error": str(e)}, 500
        
        return send_file(
            audio_buffer,
            mimetype="audio/wav",
            as_attachment=True,
            download_name=f"{sanitized_description}.wav"
        )

    def _sanitize_description(self, description: str):
        ''' Sanitizes the provided description by removing special characters and replacing spaces with underscores.

        Args:
            description (str): The description to be sanitized.

        Returns:
            str: The sanitized description.
        '''

        # Remove special characters and replace spaces with underscores
        sanitized = re.sub(r'[^a-zA-Z0-9]', '', description)
        sanitized = '_'.join(sanitized.split(sep=' '))
        return sanitized[:20]