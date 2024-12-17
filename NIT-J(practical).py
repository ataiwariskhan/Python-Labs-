#!/usr/bin/env python
# coding: utf-8

# In[6]:


#wap that writes a data to a file in such a way that each character after a full stop is capatilized and all the numbers are written in barcket 
import re

def format_text(input_text):
    # Capitalize characters after a full stop
    sentences = re.split(r'(\. )', input_text)
    formatted_text = ""
    for i in range(len(sentences)):
        if i > 0 and sentences[i-1] == '. ':
            formatted_text += sentences[i].capitalize()
        else:
            formatted_text += sentences[i]
    
    # Enclose numbers in brackets
    formatted_text = re.sub(r'(\d+)', r'(\1)', formatted_text)
    
    return formatted_text

def write_to_file(input_file, output_file):
    # Read from input file
    with open(input_file, 'r') as file:
        data = file.read()
    
    # Format the text
    formatted_data = format_text(data)
    
    # Write to output file
    with open(output_file, 'w') as file:
        file.write(formatted_data)
    print(f"Formatted data has been written to {output_file}")

# Example usage
if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"

    # Create an example input file
    with open(input_filename, 'w') as file:
        file.write("hello class. today is CPBP lab exam . the year is 2024 and 28 people are attendeding.")

    # Process the file and write the result
    write_to_file(input_filename, output_filename)

    # Display the output
    with open(output_filename, 'r') as file:
        print("\nFormatted Output:")
        print(file.read())


# In[5]:


#program-2(create a program that find all occuerence of a pattern in a string,including overlapping matches)
import re

class PatternFinder:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.regex = re.compile(pattern)

    def _find_overlapping_matches(self, string: str):
        matches = []
        start = 0
        while start < len(string):
            match = self.regex.search(string, start)
            if not match:
                break
            matches.append((match.start(), match.group()))
            start = match.start() + 1  # Move forward by one to allow overlapping
        return matches

    def find_all(self, string: str):
        return self._find_overlapping_matches(string)

# Example usage
if __name__ == "__main__":
    string = "ABABA"
    pattern = "ABA"
    finder = PatternFinder(pattern)
    matches = finder.find_all(string)
    print("All Overlapping Matches:")
    for index, match in matches:
        print(f"Match at index {index}: '{match}'")


# In[2]:


#wap to accept a list of integer from the user and find two numbers in the list whose sum is closest to zero
def find_closest_to_zero(nums):
    # If there are fewer than two numbers, return None
    if len(nums) < 2:
        return None
    
    # Sort the list first
    nums.sort()
    
    # Initialize two pointers
    left = 0
    right = len(nums) - 1
    
    # Initialize variables to keep track of the closest sum and the pair
    closest_sum = float('inf')  # start with an infinitely large value
    closest_pair = (None, None)
    
    # Use two-pointer technique to find the closest sum to zero
    while left < right:
        current_sum = nums[left] + nums[right]
        
        # If the current sum is closer to zero, update the closest pair
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            closest_pair = (nums[left], nums[right])
        
        # Move the pointers based on the current sum
        if current_sum < 0:
            left += 1  # If sum is negative, move left pointer to the right to increase the sum
        elif current_sum > 0:
            right -= 1  # If sum is positive, move right pointer to the left to decrease the sum
        else:
            # If the sum is exactly zero, we can return the pair immediately
            return closest_pair
    
    return closest_pair

# Input from the user
nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Call the function and print the result
result = find_closest_to_zero(nums)
if result:
    print(f"The two numbers whose sum is closest to zero are: {result[0]} and {result[1]}")
else:
    print("Not enough numbers to find a pair.")


# In[ ]:




