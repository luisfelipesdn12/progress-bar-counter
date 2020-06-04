import pygame, time
from bar import Bar
from text import  Text

window_title = "Progress Bar Counter"
window_size = width, height = (600, 200)
window_icon = pygame.image.load('./icons/countdown1.png')
window = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)
pygame.display.set_icon(window_icon)

bar = Bar(window)

text = Text(window)

hours_required = 0
minutes_required = 0
seconds_required = 30

minutes_in_total = (
    (hours_required*60) +
    (minutes_required) +
    (seconds_required/60)
)

#seconds_in_total = minutes_in_total * 60

seconds_in_total = (
    ((hours_required*60)*60) +
    (minutes_required*60) +
    (seconds_required)
)

divisor = width / 60

c = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    window.set_alpha(240)
    window.fill((64,45,65))
    bar.draw(
        (width / (
            (minutes_in_total * 60)) / bar.smoothness_of_bar
        )
    )
    text.define_what_to_write(
        time.gmtime(seconds_in_total)[3:6]
    )
    text.draw()

    if c % bar.smoothness_of_bar == 0 and seconds_in_total > 0:
        seconds_in_total -= 1

    time.sleep(1/bar.smoothness_of_bar)

    c += 1
    pygame.display.update()