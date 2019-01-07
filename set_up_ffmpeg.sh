#!/bin/sh

# This was built for Ubuntu 18.04 launched on top of EC2.
#
# We really hope it works for you.
#

set -e
set -x

if [ "$(id -u)" -eq 0 ]; then
   echo "Do not run this script as root" 
   exit 1
fi

sudo apt-get update -qq && sudo apt-get -y install \
  autoconf \
  automake \
  build-essential \
  cmake \
  coreutils \
  git-core \
  libass-dev \
  libfdk-aac-dev \
  libfreetype6-dev \
  libmp3lame-dev \
  libnuma-dev \
  libopus-dev \
  libtool \
  libvorbis-dev \
  libvpx-dev \
  libx264-dev \
  libx265-dev \
  pkg-config \
  texinfo \
  wget \
  yasm \
  zlib1g-dev

mkdir -p build/ffmpeg build/ffmpeg_sources
cd build/ffmpeg_sources && \
wget -O ffmpeg-snapshot.tar.bz2 https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && \
tar xjvf ffmpeg-snapshot.tar.bz2 && \
cd ffmpeg && \
PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" ./configure \
  --prefix="$HOME/ffmpeg_build" \
  --pkg-config-flags="--static" \
  --extra-cflags="-I$HOME/ffmpeg_build/include" \
  --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
  --extra-libs="-lpthread -lm" \
  --bindir="$HOME/bin" \
  --enable-gpl \
  --enable-libass \
  --enable-libfdk-aac \
  --enable-libfreetype \
  --enable-libmp3lame \
  --enable-libopus \
  --enable-libvorbis \
  --enable-libvpx \
  --enable-libx264 \
  --enable-libx265 \
  --enable-nonfree && \
PATH="$HOME/bin:$PATH" make -j$(nproc --all) && \
make install && \
hash -r

echo "Looks like the ffmpeg setup worked"
