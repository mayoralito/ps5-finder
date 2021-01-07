#!/bin/sh

cd "$(dirname "$0")/ps5-finder/";
CWD="$(pwd)"
echo $CWD

source ~/envs/target/bin/activate
python3 launcher.py