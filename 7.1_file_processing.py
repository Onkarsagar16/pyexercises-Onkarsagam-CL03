# Problems found in names.txt:
# 1. Some names have capital and small letters mixed.
# 2. Some names have extra spaces at the beginning.
# 3. There are empty lines between some names.
# 4. Some last names have more than one word.

# 1. In: Names from names.txt.
# 2. Process: Remove empty lines and extra spaces.
# Make the capital letters consistent.
# Keep multi-word last names together.
# Sort the names by last name.
# 3. Out: cleaned_names.txt with sorted names.
# 4. The first word is the first name.
# The remaining words are the last name.

with open("names.txt", "r") as file:
    names = file.readlines()

cleaned_names = []

for name in names:
    name = name.strip()

    if name == "":
        continue

    name = " ".join(name.split())
    name = name.title()

    cleaned_names.append(name)

def get_last_name(name):
    return " ".join(name.split()[1:]).lower()

cleaned_names.sort(key=get_last_name)

with open("cleaned_names.txt", "w") as file:
    for name in cleaned_names:
        file.write(name + "\n")

print("Names cleaned and saved successfully!")
print("Original lines:", len(names))
print("Cleaned names:", len(cleaned_names))
print("First name:", cleaned_names[0])
print("Last name:", cleaned_names[-1])
