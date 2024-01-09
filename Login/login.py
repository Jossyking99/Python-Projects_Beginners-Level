import time

# Define constants for the correct username and password
CORRECT_USERNAME = 'Jweb'
CORRECT_PASSWORD = 'wonderland'

def get_user_input():
   """Prompt the user to enter their username and password, and return them."""
   try:
       username_input = input('Username: ')
       password_input = input('Password: ')
       return username_input, password_input
   except Exception as e:
       print("An error occurred while getting user input: ", str(e))
       return None, None

def check_credentials(username_input, password_input):
   """Check if the provided username and password match the correct ones."""
   if username_input == CORRECT_USERNAME and password_input == CORRECT_PASSWORD:
       return True
   else:
       return False

def print_messages(is_correct):
   """Print the appropriate messages based on whether the credentials are correct."""
   if is_correct:
       print('Access granted')
       print('Please wait')
       time.sleep(5)
       print('Ok... Loading...')
       time.sleep(1)
       print('...')
       time.sleep(1)
       print('...')
       print('Alright you have security clearance. Pulling up the secret mainframe.')
   else:
       print('Username or Password incorrect')

def main():
   """Main function to run the program."""
   username_input, password_input = get_user_input()
   if username_input is not None and password_input is not None:
       is_correct = check_credentials(username_input, password_input)
       print_messages(is_correct)

if __name__ == "__main__":
   main()
