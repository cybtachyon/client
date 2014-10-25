#!/bin/sh

# Install libgit2 from untrusted source ppa
sudo add-apt-repository "deb http://ubuntu-archive.mirror.nucleus.be/ utopic main"
sudo add-apt-repository "deb-src http://ubuntu-archive.mirror.nucleus.be/ utopic main"

sudo apt-get update -q &> /dev/null && echo "apt-get caches updated."

if [[ $? != 0 ]]; then
	echo "apt-get update failed." > /dev/fd/2
	exit 1
fi

pip install -q cffi && echo "Installed cffi."
sudo apt-get install -q libgit2-dev python-qt4 > /dev/null \
	&& echo "Installed libgit2-dev python-qt4"


apt-shows-versions cffi libgit2-dev python-qt4
