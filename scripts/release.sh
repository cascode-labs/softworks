#!/bin/bash
VERSION=$(cat version)
RDS_PROJ_PATH="/rds/devel/R/HOTCODE/amslibs/oa614/cdsware/IDS/softworks"
RDS_PATH="${RDS_PROJ_PATH}/v$VERSION"
echo "Releasing IDS-skill v$VERSION"
echo "  releasing to ${RDS_PATH}"
#rm -rf "${RDS_PATH}"
#mkdir "${RDS_PATH}"

cp -r "dist/v${VERSION}" "${RDS_PROJ_PATH}"
rm -f "$RDS_PROJ_PATH/latest"
ln -s "v$VERSION" "$RDS_PROJ_PATH/latest"