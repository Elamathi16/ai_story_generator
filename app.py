import random

# Story elements
genres = [
    "Fantasy", "Science Fiction", "Horror", "Mystery",
    "Adventure", "Romance", "Thriller", "Historical"
]

names = ["Arjun", "Maya", "Karthik", "Anika", "Ravi", "Diya"]

places = [
    "an ancient temple",
    "a mysterious forest",
    "a space station",
    "a haunted village",
    "a secret laboratory",
    "an abandoned castle"
]

twists = [
    "the hero discovers a hidden power",
    "the villain is actually a close friend",
    "a secret portal opens to another world",
    "time suddenly stops",
    "a hidden treasure changes everything",
    "a robot develops human emotions"
]

# Random selections
genre = random.choice(genres)
name = random.choice(names)
place = random.choice(places)
twist = random.choice(twists)

# Story generation
story = f"""
Genre: {genre}

Once upon a time, a young person named {name} was exploring {place}.
Everything seemed normal at first, but strange things soon started happening.

While exploring deeper, {name} discovered clues that something unusual was hidden there.
The journey became more dangerous and exciting with every step.

Suddenly, {twist}. This unexpected event changed the entire situation.

With courage and determination, {name} faced every challenge and finally solved the mystery.

In the end, the adventure taught {name} an important lesson about bravery, friendship, and believing in oneself.
"""

print(story)