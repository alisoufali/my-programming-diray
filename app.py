from pathlib import Path
from typing import Optional

from modules.configs import Configs
from modules.database import Database
from modules.enums import MenuFunctionalities
from modules.menu import Menu
from modules.user import UserFunctions


class Main:

    @classmethod
    def main(cls, config_path: Optional[Path] = None):

        Configs.load_configs(config_path=config_path)

        menu = Menu(indent=2)
        Database.connect_to_db()

        while (user_input := input(menu)) != MenuFunctionalities.EXIT.value:
            if user_input == MenuFunctionalities.ADD.value:
                UserFunctions.add_new_entry()
            elif user_input == MenuFunctionalities.VIEW.value:
                UserFunctions.view_entries()
            else:
                print("Invalid option, please try again!")


if __name__ == "__main__":
    Main.main()
