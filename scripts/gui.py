import pygame
from scripts.ui_fragment import *
from scripts.players_views import viewsPositions
from scripts.object import *
from scripts.player import Player

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


class Gui_drawer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.otherGuiIsActive = False
        self.pressed = False

    # Inicializa los fragment necesarios
    def createGUI(self):
        self.equipment_area_fragment_array = []
        # *Mains
        self.master_gui_fragment = Ui_fragment(self.screen)  # Padre de todos
        self.default_gui_fragment = Ui_fragment(self.screen)
        self.master_gui_fragment.addFragment(self.default_gui_fragment)
        self.createInventoryGUI()

    # TODO: Hacer que los objetos se muestren el slots correspondiente
    # TODO: Crear la ventana para de descripcion del Objeto
    # TODO: Crear la ventana de estadísticas
    # TODO: Mejorar el código de createGUI_arrays
    def createGUI_array(self, size: int = 1):
        self.equipment_area_btn_frag_array = []
        for i in range(size):
            if len(self.equipment_area_btn_frag_array) < size:
                self.equipment_area_btn_frag_array.append(
                    Button_fragment(
                        self.screen,
                        inventory_button_texture,
                        (0, 0),
                        (CELL_SIZE * 3, CELL_SIZE),
                    )
                )

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

            def openEquipmentArea1():
                print("Equipment1")

            def openEquipmentArea2():
                print("Equipment2")

            def openEquipmentArea3():
                print("Equipment3")

            def openEquipmentArea4():
                print("Equipment4")

            def openStatisticsArea1():
                print("Statistics1")

            def openStatisticsArea2():
                print("Statistics2")

            def openStatisticsArea3():
                print("Statistics3")

            def openStatisticsArea4():
                print("Statistics4")

            openEquipmentAreaMethods = [
                openEquipmentArea1,
                openEquipmentArea2,
                openEquipmentArea3,
                openEquipmentArea4,
            ]
            openStatisticsAreaMethods = [
                openStatisticsArea1,
                openStatisticsArea2,
                openStatisticsArea3,
                openStatisticsArea4,
            ]

            self.equipment_area_btn_frag_array[i].setOnClick(
                openEquipmentAreaMethods[i]
            )
            self.equipment_area_btn_frag_array[i].setPosition(
                (position_x + 16, position_y + 16)
            )
            text_button = Text_fragment(
                self.equipment_area_btn_frag_array[i].getScreen(),
                "Equipamiento",
                20,
                (
                    self.equipment_area_btn_frag_array[i].getPosition().x,
                    self.equipment_area_btn_frag_array[i].getPosition().y,
                ),
                (
                    self.equipment_area_btn_frag_array[i].getArea().x,
                    self.equipment_area_btn_frag_array[i].getArea().y,
                ),
            )
            equipment_buttons.addFragment(
                self.equipment_area_btn_frag_array[i], text_button
            )
            inventory_equipment_panel_fragment_group.addFragment(
                inventory_equipment_panel_fragment,
                inventory_equipment_area_fragment,
                equipment_buttons,
            )
            self.equipment_area_fragment_array.append(inventory_equipment_area_fragment)
        self.inventory_fragment.addFragment(inventory_equipment_panel_fragment_group)

        equipment_statistics_fragment_array = []
        for i in range(size):
            equipment_statistics_fragment_array.append(Ui_fragment(self.screen))
        # for equipment_statistics_fragment in equipment_statistics_fragment_array:
        #     self.inventory_fragment.addFragment(equipment_statistics_fragment)

    def createInventoryGUI(self):
        self.inventory_fragment = Ui_fragment(self.screen)
        self.equipment_area_fragment = Ui_fragment(self.screen)
        self.slotObjectsGroupFragment = Ui_fragment(self.screen)
        self._pressed = True

        self.inventory_slot_group_fragment = Ui_fragment(self.screen)

        inventory_bag_fragment = Panel_fragment(
            self.screen, inventory_bag_texture, ("36%", "20%"), (216, 312)
        )
        inventory_equipment_fragment = Panel_fragment(
            self.screen,
            inventory_equipment_panel_texture,
            ("10%", "10%"),
            inventory_equipment_area_texture.get_size(),
        )
        inventory_text_fragment = Text_fragment(
            self.screen,
            "Inventario",
            32,
            inventory_bag_fragment.getPosition(),
            (CELL_SIZE * 6.75, CELL_SIZE),
            WHITE,
        )

        self.indexTextFragment = Text_fragment(
            self.screen,
            str(Player.inventoryIndex + 1) + "/" + str(len(Player.inventory)),
            24,
            (
                inventory_bag_fragment.getPosition().x,
                inventory_bag_fragment.getPosition().y + CELL_SIZE * 8.75,
            ),
            (CELL_SIZE * 6.75, CELL_SIZE),
            WHITE,
        )

        inventory_slot_fragment = Panel_fragment(self.screen, inventory_slot, (0, 0))

        # Creo los slots para el inventario
        self.inventory_slot_group_fragment = Ui_fragment.fragmentsMatrixGroupMaker(
            inventory_slot_fragment,
            (
                inventory_bag_fragment.getPosition().x + 24,
                inventory_bag_fragment.getPosition().y + CELL_SIZE * 2,
            ),
            (4, 4),
            (0, 0, 12, 12),
        )

        inventory_bag_fragment.addFragment(self.inventory_slot_group_fragment)
        self.inventory_fragment.addFragment(  # Carga el inventory fragment
            inventory_bag_fragment, inventory_text_fragment, self.indexTextFragment
        )

    def updateEquipmentPanel(self, playerList):
        Ui_fragment.clearFragments(self.equipment_area_fragment)
        for index, player in enumerate(playerList):
            equipmentsKeys = player.getEquipmentsKeys()
            equipmentsList = player.getEquipments()
            self.equipment_area_fragment_array[index]
            for key in equipmentsKeys:
                position_x = self.equipment_area_fragment_array[index].getPosition().x
                position_y = self.equipment_area_fragment_array[index].getPosition().y
                if key == PrimaryWeapon:
                    position_x += CELL_SIZE * 5.5
                if key == SecondaryWeapon:
                    position_x += CELL_SIZE * 5.5
                    position_y += CELL_SIZE
                if key == Armor:
                    position_y += CELL_SIZE
                if key == Glove:
                    position_y += CELL_SIZE * 2
                if key == Pants:
                    position_y += CELL_SIZE * 4
                if key == Helmet:
                    position_y += 0
                if key == Shoes:
                    position_y += CELL_SIZE * 5
                if key == Cape:
                    position_y += CELL_SIZE * 3
                position = (position_x, position_y)
                equipmentImage = equipmentsList[key].getImage()
                imgFrag = Panel_fragment(self.screen, equipmentImage, position)
                self.equipment_area_fragment.addFragment(imgFrag)
        self.inventory_fragment.addFragment(self.equipment_area_fragment)

    def createInventoryContents(self, objects: []):
        Ui_fragment.clearFragments(self.slotObjectsGroupFragment)
        for index, object in enumerate(objects[Player.inventoryIndex]):
            position = self.inventory_slot_group_fragment.getFragmentList()[
                index
            ].getPosition()
            slotObjectFragment = Button_fragment(
                self.screen,
                object.getImage(),
                position,
                object.getImage().get_size(),
            )
            #!Arreglar que cada botón tenga su propio método que no esté por referencia
            def openObjectPanel():
                object.showPanelFragments(self.inventory_slot_group_fragment, (position.x+CELL_SIZE,position.y))
            slotObjectFragment.setOnClick(openObjectPanel)
            self.slotObjectsGroupFragment.addFragment(slotObjectFragment)
            self.indexTextFragment.setText(
                str(Player.inventoryIndex + 1) + "/" + str(len(Player.inventory))
            )            
        self.inventory_slot_group_fragment.addFragment(self.slotObjectsGroupFragment)

    def draw_GUI(self):
        # *Draw GUI
        self.master_gui_fragment.drawListFragments()

    def hello(self):
        print("hello")

    def showInventory(self):
        Ui_fragment.toggleFragment(self.default_gui_fragment, self.inventory_fragment)
        self.otherGuiIsActive = True

    def isActiveInventory(self):
        return self.otherGuiIsActive
