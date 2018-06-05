#!/bin/sh

export \
    VAR1=Hello \
    VAR2=1,s,3,c \
    VAR3=false \
    VAR4=y \
    VAR5=5 \
    VAR6=1.3

python3 test.py -c test.yml
