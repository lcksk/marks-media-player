# gstcore.py
# Media Player Version 6

import os

import pygst
try:
    pygst.require("0.10")
except:
    print("pyGST 0.10 not available")
    sys.exit(1)
    
import gst

import mediaplayercore
from media_player_error import *

class GstCore(mediaplayercore.MediaPlayerCore):
    """
    An implementation of MediaPlayerCore using GStreamer.
    """
    
    def __init__(self, parent):
        #super(MediaPlayerCore, self).__init__(parent)
        super(GstCore, self).__init__(parent)
        
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
        
    def play(self):
        """
        Tell the player to play the current file.
        """            
        self._player.set_property("uri", "file://" + 
                self._parent.get_current_file())
        
        try:
            new_state = self._player.set_state(gst.STATE_PLAYING)
        except Error:
            return False
            
        if (new_state == gst.STATE_CHANGE_ASYNC):
            return True
        else:
            return False
        
    def stop(self):
        """
        Stop playing the current file. Does nothing if there isn't 
        anything playing.
        """
        if self._player.get_state()[1] == gst.STATE_PLAYING:
            if (self._player.set_state(gst.STATE_NULL) == 
                    gst.STATE_CHANGE_SUCCESS):
                return True
        
        return False
            
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
        if self._player.set_state(gst.STATE_NULL) == gst.STATE_CHANGE_SUCCESSFUL:
            self._parent._interface.notify_stopped()
        
    def _on_message_error(self, bus, message):
        """
        Function called when the bus sends an error message.
        """
        self._player.set_state(gst.STATE_NULL)
        err, debug = message.parse_error()
        print "Error : %s," %err, debug
