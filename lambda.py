people = [
    {"name": "Harry", "house": "Griy"},
    {"name": "Harriet", "house": "Grey"},
    {"name": "Harr", "house": "Style"},
]

people.sort(key=lambda person: person["name"])

print(people)