import re

text = open('Exercise_2.txt', 'r')
text_str = str(text.read())


def sum_text_numbers():
    numbers = re.findall(r'[+-]?\d+', text_str)
    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers += int(num)
    print('Sum of all numbers in the document returns', sum_of_numbers)


sum_text_numbers()
