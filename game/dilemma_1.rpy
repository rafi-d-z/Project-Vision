label dilemma_1:
    $ day_num = 2
    show king_sprite at right
    king "There is a battle on the horizon? Dire news indeed. Captain, what do you recommend?"
    hide king_sprite
    show defense_sprite at right
    defense "It would be wise to ready our defenses, but we only have so many guards. We can bolster your personal guard, or we can fortify the perimeter of the city."
    defense "Each choice has its merits, but I'd like to hear your thoughts."
    hide defense_sprite
    hide oracle_idle
    menu:
        "Strengthen the king's personal guard":
            $ event_num += 1
            jump .choice1
        "Strengthen the city watch":
            $ event_num -= 1
            jump .choice2
    nvl clear

label .choice1:
    show oracle_idle at left
    show defense_sprite at right
    defense "We will strengthen the king's guard. None will threaten the face of our country."
    hide defense_sprite
    jump end_of_day

label .choice2:
    show oracle_idle at left
    show defense_sprite at right
    defense "We will strengthen the city watch. We'll make sure nobody slips our defenses."
    hide defense_sprite
    jump end_of_day
