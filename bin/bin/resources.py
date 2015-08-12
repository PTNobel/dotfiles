#!/usr/bin/env python3

import os
import pickle
import random


class NationClass:
    cities = dict()
    resources = {1: dict(),
                 2: dict(),
                 3: dict(),
                 4: dict(),
                 5: dict(),
                 6: dict(),
                 7: dict(),
                 8: dict(),
                 9: dict(),
                 10: dict(),
                 11: dict(),
                 12: dict(),
                 }
    state = {'wood': int(),
             'stone': int(),
             'horses': int(),
             'iron': int(),
             'wheat': int(),
             'sheep': int(),
             'aluminum': int(),
             'gasoline': int(),
             'uranium': int(),
             }

    def __init__(self, player_name):
        self.name = player_name

    def __repr__(self):
        return "<nation '" + self.name + "'>"

    def copy(self):
        output = NationClass(self.name)
        for i in self.cities.key():
            output.add_city(self.cities[i].name,
                            self.cities[i].resources.copy())
        if output.resources != self.resources:
            False
        else:
            output.state = self.state.copy()
        return output

    def add_city(self, city_name, city_description):
        self.cities[city_name] = CityClass(city_name, city_description)
        self._rebuild_resources()

    def _rebuild_resources(self):
        _resources = {'wood': int(),
                      'stone': int(),
                      'horses': int(),
                      'iron': int(),
                      'wheat': int(),
                      'sheep': int(),
                      'aluminum': int(),
                      'gasoline': int(),
                      'uranium': int(),
                      }
        for city in self.cities:
            for resource in city.resources.key():
                _resources[resource] += city.level * city.resources[resource]
        self.resources = _resources

    def roll(self, number):
        for i in self.resources[number].keys():
            self.state[i] += self.resources[number][i]

    def transfer_city(self, city_name, recieving_nation):
        recieving_nation.add_city(self.cities.pop(city_name))
        self._rebuild_resources()

    def delete_city(self, city_name):
        self.cities.pop(city_name)
        self._rebuild_resources()

    def change_tile(self, city_name, tile_delta):
        self.cities[city_name].change_tile(tile_delta)
        self._rebuild_resources()

    def upgrade_city(self, city_name, upgrade_level):
        self.cities[city_name].level = upgrade_level
        self._rebuild_resources()

    def buy_unit(self, unit_details):
        can_buy = dict()
        for resource in unit_details.keys():
            if self.resources[resource] > unit_details[resource]:
                can_buy[resource] = True
            else:
                can_buy[resource] = False

        if False in can_buy:
            return False
        else:
            for resource in unit_details.keys():
                self.resources[resource] -= unit_details[resource]


class CityClass:
    level = 1

    def __init__(self, city_name, city_description):
        self.name = city_name
        self.resources = city_description

    def __repr__(self):
        return self.name

    def change_tile(self, tile_delta):
        for resource in tile_delta.key():
            self.resources[resource] += self.resources[resource]


def save_game_state(turn_log):
    os.makedirs('~/Backup_Dump/', exist_ok=True)
    save_file = open('~/Backup_Dump/Turn' + str(turn_log[-1][1]), 'wb')
    pickle.dump(turn_log, save_file)
    save_file.close()


def turn(nations, turn_log):
    backup_nation = dict()
    for i in nations.keys():
        backup_nation[i] = nations[i].copy()
    turn_log.append((turn_log[-1][0]+1, backup_nation))
    save_game_state(turn_log)


def build_initial_nations(name_list):
    nations = dict()
    for i in name_list:
        nations[i] = NationClass(i)

    calculate_dice_rolls(nations, 6)

    return nations


def roll_dice(number_of_rolls):
    output = list()
    for i in range(number_of_rolls):
        output.append(random.randint(1, 6) + random.randint(1, 6))
    return output


def calculate_dice_rolls(nations, num_of_rolls):
    for i in roll_dice(num_of_rolls):
        for nation in nations.keys():
            nations[nation].roll(i)


# nationList = (build_initial_nations(['prince', 'parth', 'shaam', 'moulton']))
