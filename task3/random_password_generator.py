import random
import string

def get_password_length():
    """Enforces minimum 8 characters and validates integer input."""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length >= 8:
                return length
            else:
                print("❌ Security Warning: Password length must be at least 8 characters. Try again.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid whole number.")

def get_character_pool():
    """Prompts user for character types and ensures at least 2 types are selected."""
    while True:
        print("\n--- Select Character Types to Include ---")
        use_upper = input("Include Uppercase letters? (A-Z) [y/n]: ").strip().lower() == 'y'
        use_lower = input("Include Lowercase letters? (a-z) [y/n]: ").strip().lower() == 'y'
        use_digits = input("Include Numbers? (0-9) [y/n]: ").strip().lower() == 'y'
        use_symbols = input("Include Symbols? (@, #, $, etc.) [y/n]: ").strip().lower() == 'y'

        # Count how many types were selected
        selected_count = sum([use_upper, use_lower, use_digits, use_symbols])

        # Input Validation: At least 2 types must be selected
        if selected_count >= 2:
            char_pool = ""
            mandatory_chars = []

            # Building the pool and ensuring at least one character from each selected type
            if use_upper:
                char_pool += string.ascii_uppercase
                mandatory_chars.append(random.choice(string.ascii_uppercase))
            if use_lower:
                char_pool += string.ascii_lowercase
                mandatory_chars.append(random.choice(string.ascii_lowercase))
            if use_digits:
                char_pool += string.digits
                mandatory_chars.append(random.choice(string.digits))
            if use_symbols:
                char_pool += string.punctuation
                mandatory_chars.append(random.choice(string.punctuation))

            return char_pool, mandatory_chars
        else:
            print("❌ Security Restriction: You must select at least 2 character types for a strong password!")

def generate_password(length, char_pool, mandatory_chars):
    """Generates the password ensuring all selected criteria are met."""
    # Calculate how many remaining characters we need to pick randomly
    remaining_length = length - len(mandatory_chars)
    
    # Pick random characters from the combined pool
    random_pool_chars = [random.choice(char_pool) for _ in range(remaining_length)]
    
    # Combine mandatory characters with the random ones
    password_list = mandatory_chars + random_pool_chars
    
    # Shuffle the list so the mandatory characters aren't always at the beginning
    random.shuffle(password_list)
    
    # Convert list back to a string
    return "".join(password_list)

def main():
    print("=========================================")
    print("       🔐 SECURE PASSWORD GENERATOR     ")
    print("=========================================")
    
    while True:
        # Step 1: Get validated password length
        length = get_password_length()
        
        # Step 2: Get character pool based on user choices
        char_pool, mandatory_chars = get_character_pool()
        
        # Step 3: Generate the password
        password = generate_password(length, char_pool, mandatory_chars)
        
        # Step 4: Display the result
        print("\n" + "="*40)
        print(f"🔑 Generated Password: {password}")
        print("="*40 + "\n")
        
        # Step 5: Option to generate another password without restarting
        repeat = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if repeat not in ['yes', 'y']:
            print("\nThank you for using Password Generator. Stay safe online! 👋")
            break

if __name__ == "__main__":
    main()