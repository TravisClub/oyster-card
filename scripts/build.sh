#!/bin/bash

ZIP_DIR=$PWD
ZIP_NAME=oyster-card.zip
ZIP_FILE="$ZIP_DIR/$ZIP_NAME"

zip -9 $ZIP_FILE

if [[ ! -d $VIRTUAL_ENV ]] ; then
    echo "Must be in a VIRTUAL_ENV to build."
    exit 1
fi

echo "Packaging the library"
pushd $VIRTUAL_ENV/lib/python3.6/site-packages
zip -r9 $ZIP_FILE *
popd

echo "Adding the code"
zip -g $ZIP_NAME oyster/card.py oyster/oyster_card.py oyster/trip.py

echo "Deployment package created at $ZIP_FILE"
