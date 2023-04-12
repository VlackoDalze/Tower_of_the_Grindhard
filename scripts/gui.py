import pygame
from scripts.ui_fragment import *

# * User interface

inventory_bag_texture = pygame.image.load(
    'assets/gui/inventory/inventory_bag_panel.png')
inventory_button_texture = pygame.image.load(
    'assets/gui/inventory/inventory_button.png')
inventory_equipment_panel_texture = pygame.image.load(
    'assets/gui/inventory/inventory_equipment_panel.png')
inventory_equipment_area_texture = pygame.image.load(
    'assets/gui/inventory/equipment_area.png')
inventory_slot = pygame.image.load(
    "./assets/gui/inventory/inventory_slot.png")

default_fragment = Ui_fragment(ui_frag.getScreen())
inventory_fragment = Ui_fragment(ui_frag.getScreen())
inventory_bag_fragment = Panel_fragment(ui_frag.getScreen(), inventory_bag_texture, ('288', '16'), inventory_bag_texture.get_size())
inventory_slot_fragment = Interactable_fragment(ui_frag.getScreen(), inventory_slot, ('0','16'))
inventory_equipment_area_fragment_group = Ui_fragment(screen)
# inventory_equipment_fragment = Panel_fragment(ui_frag.getScreen(), inventory_equipment_panel_texture, ('10%','10%'),inventory_equipment_area_texture.get_size())

inventory_fragment.add_fragment(inventory_bag_fragment,inventory_slot_fragment)

def get_inventory():
    return inventory_fragment

def get_combat_zone():
    return combat_zone_fragment


