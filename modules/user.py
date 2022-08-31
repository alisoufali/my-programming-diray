from modules.database import Database


class UserFunctions:

    @classmethod
    def add_new_entry(cls) -> None:
        entry_content = input("What have you learned today? ")
        entry_date = input("Enter the date: ")
        Database.create_entry(
            entry_content=entry_content,
            entry_date=entry_date
        )

    @classmethod
    def view_entries(cls) -> None:
        cursor = Database.read_entries()
        for entry in cursor:
            print(f"{entry['date']}\n{entry['content']}\n\n")
