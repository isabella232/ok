#!/usr/bin/env bash

wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_$GAE_VERSION.zip -o gae_sdk.zip
unzip -q google_appengine_$GAE_VERSION.zip
mv google_appengine gae_sdk
export GAE_SDK=$PWD/gae_sdk
export PATH=$PATH:$GAE_SDK
export PYTHONPATH=$PYTHONPATH:$GAE_SDK
python server/app/generate_keys.py