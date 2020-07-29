import pygame.midi

class MidiApapter:

    # Initialize the midi device
    def __init__(self):
        pygame.midi.init()

        print("\n\n\n\nScanning for midi input devices...")
        inputDeviceIndex = self.getInputDevice()

        self.inputDevice = pygame.midi.Input(inputDeviceIndex)
        self.noteNumbers = set()

    # Helper function for detecting midi inputs. 
    def getInputDevice(self):
        inputDevices = []
        for i in range(pygame.midi.get_count()):
            _, name, isInput, _, _ = pygame.midi.get_device_info(i)
            if (isInput):
                inputDevices.append((i, name))

        if (len(inputDevices) == 0):
            print("No midi devices detected. Please plug in a device and try again.")
            exit(0)

        if (len(inputDevices) == 1):
            print("Using: {}".format(inputDevices[0][1]))
            return inputDevices[0][0]
        
        print("Multiple input device detected...")
        for device in inputDevices:
            print("\tEnter: '{}' for '{}'".format(device[0], device[1]))

        return int(input("\nSelect midi device: "))
    
    # Helper function to convert midi numbers to notes.
    def numberToNote(self, number):
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return notes[number % 12]

    # Should be called every cycle of the main loop to fetch changes in midi input
    def onUpdate(self):

        # Check to see if we have any new inputs. This could be pressing or releasing a key
        if self.inputDevice.poll():

            # Grab the event and extract data from it
            event = self.inputDevice.read(1)[0]
            data = event[0]
            action = data[0]
            noteNumber = data[1]

            # Respond to the event based on the action
            if action == 144:
                # 144 is press
                self.noteNumbers.add(noteNumber)
            elif action == 128 and noteNumber in self.noteNumbers:
                # 128 is release
                self.noteNumbers.remove(noteNumber)

        # Return all notes in ascending order of pitch (note number)
        notes = []
        for noteNumber in sorted(self.noteNumbers):
            notes.append(self.numberToNote(noteNumber))
        return notes