#!/bin/bash

# Add a preset to presets.toml
# Replace ['preset title'] with your preset's name
# Put all your files in a directory
# Replace [folder] with your dirname
# And go

for f in /[folder]/* [folder]/**/*; do

python3 stretch_silence/stretch_silence.py f -p ['preset title']

done;

# TODO: Make and implement output folder
