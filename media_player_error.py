# media_player_error.py
# Media Player Version 6.5
#
# This file contains all custom exceptions for MediaPlayer

class MediaPlayerError(Exception):
    """
    The super class of all MediaPlayer-specific errors.
    """
    def __init__(self, *args):
        super(MediaPlayerError, self).__init__(*args)
        
class ManagerError(MediaPlayerError):
    def __init__(self, *args):
        MediaPlayerError.__init__(self, *args)
        
class InvalidFilepathError(ManagerError):
    """
    Error raised when an entered filepath is invalid
    """
    def __init__(self, *args):
        ManagerError.__init__(self, *args)
        
class NoCurrentFileError(ManagerError):
    """
    Error raised when there is no cuurent file.
    """
    def __init__(self, *args):
        ManagerError.__init__(self, *args)
