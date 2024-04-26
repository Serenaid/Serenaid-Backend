''' This module defines the health route for the Serenaid Backend application.

The health route provides a simple healthcheck endpoint that can be used to verify the status of the service.

Attributes:
    health_bp (flask.Blueprint): The Blueprint object for the health route.

Contributors:
    - Sam Sui
'''

# Third-party libraries
from flask import Blueprint, jsonify

health_bp = Blueprint('health_bp', __name__)

@health_bp.route('/healthcheck', methods=['GET'])
def handle_healthcheck():
    """
    Handle the healthcheck request.

    Returns:
        A JSON response indicating the service is healthy.

    Examples:
        >>> handle_healthcheck()
        {
            "message": "Service is healthy."
        }

    """
    return jsonify({"message": "Service is healthy."}), 200