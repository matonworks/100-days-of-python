import random
from day_14_data import data
from day_14_logo import logo_1,logo_2

# Format account information into a printable string
def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Compare two accounts and return if the user is correct
def compare(account_a, account_b, user_choice):
    follower_a = account_a["follower_count"]
    follower_b = account_b["follower_count"]
    if user_choice == "a":
        return follower_a > follower_b
    elif user_choice == "b":
        return follower_b > follower_a
    else:
        print("Invalid choice")
        return False

# Main game function
def game():
    game_should_continue = True
    score = 0

    account_a = random.choice(data)
    account_b = random.choice(data)

    while account_b == account_a:
        account_b = random.choice(data)

    while game_should_continue:
        print(logo_1)
        print(f"Compare A: {format_account(account_a)}")
        print(logo_2)
        print(f"Against B: {format_account(account_b)}")
        
        user_choice = input("Who has more followers? Type 'a' or 'b': ").lower()

        is_correct = compare(account_a, account_b, user_choice)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")

            account_a = account_b
            account_b = random.choice(data)
            while account_b == account_a:
                account_b = random.choice(data)
            
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False


game()
