from typing import List

from modules.enums import MenuFunctionalities


class Menu:

    WELCOME_MESSAGE = "Welcome to the programming diary!"

    def __init__(self, indent: int = 4) -> "Menu":
        print(f"{self.WELCOME_MESSAGE}\n")
        self.message = self.__create_menu_message(indent=indent)

    def __create_menu_items(self, indent: int = 4) -> List[str]:
        indentation = " " * indent

        menu_items = [None] * len(MenuFunctionalities)
        menu_items[0] = (f"{indentation}{MenuFunctionalities.ADD.value}) "
                         "Add new entry for today.")
        menu_items[1] = (f"{indentation}{MenuFunctionalities.VIEW.value}) "
                         "View entries.")
        menu_items[2] = (f"{indentation}{MenuFunctionalities.EXIT.value}) "
                         "Exit.")

        return menu_items

    def __create_menu_message(self, indent: int = 4) -> str:
        menu_items = self.__create_menu_items(indent=indent)
        menu_items_string = ""
        for item in menu_items:
            menu_items_string += f"{item}\n"
        menu_message = (
            "Please select one of the following options:\n"
            f"{menu_items_string}"
            "\n"
            "Your selection: "
        )
        return menu_message

    def __str__(self) -> str:
        output_string = f"{self.message}"
        return output_string
