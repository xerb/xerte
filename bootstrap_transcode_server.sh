#!/bin/bash

set -e

echo "Setting up ffmpeg..."
./set_up_ffmpeg.sh
echo "Finished setting up ffmpeg"

echo "Setting up mp4box..."
./set_up_mp4box.sh
echo "Finished setting up mp4box"
