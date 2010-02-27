# datastructures.py
# Media Player Version 6.5
#
# This file contains specificastions for data structures

class List(object):
    def __contains__(self, item):
        raise NotImplementedError
        
    def __len__(self):
        raise NotImplementedError
        
    def __str__(self):
        raise NotImplementedError
        
    def add(self, item):
        raise NotImplementedError
        
    def remove(self, item):
        raise NotImplementedError

class Queue(object):
    def enqueue(self, item):
        raise NotImplementedError
        
    def dequeue(self):
        raise NotImplementedError
