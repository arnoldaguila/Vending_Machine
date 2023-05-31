"""
Name: Arnold Aguila
Version: 1
"""


class VendingMachine:
    """
    This is the VendingMachine class. It has the class instance variable count and methods __init__(), __del__(),
    __str__(), .get_items(), .get_money(), .set_money(), .check_input(), and .run()
    """
    count = 0

    def __init__(self, items):
        """
        Initialize method that creates the VendingMachine object and adds 1 to the Class instance variable,
        count.
        :param items:
        """
        VendingMachine.count += 1
        self.identification = VendingMachine.count
        self.storage = items
        self.money = 0

    def __del__(self):
        """
        Delete method that deletes the VendingMachine object and subtracts 1 to the Class
        instance variable, count.
        :return:
        """
        VendingMachine.count -= 1

    def __str__(self):
        """
        String method that identifies the object when printed.
        :return: String
        """
        return f"This is a Vending Machine {self.identification}"

    def get_items(self):
        """
        Prints the key and value of the instance variable storage, five in a row, then crates a new line, and repeats.
        :return:
        """
        count = 0
        for key, value in self.storage.items():
            print(f"{key}: {value:.2f}", end=" ")
            count += 1
            if count == 5:
                print()
                count = 0

    def get_money(self):
        """
        Prints the instance variable money.
        :return:
        """
        print(f"${self.money:.2f}")
        print()

    def set_money(self, incoming_money):
        """
        Accumulates the instance variable money.
        :param incoming_money:
        :return:
        """
        self.money += incoming_money

    def check_input(self, user_input):
        """
        Checks and cleans user_input by replacing all spaces, changing the string to uppercase only.
        Try to typecast the user_input to float. If successful then return user_input as float. If not except the
        ValueError and pass. If the user_input is in the instance storage, return the value of user_input from the
        instance storage. Else if the user_input not in the instance storage, return None.
        :param user_input: String
        :return:
        """
        user_input = user_input.replace(" ", "")
        user_input = user_input.upper()
        try:
            user_input = float(user_input)
            if user_input >= 0:
                self.set_money(user_input)
                return
            return
        except ValueError:
            pass

        # If the variable user_input is in instance storage. Get the value of user_input from instance storage.
        if user_input in self.storage:
            item_cost = self.storage[user_input]

            # If self.money is greater than 0
            if self.money > 0:
                if self.money == item_cost:
                    print(f"Dispensing Item: {user_input}")
                    print("Dispensing Change: $0.00")
                    print()
                    self.money = 0
                    return

                elif self.money >= item_cost:
                    change = self.money - item_cost
                    print(f"Dispensing Item: {user_input}")
                    print(f"Dispensing Change: ${change:.2f}")
                    print()
                    self.money = 0
                    return

            else:
                print(f"The item costs: ${item_cost:.2f}")
                print()
                return

        # Else if the variable cleaned_user_input is not in instance storage, print an Error message and continue.
        elif user_input not in self.storage:
            print("Error not a valid input.")
            print()
            return

        return

    def run(self):
        """
        This is the driver method that makes the object VendingMachine work.
        :return:
        """
        # Loop to keep the VendingMachine object running.
        while True:

            # Prints the instance items on the console.
            self.get_items()

            # Prints the instance money on the console.
            self.get_money()

            # Gets user input.
            user_input = input("Enter code or money: ")
            print()

            # Stores the return of the instance method, .check_input()
            self.check_input(user_input)


def main():
    """
    Driver function.
    :return:
    """

    # Dictionary for the VendingMachine objects.
    inventory = {"A1": 1.25, "A2": 2.00, "A3": 1.50, "A4": 1.25, "A5": 1.75,
                 "B1": 1.25, "B2": 2.00, "B3": 1.50, "B4": 1.50, "B5": 1.75,
                 "C1": 1.25, "C2": 2.00, "C3": 1.50, "C4": 1.75, "C5": 1.75,
                 "D1": 1.25, "D2": 2.00, "D3": 1.50, "D4": 2.00, "D5": 1.75, }

    # The variable x is now an object VendingMachine. Then run x.
    x = VendingMachine(inventory)
    x.run()


if __name__ == '__main__':
    main()
