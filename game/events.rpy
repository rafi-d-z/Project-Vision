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
