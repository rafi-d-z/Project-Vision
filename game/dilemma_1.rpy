label dilemma_1:
    defense "Your majesty, I believe that it would be wise to focus our defenses, but unfortunately, with our limited resources, we can either increase security for the king or the citizens. You are the wisest member of the court, which action do you believe would be best for the kingdom?"
    menu:
        "Increase security for the king":
            $ scenes.append(".choice1")
            $ event_num += 1
        "Increase security for the citizens":
            $ scenes.append(".choice2")
    nvl clear

label .choice1:
    defense "We have increased security for the king. There are more soldiers around the king's palace."
    jump .end_of_day

label .choice2:
    defense "We have increased security for the citizens. There are undercover soldiers around the neighborhoods."
    jump .end_of_day

label .end_of_day:
    scene main bg curtains down with fade
    you "As the daylight fades, you close the curtains to your tent, and fall into a restless sleep, dreams plagued by visions of calamity to come."

    
