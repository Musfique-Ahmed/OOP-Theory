"""
Question 2: Code Output - Item Class
This file contains the Item class implementation and example code
"""


class Item:
    """Item class with class variable and various methods"""
    
    total_items = 0
    
    def __init__(self, value):
        """Initialize Item with value and increment total_items counter"""
        self.value = value
        Item.total_items += 1
        self.item_id = Item.total_items
    
    def mix(self, other):
        """
        Mix method with conditional logic
        - If self.value > other.value, swap them and return new Item with self.value
        - Otherwise, return new Item with other.value
        """
        if self.value > other.value:
            self.value, other.value = other.value, self.value
            return Item(self.value)
        else:
            return Item(other.value)
    
    def display(self):
        """Display method that prints value and returns a new Item"""
        print(self.value)
        return Item(self.value)
    
    def __str__(self):
        """String representation of Item"""
        return f"Item {self.item_id}: {self.value}"


# Example code execution to demonstrate output
if __name__ == "__main__":
    print("=== Item Class Code Output Demo ===\n")
    
    # Create Item objects
    i1 = Item(10)
    i2 = Item(20)
    i3 = i1  # Reference assignment
    
    print(f"Initial state:")
    print(f"i1: {i1}")
    print(f"i2: {i2}")
    print(f"i3: {i3}")
    print(f"Total items: {Item.total_items}\n")
    
    # Modify attribute
    i1.value = 30
    print(f"After i1.value = 30:")
    print(f"i1: {i1}")
    print(f"i3: {i3}")
    print()
    
    # Method calls
    print("Executing: result = i1.mix(i2).display().value")
    result = i1.mix(i2).display().value
    print(f"Result value: {result}")
    print(f"i1 after mix: {i1}")
    print(f"i2 after mix: {i2}")
    print(f"Total items: {Item.total_items}\n")
    
    # Print statements
    print("Print statements:")
    print(i1)
    print(i2)
    print(i3)
    print(f"Total items: {Item.total_items}")


"""
EXPLANATION OF CODE EXECUTION:

1. i1 = Item(10)
   - Creates Item with value=10, item_id=1, total_items=1

2. i2 = Item(20)
   - Creates Item with value=20, item_id=2, total_items=2

3. i3 = i1
   - i3 references the same object as i1

4. i1.value = 30
   - Changes i1.value to 30 (also affects i3 since they reference the same object)

5. i1.mix(i2).display().value
   - i1.value = 30, i2.value = 20
   - In mix(): 30 > 20, so swap values
   - After swap: i1.value = 20, i2.value = 30
   - Returns Item(20) (new Item with item_id=3)
   - display() on this new Item prints: 20
   - display() returns another new Item(20) with item_id=4
   - .value returns 20

6. Final state:
   - i1 (and i3): Item 1: 20
   - i2: Item 2: 30
   - Total items: 4 (original 2 + 2 created during mix/display)
"""
