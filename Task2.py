single_dimensional_array = ["apple", "banana", "durian", "watermelon"]

two_dimensional_array = [
    [1, 2, 3],
    [4, 3, 6],
    [7, 8, 9]
]
for single in single_dimensional_array:
    print(single_dimensional_array)
def display_single_dimensional_array(array):
    print("elements in the single-dimensional array:")
    for element in array:
        print(element)

def display_two_dimensional_array(array):
    print("Elements in the two-dimensional array:")
    for sublist in array:
        print(sublist)
user_choice = str(input("Choose between two (single or two-dimensional): "))
if user_choice == "single":
    display_single_dimensional_array(single_dimensional_array)
elif user_choice == "two-dimensional":
    display_two_dimensional_array(two_dimensional_array)
else:
    print("invalid choice. please enter 'single' or 'two-dimensional'.")