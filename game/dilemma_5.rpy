label dilemma_5:
    you "The sun rises, and you peer into your crystal ball, anxiously awaiting more information on the coming battle."
    scene vision_background with dissolve
    "You see the enemy army charging through the gates, cutting down townspeople along their way. Screams ring out, echoing off the stone walls of the city."
    "Desperate people claw at the gates of the castle, but it remains firmly shut, and corpses pile up against the gate as the marauders cut them down."
    nvl clear
    scene main bg curtains up with dissolve
    you "You rush to tell your king the news."
    show king_sprite at right
    king "Right. When the enemy arrives, we cannot afford to defend the entire perimeter of the city. Our generals recommended fortifying the castle gates instead."
    king "What of the townspeople? It would be greatly taxing on our resources to evacuate them all inside the castle walls."
    king "It would take hours to get everyone inside, and the enemy may be able to catch us off guard."
    hide king_sprite
    show defense_sprite at right
    defense "But we can't just let the townspeople die, that wouldn't just be abhorrent, it would be bad for our kingdom."
    defense "Plus, our soldiers have family too. It would be difficult for them to fight well knowing their families are in danger."
    hide defense_sprite
    show king_sprite at right
    king "Our kingdom's survival is the only thing that matters, but we should not sacrifice our townspeople, either. What are your thoughts?"
    hide king_sprite

    menu:
        "Evacuate the people":
            $ event_num += 2
            jump .choice1

        "Let the townspeople fend for themselves":
            $ event_num -= 5
            jump .choice2

label .choice1:
    show king_sprite at right
    king "Of course. It would be horrible to let the townspeople die, and even if we survive the attack, the kingdom may never recover."
    hide king_sprite
    jump epilogue

label .choice2:
    show king_sprite at right
    king "The people can hide in their homes. The enemy has made it clear they are coming for my head first, and we cannot weaken our defenses."
    hide king_sprite
    jump epilogue
