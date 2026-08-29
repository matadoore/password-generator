import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generate a random password with customizable options.
    
    Args:
        length (int): Length of the password (default: 12)
        use_uppercase (bool): Include uppercase letters (default: True)
        use_lowercase (bool): Include lowercase letters (default: True)
        use_digits (bool): Include digits (default: True)
        use_special (bool): Include special characters (default: True)
    
    Returns:
        str: A randomly generated password
    """
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected!")
    
    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    """Main function to run the password generator."""
    print("🔐 Welcome to the Password Generator! 🔐")
    print("-" * 40)
    
    try:
        # Get password length from user
        length = input("\nEnter password length (default 12): ").strip()
        length = int(length) if length else 12
        
        if length < 4:
            print("❌ Password length must be at least 4 characters!")
            return
        
        # Get character type preferences
        print("\nCharacter types to include:")
        use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        use_lowercase = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
        use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
        use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'
        
        # Generate password
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_digits=use_digits,
            use_special=use_special
        )
        
        # Display result
        print("\n" + "=" * 40)
        print(f"Generated Password: {password}")
        print("=" * 40)
        
        # Option to generate another
        if input("\nGenerate another? (y/n): ").lower() == 'y':
            main()
        else:
            print("Thanks for using Password Generator! 👋")
    
    except ValueError as e:
        print(f"❌ Error: {e}")
        main()


if __name__ == "__main__":
    main()
