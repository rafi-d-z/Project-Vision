# The script of the game goes in this file.

init python:
    import random

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

    scene main bg curtains up

    # These display lines of dialogue.

    "You're presented with a dreadful sight. Your king lays before you, in a pool of his own blood."
    "A spear is lodged deep within his chest, and amidst the chaos and fighting, you see him sputter and cough before finally falling still."
    nvl clear
    you "The crystal ball dims, and the vision ends. You dash out of your tent to break the news to the king."
    you2 "My liege! I bring dire news. I've received a dreadful vision, that you will fall in battle, and soon."

    jump dilemma_1

label end_of_day:
    scene main bg curtains down with fade
    you "As the daylight fades, you close the curtains to your tent, and fall into a restless sleep, dreams plagued by visions of calamity to come."
    scene main bg curtains up with fade
    jump expression ("dilemma_" + str(day_num))

return
