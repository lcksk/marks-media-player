# mediaplayer.py
# Media Player Version 5.7
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

import gstcore
import gtkinterface
from media_player_error import *
    
class MediaPlayer(object):
    """
    A GUI that plays music files.
    """    
    def __init__(self):
        """
        Create a new MediaPlayer
        """        
        # instance variables
        self._current_file = None
        
        # gstreamer initialization
        self._init_core()
        
        # gtk initialization
        self._init_interface()
        
    def _init_interface(self):
        """
        Initialize the interface of the MediaPlayer.
        """
        self._interface = gtkinterface.GtkInterface(self)
        self._interface.begin()
        
    def _init_core(self):
        """
        Initialize the backend of the MediaPlayer.
        """
        self._core = gstcore.GstCore(self)
        
    def get_filepath(self):
        """
        Retrieve a filepath from the interface."
        """
        # This should eventually be replaced by a call to a class that 
        # deals specifically with managing files.
        return self._interface._file_entry.get_text()
        
    def play(self):
        """
        Tell the player to play the current file.
        """
        try:
            self.set_current_file(self.get_filepath())
        except InvalidFilepathError:
            self._interface.show_message("Please enter a valid filepath.")
            raise
            
        if self._core.play():
            self._interface.notify_playing()
        
    def stop(self):
        """
        Stop playing the current file.
        """
        if self._core.stop():
            self._interface.notify_stopped()
        
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
