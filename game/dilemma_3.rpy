label dilemma_3:
    $ day_num = 4
    you "The sun rises, and you peer into your crystal ball, anxiously awaiting more information on the coming battle."
    "You see a shady-looking individual flitting about the city streets, and beneath their cloak you catch a flash of steel."
    "As they make their way towards the castle, you see them crouch into the shadows, and they vanish."
    nvl clear
    you "You rush to tell your king the news."
    show king_beard_down at right
    pause 0.2
    hide king_beard_down
    show king_beard_up at right
    pause 0.2
    hide king_beard_up
    show king_beard_down at right
    king "An assassin. Or a spy. We must be on guard."
    king "Our enemies are out for my life. We must keep the guards on high alert. Captain, what are your thoughts?"
    hide king_beard_down
    defense "The way I see it, we have two options. We can make the guards search people in the city, or we can simply tell them to stay vigilant."
    defense "Having the guards search the people will make it harder for any potential assassins to get in, but it will greatly disturb the people."
    defense "Keeping the guards vigilant increases the odds sinister folk enter the castle, but it won't be as intrusive for the people."
    show king_beard_down at right
    pause 0.2
    hide king_beard_down
    show king_beard_up at right
    pause 0.2
    hide king_beard_up
    show king_beard_down at right
    king "Hmm. My safety is of utmost importance, of course, but we must keep the people in mind. What are your thoughts?"
    hide king_beard_down

    menu:
        "Authorize invasive searches":
            $ event_num += 1
            jump .choice1

        "Tell the guards to keep an eye out":
            $ event_num -= 1
            jump .choice2

label .choice1:
    show king_beard_down at right
    pause 0.2
    hide king_beard_down
    show king_beard_up at right
    pause 0.2
    hide king_beard_up
    show king_beard_down at right
    king "An assassin is a big deal. We can't let anyone with bad intentions across the castle walls."
    hide king_beard_down
    jump end_of_day

label .choice2:
    show king_beard_down at right
    pause 0.2
    hide king_beard_down
    show king_beard_up at right
    pause 0.2
    hide king_beard_up
    show king_beard_down at right
    king "Although the threat is large, it is unacceptable to accuse our own people of treachery, and search them on a whim."
    hide king_beard_down
    jump end_of_day