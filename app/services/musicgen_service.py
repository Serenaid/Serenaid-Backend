''' This module contains the MusicGenService class, which represents a music generation service.

The MusicGenService class provides methods to initialize the model and processor resources,
and generate audio based on input description and duration.

Example:

    # Create an instance of the MusicGenService class
    music_gen_service = MusicGenService()

    # Generate audio based on input description and duration
    audio, sampling_rate = music_gen_service.generate_audio("Piano melody", duration=60)

Attributes:
    _instance (MusicGenService): The singleton instance of the MusicGenService class.

Contributors:
    - Sam Sui
'''

# Standard library
import logging

# Third-party libraries
from transformers import AutoProcessor, MusicgenForConditionalGeneration

logger = logging.getLogger(__name__)

class MusicGenService:
    ''' A class that represents a music generation service.

    This class provides methods to initialize the model and processor resources,
    and generate audio based on input description and duration.

    Attributes:
        _instance (MusicGenService): The singleton instance of the MusicGenService class.

    '''

    _instance = None

    def __new__(cls):
        ''' Creates a new instance of the MusicGenService class if it doesn't exist.

        Returns:
            MusicGenService: The singleton instance of the MusicGenService class.

        Raises:
            RuntimeError: If initialization fails.
        '''

        if cls._instance is None:
            try:
                cls._instance = super(MusicGenService, cls).__new__(cls)
                cls._instance.init_resources()
            except Exception as e:
                logger.exception("Failed to initialize MusicGenService resources")
                cls._instance = None 
                raise RuntimeError(f"Initialization failed: {e}")
        return cls._instance

    def init_resources(self):
        '''
        Initializes the model and processor resources.
        '''

        self.processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
        self.model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
        self.model.eval()  # Set the model to evaluation mode

    def generate_audio(self, input_description: str, duration: int=30):
        ''' Generates audio based on the input description and duration.

        Args:
            input_description (str): Description of the audio content to generate.
            duration (int): The duration to control the length of the generated audio.

        Returns:
            tuple: A tuple containing the audio tensor and the sampling rate.

        Raises:
            Exception: Propagates any exceptions that occur during audio generation.
        '''

        try:
            sampling_rate = self.model.config.audio_encoder.sampling_rate
            inputs = self.processor(
                text=[input_description],
                padding=True,
                return_tensors="pt"
            )
            audio_values = self.model.generate(**inputs, max_new_tokens=duration*60)
            return audio_values, sampling_rate
        except Exception as e:
            logger.error(f"Error during audio generation: {str(e)}")
            raise e