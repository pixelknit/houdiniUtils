#!/bin/bash

for filename in /Users/felipepesantez/Documents/H_dev/test_objs/*.obj; do
    hython script.py "/Users/felipepesantez/Documents/H_dev/main_basic_template.hipnc" "$filename"
done
