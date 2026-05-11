#!/usr/bin/env python3

with open('/var/log/auth.log', 'r') as file:
    for line in file:
        if 'Failed password' in line:
            print(line)
