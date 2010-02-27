# clinterface.py
# Media Player Version 6
#
# This file contains CLInterface

import mediaplayerinterface

class CLInterface(mediaplayerinterface.MediaPlayerInterface):
    def __init__(self, parent):
        super(CLInterface, self).__init__(parent)
        self._commands = {"play" : ["play"], "quit" : ["quit", "end", "exit"], "stop" : ["stop"]}
        self._prompt = ":-P" + " "

    def begin(self):
        self._ended = False
        
        self._display_intro()
        
        while not self._ended:
            try:
                command = raw_input(self._prompt)
            except EOFError: # if Ctrl-D is pressed
                command = self._commands["quit"][0]
            self._parse_command(command)
        
    def end(self):
        self._ended = True
        self.show_message("Goodbye")
    
    def show_message(self, message):
        print "\n", message, "\n"
        
    def notify_playing(self):
        self.show_message("Playing", self._parent.get_file())
        
    def notify_stopped(self):
        self.show_message("Stopped")
    
    def signal_play(self):
        self._parent.on_play()
    
    def signal_stop(self):
        self._parent.on_stop()
        
    def signal_quit(self):
        self._parent.on_quit()
        
    def _display_intro(self):
        print "Media Player"
        print "\nEnter a command to continue"
        
    def _parse_command(self, command):
        if command in self._commands["quit"]:
            self.signal_quit()
            return
        elif command in self._commands["play"]:
            self.signal_play()
        elif command in self._commands["stop"]:
            self.signal_stop()
