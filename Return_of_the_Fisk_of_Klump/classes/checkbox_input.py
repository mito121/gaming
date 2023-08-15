import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
FONT = pg.font.Font(None, 32)

## Start Menu
checkmark = pg.image.load("assets/icons/checkmark.png").convert_alpha()
checkmark = pg.transform.rotozoom(checkmark, 0, .2)

class Checkbox:
    def __init__(self, x, y, w, h, label= "Enable sausages", checked = False):
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color('lightskyblue3')
        self.checked = checked
        self.txt_surface = FONT.render(label, True, "#FFFFFF", None)
        self.label = label

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the checkbox rect.
            if self.rect.collidepoint(event.pos):
                # Toggle checked
                self.checked = not self.checked

    def draw(self, screen):
        self.txt_surface = FONT.render(self.label, True, "#FFFFFF", None)
        # Blit the label.
        screen.blit(self.txt_surface, (405, 615))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
        if self.checked:
            screen.blit(checkmark, (self.rect.x, self.rect.y-10))
