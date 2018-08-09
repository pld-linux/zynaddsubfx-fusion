#!/bin/sh -e

# Make archives of Zyn-Fusion sources from GIT

if [ -z "$1" -o -n "$2" ] ; then
	echo "Usage:"
	echo "  $0 <commit>"
	echo "E.g.:"
	echo "  $0 c4c9221"
	exit 1
fi

commit="$1"

set -x

if [ -d mruby-zest-build/.git ] ; then
	cd mruby-zest-build
	git fetch origin
	git checkout master
else
	git clone --recursive https://github.com/mruby-zest/mruby-zest-build.git
	cd mruby-zest-build
fi
git reset --hard "$commit"
git submodule sync
git submodule update

version="$(git describe --tags | sed -e's/^v//;s/-/_/g')"
archive_name="mruby-zest-build-$version.tar"

echo "Building $archive_name..."
git archive --prefix mruby-zest-build/ -o ../$archive_name HEAD
git submodule --quiet foreach 'cd $toplevel/..; tar rf '"$archive_name"' mruby-zest-build/$path'
xz ../$archive_name
