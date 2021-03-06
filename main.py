# Modules:
import pygame, time, sys

# Classes:
from bar import Bar
from text import  Text

# Preferences
window_title = "Progress Bar Counter"
window_size = width, height = (600, 200)
window_icon = pygame.image.load('./icons/countdown1.png')
window_color = (64,45,65, 50)

# Aplying preferences:
window = pygame.display.set_mode(window_size, pygame.SRCALPHA)
pygame.display.set_caption(window_title)
pygame.display.set_icon(window_icon)

# Creating new objects:
bar = Bar(window)
text = Text(window)

# Input of time:
hours_required = 0
minutes_required = 0
seconds_required = 45

# If has any argument in the CLI 
if len(sys.argv) > 1:

    # If the CLI argument was like:
    # `progbar.py 25`, it is the seconds
    if len(sys.argv) == 2:
        hours_required = 0
        minutes_required = 0
        seconds_required = int(sys.argv[1])
        
    # If the CLI argument was like:
    # `progbar.py 1 25`, it is the minutes
    # followed by the seconds
    if len(sys.argv) == 3:
        hours_required = 0
        minutes_required = int(sys.argv[1])
        seconds_required = int(sys.argv[2])

    # If the CLI argument was like:
    # `progbar.py 1 25 30`, it is the hours
    # followed by the minutes, followed by
    # the seconds
    if len(sys.argv) == 4:
        hours_required = int(sys.argv[1])
        minutes_required = int(sys.argv[2])
        seconds_required = int(sys.argv[3])

# Calc of total minutes:
minutes_in_total = (
    (hours_required*60) +
    (minutes_required) +
    (seconds_required/60)
)

# Calc of seconds:
seconds_in_total = (
    ((hours_required*60)*60) +
    (minutes_required*60) +
    (seconds_required)
)

# Seting a while loop counter var:
c = 0

# Runtime:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill the window:
    window.fill(window_color)

    # Divide the bar in pieces:
    piece_of_the_bar = (
        (width / (
            (minutes_in_total * 60)) / bar.smoothness_of_bar
        )
    )

    # Add that piece to the bar:
    bar.draw(add_value=piece_of_the_bar)

    # Define and draw the actual time to the screen:
    text.define_what_to_write(
        time.gmtime(seconds_in_total)[3:6]
    )
    text.draw()

    # Down the seconds if one second has passed:
    # case the smoothnes of bar == 1, add every loop
    # and wait 1 second:
    if c % bar.smoothness_of_bar == 0 and seconds_in_total > 0:
        seconds_in_total -= 1

    # If the smoothnes of bar == 1, the program waits 1 second,
    # and the bar go second per second:
    time.sleep(1/bar.smoothness_of_bar)

    c += 1
    pygame.display.update()
