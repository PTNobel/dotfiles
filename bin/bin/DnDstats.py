#!/usr/bin/eval python3

import random
from typing import List

AbilityScores = List[int]


def calculateCostOfAbilityScores(abilities: AbilityScores) -> int:
    output: int = 0
    for ability in abilities:
        output += {
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
    return output


def main() -> None:
    totalCost:int = 0
    while totalCost not in range(30, 33):
        totalCost = 0
        abilities: AbilityScores = list()
        # Generate 6 ability scores
        for i in range(6):
            dieRolls:List[int] = list()
            
            # Roll 4 d6
            for j in range(4):
                dieRolls.append(random.randint(1, 6))


            print(dieRolls)
            abilities.append(sum(sorted(dieRolls)[1:]))
            print('\t' + str(abilities[-1]))
        
        totalCost = calculateCostOfAbilityScores(abilities)
        print(totalCost)

if __name__ == '__main__':
    main()
