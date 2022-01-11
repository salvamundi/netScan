#!/usr/bin/python3

import scan
import handle_args as ha

if __name__ == '__main__':
    options = ha.handle_args() # values from -m & -t arguments

    scan.scan(options.method, options.target)
