# cisco_ios_2_eve-ng
Convert Cisco IOS config to compatible config for running in EVE-NG network emulation

This script will remove or comment_out config lines that are not supported (or wanted) in EVE-NG config so you can quickly create or update your lab environment with production config



Requirements
============
Python + Git

Usage
=====
Clone this repo
Make executable: chmod +x convert_and_comment.py


Modify the interface change_lines to fit your needs in your config. This is currently not dynamic because I didnt need this (yet)


usage : pyhton convert_and_comment.py /path/to/configs/    must be *.confg

