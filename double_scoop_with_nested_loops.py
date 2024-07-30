# Task 1: Your Mood Tracker 
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week.
# Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day.
# For each time, randomly select a mood from a predefined list and print it.
# Use the random module again to randomly select the mood.

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm', 'Tired']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['Morning', 'Afternoon', 'Evening']

for day in days:
    print(f"{day}: ")

    for time in times:
        random_mood = random.choice(moods)
        print(f"  {time}: {random_mood}")