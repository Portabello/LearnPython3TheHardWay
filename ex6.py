# declares variable
types_of_people = 10
# declares string with above variable
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
#prints variables
print(x)
print(y)
#prints variables formatted within string
print(f"I said: {x}")
print(f"I also said: '{y}'")
#declare boolean and string with blank variable format
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#prints string formatted with variable
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
