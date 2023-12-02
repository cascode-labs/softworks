#!/bin/bash
VERSION=$(cat softworks/version)
DIST_PATH="dist/v$VERSION"
echo "Building softworks v$VERSION"

rm -rf "$DIST_PATH"
mkdir -p "$DIST_PATH/src"
#cp -rf src "$DIST_PATH/"
cp softworks "$DIST_PATH/"
cp README.md "$DIST_PATH/"
cp CHANGELOG.md "$DIST_PATH/"

#cp IDS.cdsLibMgr.il "$DIST_PATH/"
echo "  build saved to $DIST_PATH"
echo "  build complete!"