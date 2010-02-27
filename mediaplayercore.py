# mediaplayercore.py
# Media Player Verison 5.7
#
# This file contains the abstract class MediaPlayerCore

# Version 5.7

class MediaPlayerCore(object):
    """
    A superclass that all MediaPlayer back ends should inherit from.
    It defines the standard interface for these classes.
    """
    
    def __init__(self, parent):
        self._parent = parent
        
    def play(self):
        raise NotImplementedError
        
    def stop(self):
        raise NotImplementedError
