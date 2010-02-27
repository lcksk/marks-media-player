# mediaplayerinterface.py
# Media Player Version 5.7
#
# This file contains the abstract class MediaPlayerInterface
    
class MediaPlayerInterface(object):
    """
    A superclass that all MediaPlayer interfaces should inherit from.
    It defines the standard interface for these classes.
    """
    def __init__(self, parent):
        self._parent = parent
        
    def brgin(self):
        """
        Start the interface.
        """
        raise NotImplementedError
        
    def end(self):
        """
        Stop the interface
        """
        
    def show_message(self, message):
        """
        Convey a message to the user.
        """
        raise NotImplementedError
        
    def notify_playing(self):
        """
        Notify the user that a file is being played.
        """
        raise NotImplementedError
        
    def notify_stopped():
        """
        Notify the user that the MediaPlayer has stopped playing.
        """
        raise NotImplemented
