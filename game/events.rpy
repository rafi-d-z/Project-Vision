label test_event1:
    town "My wedding is tomorrow! It won't rain, will it?"
    "You see a vision of a bright blue sky and the sun shining, clear as day, in the sky."
    menu:
        "You should be all good.":
            $ scenes.append("test_event1_followup1")
        "You might want to reschedule.":
            $ scenes.append("test_event1_followup2")
    nvl clear
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

label dilemma_1:
    defense "Your majesty, I believe that it would be wise to focus our defenses, but unfortunately, with our limited resources, we can either increase security for the king or the citizens. You are the wisest member of the court, which action do you believe would be best for the kingdom?"
    menu:
        "Increase security for the king":
            $ scenes.append("dilemma_1_1")
        "Increase security for the citizens":
            $ scenes.append("dilemma_1_2")

label dilemma_1_1:
    defense "We have increased security for the king. There are more soldiers around the king's palace."
    jump home

label dilemma_1_2:
    defense "We have increased security for the citizens. There are undercover soldiers around the neighborhoods."
    jump home

    
