# Question 1
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)
# Question 2
print((2+3)*6/2 and 18.0)
# Question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

# Question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Question 4
print(palindrome("2704702208931031198668911301398022074072"))
print(palindrome("7798338247658278460338648728567428338977"))
print(palindrome("0974101607733149676776769413377061014790"))
print(palindrome("4257304920394478392772938744930294037524"))

# Question 5
def count_pattern_occurrences(text):
    """
    This function allows the user to find all occurrences of words that start with 'un',
    have unlimited letters, and end with 'an' in the given text.

    :param text: The input text to search in
    :return: The number of matches found
    """
    words = text.split()  # Split the text into words
    count = 0  # Counter for matches

    for word in words:
        if word.lower().startswith("un") and word.lower().endswith("an") and len(word) > 4:
            count += 1  # Increment count if the word meets criteria

    return count

# Example usage
sample_text = "An unknown human unitarian and uncertain unban urban"
print(count_pattern_occurrences(sample_text))  # Expected out

# Question 6
def divisor(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors
print(divisor(10))

#Question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # Replace numbers lower than or equal to 50 with "XX"
        random_numbers[i] = "XX"

# Print the modified list
print(random_numbers)

# Question 8
def is_valid_url(url):
    """
    Checks if the given string is a valid URL assuming the basic rules:
    - Starts with 'http://' or 'https://'
    - Contains at least one '.'
    - Has something after the last '.'

    :param url: The URL string to check
    :return: If valid return True, otherwise False
    """
    # A valid URL should start with 'http://' (7 characters) or 'https://' (8 characters)
    if not (url[:7] == "http://" or url[:8] == "https://"):
        return False

    # A valid URL should contain at least one '.'
    if "." not in url:
        return False

    # A valid URL should have something after the last '.'
    last_dot_position = url.rfind(".")  # Get the position of the last '.'
    if last_dot_position == len(url) - 1:  # If the last character is '.'
        return False

    return True

# Question 9
def years_since_birthday(birthday):
    """
    Calculates how many whole years have passed since the given birthday.
    :param birthday: The birthday in the format "DD-MM-YYYY"
    :return: Number of whole years passed
    """
    birthday = input("Enter your birthday (DD-MM-YYYY):")
    # Extract the birth year
    birth_year = int(birthday[-4:])  # Last 4 characters represent the year

    # Ask the user for the current year
    current_year = int(input("Enter the current year: "))

    # Calculate whole years passed
    return current_year - birth_year - 1

# Example usage
birthday = input("Enter your birthday (DD-MM-YYYY): ")
print("Whole years passed:", years_since_birthday(birthday))