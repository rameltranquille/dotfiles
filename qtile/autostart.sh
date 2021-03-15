#!/bin/sh

# compositor
picom &
# lutris permissions
sudo sh -c 'sysctl -w abi.vsyscall32=0'

