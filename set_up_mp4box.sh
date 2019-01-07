# This was designed on Ubuntu 18.04

set -e
set -x

echo "Getting the 0.7.0 release of GPAC"
cd src
wget "https://download.tsi.telecom-paristech.fr/gpac/release/0.7.0/gpac_0.7.0_amd64.deb"

echo "Unpacking .deb package and installing dependencies"
sudo dpkg -i "gpac_0.7.0_amd64.deb" || true
sudo apt-get -f install -y
