# Dictionary of all notes and their relative positions. Arbitrarily start at A.
# Subtracting one value from another will give you the distance between two notes in semi-tones
allNotes = {
    'A': 0,
    'A#': 1,
    'Bb': 1,
    'B': 2,
    'C': 3,
    'C#': 4,
    'Db': 4,
    'D': 5,
    'D#': 6,
    'Eb': 6,
    'E': 7,
    'F': 8,
    'F#': 9,
    'Gb': 9,
    'G': 10,
    'G#': 11,
    'Ab': 11
}

# Some notes just to help keep track
# Major scale has a full tone between all notes except 3-4 and 7-1 which use a semi-tone

# The chords below are defined as the number of semi-tones that will be found between each note when they are layed out in increasing order starting from the root.
# For example, the major chord (1 3 5) is defined as '4 3 5'. This is because the distance from 1 to 3 is 4 semi tones, 3 to 5 is 3 semi tones, and 5 to 8(1) is 5 semi-tones

triads = {
    '4 3 5': 'maj', # (1 3 5)
    '3 4 5': 'min', # (1 3b 5)
    '3 3 6': 'dim', # (1 3b 5b)
    '4 4 4': 'aug' # (1 3 5#)
}

# There are some weird ones like Major Minor 7th and Augmented Major 7th that I don't have here but these are all the common ones
sevenths = {
    '4 3 4 1': 'maj7', # (1 3 5 7)
    '4 3 3 2': '7', # (1 3 5 7b)
    '3 4 3 2': 'min7', # (1 3b 5 7b)
    '3 3 4 2': 'min7b5', # (1 3b 5b 7b)
    '3 3 3 3': 'dim7' # (1 3b 5b 7bb)
}

# sus2 replaces 3rd in major or minor triad with major 2
# sus4 replaces 3rd in major or minor triad with perfect 4
suspensions = {
    '5 2 5': 'sus4', # (1 4 5)
    '2 5 5': 'sus2' # (1 2 5)
}

# Sixth chords take a major or minor traid and replace the perfect 5th with a major 6th
sixths = {
    '4 5 3': '6', # (1 3 6)
    '3 6 3': 'min6', # (1 3b 6)
}

# Tensions (also called extensions) add a 9(2), 11(4), or a 13(6) to a 7th chord.
# Since we are going to be analyzing notes in order (i.e. a single octive), we will identify them with the extension note
# falling within the same octive as the root note (e.g. the 2 instead of the 9). In actuality, it is likely played in a later
# octive, but this makes analysis easier.
tensions = {
    # Extensions of maj7
    '2 2 3 4 1': 'maj7(9)', # (1 2 3 5 7)
    '4 1 2 4 1': 'maj7(11)', # (1 3 4 5 7)
    '4 3 2 2 1': 'maj7(13)', # (1 3 5 6 7)

    # Extensions of natural 7
    '2 2 3 3 2': '7(9)', # (1 2 3 5 7b)
    '4 1 2 3 2': '7(11)', # (1 3 4 5 7b)
    '4 3 2 1 2': '7(13)', # (1 3 5 6 7b)

    # Extensions of min7
    '2 1 4 3 2': 'min7(9)', # (1 2 3b 5 7b)
    '3 2 2 3 2': 'min7(11)', # (1 3b 4 5 7b)
    '3 4 2 1 2': 'min7(13)', # (1 3b 5 6 7b)

    # Extensions of min7b5 (half-diminished)
    '2 1 3 4 2': 'min7b5(9)', # (1 2 3b 5b 7b)
    '3 2 1 4 2': 'min7b5(11)', # (1 3b 4 5b 7b)
    '3 3 3 1 2': 'min7b5(13)', # (1 3b 5b 6 7b)

    # Extensions of diminished
    '2 1 3 3 3': 'dim7(9)', # (1 2 3b 5b 7bb)
    '3 2 1 3 3': 'dim7(11)' # (1 3b 4 5b 7bb)
    # (1 3b 5b 6 7bb) This is not included here because the 6 and 7bb are the same so this is just a dim7 chord.
}

# Same as extensions but sharp or flat the extension note.
alteredTensions = {
    # Altered Extensions of maj7
    '1 3 3 4 1': 'maj7(b9)', # (1 2b 3 5 7)
    '3 1 3 4 1': 'maj7(#9)', # (1 2# 3 5 7)

    # maj7(b11)' (1 3 4b 5 7) This doesn't exist. 3-4 are one semi-tone away so can't flattening 4 just gives maj7
    '4 2 1 4 1': 'maj7(#11)', # (1 3 4# 5 7)

    '4 3 1 3 1': 'maj7(b13)', # (1 3 5 6b 7)
    '4 3 3 1 1': 'maj7(#13)', # (1 3 5 6# 7)

    # Altered Extensions of natural 7
    '1 3 3 3 2': '7(b9)', # (1 2b 3 5 7b)
    '3 1 3 3 2': '7(#9)', # (1 2# 3 5 7b)

    # '7(b11)' (1 3 4b 5 7b) 3 == 4b making this just natural 7
    '4 2 1 3 2': '7(#11)', # (1 3 4# 5 7b)

    '4 3 1 2 2': '7(b13)', # (1 3 5 6b 7b)
    # '7(#13)' (1 3 5 6# 7b) 6# == 7b making this natrual 7

    # Altered Extensions of min 7
    '1 2 4 3 2': 'min7(b9)', # (1 2b 3b 5 7b)
    # min7(#9)' (1 2# 3b 5 7b) 2# == 3b making this min7

    '3 1 3 3 2': 'min7(b11)', # (1 3b 4b 5 7b)
    '3 3 1 3 2': 'min7(#11)', # (1 3b 4# 5 7b)

    '3 4 1 2 2': 'min7(b13)', # (1 3b 5 6B 7b)
    # 'min7(#13)' (1 3b 5 6# 7b) 6# == 7b making this a min 7

    # Altered Extensions of min7b5 (half-diminished)
    '1 2 3 4 2': 'min7b5(b9)', # (1 2b 3b 5b 7b)
    # 'min7b5(#9)' (1 2# 3b 5b 7b) 2# == 3b making this a min7b5

    '3 1 2 4 2': 'min7b5(b11)', # (1 3b 4b 5b 7b)
    # 'min7b5(#11)' (1 3b 4# 5b 7b) 4# == 5b making this a min7b5

    '3 3 2 2 2': 'min7b5(b13)', # (1 3b 5b 6b 7b)
    # 'min7b5(#13)' (1 3b 5b 6# 7b) 6# == 7b making this a min7b5

    # Altered extensions of diminished
    '1 2 3 3 3': 'dim7(b9)', # (1 2b 3b 5b 7bb)
    # 'dim7(#9)'  (1 2# 3b 5b 7bb) 2# == 3b making this a dim

    '3 1 2 3 3': 'dim7(b11)' # (1 3b 4b 5b 7bb)
    # 'dim7(#11)' (1 3b 4# 5b 7bb) 4# == 5b making this a dim
}

allChords = {**triads, **sevenths, **suspensions, **sixths, **tensions, **alteredTensions}

