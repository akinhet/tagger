#!/usr/bin/env python3

import music_tag
from bitarray import bitarray


def change_tags(filename: str, flags: bitarray):
    if len(flags.to01()) != 17:
        raise ValueError('flags argument is not of length 17')

    f = music_tag.load_file(filename)

    if flags[0] == 1:  # album
        user_input = str(input('album: '))
        f['album'] = user_input

    if flags[2] == 1:  # albumartist
        user_input = str(input('albumartist: '))
        f['albumartist'] = user_input

    if flags[3] == 1:  # artist
        user_input = str(input('artist: '))
        f['artist'] = user_input

    if flags[4] == 1:  # artwork
        user_input = str(input('path to the artwork: '))
        with open(user_input, 'rb') as img:
            f['artwork'] = img.read()

    if flags[5] == 1:  # comment
        user_input = str(input('comment: '))
        f['comment'] = user_input

    if flags[6] == 1:  # compilation
        while True:
            user_input = str(input('compilation [y/n]: '))
            if user_input == 'y' or user_input == 'Y' or \
               user_input == 'yes' or user_input == 'Yes':
                f['compilation'] = True
                break
            if user_input == 'n' or user_input == 'N' or \
               user_input == 'no' or user_input == 'No':
                f['compilation'] = False
                break
    if flags[7] == 1:  # composer
        user_input = str(input('composer '))
        f['composer'] = user_input

    if flags[8] == 1:  # discnumber
        user_input = str(input('disc number: '))
        f['discnumber'] = user_input

    if flags[9] == 1:  # genre
        user_input = str(input('genre: '))
        f['genre'] = user_input

    if flags[10] == 1:  # lyrics
        user_input = str(input('lyrics: '))
        f['lyrics'] = user_input

    if flags[11] == 1:  # totaldiscs
        user_input = str(input('total discs: '))
        f['totaldiscs'] = user_input

    if flags[12] == 1:  # totaltracks
        user_input = str(input('total tracks '))
        f['totaltracks'] = user_input

    if flags[13] == 1:  # tracknumber
        user_input = str(input('track number: '))
        f['tracknumber'] = user_input

    if flags[14] == 1:  # tracktitle
        user_input = str(input('tracktitle: '))
        f['tracktitle'] = user_input

    if flags[15] == 1:  # year
        user_input = str(input('year: '))
        f['year'] = user_input

    if flags[16] == 1:  # isrc
        user_input = str(input('isrc: '))
        f['isrc'] = user_input
