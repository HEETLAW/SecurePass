# SecurePass

## SecurePass: Advanced Password Management Tool

SecurePass is an advanced password management tool designed to ensure the strength and security of user passwords. This tool provides real-time password assessment, secure password generation, and comprehensive feedback on password strength and entropy. Built with a user-friendly graphical interface, SecurePass helps users create and manage robust passwords to enhance their cybersecurity posture.

### Key Features:

1. **Real-Time Password Assessment:**
   - Assesses the strength of passwords based on length, uppercase and lowercase letters, digits, and special characters.
   - Provides instant feedback and strength ratings from "Very Weak" to "Very Strong".

2. **Common Password Check:**
   - Checks against a list of common passwords to prevent the use of easily guessable passwords.

3. **Password Generation:**
   - Generates strong, random passwords with a mix of characters for enhanced security.

4. **Entropy Calculation:**
   - Calculates and displays the entropy of the password, providing an additional measure of password strength.

5. **User-Friendly Interface:**
   - Easy-to-use graphical interface for password entry, real-time assessment, and feedback.
   - Suggestions for generating strong passwords.

6. **History Tracking:**
   - Maintains a history of recent password assessments for user reference.

### How to Get and Use SecurePass

#### Step 1: Clone the Repository

Open Terminal: Open your terminal (Command Prompt, PowerShell, or any terminal you use).

Clone the Repository: Use the git clone command followed by the URL of your GitHub repository.

```bash
git clone https://github.com/HEETLAW/SecurePass.git
```

#### Step 2: Navigate to the Repository Directory

```bash
cd SecurePass
```

#### Step 3: Ensure Required Dependencies are Installed

Ensure you have Python and the `zxcvbn` library installed. If not, you can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

#### Step 4: Run the Script

You can now run your SecurePass tool. Assuming your main script is named `SecurePass.py`, you would run:

```bash
python SecurePass.py
```

#### Step 5: Using the Tool

Follow the graphical user interface to use the various functionalities:

- **Password Entry:** Enter a password to receive real-time assessment, feedback, and entropy calculation.
- **Generate Strong Password:** Click the button to generate a strong, random password.
- **View Feedback:** Review the feedback provided for password improvements.

### Example Usage

- **Real-Time Assessment:**
  - Enter a password to receive immediate feedback on its strength and suggestions for improvement.
  
- **Generate Strong Password:**
  - Click the "Generate Strong Password" button to get a suggestion for a strong, randomly generated password.

- **Entropy Calculation:**
  - View the entropy calculation to understand the strength of the password in bits.

SecurePass enhances password security by providing users with the tools and information needed to create strong, secure passwords, essential for protecting sensitive information in today's digital world.
