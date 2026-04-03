# Exercises:  
# 1. Create a grocery list and perform various  operations.
# 2.Write a program that finds the largest and smallest number inlist.

grocery_list = ['milk', 'eggs', 'bread', 'fruits', 'vegetables']

# Adding an item to the grocery list
grocery_list.append('cheese')

# Updating an item in the grocery list
grocery_list[3] = 'organic eggs' #Replace existing
#or
grocery_list.insert(2,'tomatoes sauce') #Nothing is deleted — just inserted (Added new item)

# Removing an item from the grocery list
grocery_list.remove('bread')

# Reversing the grocery list
grocery_list.reverse()

# Sorting the grocery list
grocery_list.sort()

# Printing the updated grocery list
print("Updated Grocery List:", grocery_list)

# Checking if an item is in the grocery list
if 'cheese' in grocery_list:
    print("Cheese are in the grocery list.")

#remove & return the last item in the grocery list
last_item = grocery_list.pop()
print("Removed last item:", last_item) 

#total number of items in the grocery list
total_items = len(grocery_list)
print("Total number of items in the grocery list:", total_items)

#concatenating two lists
additional_items = ['juice', 'snacks']
full_grocery_list = grocery_list + additional_items
print("Full Grocery List:", full_grocery_list)

#repeating list multiple times
repeated_grocery_list = grocery_list * 2
print("Repeated Grocery List:", repeated_grocery_list)


# 2. Finding the largest and smallest number in a list
numbers = [5, 2, 9, 1, 5, 6]
largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)
