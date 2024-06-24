#!/bin/bash 

samples=("")
if [[ $1 == "runheadless" ]];
then
    /isaac-sim/runheadless.native.sh
else
    /isaac-sim/kit/python/bin/python3 -m pip install --upgrade pip
    /isaac-sim/python.sh -m pip install hydra-core
    apt update && apt install git -y
    /isaac-sim/python.sh /root/workspace/src/env.py
fi

