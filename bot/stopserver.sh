#!/bin/bash

echo "Stopping server..."
screen -S minecraft -X stuff "stop$(printf \\r)"
echo "Stopped server!"