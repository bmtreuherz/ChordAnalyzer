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
            self.drawChordMessage(message, fontColor)

        if notes:
            message = " ".join(notes)
            self.drawNotesMessage(message, fontColor)
        
        pygame.display.update()
    
    def drawChordMessage(self, message, color):
        # Draw chord text
        font = pygame.font.Font('freesansbold.ttf', 80)
        textSurface = font.render(message, True, color)
        textRec = textSurface.get_rect()
        textRec.center = ((self.screenW/2), (self.screenH/2))
        self.screen.blit(textSurface, textRec)

    def drawNotesMessage(self, message, color):
        # Draw notes text
        font = pygame.font.Font('freesansbold.ttf', 40)
        textSurface = font.render(message, True, color)
        textRec = textSurface.get_rect()
        textRec.center = ((self.screenW/2), (self.screenH/2) + 70)
        self.screen.blit(textSurface, textRec)