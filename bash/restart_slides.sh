#!/bin/sh
#
# modified from 'Script to run Digital Signage Solution using Feh'
# jonathan@learningspaces.net

pkill feh

sleep 3s

# Start slide show
/usr/bin/feh --quiet --fullscreen --recursive --hide-pointer --randomize --slideshow-delay 45 ./pictures/ &

exit 0
