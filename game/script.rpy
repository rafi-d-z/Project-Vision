# The script of the game goes in this file.

init python:
    import random

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character(None, kind=adv)
define town = Character("Townsperson")
define narrator = nvl_narrator
default day_num = 0
default event_num = 0
default scenes = ["test_event1", "test_event2"]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene main bg curtains up

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    you "You are an oracle. You have foreseen a great calamity that will befall your town. Help the townspeople escape the devastation."
    jump home

label home:
    scene main bg curtains up with fade
    if len(scenes) != 0:
        $ scene_num = random.randint(0,len(scenes)-1)
        $ curr_scene = scenes[scene_num]
        $ scenes.pop(scene_num)
        jump expression curr_scene
    else:
        scene main bg curtains down with fade
        you "As the daylight fades, you close the curtains to your tent, and fall into a restless sleep, dreams plagued by visions of calamity to come."

return
