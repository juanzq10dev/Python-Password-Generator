import random 
import string

password_length = 12

def generate_password():
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(password_length))
    
    return random_string