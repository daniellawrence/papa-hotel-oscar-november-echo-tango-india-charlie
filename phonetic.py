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
            w.append("{1}".format(char, new_char))
        new_words.append("({0}) {1}".format(word, " ".join(w)))
    return "\n".join(new_words)


def go_unix():
    unix = {
       'a': 'awk',
       'b': 'biff',
       'c': 'cc',
       'd': 'dd',
       'e': 'emacs',
       'f': 'fsck',
       'g': 'grep',
       'h': 'halt',
       'i': 'indent',
       'j': 'join',
       'k': 'kill',
       'l': 'lex',
       'm': 'more',
       'n': 'nice',
       'o': 'od',
       'p': 'passwd',
       'q': 'quota',
       'r': 'ranlib',
       's': 'spell',
       't': 'true',
       'u': 'uniq',
       'v': 'vi',
       'w': 'whoami',
       'x': 'x11',
       'y': 'yes',
       'z': 'zcat'
    }
    return unix


def go_evil():
    evil = {
        'b': 'bdellium',
        'c': 'czar',
        'h': 'heir',
        'a': 'alsle',
        'g': 'gnat',
        'k': 'known',
        'p': 'phlegm',
        's': 'sea',
        'r': 'right',
        'w': 'write',
        'o': 'ouija',
        'x': 'xian',
        'y': 'yiperite',
        'm': 'mnemonic',
        'e': 'euphrates',
        'd': 'django',
        't': 'tsunami',
        'q': 'qat',
    }
    nato = go_nato()
    nato.update(evil)
    return nato


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
    return nato


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
    return nato


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--dialect', choices=['nato', 'nato-phonetic', 'evil', 'unix'],
                        default='nato',
                        help='phonetci alphabet to use')
    args = parser.parse_args()

    if args.dialect == 'nato':
        m = go_nato()
        print translate(m)
        return

    if args.dialect == 'nato-phonetic':
        m = go_nato_phonetic()
        print translate(m)
        return

    if args.dialect == 'evil':
        m = go_evil()
        print translate(m)
        return

    if args.dialect == 'unix':
        m = go_unix()
        print translate(m)
        return

if __name__ == '__main__':
    main()
