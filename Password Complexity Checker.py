import re

def calculate_password_strength(password):
    score = 0
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_criteria = re.search(r'[@$!%*?&#]', password)
    
    if length_criteria:
        score += 2
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_criteria:
        score += 1
    
    return score

def provide_feedback(score):
    if score < 3:
        return "Weak password. Try adding more characters and including uppercase, lowercase, numbers, and special characters."
    elif score < 5:
        return "Moderate password. Consider adding more character variety to strengthen it."
    else:
        return "Strong password."

def main():
    password = input("Enter a password: ")
    score = calculate_password_strength(password)
    feedback = provide_feedback(score)
    print(f"Password Strength: {score}/6")
    print(feedback)

if __name__ == "__main__":
    main()
