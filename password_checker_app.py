import streamlit as st
import re

# Title of the app
st.title("🔒 Password Strength Checker")

# Input box for password
password = st.text_input("Enter your password:", type="password")

# Function to check password strength
def check_strength(password):
    if len(password) < 8:
        return "Weak"
    
    # Check for different criteria
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    
    if all([upper, lower, digit, special]):
        return "Strong"
    else:
        return "Medium"

# Display the strength with color
if password:
    strength = check_strength(password)
    
    if strength == "Weak":
        st.error(f"Password Strength: {strength}")
    elif strength == "Medium":
        st.warning(f"Password Strength: {strength}")
    else:
        st.success(f"Password Strength: {strength}")

    # Optional: Show which rules are missing
    st.write("Password Rules:")
    st.write(f"- Minimum 8 characters ✅" if len(password) >= 8 else "- Minimum 8 characters ❌")
    st.write(f"- Uppercase letter ✅" if re.search(r"[A-Z]", password) else "- Uppercase letter ❌")
    st.write(f"- Lowercase letter ✅" if re.search(r"[a-z]", password) else "- Lowercase letter ❌")
    st.write(f"- Number ✅" if re.search(r"[0-9]", password) else "- Number ❌")
    st.write(f"- Special character ✅" if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else "- Special character ❌")
