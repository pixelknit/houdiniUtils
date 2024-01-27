#!/bin/bash

MAIN_FOLDER="/Users/felipepesantez/Downloads/assets/zip_test"

for SUBFOLDER in "$MAIN_FOLDER"/*; do
    if [ -d "$SUBFOLDER" ]; then
        echo "Processing $SUBFOLDER"

        hython run_on_template.py "/Users/felipepesantez/Documents/H_dev/AssetMigration_toUSD_v002.hipnc" "$SUBFOLDER"

    fi
done
