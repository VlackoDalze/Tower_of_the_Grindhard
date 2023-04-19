import pygame
from scripts.ui_fragment import *
from scripts.players_views import viewsPositions

# * Texture

inventory_bag_texture = pygame.image.load(
    "assets/gui/inventory/inventory_bag_panel.png"
)
inventory_button_texture = pygame.image.load(
    "assets/gui/inventory/inventory_button.png"
)
inventory_equipment_panel_texture = pygame.image.load(
    "assets/gui/inventory/inventory_equipment_panel.png"
)
inventory_equipment_area_texture = pygame.image.load(
    "assets/gui/inventory/equipment_area.png"
)
inventory_slot = pygame.image.load("./assets/gui/inventory/inventory_slot.png")


def get_inventory():
    return inventory_fragment


def get_combat_zone():
    return combat_zone_fragment


class Gui_drawer(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.otherGuiIsActive = False

    def setEventListener(self, event: pygame.event):
        self.event = event

    # Inicializa los fragment necesarios
    def createGUI(self):
        # *Mains
        self.master_gui_fragment = Ui_fragment(self.screen)  # Padre de todos
        self.default_gui_fragment = Ui_fragment(self.screen)
        self.inventory_fragment = Ui_fragment(self.screen)
        self.inventory_slot_group_fragment = Ui_fragment(self.screen)

        self.inventory_bag_fragment = Panel_fragment(
            self.screen,
            inventory_bag_texture,
            ("288", "16"),
            inventory_bag_texture.get_size(),
        )
        self.inventory_equipment_fragment = Panel_fragment(
            self.screen,
            inventory_equipment_panel_texture,
            ("10%", "10%"),
            inventory_equipment_area_texture.get_size(),
        )
        self.inventory_text_fragment = Text_fragment(
            self.screen, "Inventario", 42, (288, 16), (478, 64), WHITE
        )
        self.inventory_slot_fragment = Panel_fragment(
            self.screen, inventory_slot, (0, 0)
        )

        self.master_gui_fragment.add_fragment(self.default_gui_fragment)
        self.inventory_slot_group_fragment.add_fragment(
            Ui_fragment.fragments_matrix_group_maker(
                self.inventory_slot_fragment,
                (
                    self.inventory_bag_fragment.get_position().x + 24,
                    self.inventory_bag_fragment.get_position().y + CELL_SIZE * 3,
                ),
                (11, 12),
                (0, 0, 8, 8),
            )
        )
        self.inventory_fragment.add_fragment(  # Carga el inventory fragment
            self.inventory_bag_fragment,
            self.inventory_text_fragment,
            self.inventory_slot_group_fragment,
        )

    # TODO: Hacer que los objetos se muestren el slots correspondiente
    # TODO: Crear la ventana para de descripcion del Objeto
    # TODO: Crear la ventana de estadísticas
    # TODO: Mejorar el código de createGUI_arrays
    def createGUI_array(self, size: int = 1):
        equipment_area_btn_frag_array = []
        for i in range(0, size):
            if len(equipment_area_btn_frag_array) < size:
                equipment_area_btn_frag_array.append(
                    Button_fragment(
                        self.screen,
                        inventory_button_texture,
                        (0, 0),
                        (CELL_SIZE * 3, CELL_SIZE),
                    )
                )
            equipment_area_btn_frag_array[i].setEventListener(self.event)
        equipment_statistics_fragment_array = []
        for i in range(size):
            equipment_statistics_fragment_array.append(Ui_fragment(self.screen))
        inventory_equipment_panel_fragment_group = Ui_fragment(self.screen)
        for i in range(0, size):
            position_x = viewsPositions[i][0]
            position_y = viewsPositions[i][1]
            if ((i + 1) % 2) == 0:
                position_x *= 1.425
            position_x += 32
            position_y += 16
            inventory_equipment_panel_fragment = Panel_fragment(
                self.screen,
                inventory_equipment_panel_texture,
                (str(position_x), str(position_y)),
            )
            inventory_equipment_area_fragment = Panel_fragment(
                self.screen,
                inventory_equipment_area_texture,
                (str(position_x + 16), str(position_y + CELL_SIZE * 3)),
            )
            # TODO: hacer que el area de estadísticas se muestre cuando se presiona el botón correspondiente
            equipment_buttons = Ui_fragment(self.screen)

            def openEquipmentArea():
                print("Equipment")

            def openStatisticsArea():
                print("Statistics")

            equipment_area_btn_frag_array[i].setOnClick(openEquipmentArea)
            equipment_area_btn_frag_array[i].set_position(
                (position_x + 16, position_y + 16)
            )
            text_button = Text_fragment(
                equipment_area_btn_frag_array[i].getScreen(),
                "Equipamiento",
                20,
                (
                    equipment_area_btn_frag_array[i].get_position().x,
                    equipment_area_btn_frag_array[i].get_position().y,
                ),
                (equipment_area_btn_frag_array[i].getArea().x, equipment_area_btn_frag_array[i].getArea().y)
            )
            equipment_buttons.add_fragment(
                equipment_area_btn_frag_array[i], text_button
            )
            inventory_equipment_panel_fragment_group.add_fragment(
                inventory_equipment_panel_fragment,
                inventory_equipment_area_fragment,
                equipment_buttons,
            )
        self.inventory_fragment.add_fragment(inventory_equipment_panel_fragment_group)

        # for equipment_statistics_fragment in equipment_statistics_fragment_array:
        #     self.inventory_fragment.add_fragment(equipment_statistics_fragment)

    def draw_GUI(self):
        self.event
        # *Draw GUI
        self.master_gui_fragment.drawListFragments()

    def hello(self):
        print("hello")

    def showInventory(self):
        Ui_fragment.toggle_fragment(self.default_gui_fragment, self.inventory_fragment)
        self.otherGuiIsActive = True

    def isActiveInventory(self):
        return self.otherGuiIsActive
