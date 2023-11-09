label dilemma_4:
    $ day_num = 5
    you "The sun rises, and you peer into your crystal ball, anxiously awaiting more information on the coming battle."
    "You see guards and soldiers in the courtyard, and though they aren't on-duty, tensions still seem high. A harsh word between two men turns into a shouting match."
    "Soon, the first punch is thrown, and before long there's a brawl in the courtyard."
    nvl clear
    you "You rush to tell your king the news."
    show king_sprite at right
    king "Low morale in the army is unacceptable when there's an enemy army on the horizon."
    king "We need our soldiers in top shape when the enemy arrives. How can we avoid this?"
    hide king_sprite
    show defense_sprite at right
    defense "My liege, the men have been on high alert for many days now, and they are tired and angry."
    defense "The guards have been assigned extra shifts, and the soldiers have been undergoing extra training."
    defense "We could give them a day of rest, having reduced shifts for guards, and giving soldiers the day off."
    defense "Or, we could make sure morale is high by force, making sure there are no deserters and defenses are as high as possible."
    hide defense_sprite
    show king_sprite at right
    king "We can't afford to lower defenses now, so close to the moment of truth, but being strict on our soldiers may backfire."
    hide king_sprite

    menu:
        "Give the troops a day off":
            $ event_num += 2
            jump .choice1

        "Punish deserters harshly":
            $ event_num -= 2
            jump .choice2

label .choice1:
    show king_sprite at right
    king "We must ensure everyone is well-rested and keep morale high. Reduce their workload for today."
    hide king_sprite
    jump end_of_day

label .choice2:
    show king_sprite at right
    king "We cannot allow our defenses to falter, not now. It must be done. Keep everyone on high alert."
    hide king_sprite
    jump end_of_day
