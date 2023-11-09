label dilemma_1:
    show king_beard_down at right
    pause 0.2
    hide king_beard_down
    show king_beard_up at right
    pause 0.2
    hide king_beard_up
    show king_beard_down at right
    king "There is a battle on the horizon? Dire news indeed. Captain, what do you recommend?"
    hide king_beard_down
    defense "It would be wise to ready our defenses, but we only have so many guards. We can bolster your personal guard, or we can fortify the perimeter of the city."
    defense "Each choice has its merits, but I'd like to hear your thoughts."
    menu:
        "Strengthen the king's personal guard":
            $ event_num++
            jump .choice1
        "Strengthen the city watch":
            $ event_num--
            jump .choice2
    nvl clear

label .choice1:
    defense "We will strengthen the king's guard. None will threaten the face of our country."
    day_num++;
    jump end_of_day

label .choice2:
    defense "We will strengthen the city watch. We'll make sure nobody slips our defences".
    day_num++;
    jump end_of_day
