# mediaplayer.py
# Media Player Version 6.5
#
# This file contains the MediaPlayer class.

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
import clinterface
import mediafilemanager
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
        
        # backend initialization
        self._init_core()
        
        # file management initialization
        self._init_manager()
        
        # interface initialization
        self._init_interface()
        
    def _init_interface(self):
        """
        Initialize the interface of the MediaPlayer.
        """
        #self._interface = clinterface.CLInterface(self)
        self._interface = gtkinterface.GtkInterface(self)
        self._interface.begin()
        
    def _init_core(self):
        """
        Initialize the backend of the MediaPlayer.
        """
        self._core = gstcore.GstCore(self)
        
    def _init_manager(self):
        """
        Initialize the file manager.
        """
        self._manager = mediafilemanager.SingleFileManager(self)
        self.add_file("/home/mark/Music/Major_Tom.mp3")#########################################
        
    def play(self):
        """
        Tell the player to play the current file.
        """
        if self._core.play():
            self._interface.notify_playing(self._manager.get_current_file())
        
    def stop(self):
        """
        Stop playing the current file.
        """
        if self._core.stop():
            self._interface.notify_stopped()
            
    def quit(self):
        self._interface.end()
            
    def on_play(self):
        self.play()
    
    def on_stop(self):
        self.stop()
        
    def on_quit(self):
        self.quit()
    
    def get_current_file(self):
        """
        Return the current file.
        """
        return self._manager.get_current_file()
        
    def add_file(self, file):
        try:
            self._manager.add_file(file)
        except InvalidFilepathError:
            self._interface.show_message("Please enter a valid filepath.")
            raise
