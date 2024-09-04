# PyBot: My First Python Mini Bot

Welcome to **PyBot**! This is a simple Python bot that interacts with you by asking your name, age, and favorite color. It's a beginner-friendly project designed to help you understand basic Python concepts like `print`, `input`, `variables`, and `lists`.

## Features

- Greets the user and asks for their name.
- Asks for the user's age and compares it to the bot's age.
- Asks for the user's favorite color and shares its own favorite color.

## Code Explanation

```python
print("Hello! I am your Python bot, PyBot!")

user_name = input("What is your name? ")
print(f"Nice to meet you, {user_name}!")

age = input("How old are you? ")
bot_age = 3
age_difference = int(age) - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!")

random_color = ["red", "blue", "green", "yellow", "orange", "purple"]
print(f"My favorite color is {random_color[4]}")
```

### How the Code Works

1. **Greeting and Name Input:**
   - The bot starts by greeting the user and asks for their name using the `input()` function.
   - It then displays a personalized message using an f-string.

2. **Age Comparison:**
   - The bot asks for the user's age and calculates the difference between the user's age and the bot's age (which is set to 3).
   - It displays the age difference to the user.

3. **Favorite Color Interaction:**
   - The bot asks the user for their favorite color and responds with a comment.
   - It then shares its own favorite color, selected from a predefined list.

## How to Run the Code

1. Ensure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/).
2. Copy the code into a file named `pybot.py`.
3. Open a terminal or command prompt and navigate to the directory containing `pybot.py`.
4. Run the following command:

    ```bash
    python pybot.py
    ```

5. Follow the prompts to interact with PyBot!

## Future Improvements

- Add more questions for a more engaging conversation.
- Implement error handling for non-numeric input in the age question.
- Randomize the bot's favorite color from the list each time.

## License

This project is open source and available under the [MIT License](LICENSE).

---

