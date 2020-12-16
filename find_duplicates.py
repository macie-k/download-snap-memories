# run after download script didn't download all memories
import os
import json

def save_duplicates(media):
    # get all dates from json
    list_of_dates = []
    for obj in media:
        list_of_dates.append(obj['Date'])

    # find all duplicates
    seen = set()
    seen_add = seen.add
    duplicates = list(set(x for x in list_of_dates if x in seen or seen_add(x)))

    with open('duplicates.txt', 'w+') as f:
        for d in duplicates:
            f.write(d + '\n')
