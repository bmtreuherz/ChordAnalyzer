import pygame

class DisplayAdapter:

    # Initialize the display
    def __init__(self):
        self.screenW = 1200
        self.screenH = 400
        self.screen = pygame.display.set_mode([self.screenW, self.screenH])
        self.onUpdate([], [])

    # Called once per loop cycle. Will update the display with any notes or chords
    def onUpdate(self, notes, chords):

        # Fill background with black
        self.screen.fill((49, 49, 49))

        # Default text color with no chords is white
        fontColor = (199, 199, 199)
        if chords:
            # If we found a chord, make the text green
            fontColor = (0, 169, 127)
            message = " ".join(chords)
            self.renderMessage(message, fontColor, 80)

        if notes:
            message = " ".join(notes)
            self.renderMessage(message, fontColor, 40, 70)
        
        pygame.display.update()

    def renderMessage(self, message, color, fontSize, verticalOffset=0):
        textTooBig = True
        while (textTooBig):
            font = pygame.font.Font('freesansbold.ttf', fontSize)
            textSurface = font.render(message, True, color)
            textRec = textSurface.get_rect()

            if (textRec.width < self.screenW):
                textTooBig = False
            fontSize -= 5

        textRec.center = ((self.screenW/2), (self.screenH/2) + verticalOffset)
        self.screen.blit(textSurface, textRec)