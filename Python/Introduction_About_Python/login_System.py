def Login_System():
    users = {
        "Ahmed": "1239",
        "Amr": "6078"
    }
    
    username = input("Username: ")
    # task consecutive incorrect password attemps
    incorrect_attempts = 0
    while True:   #infinite loop until correct login or too many incorrect
        password = input("password: ")
        if username in users and password == users[username]:
            print("Success Welcome, " + username + "!")
            return #means exit function if login is correect
        else:
            print("Incorrect Entry.")
        incorrect_attempts += 1
        
        if incorrect_attempts  == 3:
            print("Too many incorrect password. Please contact Support.")
            return
        
Login_System()        