

class ExceptionHandler:

    def __init__(self):
        pass

    def handle_general_exception(self, msg, error_field, code):
        """
        Return a custom message and 400 status code
        """
        return {'message': msg, 'error': {'field': error_field}}, code

    def handle_validation_exception(selfl, error_field):
        """
        Return a validation fail message and 400 status code
        """
        return {'message': 'Parameter validation fail', 'error': {'field': error_field}}, 400