import pygst
try:
    pygst.require("0.10")
except:
    print("pyGST 0.10 not available")
    sys.exit(1)
    
import gst

def MusicPlayerCore(object):
    def __init__(self):
        pass
        
    def play(self):
        raise NotImplementedError
        
    def stop(self):
        raise NotImplementedError
