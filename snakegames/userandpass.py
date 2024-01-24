# Predefined username and password
# Index         0       1        2         3             

usernames = ["Lucas", "Faye", "Brandon", "Margel"]
passwords = ["Kulas", "Pingot", "Rogbu", "Gamer"]

# Input username and password

entered_username = input("Enter your Username: ")
entered_password = input("Enter your Password: ")

# Loop through the list of usernames and passwords

for i in range(len(usernames)):
        if entered_username == usernames[i] and entered_password == passwords[i]:
            print("Welcome," + " " + usernames[i])
            break
else: 
    print("ACCOUNT NOT FOUND")
