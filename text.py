import pygame, math

class Text():

    # Preferences:
    window = None
    text_color = (255, 255, 255)
    default_text_size = None

    def __init__(self, window):
        pygame.font.init()
        self.window = window
        if self.default_text_size == None:
            self.text_size = math.floor(window.get_width()/10/2)
        else: self.text_size == self.default_text_size

    def define_what_to_write(self, hms:tuple):
        h, m, s = hms

        list_to_make_str = list()

        if h != 0:
            if h > 1: list_to_make_str.append(f'{h} hours')
            else: list_to_make_str.append(f'{h} hour')
        
        if m != 0:
            if m > 1: list_to_make_str.append(f'{m} minutes')
            else: list_to_make_str.append(f'{m} minute')

        if s != 0:
            if s > 1: list_to_make_str.append(f'{s} seconds')
            else: list_to_make_str.append(f'{s} second')
        
        if (h, m, s) == (0, 0, 0):
            list_to_make_str.append(f'Time expired!')

        str_to_return = str()
        for i in list_to_make_str: str_to_return += i + ' and '
        
        self.write = str_to_return[:-4]

    def render_text(self):
        font = pygame.font.Font(
            'freesansbold.ttf',
            self.text_size
        )

        self.text = font.render(
            self.write,
            True,
            self.text_color
        )
        self.textRect = self.text.get_rect()
        self.textRect.center = (
            self.window.get_width() // 2,
            self.window.get_height() // 2
        )

    def draw(self):
        self.render_text()
        self.window.blit(self.text, self.textRect)
