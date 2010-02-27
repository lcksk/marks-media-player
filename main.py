# Version 4

import sys, os

# import Gimp Toolkit
import gtk
import pygtk
try:
    pygtk.require("2.0")
except:
    print("pyGTK 2.0 not available")
    sys.exit(1)
    
# import GStreamer
import pygst
try:
    pygst.require("0.10")
except:
    print("pyGST 0.10 not available")
    sys.exit(1)

import gst

import cores
from media_player_error import *
    
class MediaPlayer(object):
    """
    A GUI that plays music files.
    """
    
    def __init__(self):
        """
        Create a new MediaPlayer
        """
        # gtk initialization
        self._init_interface()
        
        # gstreamer initialization
        self._init_core()
        
        # other
        self._current_file = None
        
    def _init_interface(self):
        """
        Initialize the interface of the MediaPlayer.
        """
        builder = gtk.Builder()
        builder.add_from_file("main_window.glade")
        
        builder.connect_signals(self)
        self._file_entry = builder.get_object("file_entry")
        self._statusbar_label = builder.get_object("statusbar_label")
        
    def _init_core(self):
        """
        Initialize the backend of the MediaPlayer.
        """
        self._core = cores.GstCore(self)
        
    def _on_play_button_clicked(self, widget, data=None):
        """
        Actions performed when the play button is clicked.
        """
        self._core.play()
        
    def _on_stop_button_clicked(self, widget, data=None):
        """
        Actions performed when the stop button is clicked.
        """
        self._core.stop()
        
    def _on_main_window_destroy(self, widget, data=None):
        """
        Actions carried out when the main window is closed.
        """
        gtk.main_quit()
        
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
            
    def _on_file_entry_activate(self, widget, data=None):
        """
        Called when file entry sends the activate signal
        """
        self._core.play()
            
    def show_message(self, message):
        """
        Display any string as a message to the user.
        """
        self._statusbar_label.set_text(message)
        
    def get_filepath(self):
        """
        Retrieve a filepath from the interface."
        """
        return self._file_entry.get_text()
        
    def play(self):
        """
        Tell the player to play the current file.
        """
        try:
            self.set_current_file(self.get_filepath())
        except InvalidFilepathError:
            self.show_message("Please enter a valid filepath.")
            raise
            
        self._player.set_property("uri", "file://" + self._current_file)
        self._player.set_state(gst.STATE_PLAYING)
        self.notify_playing()
        
    def stop(self):
        """
        Stop playing the current file.
        """
        self._player.set_state(gst.STATE_NULL)
        self.notify_stopped()
        
    def set_current_file(self, file):
        """
        Sets the current file.
        """
        if os.path.isfile(file):
            self._current_file = file
        else:
            raise InvalidFilepathError()
    
    def notify_playing(self):
        """
        Notify the user that a file is playing.
        """
        self.show_message("Playing " + self._current_file)
        
    def notify_stopped(self):
        """
        Notify the user that the playing of a file was stopped.
        """
        self.show_message("Stopped")

mp = MediaPlayer()
gtk.main()
