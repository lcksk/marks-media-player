#!/bin/bash

MAIN_DIR="/home/mark/Desktop/Third Time's the Charm"

cd $MAIN_DIR
find . -name "*.pyc" -exec rm {} \;
