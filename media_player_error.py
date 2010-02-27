class MediaPlayerError(Exception):
    """
    The super class of all MediaPlayer-specific errors.
    """
    def __init__(self):
        pass
        
class InvalidFilepathError(MediaPlayerError):
    """
    Error raised when an entered filepath is invalid
    """
    def __init__(self):
        super(InvalidFilepathError, self).__init__()
