import os

import pygst
try:
    pygst.require("0.10")
except:
    print("pyGST 0.10 not available")
    sys.exit(1)
    
import gst

from media_player_error import *

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

class GstCore(MediaPlayerCore):
    """
    An implementation of MediaPlayerCore using GStreamer.
    """
    
    def __init__(self, parent):
        #super(MediaPlayerCore, self).__init__(parent)
        MediaPlayerCore.__init__(self, parent)
        
        # the component that does the actual playing
        self._player = gst.element_factory_make("playbin", "player")
        self._player.set_state(gst.STATE_NULL)
        
        # send any video to a black hole
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        self._player.set_property("video-sink", fakesink)
        
        # Set up the bus
        bus = self._player.get_bus()
        bus.add_signal_watch() # tell the bus that it is being watched
        bus.connect("message", self._on_message)
        
        self._current_file = None
        
    def play(self):
        """
        Tell the player to play the current file.
        """
        try:
            self.set_current_file(self._parent.get_filepath())
        except InvalidFilepathError:
            self._parent.show_message("Please enter a valid filepath.")
            raise
            
        self._player.set_property("uri", "file://" + self._current_file)
        self._player.set_state(gst.STATE_PLAYING)
        self._parent.notify_playing()
        
    def stop(self):
        """
        Stop playing the current file.
        """
        self._player.set_state(gst.STATE_NULL)
        self._parent.notify_stopped()
        
        
    def set_current_file(self, file):
        """
        Sets the current file.
        """
        if os.path.isfile(file):
            self._current_file = file
        else:
            raise InvalidFilepathError()
            
    def _on_message(self, bus, message):
        """
        Actions carried out when the bus sends a message.
        
        Currently responds to gst.MESSAGE_EOS and gst.MESSAGE_ERROR
        """
        t = message.type
        
        if t == gst.MESSAGE_EOS:
            self._on_message_eos(bus, message)
        elif t == gst.MESSAGE_ERROR:
            self._on_message_error(bus, message)
            
    def _on_message_eos(self, bus, message):
        """
        Function called when the eos message is sent.
        """
        self._player.set_state(gst.STATE_NULL)
        
    def _on_message_error(self, bus, message):
        """
        Function called when the bus sends an error message.
        """
        self._player.set_state(gst.STATE_NULL)
        err, debug = message.parse_error()
        print "Error : %s," %err, debug
