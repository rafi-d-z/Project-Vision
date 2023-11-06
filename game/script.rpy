# The script of the game goes in this file.

init python:
    import random

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")
define town = Character("Townsperson")
define narrator = nvl_narrator
default scenes = ["test_event1", "test_event2"]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    you "You are an oracle. You have foreseen a great calamity that will befall your town. Help the townspeople escape the devastation."

label home:
    $ scene_num = random.randint(0,len(scenes)-1)
    jump expression scenes[scene_num]
    $ scenes.pop(scene_num)
    you "The next day."
    scene bg room with fade
    # This ends the game.

label test_event1:
    town "My wedding is tomorrow! It won't rain, will it?"
    "You see a vision of a bright blue sky and the sun shining, clear as day, in the sky."
    menu:
        "You should be all good.":
            $ scenes.append("test_event1_followup1")
        "You might want to reschedule.":
            $ scenes.append("test_event1_followup2")
    jump home


label test_event1_followup1:
    town "Thank you for your advice! The wedding went smoothly!"
    jump home

label test_event1_followup2:
    town "Can't you see the sun up there? You're a sham!"
    jump home

label test_event2:
    town "test_event2."
    jump home

return
