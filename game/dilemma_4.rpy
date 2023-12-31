label dilemma_4:
    $ day_num = 5
    you "The sun rises, and you peer into your crystal ball, anxiously awaiting more information on the coming battle."
    hide oracle_idle
    show oracle_vision1 at left
    pause 1.7
    hide oracle_vision1
    scene vision_background with dissolve
    pause 0.5
    play music "audio/Crystal_ball_music.wav"
    "You see guards and soldiers in the courtyard, and though they aren't on-duty, tensions still seem high. A harsh word between two men turns into a shouting match."
    "Soon, the first punch is thrown, and before long there's a brawl in the courtyard."
    nvl clear
    play music "audio/Oracles_-_Main_Theme_Loop.wav"
    scene main bg curtains up with dissolve
    show oracle_vision2 at left
    pause 1.35
    hide oracle_vision2
    show oracle_idle at left
    you "You rush to tell your king the news."
    show king_sprite at right
    play voice "audio/King_voice.wav"
    king "Low morale in the army is unacceptable when there's an enemy army on the horizon."
    king "We need our soldiers in top shape when the enemy arrives. How can we avoid this?"
    hide king_sprite
    show defense_sprite at right
    play voice "audio/Guard_voice.wav"
    defense "My liege, the men have been on high alert for many days now, and they are tired and angry."
    defense "The guards have been assigned extra shifts, and the soldiers have been undergoing extra training."
    defense "We could give them a day of rest, having reduced shifts for guards, and giving soldiers the day off."
    defense "Or, we could make sure morale is high by force, making sure there are no deserters and defenses are as high as possible."
    hide defense_sprite
    show king_sprite at right
    play voice "audio/King_voice.wav"
    king "We can't afford to lower defenses now, so close to the moment of truth, but being strict on our soldiers may backfire."
    hide king_sprite
    hide oracle_idle

    menu:
        "Give the troops a day off":
            $ event_num += 2
            jump .choice1

        "Punish deserters harshly":
            $ event_num -= 2
            jump .choice2

label .choice1:
    show oracle_idle at left
    show king_sprite at right
    play voice "audio/King_voice.wav"
    king "We must ensure everyone is well-rested and keep morale high. Reduce their workload for today."
    hide king_sprite
    jump end_of_day

label .choice2:
    show oracle_idle at left
    show king_sprite at right
    play voice "audio/King_voice.wav"
    king "We cannot allow our defenses to falter, not now. It must be done. Keep everyone on high alert."
    hide king_sprite
    jump end_of_day
