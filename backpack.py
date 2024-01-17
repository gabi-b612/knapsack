class Item:
    """
        Class representing an item in the backpack.

        :param name: Name of the item. type name: str
        :param weight: Weight of the item. type weight: int
        :param value: Value of the item. type value: int
    """

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


class Backpack:
    """
        Class representing the backpack.

        :param max_weight: Maximum weight the backpack can hold. type max_weight: int
    """

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
        self.current_weight = 0
        self.current_value = 0
        self.number_of_items = 0

    def add_item(self, item):
        """
            Adds an item to the backpack if it doesn't exceed the maximum weight.

            :param item: Item to be added. type item: Item
        """
        if self.current_weight + item.weight <= self.max_weight:
            self.items.append(item)
            self.current_weight += item.weight
            self.current_value += item.value
            self.number_of_items += 1

    def display_items(self):
        """
            Displays the items in the backpack.
        """
        if self.number_of_items == 0:
            print("The backpack is empty.")
        else:
            print("Items in the backpack:")
            for item in self.items:
                print(f"\t{item.name} - {item.weight} - {item.value}")

            print(f"Max weight: {self.max_weight}")
            print(f"Number of items: {self.number_of_items}")
            print(f"Total weight: {self.current_weight} - Total value: {self.current_value}")


def dynamic_knapsack(sack, items):
    """
        Solves the knapsack problem using dynamic programming.

        :param sack: Backpack. type sack: Backpack
        :param items: List of items. type items: list
    """

    max_capacity = sack.max_weight
    matrix = [[0 for _ in range(max_capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for j in range(1, max_capacity + 1):
            if items[i - 1].weight <= j:
                matrix[i][j] = max(items[i - 1].value + matrix[i - 1][j - items[i - 1].weight], matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]

    # Find the elements according to the sum
    length_items = len(items)
    capacity = max_capacity

    while length_items >= 0 and capacity >= 0:
        target_item = items[length_items - 1]
        if (matrix[length_items][capacity] == matrix[length_items - 1][capacity - target_item.weight]
                + target_item.value):
            sack.add_item(target_item)
            capacity -= target_item.weight

        length_items -= 1


def main():
    sack = Backpack(1000)
    items = [
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20),
        Item("HP i3", 5, 10),
        Item("HP i9", 4, 40),
        Item("HP i7", 6, 30),
        Item("HP i11", 3, 50),
        Item("HP i5", 2, 20)
    ]
    dynamic_knapsack(sack, items)
    sack.display_items()


if __name__ == "__main__":
    main()
