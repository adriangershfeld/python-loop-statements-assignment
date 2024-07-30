# Task 1: Your Mood Today
# Write a program that prints off different moods for each day of the week. 
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm".
# Using the range() function, loop through every day of the week and for each day,
# randomly select a mood from the list and print it. 
# Ensure that your program includes the use of the random module to select the mood.

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm', 'Tired']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


for i in range(len(days)):
    random_mood = random.choice(moods)
    print(f"On {days[i]} you were feeling {random_mood}.")
