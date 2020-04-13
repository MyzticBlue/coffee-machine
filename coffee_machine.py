class Coffee:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def supply_change(self, w=0, m=0, b=0, c=0, money=0):
        self.water += w
        self.milk += m
        self.beans += b
        self.cups += c
        self.money += money
        list1 = [self.water, self.milk, self.beans, self.cups]
        list2 = ['water', 'milk', 'beans', 'disposable cups']
        min_index = list1.index(min(list1))
        if min(list1) < 0:
            print(f"Sorry, not enough {list2[min_index]}!\n")
            self.water -= w
            self.milk -= m
            self.beans -= b
            self.cups -= c
            self.money -= money
            return 0
        else:
            return 1

    def menu(self):
        option = input("Write action (buy, fill, take, remaining, exit):\n")
        if option.lower() == 'buy':
            self.buy()
            return 1
        elif option.lower() == 'fill':
            self.fill()
            return 1
        elif option.lower() == 'take':
            self.take()
            return 1
        elif option.lower() == 'remaining':
            self.remaining()
            return 1
        elif option.lower() == 'exit':
            print()
            return 0

    def buy(self):
        choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == '1':
            possible = self.supply_change(-250, 0, -16, -1, 4)
            if possible == 1:
                print("I have enough resources, making you a coffee!\n")
        elif choice == '2':
            possible = self.supply_change(-350, -75, -20, -1, 7)
            if possible == 1:
                print("I have enough resources, making you a coffee!\n")
        elif choice == '3':
            possible = self.supply_change(-200, -100, -12, -1, 6)
            if possible == 1:
                print("I have enough resources, making you a coffee!\n")
        elif choice.lower() == 'back':
            return

    def fill(self):
        w = int(input("\nWrite how many ml of water do you want to add:\n"))
        m = int(input("Write how many ml of milk do you want to add:\n"))
        b = int(input("Write how many grams of coffee beans do you want to add:\n"))
        c = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print()
        self.supply_change(w, m, b, c)

    def take(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0

    def remaining(self):
        print(f"""\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money\n""")


coffeeshop = Coffee(400, 540, 120, 9, 550)
statement = 1
while statement == 1:
    statement = coffeeshop.menu()
