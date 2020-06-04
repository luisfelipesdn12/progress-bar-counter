import pygame

class Bar():

    color = (139,225,148)
    smoothness_of_bar = 20

    # define bar y size by 1/n of the screen
    define_bar_y_size_by = 20

    def __init__(self, window):
        self.window = window
        self.bar_y_size = (window.get_height()/
                            self.define_bar_y_size_by)
        self.pointer_pos = self.pointer_x, self.pointer_y = (
            -(window.get_width()),
            ((window.get_height())-self.bar_y_size)
        )
        size = (
            (self.window.get_width()),
            (self.window.get_height())
        )
        self.size = self.width, self.height = size
        
    def draw(self, add_value):
        pygame.draw.rect(
            self.window,
            self.color,
            (
                self.pointer_x,
                self.pointer_y,
                self.width,
                self.height
            )
        )
        if self.pointer_x < 0:
            self.pointer_x += add_value
        