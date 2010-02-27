import gtk
try:
    import pygtk
    pygtk.require("2.0")
except:
    print("pyGTK 2.0 not available")
    sys.exit(1)

def MusicPlayerInterface(object):
    def __init__(self):
        pass
        
    def show_message(self, message):
        raise NotImplementedError
        
    def notify_playing(self):
        raise NotImplementedError
        
    def notify_stopped():
        raise NotImplemented
