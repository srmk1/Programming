#!/bin/bash

(while true; do
 echo "Test "
 sleep 2
done) &
bgPID=$!; 
echo "BG PID $bgPID"
