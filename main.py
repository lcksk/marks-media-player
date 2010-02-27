import sys, os, gobject

import gtk
try:
    import pygtk
    pygtk.require("2.0")
except:
    print("pyGTK 2.0 not available")
    sys.exit(1)
    
import pygst
try:
    pygst.require("0.10")
except:
    print("pyGST 0.10 not available")
    sys.exit(1)

import gst

from media_player_error import *
    
class MediaPlayer(object):
    def __init__(self):
        # gtk initialization
        builder = gtk.Builder()
        builder.add_from_file("main_window.glade")
        
        builder.connect_signals(self)
        self._file_entry = builder.get_object("file_entry")
        self._statusbar_label = builder.get_object("statusbar_label")
        
        # gstreamer initialization
        self._player = gst.element_factory_make("playbin", "player")
        self._player.set_state(gst.STATE_NULL)
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        self._player.set_property("video-sink", fakesink)
        bus = self._player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)
        
        # other
        self._current_file = None
        
    def on_play_button_clicked(self, widget, data=None):
        self.play()
        
    def on_stop_button_clicked(self, widget, data=None):
        self.stop()
        
    def on_main_window_destroy(self, widget, data=None):
        gtk.main_quit()
        
    def on_message(self, bus, message):
        t = message.type
        
        if t == gst.MESSAGE_EOS:
            self.on_message_eos(bus, message)
        elif t == gst.MESSAGE_ERROR:
            self.on_message_error(bus, message)
            
    def on_file_entry_activate(self, widget, data=None):
        self.play()
            
    def show_message(self, message):
        self._statusbar_label.set_text(message)
        
    def get_filepath(self):
        return self._file_entry.get_text()
        
    def on_message_eos(self, bus, message):
        self._player.set_state(gst.STATE_NULL)
        
    def on_message_error(self, bus, message):
        self._player.set_state(gst.STATE_NULL)
        err, debug = message.parse_error()
        print "Error : %s," %err, debug
        
    def play(self):
        try:
            self.set_current_file(self.get_filepath())
        except InvalidFilepathError:
            raise
            return
            
        self._player.set_property("uri", "file://" + self._current_file)
        self._player.set_state(gst.STATE_PLAYING)
        self.notify_playing()
        
    def stop(self):
        self._player.set_state(gst.STATE_NULL)
        self.notify_stopped()
        
    def set_current_file(self, file):
        if os.path.isfile(file):
            self._current_file = file
        else:
            self.show_message("Please enter a valid filepath.")
            raise InvalidFilepathError()
    
    def notify_playing(self):
        self.show_message("Playing " + self._current_file)
        
    def notify_stopped(self):
        self.show_message("Stopped")
        
mp = MediaPlayer()
gtk.main()
