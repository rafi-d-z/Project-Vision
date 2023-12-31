label dilemma_5:
    you "The sun rises, and you peer into your crystal ball, anxiously awaiting more information on the coming battle."
    hide oracle_idle
    show oracle_vision1 at left
    pause 1.7
    hide oracle_vision1
    scene vision_background with dissolve
    pause 0.5
    play music "audio/Crystal_ball_music.wav"
    "You see the enemy army charging through the gates, cutting down townspeople along their way. Screams ring out, echoing off the stone walls of the city."
    "Desperate people claw at the gates of the castle, but it remains firmly shut, and corpses pile up against the gate as the marauders cut them down."
    nvl clear
    play music "audio/Oracles_-_Main_Theme_Loop.wav"
    scene main bg curtains up with dissolve
    show oracle_vision2 at left
    pause 1.35
    hide oracle_vision2
    show oracle_idle at left
    you "You rush to tell your king the news."
    show king_sprite at right
    show oracle_idle at left
    play voice "audio/King_voice.wav"
    king "Right. When the enemy arrives, we cannot afford to defend the entire perimeter of the city. Our generals recommended fortifying the castle gates instead."
    king "What of the townspeople? It would be greatly taxing on our resources to evacuate them all inside the castle walls."
    king "It would take hours to get everyone inside, and the enemy may be able to catch us off guard."
    hide king_sprite
    show defense_sprite at right
    play voice "audio/Guard_voice.wav"
    defense "But we can't just let the townspeople die, that wouldn't just be abhorrent, it would be bad for our kingdom."
    defense "Plus, our soldiers have family too. It would be difficult for them to fight well knowing their families are in danger."
    hide defense_sprite
    show king_sprite at right
    play voice "audio/King_voice.wav"
    king "Our kingdom's survival is the only thing that matters, but we should not sacrifice our townspeople, either. What are your thoughts?"
    hide king_sprite
    hide oracle_idle

    menu:
        "Evacuate the people":
            $ event_num -= 2
            jump .choice1

        "Let the townspeople fend for themselves":
            $ event_num += 5
            jump .choice2

label .choice1:
    show oracle_idle at left
    show king_sprite at right
    play voice "audio/King_voice.wav"
    king "Of course. It would be horrible to let the townspeople die, and even if we survive the attack, the kingdom may never recover."
    hide king_sprite
    jump epilogue

label .choice2:
    show oracle_idle at left
    show king_sprite at right
    play voice "audio/King_voice.wav"
    king "The people can hide in their homes. The enemy has made it clear they are coming for my head first, and we cannot weaken our defenses."
    hide king_sprite
    jump epilogue
