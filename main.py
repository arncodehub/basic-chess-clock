import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import time
import random
import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Chess Clock")
pygame.display.update()

# Flips the black clock text, which is better for OTB games!
print("*Purely Aesthetic/Convenience Settings*\n")
black_clock_flipped = bool(input("Flip it [flip black's clock for better OTB play]? "))
print("\n*Starting Time for both Players*\n")
# `last_tick` allows the clock to turn RED when time runs out, also general time inputs in MS
white_clock_start = input("White clock time (ms) [default is 180K or 3mins]: ")
black_clock_start = input("Black clock time (ms) [default is 180K or 3mins]: ")
print("\n*Fischer Increment/Bronstein Delay (same for both players)*\n")
fischer_increment = input("FISCHER Game increment (ms) [same for both players; default is 0 for no increment]: ")
bronstein_delay = input("BRONSTEIN Game delay 'special' (ms) [same for both players; default is 0 for no delay]: ")

# Allowing for a 'K' or 'M' to be inserted (!)
# 'K' means 1000ms or 1 second
# 'M' means 1 million milliseconds or 16m 40s
if white_clock_start != "":
    if white_clock_start.lower()[-1] == "k":
        white_clock_start = int(white_clock_start[:-1]) * 1000
    elif white_clock_start.lower()[-1] == "m":
        white_clock_start = int(white_clock_start[:-1]) * 1000000
if black_clock_start != "":
    if black_clock_start.lower()[-1] == "k":
        black_clock_start = int(black_clock_start[:-1]) * 1000
    elif black_clock_start.lower()[-1] == "m":
        black_clock_start = int(black_clock_start[:-1]) * 1000000
if fischer_increment != "":
    if fischer_increment.lower()[-1] == "k":
        fischer_increment = int(fischer_increment[:-1]) * 1000
    elif fischer_increment.lower()[-1] == "m":
        fischer_increment = int(fischer_increment[:-1]) * 1000000
if bronstein_delay != "":
    if bronstein_delay.lower()[-1] == "k":
        bronstein_delay = int(bronstein_delay[:-1]) * 1000
    elif bronstein_delay.lower()[-1] == "m":
        bronstein_delay = int(bronstein_delay[:-1]) * 1000000
if fischer_increment == "":
    fischer_increment = 0
if bronstein_delay == "":
    bronstein_delay = 0

if type(fischer_increment) == type('STRING'):
    fischer_increment = int(fischer_increment)
if type(bronstein_delay) == type('STRING'):
    bronstein_delay = int(bronstein_delay)

WHITE = (215, 215, 215)
BLACK = (40, 40, 40)
RED = (215, 0, 0)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Impact Regular", 64)

time_is_running_for = None
white_clock_MS = 180000 if not white_clock_start else int(white_clock_start)
black_clock_MS = 180000 if not black_clock_start else int(black_clock_start)
white_start_MS = None
black_start_MS = None
turn_start_MS = None

def format_time(MS):
    MS_approx = round(MS)
    hours = MS_approx // 3600000
    minutes = MS_approx % 3600000 // 60000
    seconds = MS_approx % 3600000 % 60000 // 1000
    d1 = MS_approx % 3600000 % 60000 % 1000 // 100
    d2 = MS_approx % 3600000 % 60000 % 1000 % 100 // 10
    if 0 < MS < 10:
        d2 = 1
    if MS < 1000:
        return f"{minutes:02d}:{seconds:02d}.{d1}{d2}"
    if MS < 10000:
        return f"{minutes:02d}:{seconds:02d}.{d1}"
    if MS < 3600000:
        return f"{minutes:02d}:{seconds:02d}"
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and min(black_clock_MS, white_clock_MS) > 0:
                time_now_MS = time.time() * 1000
                turn_start_MS = time_now_MS + bronstein_delay
                white_start_MS, black_start_MS = white_clock_MS, black_clock_MS
                if time_is_running_for == None:
                    time_is_running_for = "White"
                elif time_is_running_for == "White":
                    time_is_running_for = "Black"
                    white_clock_MS += fischer_increment
                else:
                    time_is_running_for = "White"
                    black_clock_MS += fischer_increment
    if time_is_running_for == "White" and min(black_clock_MS, white_clock_MS) > 0:
        time_now_MS = time.time() * 1000
        if turn_start_MS > time_now_MS:
            time_now_MS = turn_start_MS
        white_clock_MS = white_start_MS - (time_now_MS - turn_start_MS)
    if time_is_running_for == "Black" and min(black_clock_MS, white_clock_MS) > 0:
        time_now_MS = time.time() * 1000
        if turn_start_MS > time_now_MS:
            time_now_MS = turn_start_MS
        black_clock_MS = black_start_MS - (time_now_MS - turn_start_MS)
    white_clock_MS = max(white_clock_MS, 0)
    black_clock_MS = max(black_clock_MS, 0)
    window.fill(BLACK)
    display_white_clock = format_time(white_clock_MS)
    display_black_clock = format_time(black_clock_MS)
    black_clock_color, white_clock_color = WHITE, BLACK
    if black_clock_MS == 0:
        black_clock_color = RED
    if white_clock_MS == 0:
        white_clock_color = RED
    black_text = font.render(display_black_clock, True, black_clock_color)
    black_text = pygame.transform.flip(black_text, True, True) if black_clock_flipped else black_text
    white_text = font.render(display_white_clock, True, white_clock_color)
    pygame.draw.rect(window, WHITE, (0, 250, 500, 250))
    if time_is_running_for == "White":
        pygame.draw.polygon(window, BLACK, ((245, 270), (255, 270), (255, 300), (265, 300), (250, 315), (235, 300), (245, 300), (245, 270)))
    if time_is_running_for == "Black":
        pygame.draw.polygon(window, WHITE, ((245, 230), (255, 230), (255, 200), (265, 200), (250, 185), (235, 200), (245, 200), (245, 230)))
    window.blit(black_text, (250 - len(display_black_clock)*11, 110))
    window.blit(white_text, (250 - len(display_white_clock)*11, 360))
    pygame.display.update()
    clock.tick(60)
    