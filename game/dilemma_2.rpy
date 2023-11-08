label dilemma_2:
    you "the next day"
    king """
        Greetings, it seems that there are rogue armies that are suspiciously close to our nation.

        If what you have said is true, then I fear that this may be a threat to my life.

        The intuitive course of action would be for me to close the gates... but that is our only way in and out of the walls.

        This would mean that our trade routes would be blocked, and any income of food would be stagnant...

        Who knows how long they'll be there for. However, the longer this gate stays closed, the higher the risk there is for my people to starve...

        I don't know if I can take the risk though.. I can't die just yet... I've yet to see my beautiful daughter get married- I live before that.

        This is quite difficult..

        """

    menu:
        "Close the gate":
            $ scenes.append("choice1")
            $ event_num += 1
            jump .choice1

        "Leave the gate open":
            $ scenes.append("choice2")
            jump .choice2
    nvl clear

label .choice1:
    king "You're right. The safety of myself comes before the people. Without me, there is no nation."
    jump .end_of_day

label .choice2:
    king "You're right. The safety of the people come before me. Without the people, there is no nation."
    jump .end_of_day

label .end_of_day:
    scene main bg curtains down with fade
    you "As the daylight fades, you close the curtains to your tent, and fall into a restless sleep, dreams plagued by visions of calamity to come."
