#!/usr/bin/env python3

import music_tag
from bitarray import bitarray


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def print_tags(filename: str):
    f = music_tag.load_file(filename)

    print(color.BOLD + "Filename: " + color.END + color.GREEN + filename + color.END)

    print(color.BOLD + "\nLength: " + color.END + color.GREEN + f["#length"] + color.END)
    print(color.BOLD + "Bitrate: " + color.END + color.GREEN + f["#bitrate"] + color.END)
    print(color.BOLD + "Samplerate: " + color.END + color.GREEN + f["#samplerate"] + color.END)
    print(color.BOLD + "Channels: " + color.END + color.GREEN + f["#channels"] + color.END)

    print(color.BOLD + color.YELLOW + "\nTitle: " + color.END + color.YELLOW + f["tracktitle"] + color.END)
    print(color.BOLD + color.YELLOW + "Artist: " + color.END + color.YELLOW + f["artist"] + color.END)
    print(color.BOLD + color.YELLOW + "Album Artist: " + color.END + color.YELLOW + f["albumartist"] + color.END)
    print(color.BOLD + color.YELLOW + "Album: " + color.END + color.YELLOW + f["album"] + color.END)
    print(color.BOLD + color.YELLOW + "Date: " + color.END + color.YELLOW + f["year"] + color.END)
    print(color.BOLD + color.YELLOW + "Track: " + color.END + color.YELLOW + f["tracknumber"] + color.END)
    print(color.BOLD + color.YELLOW + "Genre: " + color.END + color.YELLOW + f["genre"] + color.END)
    print(color.BOLD + color.YELLOW + "Disc: " + color.END + color.YELLOW + f["discnumber"] + color.END)
    print(color.BOLD + color.YELLOW + "Comment: " + color.END + color.YELLOW + f["comment"] + color.END)


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
        user_input = str(input('disc: '))
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
