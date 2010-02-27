# mediaplayercore.py
# Media Player Verison 6
#
# This file contains the abstract class MediaPlayerCore

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
