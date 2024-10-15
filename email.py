class Email: # creation of the Email class with the various attributes
  def __init__(self, email_address, subject_line, email_content): # creates the constructor of the class
    self.email_address = email_address
    self.subject_line = subject_line
    self.email_content = email_content
    self.has_been_read = False  # Default unread status

  def mark_as_read(self): # marks the email as read
    self.has_been_read = True

inbox = []  # Empty list to store email objects

def populate_inbox(): # creates three sample emails and adds them to the inbox list.
  inbox.append(Email("welcome@hyperiondev.com", "Welcome to HyperionDev!",
                    "Hi there, welcome to our awesome bootcamp!"))
  inbox.append(Email("instructor@hyperiondev.com", "Great work on the bootcamp!",
                    "We're impressed with your progress so far, keep it up!"))
  inbox.append(Email("notifications@hyperiondev.com", "Your excellent marks!",
                    "Congratulations on your outstanding performance in the recent assessment!"))

def list_emails(): # iterates through inbox and displays email subject lines with corresponding numbers for selection.
  if not inbox:
    print("There are no emails in your inbox.")
    return

  print("\nInbox:")
  for i, email in enumerate(inbox):
    print(f"{i}. {email.subject_line}")

def read_email(): # allows users to choose an email by index, displays its content, and marks it as read
  list_emails()  # Display email list with numbers
  if not inbox:
    return

  while True:
    try:
      email_index = int(input("\nEnter the number of the email you want to read (or 'q' to quit): "))
      if email_index in range(len(inbox)):
        break
      else:
        print("Invalid selection. Please enter a valid email number or 'q' to quit.")
    except ValueError:
      if input("Invalid input. Enter 'q' to quit or a number: ").lower() == 'q':
        return

  email = inbox[email_index]
  print(f"\nFrom: {email.email_address}")
  print(f"Subject: {email.subject_line}")
  print(f"\n{email.email_content}")
  email.mark_as_read()
  print(f"\nEmail marked as read.\n")

def main():
  populate_inbox()  # Populate inbox with sample emails on startup

  while True: # provides the user interface with a menu and handles user interaction, calling appropriate functions based on the chosen option.
    print("\nEmail Simulator")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      read_email()
    elif choice == '2':
      unread_count = sum(not email.has_been_read for email in inbox)
      print(f"\nYou have {unread_count} unread emails.")
    elif choice == '3':
      print("\nQuitting application...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
  main()

