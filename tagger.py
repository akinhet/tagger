#!/usr/bin/env python3

import music_tag
from bitarray import bitarray
import glob
import click
from pathlib import Path
import os.path
import subprocess


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

    print(color.BOLD + "Filename: ", color.END, color.GREEN, '\t\t', filename, color.END)

    print(color.BOLD + "\nLength: " + color.END, color.GREEN, '\t\t', f["#length"], color.END)
    print(color.BOLD + "Bitrate: " + color.END, color.GREEN, '\t\t', f["#bitrate"], color.END)
    print(color.BOLD + "Samplerate: " + color.END, color.GREEN, '\t\t', f["#samplerate"], color.END)
    print(color.BOLD + "Channels: " + color.END, color.GREEN, '\t\t', f["#channels"], color.END)

    print(color.BOLD + color.YELLOW + "\nTitle: ", color.END, '\t\t', f["tracktitle"])
    print(color.BOLD + color.YELLOW + "Artist: ", color.END, '\t\t', f["artist"])
    print(color.BOLD + color.YELLOW + "Album Artist: ", color.END, '\t', f["albumartist"])
    print(color.BOLD + color.YELLOW + "Album: ", color.END, '\t\t', f["album"])
    print(color.BOLD + color.YELLOW + "Compilation: ", color.END, '\t\t', ("Yes" if f["compilation"] else "No"))
    print(color.BOLD + color.YELLOW + "Date: ", color.END, '\t\t', f["year"])
    print(color.BOLD + color.YELLOW + "Track: ", color.END, '\t\t', f["tracknumber"])
    print(color.BOLD + color.YELLOW + "Genre: ", color.END, '\t\t', f["genre"])
    print(color.BOLD + color.YELLOW + "Disc: ", color.END, '\t\t', f["discnumber"])
    print(color.BOLD + color.YELLOW + "Comment: ", color.END, '\t\t', f["comment"])


def change_tags(filename: str, flags: bitarray):
    if len(flags.to01()) != 16:
        raise ValueError('flags argument is not of length 16')

    f = music_tag.load_file(filename)

    if flags[13] == 1:  # tracktitle
        user_input = click.prompt('Tracktitle: ', type=str, default=f['tracktitle'])
        f['tracktitle'] = user_input

    if flags[2] == 1:  # artist
        user_input = click.prompt('Artist: ', type=str, default=f['artist'])
        f['artist'] = user_input

    if flags[1] == 1:  # albumartist
        user_input = click.prompt('Albumartist: ', type=str, default=f['albumartist'])
        f['albumartist'] = user_input

    if flags[0] == 1:  # album
        user_input = click.prompt('Album: ', type=str, default=f['album'])
        f['album'] = user_input

    if flags[5] == 1:  # compilation
        while True:
            user_input = click.prompt('Compilation [y/n]: ', type=str, default=('y' if f['compilation'] else 'n'))
            if user_input == 'y' or user_input == 'Y' or \
               user_input == 'yes' or user_input == 'Yes':
                f['compilation'] = True
                break
            if user_input == 'n' or user_input == 'N' or \
               user_input == 'no' or user_input == 'No':
                f['compilation'] = False
                break

    if flags[14] == 1:  # year
        user_input = click.prompt('Year: ', type=str, default=f['year'])
        f['year'] = user_input

    if flags[12] == 1:  # tracknumber
        user_input = click.prompt('Track number: ', type=str, default=f['tracknumber'])
        if user_input != '':
            f['tracknumber'] = user_input

    if flags[8] == 1:  # genre
        user_input = click.prompt('Genre: ', type=str, default=f['genre'])
        f['genre'] = user_input

    if flags[7] == 1:  # discnumber
        user_input = click.prompt('Disc: ', type=str, default=f['discnumber'])
        if user_input != '':
            f['discnumber'] = user_input

    if flags[4] == 1:  # comment
        user_input = click.prompt('Comment: ', type=str, default=f['comment'])
        f['comment'] = user_input

    # -----------------------------

    if flags[3] == 1:  # artwork
        user_input = click.prompt('Path to the artwork: ', type=str, default='')
        if user_input != '':
            with open(user_input, 'rb') as img:
                f['artwork'] = img.read()

    if flags[6] == 1:  # composer
        user_input = click.prompt('Composer ', type=str, default=f['composer'])
        f['composer'] = user_input

    if flags[9] == 1:  # lyrics
        user_input = click.prompt('Lyrics: ', type=str, default=f['lyrics'])
        f['lyrics'] = user_input

    if flags[10] == 1:  # totaldiscs
        user_input = click.prompt('Total discs: ', type=str, default=f['totaldiscs'])
        if user_input != '':
            f['totaldiscs'] = user_input

    if flags[11] == 1:  # totaltracks
        user_input = click.prompt('Total tracks ', type=str, default=f['totaltracks'])
        if user_input != '':
            f['totaltracks'] = user_input

    if flags[15] == 1:  # isrc
        user_input = click.prompt('ISRC: ', type=str, default=f['isrc'])
        f['isrc'] = user_input

    f.save()


@click.command()
@click.option('-d', default='.', help='directory with mp3 files to tag')
@click.option('-f', default='*.mp3', help='mp3 file to tag')
def main(d, f):
    if not Path(d).is_dir():
        print(color.RED + color.BOLD + 'FATAL: ' + color.END, '"' + d +
              '"', ' is not a directory! Terminating...')

    mp3_files = []

    for file in glob.glob(os.path.normpath(d) + "/" + f):
        mp3_files.append(file)

    for file in mp3_files:
        print("\n---------------------------------------\n")
        print_tags(file)

        print()
        user_input = click.prompt(color.BOLD + color.BLUE + '[S]' + color.END + 'kip, ' +
                                  color.BLUE + 'C' + color.END + 'hange tags, ' +
                                  color.BLUE + 'P' + color.END + 'lay the song, ' +
                                  color.BLUE + 'E' + color.END + 'nd the program',
                                  type=click.Choice(['S', 'C', 'P', 'E'], case_sensitive=False),
                                  show_choices=False,
                                  default='S', show_default=False)

        while True:
            match user_input:
                case 'S':
                    break
                case 'C':
                    change_tags(file, bitarray('1110110110001110'))
                case 'P':
                    subprocess.run(['mpv', file], capture_output=True)
                case 'E':
                    return

    print("Finished! Have a nice day :)")


if __name__ == '__main__':
    main()
