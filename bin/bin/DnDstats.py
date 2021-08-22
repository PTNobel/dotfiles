#!/usr/bin/eval python3

import random
from typing import List, NewType

AbilityScore = NewType('AbilityScore', int)


def calculateCostOfAbilityScores(abilities: List[AbilityScore]) -> int:
    return sum({
                3: -13,
                4: -10,
                5: -7,
                6: -4,
                7: -2,
                8: 0,
                9: 1,
                10: 2,
                11: 3,
                12: 4,
                13: 5,
                14: 7,
                15: 9,
                16: 12,
                17: 15,
                18: 19,
        }[ability]
        for ability in abilities)


def main(offer_rerun=True) -> None:
    totalCost: int = 0
    while totalCost != 32:
        totalCost = 0
        abilities: AbilityScore = list()
        # Generate 6 ability scores
        for _ in range(6):
            dieRolls: List[int] = list()

            # Roll 4 d6
            for _ in range(4):
                dieRolls.append(random.randint(1, 6))

            #print(dieRolls)
            abilities.append(AbilityScore(sum(sorted(dieRolls)[1:])))
            #print('\t' + str(abilities[-1]))

        totalCost = calculateCostOfAbilityScores(abilities)
    print("Your stats are:")
    for i in abilities:
        print('\t', i)
    print("which is worth", totalCost, "point buy points")


    if offer_rerun:
        main(False)
        print("Pick your favorite of the two options above!")


if __name__ == '__main__':
    main()
