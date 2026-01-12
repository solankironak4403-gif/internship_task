# function to cheak pelindrome number
def is_palindrome_number(num):
    original_num = str(num)
    reversed_num = original_num[::-1]
    return original_num == reversed_num
number = 121
if is_palindrome_number(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")
    