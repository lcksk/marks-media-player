# media_player_error.py
# Media Player Version 5.7
#
# This file contains all custom exceptions for MediaPlayer

class MediaPlayerError(Exception):
    """
    The super class of all MediaPlayer-specific errors.
    """
    def __init__(self, *args):
        super(MediaPlayerError, self).__init__(*args)
        
class InvalidFilepathError(MediaPlayerError):
    """
    Error raised when an entered filepath is invalid
    """
    def __init__(self, *args):
        super(InvalidFilepathError, self).__init__(*args)
        
class NoCurrentFileError(MediaPlayerError):
    """
    Error raised when there is no cuurent file.
    """
    def __init__(self, *args):
        super(NoCurrentFileError, self).__init__(*args)
