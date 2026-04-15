import re
import secrets
import string

def check_password_strength(password):
    strength = 0
    remarks = []
    
    # 1. Check Length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        remarks.append("Too short (minimum 8 characters).")

    # 2. Check Complexity (Uppercase, Lowercase, Numbers, Special characters)
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Missing mix of uppercase and lowercase.")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Missing numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Missing special characters.")

    return strength, remarks

def suggest_strong_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Using 'secrets' module for cryptographically secure random strings
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    return password

# Main Program
print("--- Thiranex Password Strength Analyzer ---")
user_pwd = input("Enter a password to test: ")

score, feedback = check_password_strength(user_pwd)

print(f"\nStrength Score: {score}/5")

if score == 5:
    print("Result: Very Strong Password!")
elif score >= 3:
    print("Result: Moderate Password.")
else:
    print("Result: Weak Password.")
    for note in feedback:
        print(f"- {note}")
    print(f"\nSuggested Strong Alternative: {suggest_strong_password()}")
    input("\nTask Complete! Press Enter to close this window...")