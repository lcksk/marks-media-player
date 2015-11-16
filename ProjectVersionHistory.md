# Introduction #
This is an overview of changes made to the project before uploading it to Google Code. In general, `*`.0 versions indicate new features/code style, while `*`.5 versions indicate refactoring of `*`.0 versions.

Occasionally I will use the notation "function`_`{1, 2}"; this notation represents "function\_1 and function\_2"

# Versions #
## Version 1 ##
  * play\_button functions
  * status\_bar\_label displays messages
  * file name obtained from file\_entry

## Version 1.5 ##
  * changed main\_window title to Media Player
  * added show\_message() function
  * added get\_filename() function
  * added on\_message{eos,error} functions
  * added play() function
  * added notify\_playing() function

## Version 2 ##
### main.py ###
  * MediaPlayer
    * added self.current\_file
      * integrated into notify\_playing
    * added on\_file\_entry\_activate function
      * calls play()
    * play()
      * changed message shown when an invalid filepath is entered
### media\_player.py ###
  * created MediaPlayerError
  * created InvalidFilepathError
### main\_window.glade ###
  * main\_window uses audio-x-generic as icon

## Version 3 ##
  * added leading underscore("`_`") to all 'private' variables
  * added stop button
    * added to main\_window.glade
    * sets player.state to NULL
    * calls notify\_playing
  * play()
    * moved self.set\_current\_file into error block
      * Exception still raised
  * created cores.py and interfaces.py

## Version 3.5 ##
  * added comments
  * created UML class diagram
  * prepended "`_`" to 'private' methods
    * propogated to main\_window.glade
  * added `_`init`_`{interface, core} methods to MediaPlayer
    * moved respective code from `_``_`init`_``_` to the new methods
  * moved message for invalid filepath from set\_current\_file to except block in play()

## Version 4 ##
### gst\_core.py ###
  * created file
  * created GstCore
    * copied code from MediaPlayer.`_``_`init`_`core to GstCore.`_``_`init`_``_`
    * moved `_`current\_file
    * copied play(), stop(), `_`on\_message(,eos,error}, set\_current\_file()
### media\_player\_error.py ###
  * added NoCurrentFileError
  * `_``_`init`_``_` modified to accept `*`args

## Version 4.5 ##
  * MediaPlayer.`__`init`__` interface calls gtk.main()
  * move `_`current\_file back into MediaPlayer
  * separate play and stop logic between MediaPlayer.notify`_`{stopped, playing} and GstCore
    * play() and stop() return True or False depending on success
  * buttons in main\_window.glade into a horizontal button box
  * removed `_`on\_message`_`{,eos,error}, set\_current\_file()
  * GstCore.`_`on\_message\_eos modified to check that state change succeeds and calls `_`parent.notify\_stopped()

## Version 5 ##
  * created interfaces.py
    * created class MediaPlayerInterface as an abstract superclass
    * copied gtk source code from mediaplayer.py to interfaces.py
    * `_`init\_interface calls GtkInterface
  * added start() method to MediaPlayerInterface

## Version 5.5 ##
  * interface code removed from MediaPlayer
  * changed MediaPlayerInterface.start() to begin() and added end()
    * GtkInterface.end() calls gtk.main\_quit()
    * GtkInterface.`_`on\_main\_windoe\_destroy() calls end()

## Version 5.7 ##
  * moved implementations of MediaPlayerCore and MediaPlayerInterface into seperate files
    * MediaPlayer currently directly loads gstcore.py and gtkinterface.py

## Version 6 **_not fully functional_** ##
  * observer pattern added into the the interface classes and MediaPlayer
    * quit() method added
    * signal`_`{play,stop,quit} methods are still hardcoded to self.`_`parent
  * created CLInterface class
    * a command line implementation of MediaPlayerInterface
    * MediaPlayer is still hardcoded to GtkInterface
      * get\_filename()

## Version 6.5 ##
  * added files from Proposed
    * mediafilemanager.py
    * datastructures.py
    * linkedstructures.py
  * modified MediaPlayer to use a MediaFileManager
    * removed `_`current\_file
      * removed set\_current\_file(self, file)
        * added add\_file(self, file)
          * calls `_`manager.add\_file(self, file)
        * get\_current\_file(self) calls `_`manager.get\_current\_file(self)