#!/usr/bin/env python3
"""
dictionary.py

Cleaned examples converted from an interactive IDLE session.
This script demonstrates basic dictionary creation and operations.
"""

def show(title, obj):
    print(f"--- {title} ---")
    print(obj)
    print()


def main():
    # initial dictionary
    d1 = {102: 'Rahul', 103: 'Kartik', 105: 'Saurabh'}
    show('initial d1', d1)

    print('type(d1):', type(d1))
    print()

    # empty the dictionary
    d1 = {}
    show('after emptying d1', d1)

    # create via dict()
    d1 = dict(a=10, b=20, c=30)
    show('d1 via dict()', d1)

    # duplicate keys: last value wins
    d1 = {102: 'Rahul', 103: 'Kartik', 105: 'Saurabh', 105: 'Kartik'}
    show('duplicate key example (105 last wins)', d1)

    # update a value
    d1[105] = 'new'
    show('after updating key 105', d1)

    # add a new key
    d1[104] = 'Saurabh'
    show('after adding key 104', d1)

    # delete a key if present
    if 102 in d1:
        del d1[102]
    show('after deleting key 102 (if present)', d1)

    # keys, values, items
    show('keys()', list(d1.keys()))
    show('values()', list(d1.values()))

    print('Iterate keys:')
    for k in d1:
        print(k)
    print()

    print('Iterate key, value:')
    for k in d1:
        print(k, d1[k])
    print()

    print('Iterate values:')
    for v in d1.values():
        print(v)
    print()

    print('Items:')
    for item in d1.items():
        print(item)
    print()


if __name__ == '__main__':
    main()

# End of file