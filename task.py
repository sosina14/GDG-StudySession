#1, Write a function that sums numbers in a list.

def sum_num(list1):
    return sum(list1)

list1 = [1, 5, 7, 9, 3]

print("Sum of the numbers ", sum_num(list1) ,".")

#2, Print even numbers between 1 and 20 using a loop.
for numbers in range(1,20):
    if numbers % 2 == 0:{
        print(numbers)
    }
#3, Write a program to find the largest number in a list.

def find_largest_number(numbers):
    if not numbers:
        return "The list is empty."
    return max(numbers)

numbers = [3, 45, 21, 78, 99, 34]
print("The largest number is:", find_largest_number(numbers))

    
#4, Write a Python program that counts the frequency of each word in a given sentence.

def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower().strip(",.?!")  # Normalize case and remove punctuation
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

sentence = "Hello world! Hello everyone. Welcome to the world of Python."
frequencies = word_frequency(sentence)
print("Word frequencies:", frequencies)
