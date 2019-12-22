people = 30 
cars = 40
truck = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide")

if truck > cars:
    print("That's too many trucks.")
elif truck < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > truck:
    print("Alright, let's stay home then.")
else:
    print("Fine, let's stay home then.")