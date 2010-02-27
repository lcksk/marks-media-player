#!/usr/bin/env bash

find ./ -maxdepth 1 -name "*.py" -exec geany {} \;
geany history.txt
