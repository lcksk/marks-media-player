# Introduction #
This page will give some background about this project such as the motivation and reasons for certain implementation decisions.

# Background #
This project was to have a personal programming. I had no itch that needed scratching(although I did recently hack together a cross-product calculator), so I chose the application I used that I was least satisfied, the music player. This program was never written with the intention of replacing a fully developed media player. Its main purpose is to be a learning experience for myself.

In Version 1, the original program is essentially copy-and-pasted from this [gtk tutorial](http://www.micahcarrick.com/12-24-2007/gtk-glade-tutorial-part-1.html) and the early sections of this [gstreamer tutorial](http://pygstdocs.berlios.de/pygst-tutorial/introduction.html). From this base, the has been almost completely refactored.

# Details #
## Mercurial ##
Mercurial was chosen after reading a quick tutorial for it at [HgInit](http://hginit.com).

## Python ##
Python was chosen as the language for this project simply for ease of programming. My motivation when starting this project was fairly weak, and I knew that I did not have the patience to deal with the finer points of C.

Python's lack of declared typing and its use of garbage collection are huge positives. For me, the convenience of programming and running Python outweighs the the performance loss versus C.

It was my original intention to write the program in Python first so that I could focus on the principles rather than the code. After that, I would rewrite the program in C. As the project has progressed, the focus has shifted from writing a gtk/gstreamer application in Python and then C, to writing a platform agnostic media player in Python.

## Use of empty superclasses ##
The use of superclasses which contain many methods which raise NotImplementedError is inspired by Java interfaces and abstract classes. Although there is no need for them due to Python's dynamic typing, they provide a central location for initializing some values and a convenient reminder of methods which are required.

## GTK and GStreamer ##
GTK and GStreamer were chosen for this project mainly because they appear often on Linux, which I use.  The use of GTK was further helped by the availability of the Glade interface design program. Since its creation, this media player has tried to move away from depending on either library, instead just providing functions that an interface or back end must provide. As an example, and a test, a command line implementation of the interface is being developed.