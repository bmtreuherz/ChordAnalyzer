# Dictionary of all notes and their relative positions
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

# Intervals between notes starting at root note
triads = {
    '4 3 5': 'maj',
    '3 4 5': 'min',
    '3 3 6': 'dim',
    '4 4 4': 'aug'
}

# There are some weird ones like Major Minor 7th and Augmented Major 7th that I don't have here but these are all the common ones
sevenths = {
    '4 3 4 1': 'maj7',
    '4 3 3 2': '7',
    '3 4 3 2': 'min7',
    '3 3 4 2': 'min7b5',
    '3 3 3 3': 'dim7'
}