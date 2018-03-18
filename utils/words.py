with open('/usr/share/dict/words') as infile:
    words = infile.read().splitlines()
    words_set = set(words)
