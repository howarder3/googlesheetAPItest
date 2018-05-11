#!/usr/bin/env bash
# start_update.sh

# get directory of the script
curr_dir=`dirname "$BASH_SOURCE"`

cd $curr_dir ;
source my_env/bin/activate
python update.py