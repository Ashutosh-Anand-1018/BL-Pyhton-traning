def calculate_sum(x: int, y: int):
    """
    This function takes two numbers as input and returns their sum.
    """
    return x + y
# 1.Describing variables and 2. Using f-strings to print the result
try:
    total_sum = int(input("Enter value for total_sum "))
    bonus_points = int(input("Enter value for bonus_points "))
    print(f"Data type of total_sum is {type(total_sum)} and bonus_points is {type(bonus_points)}")
    final_score = calculate_sum(total_sum, bonus_points)
    print(f"Final score is {final_score}")
except:
    print("Try again and Enter a proper value.")