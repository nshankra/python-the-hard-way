from sys import argv

cop, user_name = argv
prompt = '-'

print(f"Hi {user_name}, I'm the {cop} script.")
print("I'd like to ask you a few questions.")
print(f"do like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright {user_name}, so you said {likes} about liking me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""" )