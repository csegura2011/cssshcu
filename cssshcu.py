#!/bin/python3

import paramiko
import csv
import sys
import getopt

REMOTE_SERVER_OUT_SEPARATOR=""

REMOTE_SERVER_CMDS_LIST=[
    "pwd",
    "hostname",
    "uname -a"
]


def main():

    try:
        opts, args = getopt.getopt(argv, "hi:o:", )
    except getopt.GetOptError:
        print("csshcu.py -s <servers-list.csv> -o <output-file.lst>")
        sys.exit(2)
    for opt, arg in opts:




if __name__ == "__name__" :
    main(sys.argv)



#--------------#
# References   #
#--------------#
# - Get Options: https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
#

