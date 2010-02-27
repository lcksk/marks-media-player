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
    
class MediaPlayer(object):
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("main_window.glade")
        
        builder.connect_signals(self)
        self.file_entry = builder.get_object("file_entry")
        self.statusbar_label = builder.get_object("statusbar_label")
        
        self.player = gst.element_factory_make("playbin", "player")
        self.player.set_state(gst.STATE_NULL)
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        self.player.set_property("video-sink", fakesink)
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)
        
    def on_play_button_clicked(self, widget, data=None):
        self.play()
        
    def on_main_window_destroy(self, widget, data=None):
        gtk.main_quit()
        
    def on_message(self, bus, message):
        t = message.type
        
        if t == gst.MESSAGE_EOS:
            self.on_message_eos(bus, message)
        elif t == gst.MESSAGE_ERROR:
            self.on_message_error(bus, message)
            
    def show_message(self, message):
        self.statusbar_label.set_text(message)
        
    def get_filename(self):
        return self.file_entry.get_text()
        
    def on_message_eos(self, bus, message):
        self.player.set_state(gst.STATE_NULL)
        
    def on_message_error(self, bus, message):
        self.player.set_state(gst.STATE_NULL)
        err, debug = message.parse_error()
        print "Error : %s," %err, debug
        
    def play(self):
        filepath = self.get_filename()
        if os.path.isfile(filepath):
            self.player.set_property("uri", "file://" + filepath)
            self.player.set_state(gst.STATE_PLAYING)
            self.notify_playing(filepath)
        else:
            self.show_message("not a file")
            
    def notify_playing(self, filepath):
        self.show_message("Playing " + filepath)

mp = MediaPlayer()
gtk.main()
