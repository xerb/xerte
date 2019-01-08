Xerte
=====

Xerb Transcode Everything

A server to change input videos into MPEG-DASH and HLS output files.

This works more or less like a replacement to Amazon ETS or similar.

## Running

### Locally

You will need to have Docker CE installed: https://docs.docker.com/install/

You can run the container using the `docker` command line tool. If you're not
familiar with using it, the Getting Started guide is quite good:

https://docs.docker.com/get-started/

## Components

_Standing on the shoulders of gigantes_

### FFMPEG

ffmpeg is a CLI utility to encode, decode, mux, and demux video and audio
files, among other things.

You can check it out here: http://ffmpeg.org/

#### How we use it

We expect ffmpeg will first be called from within a Python API, likely by
using subprocess.run().

### MP4BOX

mp4box, part of the GPAC Multimedia Open Source Project, does quite a few
things, but for our purposes it's used to generate the XML files needed for
MPEG-DASH streaming.

You can check it out here: https://gpac.wp.imt.fr/mp4box/

#### How we use it

Like ffmpeg, we expect mp4box will be invoked from within a Python API, again
probably with suprocess.run().

## Why MPEG-DASH and HLS?

We would love to use MPEG-DASH for everything, because it's an open standard
defined by the International Standards Organization (ISO), and has the best
feature set. This is why MPEG-DASH is used.

Unfortunately, iOS currently still doesn't support MPEG-DASH, because it has no
support for Media Source Extensions (MSE). This is why HLS is used.
