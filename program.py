import pygame
from helpers.chordAnalyzer import ChordAnalyzer
from helpers.midiAdapter import MidiApapter
from helpers.displayAdapter import DisplayAdapter

def main():

    # Initialize everything
    pygame.init()
    midiAdapter = MidiApapter()
    chordAnalyzer = ChordAnalyzer()
    displayAdapter = DisplayAdapter()

    # Main loop
    running = True
    while running:
        # Find which notes are being pressed 
        notes = midiAdapter.onUpdate()

        # Identify if the combination of notes forms a chord
        chords = chordAnalyzer.analyze(notes)
        # Display the notes played and any chords formed.
        displayAdapter.onUpdate(notes, chords)

        # Terminate if user closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()