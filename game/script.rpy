# The script of the game goes in this file.

init python:
    import random

image king_sprite:
    "king_beard_down.png"
    0.2
    "king_beard_up.png"
    0.2
    repeat

image defense_sprite:
    "knight_mask_down.png"
    0.2
    "knight_mask_up.png"
    0.2
    repeat

image oracle_vision1:
    "vision_000.png"
    0.15
    "vision_001.png"
    0.15
    "vision_002.png"
    0.15
    "vision_003.png"
    0.15
    "vision_004.png"
    0.15
    "vision_005.png"
    0.15
    "vision_006.png"
    0.15
    "vision_007.png"
    0.30
image oracle_vision2:
    "vision_008.png"
    0.15
    "vision_009.png"
    0.15
    "vision_010.png"
    0.15
    "vision_011.png"
    0.15
    "vision_012.png"
    0.15
    "vision_013.png"
    0.15
    "vision_014.png"
    0.15
    "vision_015.png"
    0.30

image oracle_idle:
    "Scene1_000.png"
    0.15
    "Scene1_001.png"
    0.15
    "Scene1_002.png"
    0.15
    "Scene1_003.png"
    0.15
    "Scene1_004.png"
    0.15
    "Scene1_005.png"
    0.15
    "Scene1_006.png"
    0.15
    "Scene1_007.png"
    0.15
    "Scene1_008.png"
    0.15
    "Scene1_009.png"
    0.15
    "Scene1_010.png"
    0.15
    "Scene1_011.png"
    0.15
    "Scene1_012.png"
    0.15
    "Scene1_013.png"
    0.15
    "Scene1_014.png"
    0.15
    "Scene1_015.png"
    0.15
    repeat

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character(None, kind=adv)
define you2 = Character("You, the Court Oracle")
define town = Character("Townsperson")
define defense = Character("Minister of Defense")
define king = Character("The King")
define narrator = nvl_narrator

default day_num = 1
default event_num = 0 # we declare this number as an accumulator of "bad" vs "good" choices. Good choices > 3, bad choices <=3

# The game starts here.

label start:

    scene vision_background
    pause 0.5
    "You're presented with a dreadful sight. Your king lays before you, in a pool of his own blood."
    "A spear is lodged deep within his chest, and amidst the chaos and fighting, you see him sputter and cough before finally falling still."
    nvl clear
    scene main bg curtains up with dissolve
    show oracle_vision2 at left
    pause 1.35
    hide oracle_vision2
    show oracle_idle at left
    you "The crystal ball dims, and the vision ends. You dash out of your tent to break the news to the king."
    you2 "I bring grim tidings. I've received a dreadful vision, that you will fall in battle, and soon."
    jump dilemma_1

label end_of_day:
    scene main bg curtains down with dissolve
    you "As the daylight fades, you close the curtains to your tent, and fall into a restless sleep, dreams plagued by visions of calamity to come."
    scene main bg curtains up with fade
    show oracle_idle at left with dissolve
    jump expression ("dilemma_" + str(day_num))

return
