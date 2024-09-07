#!/bin/sh

current_dir=$(basename "$PWD")

    cd ..
    rm -rf "$current_dir"
    
    git clone https://github.com/JJLin14/pakobbtool.git
    cd
    cd pakobbtool
    bash req.sh
    python3 main.py
else
    echo "取消。"
fi