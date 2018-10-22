#!/bin/bash

export LD_LIBRARY_PATH=/home/linaro/mjpg-streamer/
mjpg-streamer/mjpg_streamer -i "/home/linaro/mjpg-streamer/input_uvc.so -y -r 640x480 -f 30 -n" -o "/home/linaro/mjpg-streamer/output_http.so -w ./www"
