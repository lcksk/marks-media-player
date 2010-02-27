import pygst
try:
    pygst.require("0.10")
except:
    print("pyGST 0.10 not available")
    sys.exit(1)
    
import gst

def MediaPlayerCore(object):
    """
    A superclass that all MediaPlayer back ends should inherit from.
    It defines the standard interface for these classes.
    """
    
    def __init__(self):
        pass
        
    def play(self):
        raise NotImplementedError
        
    def stop(self):
        raise NotImplementedError
