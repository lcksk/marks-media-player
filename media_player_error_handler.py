class MediaPlayerErrorHandler(object):
    def __init__(self):
        pass
        
    def handle(self, error):
        """
        Determines the appropriate method to call to handle errors.
        """
        pass
        
    def _handle_NoCurrentFileError(self, error):
        pass
        
    def _handle_InvalidFilepathError(self, error):
        pass
