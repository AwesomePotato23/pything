import time

time.sleep(3.5)
print("Welcome to the Pything setup!")
time.sleep
print("")
print(" == SETUP MENU == ")
print("Welcome to Pything!")
print("Please answer these Qs.")

username = input("Enter a name: ")
print("Welcome, " + username + "!")
password = input("Make a password: ")
if password == "" or password == " ":
  print("PLEASE ENTER A PASSWORD NEXT TIME.")
  quit()
else:
  import survey
