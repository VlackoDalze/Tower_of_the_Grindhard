import json
from typing import List, Dict, Annotated
from random import randint, random, randrange, shuffle, choice
from scripts.character import Character, GAME_CLASSES

with open('loot/loot_table.json') as loot_table:
        AVAILABLE_POOLS = json.load(loot_table)
    
def build_pool(character: Character,origin: str)-> dict:
    pool_template: dict = AVAILABLE_POOLS.copy()
    translated_origin: list[str] = origin.upper().split('.')

    for key in translated_origin:
        if key in pool_template:
            pool_template = pool_template[key]
        else:
            raise KeyError(
                f"The acces key {key} does not exists in the available pools for the value {origin}"
            )
        
    return pool_template

def start_loot(character: Character,origin: str)-> List[dict]:
    selected_pool: dict = build_pool(character,origin)

    return[{selected_pool}]
