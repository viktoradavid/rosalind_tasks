#!/usr/bin/env python3.5
import sys

months = int(sys.argv[1])
children = int(sys.argv[2])


def breed(month):
    # print(month)
    if month == 1 or month == 2:
        return 1
    return (breed(month - 1) + children * breed(month - 2))

rabbit_count = breed(months)

print(rabbit_count)
