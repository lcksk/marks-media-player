# linkedstructures.py
# Media Player Version 6.5
#
# This file contains linked structure implementations.

import datastructures

class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class LinkedQueue(datastructures.Queue):
    def __init__(self):
        self._front = None
        self._rear = None
        
    def enqueue(self, item):
        if self._front == None:
            self._front = Node(item, None)
            self._rear = self._front
            
        self._rear.next = Node(item, self._rear.next)
        self._rear = self._rear.next
        
    def dequeue(self):
        if self._head == None:
            raise AttributeError, "no items in queue"
            
        temp = self._front
        self._front = self._front.next
        
        return temp.data
