# media_file_manager.py
# Media Player Version 6.5
#
# This file contains the file/playlist manager for MediaPlayer

import os

import linkedstructures
import mediaplayer
from media_player_error import *

class MediaFileManager(object):
    """
    A class that manages which files are to be played.
    """
    def __init__(self, parent):
        self._parent = parent
        
    def get_current_file(self):
        """
        Get the current file on the playlist.
        """
        raise NotImplementedError
    
    def next(self):
        """
        Change the next file to the current file and return it.
        """
        raise NotImplementedError
        
    def add_file(self, file):
        """
        Add a file to the playlist.
        """
        raise NotImplementedError

class QueuedFileManager(MediaFileManager):
    """
    An implementation of MediaFileManager using a linked queue.
    """
    def __init__(self, parent):
        MediaFileManager.__init__(self, parent) 
        self._current_file = None
        self._queue = linkedstructures.LinkedQueue()
            
    def add_file(self, file):
        if os.path.isfile(file):
            self._queue.enqueue(file)
        else:
            raise InvalidFilepathError
        
    def get_next_file(self):
        try:
            self._current_file = self._queue.dequeue().data
        except AttributeError: # if the queue is empty
            self._current_file = None
            raise
        
        return self.get_current_file
        
    def get_current_file(self):
        if self._current_file is None:
            try:
                self.get_next_file()
            # if there was no next file, this avoids an infinite loop
            except AttributeError:
                raise NoCurrentFileError
        else:
            return self._current_file

class SingleFileManager(MediaFileManager):
    """
    An implementation of MediaFileManager that will only deal with one 
    file at a time.
    
    This class is intended mainly for testing purposes.
    """
    def __init__(self, parent):
        MediaFileManager.__init__(self, parent)    
        self._file = None
        
    def add_file(self, file):
        """
        Sets self._file
        Any prevoius value of self._file is overwritten.
        """
        if os.path.isfile(file):
            self._file = file
        else:
            raise InvalidFilepathError
        
    def get_current_file(self):
        if self._file is None:
            raise NoCurrentFileError
        else:
            return self._file
        
    def next(self):
        return self.get_current_file()
