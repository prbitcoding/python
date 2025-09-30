c_password = "python@123"

unlocked = False
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1} of {max_attempts}: Enter password: ")
    attempts += 1

    if guess == c_password:
        unlocked = True
        break  

print(f"Unlocked? {unlocked} | Tries used: {attempts}")
