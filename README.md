# Prerequisites
You must have python 3 installed.

You must have pygame installed. To do this, run:
    pip install pygame

Boom you're good to go.

# Running
Plug in your midi keyboard to your computer.

From the root directory, run:
    python program.py

The program will start and will search for midi inputs.
    If no devices are detected, the program will exit.

    If one device is detected, this device will be used.

    If multiple devices are detected, the user will be prompted to select which device to use.

Play notes on the keyboard.
    As you play notes, they will appear on the screen.

    Whenever the notes form a chord, it will show the chord and the color will change to green.

Thats about it!