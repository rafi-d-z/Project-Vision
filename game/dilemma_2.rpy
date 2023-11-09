label dilemma_2:
    $ day_num = 3
    you "The sun rises, and you peer into your crystal ball, anxiously awaiting more information on the coming battle."
    "You see a swarm of people, soldiers, milling about in some kind of army camp. You aren't sure who they are, until you recognize the insignia on one of their battle flags."
    "It's the seal of a neighboring country, and from what you can tell, they're preparing for war. A man wearing bulky, intricate armor and wielding a massive greatsword steps onto a makeshift stage."
    "\"We will have victory! In the name of our lord!\" he shouts. The crowd echoes his chant, screaming and shouting in jubilation."
    nvl clear
    you "You rush to tell your king the news."
    show king_sprite at right
    king "Rogue armies amassing at our doorstep? Worrying indeed."
    king "This is troubling. If what you say is true, I may not be long for the world."
    king "We must secure the borders, yes? Stop anyone from going in and out of our country."
    hide king_sprite
    show defense_sprite at right
    defense "But sire, what about traders? Our people need trade to survive. If we close the borders, they'll starve!"
    hide defense_sprite
    show king_sprite at right
    king "It will be risky, yes. But some risks are necessary for the safety of our nation, and its leader."
    king "What do you think?"
    hide king_sprite

    menu:
        "Secure the borders":
            $ event_num += 1
            jump .choice1

        "Keep the borders open":
            $ event_num -= 1
            jump .choice2

label .choice1:
    show king_sprite at right
    king "You're right. We must make sacrifices for the safety of the nation. The people will have to make do for a time."
    hide king_sprite
    jump end_of_day

label .choice2:
    show king_sprite at right
    king "You're right. We cannot sacrifice the people for the sake of cowardice. We must keep the lifeline of our people alive."
    hide king_sprite
    jump end_of_day
