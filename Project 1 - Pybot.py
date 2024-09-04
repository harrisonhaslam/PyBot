# INTRO #

print("Hello! I am your Python bot, PyBot!")
user_name = input("What is your name? ")
print(f"Nice to meet you, {user_name}!")
age = input("How old are you? ")
bot_age = 3
age_difference = int(age) - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!")
random_color = ["red","blue","green","yellow","orange","purple"]
print(f"My favorite color is {random_color[4]}.")

## JOKE SECTION ##

print(f"Hey, {user_name}. Would you like to hear a joke?")

joke = "Why did the python get promoted?"
answer = "Because it always delivered “exceptional” results!"

yes_no = input("Yes or No? ")

if yes_no == "Yes" or "yes":
    print(joke)
    print(answer)
else:
    print("Well, that's a shame.")