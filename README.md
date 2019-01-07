Xerte
=====

Xerb Transcode Everything

A server to change input videos into MPEG-DASH and HLS output files.

This works more or less like a replacement to Amazon ETS or similar.

## Components

### FFMPEG

ffmpeg is a CLI utility to encode, decode, mux, and demux video and audio
files, among other things.

### MP4BOX

mp4box does quite a few things, but for our purposes it's used to generate the
XML files needed for MPEG-DASH streaming.
