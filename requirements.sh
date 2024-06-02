#!/bin/bash

# Update package lists
sudo apt-get update

# Install pip for Python 3
sudo apt-get install -y python3-pip

# Install tkinter for Python 3
sudo apt-get install -y python3-tk

# Install necessary Python packages
pip3 install -r requirements.txt

# Verify installation
python3 -m tkinter -c "print('tkinter is installed')"
pip3 show zxcvbn
