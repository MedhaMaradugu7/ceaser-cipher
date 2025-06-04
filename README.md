# Caesar Cipher

A simple Python implementation of the Caesar cipher, a classic encryption technique that shifts letters in the alphabet by a specified number of positions. This program supports both encryption and decryption, preserving case and non-alphabetic characters.

## Features

- Encrypts and decrypts text using the Caesar cipher algorithm.
- Handles both uppercase and lowercase letters.
- Preserves non-alphabetic characters (e.g., spaces, punctuation).
- Command-line interface for user interaction.
- Validates shift values (0–26) and provides feedback for invalid inputs.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/caesar-cipher.git
   ```
2. Navigate to the project directory:

   ```bash
   cd caesar-cipher
   ```

## Usage

1. Run the script:

   ```bash
   python caesar.py
   ```
2. Follow the prompts:
   - Enter `1` to encrypt, `2` to decrypt, or `3` to exit.
   - Provide a word or phrase to process.
   - Enter a shift value (0–26).
3. Example:

   ```
   Enter 1 if encrypt
   2 if decrypt
   3 for exit: 1
   Enter the word: Hello, World!
   Enter the shift key: 3
   Khoor, Zruog!
   ```

## Code Structure

- `caesar.py`: Main script containing the Caesar cipher implementation and command-line interface.
  - `caesar(text, shift, encrypt=True)`: Core function to encrypt or decrypt text.
  - Main loop: Handles user input and program flow.


