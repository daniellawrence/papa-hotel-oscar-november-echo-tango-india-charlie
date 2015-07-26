#!/usr/bin/env python
import argparse
import sys


def translate(translate_map):
    words = "".join([s for s in sys.stdin]).split()
    new_words = []
    for word in words:
        w = []
        for char in word:
            new_char = translate_map.get(char, char)
            if new_char is None:
                new_char = char
            w.append("{1}".format(char, new_char))
        new_words.append("({0}) {1}".format(word, " ".join(w)))
    return "\n".join(new_words)


def go_evil():
    nato = {
        'a': None,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None,
        'g': 'gnome',
        'h': None,
        'i': None,
        'j': None,
        'k': 'known',
        'l': None,
        'm': None,
        'n': None,
        'o': None,
        'p': None,
        'q': None,
        'r': None,
        's': 'sea',
        't': None,
        'y': None,
        'v': None,
        'w': None,
        'x': None,
        'y': None,
        'z': None,
    }
    return translate(nato)


def go_nato_phonetic():
    nato = {
        'a': 'al-fah',
        'b': 'brah-voh',
        'c': 'char-lee',
        'd': 'dell-tar',
        'e': 'eck-oh',
        'f': 'foks-trot',
        'g': 'go-elf',
        'h': 'hoh-tel',
        'i': 'in-dee-ah',
        'j': 'jew-lee-ett',
        'k': 'key-loh',
        'l': 'lee-mah',
        'm': 'mike',
        'n': 'no-vember',
        'o': 'oss-cah',
        'p': 'pah-pah',
        'q': 'keh-beck',
        'r': 'row-me-oh',
        's': 'see-air-rah',
        't': 'tang-go_nato',
        'y': 'you-nee-form',
        'v': 'vik-tah',
        'w': 'wiss-key',
        'x': 'ecks-ray',
        'y': 'yang-kee',
        'z': 'zoo-loo',
        '1': 'wun',
        '2': 'too',
        '3': 'tree',
        '4': 'fow-er',
        '5': 'fife',
        '6': 'six',
        '7': 'sev-en',
        '8': 'ait',
        '9': 'nin-err',
        '0': 'zee-ro',
        '.': 'STOP',
    }
    return translate(nato)


def go_nato():
    nato = {
        'a': 'alfa',
        'b': 'bravo',
        'c': 'charlie',
        'd': 'delta',
        'e': 'echo',
        'g': 'golf',
        'h': 'hotel',
        'i': 'india',
        'j': 'juliett',
        'k': 'kilo,',
        'l': 'lima',
        'm': 'mike',
        'n': 'november',
        'o': 'oscar',
        'p': 'papa',
        'q': 'quevec',
        'r': 'romeo',
        's': 'sierra',
        't': 'tango',
        'u': 'uniform',
        'v': 'victor',
        'w': 'whiskey',
        'x': 'xray',
        'y': 'yankee',
        'z': 'zulu',
        '.': 'STOP',
    }
    return translate(nato)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--dialect', choices=['nato', 'nato-phonetic', 'evil'],
                        default='nato',
                        help='phonetci alphabet to use')
    args = parser.parse_args()

    if args.dialect == 'nato':
        print go_nato()
        return

    if args.dialect == 'nato-phonetic':
        print go_nato_phonetic()
        return

    if args.dialect == 'evil':
        print go_evil()
        return

if __name__ == '__main__':
    main()
