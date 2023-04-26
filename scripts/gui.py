import pygame
from scripts.ui_element import *
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
    def __init__(self):
        self.otherGuiIsActive = False
        self.pressed = False

    # Inicializa los element necesarios
    def createGUI(self):
        self.equipment_area_element_array = []
        # *Mains
        self.master_gui_element = UiElement()  # Padre de todos
        self.default_gui_element = UiElement()
        self.master_gui_element.addElement(self.default_gui_element)
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
                    Button_element(
                        inventory_button_texture,
                        (0, 0),
                        (CELL_SIZE * 3, CELL_SIZE),
                    )
                )

        inventory_equipment_panel_element_group = UiElement()
        for i in range(0, size):
            position_x = viewsPositions[i][0]
            position_y = viewsPositions[i][1]
            if ((i + 1) % 2) == 0:
                position_x *= 1.425
            position_x += 32
            position_y += 16
            inventory_equipment_panel_element = Panel_element(
                inventory_equipment_panel_texture,
                (str(position_x), str(position_y)),
            )
            inventory_equipment_area_element = Panel_element(
                inventory_equipment_area_texture,
                (str(position_x + 16), str(position_y + CELL_SIZE * 3)),
            )
            # TODO: hacer que el area de estadísticas se muestre cuando se presiona el botón correspondiente
            equipment_buttons = UiElement()

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
            text_button = TextElement(
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
            equipment_buttons.addElement(
                self.equipment_area_btn_frag_array[i], text_button
            )
            inventory_equipment_panel_element_group.addElement(
                inventory_equipment_panel_element,
                inventory_equipment_area_element,
                equipment_buttons,
            )
            self.equipment_area_element_array.append(inventory_equipment_area_element)
        self.inventory_element.addElement(inventory_equipment_panel_element_group)

        equipment_statistics_element_array = []
        for i in range(size):
            equipment_statistics_element_array.append(UiElement())
        # for equipment_statistics_element in equipment_statistics_element_array:
        #     self.inventory_element.addElement(equipment_statistics_element)

    def createInventoryGUI(self):
        self.inventory_element = UiElement()
        self.equipment_area_element = UiElement()
        self.slotObjectsGroupElement = UiElement()
        self._pressed = True

        self.inventory_slot_group_element = UiElement()

        inventory_bag_element = Panel_element(
            inventory_bag_texture, ("36%", "20%"), (216, 312)
        )
        inventory_equipment_element = Panel_element(
            inventory_equipment_panel_texture,
            ("10%", "10%"),
            inventory_equipment_area_texture.get_size(),
        )
        inventory_text_element = TextElement(
            "Inventario",
            32,
            inventory_bag_element.getPosition(),
            (CELL_SIZE * 6.75, CELL_SIZE),
            WHITE,
        )

        self.indexTextElement = TextElement(
            str(Player.inventoryIndex + 1) + "/" + str(len(Player.inventory)),
            24,
            (
                inventory_bag_element.getPosition().x,
                inventory_bag_element.getPosition().y + CELL_SIZE * 8.75,
            ),
            (CELL_SIZE * 6.75, CELL_SIZE),
            WHITE,
        )

        inventory_slot_element = Panel_element(inventory_slot, (0, 0))

        # Creo los slots para el inventario
        self.inventory_slot_group_element = UiElement.ElementsMatrixGroupMaker(
            inventory_slot_element,
            (
                inventory_bag_element.getPosition().x + 24,
                inventory_bag_element.getPosition().y + CELL_SIZE * 2,
            ),
            (4, 4),
            (0, 0, 12, 12),
        )

        inventory_bag_element.addElement(self.inventory_slot_group_element)
        self.inventory_element.addElement(  # Carga el inventory element
            inventory_bag_element, inventory_text_element, self.indexTextElement
        )

    def updateEquipmentPanel(self, playerList):
        UiElement.clearElements(self.equipment_area_element)
        for index, player in enumerate(playerList):
            equipmentsKeys = player.getEquipmentsKeys()
            equipmentsList = player.getEquipments()
            self.equipment_area_element_array[index]
            for key in equipmentsKeys:
                position_x = self.equipment_area_element_array[index].getPosition().x
                position_y = self.equipment_area_element_array[index].getPosition().y
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
                imgFrag = Panel_element(equipmentImage, position)
                self.equipment_area_element.addElement(imgFrag)
        self.inventory_element.addElement(self.equipment_area_element)

    def createInventoryContents(self, objects: []):
        UiElement.clearElements(self.slotObjectsGroupElement)
        for index, object in enumerate(objects[Player.inventoryIndex]):
            position = self.inventory_slot_group_element.getElementList()[
                index
            ].getPosition()
            slotObjectElement = Button_element(
                object.getImage(),
                position,
                object.getImage().get_size(),
            )

            #!Arreglar que cada botón tenga su propio método que no esté por referencia
            def openObjectPanel():
                object.showPanelElements(
                    self.inventory_slot_group_element,
                    (position.x + CELL_SIZE, position.y),
                )

            slotObjectElement.setOnClick(openObjectPanel)
            self.slotObjectsGroupElement.addElement(slotObjectElement)
            self.indexTextElement.setText(
                str(Player.inventoryIndex + 1) + "/" + str(len(Player.inventory))
            )
        self.inventory_slot_group_element.addElement(self.slotObjectsGroupElement)

    def draw_GUI(self):
        # *Draw GUI
        self.master_gui_element.drawListElements()

    def hello(self):
        print("hello")

    def showInventory(self):
        UiElement.toggleElement(self.default_gui_element, self.inventory_element)
        self.otherGuiIsActive = True

    def isActiveInventory(self):
        return self.otherGuiIsActive
