def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese, {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for party!'\nget a blanket.' ")

print("We can just give the function number directly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers =50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)