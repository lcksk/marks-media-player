# gtkinterface.py
# Media Player Version 6
#
# This file contains a gtk implementation of MediaPlayerInterface
#
import mediaplayerinterface

# import the Gimp Toolkit
import gtk
try:
    import pygtk
    pygtk.require("2.0")
except:
    print("pyGTK 2.0 not available")
    sys.exit(1)
    
class GtkInterface(mediaplayerinterface.MediaPlayerInterface):
    """
    A graphical implementation of MediaPlayerInterface using the Gimp 
    Toolkit.
    """
    def __init__(self, parent, wants_interface=True):
        """
        Creates a new Gtk interface.
        
        gtk.main() afterwards must be called to activate the GUI.
        """
        super(GtkInterface, self).__init__(parent)
        
        builder = gtk.Builder()
        builder.add_from_file("main_window.glade")
        
        builder.connect_signals(self)
        self._file_entry = builder.get_object("file_entry")
        self._statusbar_label = builder.get_object("statusbar_label")
        
    def begin(self):
        gtk.main()
        
    def end(self):
        gtk.main_quit()
        
    def notify_playing(self):
        """
        Notify the user that a file is playing.
        """
        self.show_message("Playing " + self._parent.get_current_file())
        
    def notify_stopped(self):
        """
        Notify the user that the playing of a file was stopped.
        """
        self.show_message("Stopped")

    def show_message(self, message):
        """
        Display any string as a message to the user.
        """
        self._statusbar_label.set_text(message)
        
    def signal_play(self):
        self._parent.on_play()
        
    def signal_stop(self):
        self._parent.on_stop()
        
    def signal_quit(self):
        self._parent.on_quit()
    
    def _on_play_button_clicked(self, widget, data=None):
        """
        Actions performed when the play button is clicked.
        """
        self.signal_play()
        
    def _on_stop_button_clicked(self, widget, data=None):
        """
        Actions performed when the stop button is clicked.
        """
        self.signal_stop()
        
    def _on_main_window_destroy(self, widget, data=None):
        """
        Actions carried out when the main window is closed.
        """
        self.signal_quit()
        
    def _on_file_entry_activate(self, widget, data=None):
        """
        Called when file entry sends the activate signal
        """
        self.signal_play()
