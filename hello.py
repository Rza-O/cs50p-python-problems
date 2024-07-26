# Ask user your name
name = input("What's Your Name?").strip().title()

#cpitalizing
#name = name.strip().title()

#split users name into first and last

first, last = name.split(" ")

#say hello to user
#print(f"Hello, {name}")

#example of split function
print(f"Hello {first}")
