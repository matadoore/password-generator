# 🔐 Password Generator

A beginner-friendly Python password generator with customizable options. Generate strong, random passwords with the character types of your choice!

## Features

✨ **Easy to Use** - Simple command-line interface
🎛️ **Customizable** - Choose password length and character types
🔤 **Multiple Character Types** - Uppercase, lowercase, digits, and special characters
🔄 **Reusable** - Generate multiple passwords in one session
📚 **Well-Documented** - Clear code with helpful comments

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/matadoore/password-generator.git
cd password-generator
```

2. No additional installation needed! Just run the script.

## Usage

### Interactive Mode (Recommended for Beginners)

Run the script and follow the prompts:
```bash
python password_generator.py
```

The program will ask you:
- **Password length** - How many characters long (default: 12)
- **Character types** - Which types to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (!@#$%^&*)

### Example Session

```
🔐 Welcome to the Password Generator! 🔐
----------------------------------------

Enter password length (default 12): 16

Character types to include:
Include uppercase letters? (y/n, default y): y
Include lowercase letters? (y/n, default y): y
Include digits? (y/n, default y): y
Include special characters? (y/n, default y): y

========================================
Generated Password: K9@mLpQx#vR2sWjN
========================================

Generate another? (y/n): y
```

### Using as a Module

You can also import and use the `generate_password()` function in your own code:

```python
from password_generator import generate_password

# Generate a 20-character password with all character types
password = generate_password(length=20)
print(f"Your password: {password}")

# Generate a 12-character password with only letters and digits
password = generate_password(
    length=12,
    use_special=False
)
print(f"Your password: {password}")
```

## Function Parameters

```python
generate_password(
    length=12,              # Password length (default: 12)
    use_uppercase=True,     # Include A-Z (default: True)
    use_lowercase=True,     # Include a-z (default: True)
    use_digits=True,        # Include 0-9 (default: True)
    use_special=True        # Include special chars (default: True)
)
```

**Returns:** A randomly generated password string

## Learning Concepts

This project is great for learning:
- 📚 Python string manipulation
- 🎲 Random number generation
- 🔄 Loop and conditional statements
- 💬 User input and output
- 🔧 Functions and parameters
- 📝 Error handling

## Tips for Beginners

1. **Strong passwords** should:
   - Be at least 12 characters long
   - Include mixed character types
   - Avoid dictionary words
   - Avoid personal information

2. **Running the script:**
   - Make sure Python 3 is installed: `python --version`
   - Run from the project directory
   - Press Ctrl+C to exit anytime

3. **Customizing the code:**
   - Try changing the default password length
   - Modify the emoji in the welcome message
   - Add a feature to save passwords to a file (advanced!)

## Common Issues

**Issue:** `python: command not found`
- **Solution:** Use `python3` instead, or check that Python is installed and added to your PATH

**Issue:** `ValueError: At least one character type must be selected!`
- **Solution:** Make sure you select at least one character type when prompted

## Future Enhancement Ideas

- 🎯 Generate multiple passwords at once
- 💾 Save generated passwords to a file
- 📋 Copy password to clipboard automatically
- 🎨 Color-coded output for different character types
- 🔍 Password strength checker
- ⌨️ Command-line arguments for automation

## Contributing

Found a bug or have an idea? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Resources

- [Python random module documentation](https://docs.python.org/3/library/random.html)
- [Python string module documentation](https://docs.python.org/3/library/string.html)
- [Password Security Best Practices](https://www.cisa.gov/sites/default/files/publications/passphrases_700-63b_mt_v3.pdf)

---

**Happy Coding! 🚀**

Have questions? Feel free to open an issue or start a discussion in the repository!
