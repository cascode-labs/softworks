#!/bin/tcsh
echo "Initializing Softworks..."

setenv SOFTWORKS_ROOT "${SKYVER_ROOT}/src/Softworks"

if ($?PATH) then
	setenv PATH "${PATH}:${SOFTWORKS_ROOT}/bin"
else
	setenv PATH "${SOFTWORKS_ROOT}/bin"
endif
echo "  Softworks Initialized"

