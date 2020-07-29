from helpers.metadata import *

class ChordAnalyzer:

    # Takes a list of notes and analyzes it to see if there are any chords
    def analyze(self, notes):
        # First remove duplicates and sort in note name order
        uniqueNotes = sorted(set(notes))

        # A chord must be at least 3 notes to identify
        if len(uniqueNotes) < 3:
            return []  

        # Identify Triads
        if len(uniqueNotes) < 5 :
            return self.identifyChords(uniqueNotes)

        return []


    def identifyChords(self, notes):
        # Iterate over the notes finding distances between each
        relativePositions = self.computeRelativePositions(notes)
        
        # Iterate over all the relative positions and see if they represent a chord rooted
        # at the ith index.
        chords = []
        for i in range(len(notes)):
            intervals = []
            for j in range(len(notes)):
                index = (i + j) % len(notes)
                intervals.append(str(relativePositions[index]))

            # The chord identifier will be a string representing all the intervals between
            # each note starting at the ith position.
            chordIdentifier = " ".join(intervals)
            if chordIdentifier in triads:
                chords.append("{}{}".format(notes[i], triads[chordIdentifier]))

            if chordIdentifier in sevenths:
                chords.append("{}{}".format(notes[i], sevenths[chordIdentifier]))

        return chords
        
    def computeRelativePositions(self, notes):
        # This will iterate through the list of notes, treating each note as a potential
        # root of the chord. It then gives all the intervals starting from that notes.
        relativePositions = []
        for i in range(len(notes)):
            first = notes[i]
            second = notes[(i + 1) % len(notes)]

            # Find the relative position of the two notes
            firstPos = allNotes[first]
            secondPos = allNotes[second]
            distance = secondPos - firstPos
            
            # Adjust if we need to wrap around
            if distance < 0: 
                distance = 12 + distance

            relativePositions.append(distance)
        return relativePositions