# mediaplayer.py - Version 4.5
#
# This file contains the MediaPlayer class.
#

import sys, os

# import Gimp Toolkit
import gtk
import pygtk
try:
    pygtk.require("2.0")
except:
    print("pyGTK 2.0 not available")
    sys.exit(1)

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
        # gstreamer initialization
        self._init_core()
        
        # gtk initialization
        self._init_interface()
        
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
        
        gtk.main()
        
    def _init_core(self):
        """
        Initialize the backend of the MediaPlayer.
        """
        self._core = cores.GstCore(self)
        
    def _on_play_button_clicked(self, widget, data=None):
        """
        Actions performed when the play button is clicked.
        """
        self.play()
        
    def _on_stop_button_clicked(self, widget, data=None):
        """
        Actions performed when the stop button is clicked.
        """
        self.stop()
        
    def _on_main_window_destroy(self, widget, data=None):
        """
        Actions carried out when the main window is closed.
        """
        gtk.main_quit()
            
    def _on_file_entry_activate(self, widget, data=None):
        """
        Called when file entry sends the activate signal
        """
        self.play()
            
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
            
        self._core.play()
        self.notify_playing()
        
    def stop(self):
        """
        Stop playing the current file.
        """
        if self._core.stop():
            self.notify_stopped()
        
    def get_current_file(self):
        """
        Return the current file.
        """
        return self._current_file
        
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
