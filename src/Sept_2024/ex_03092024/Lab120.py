# Web Automation Selenium
# Page - You are going automate


class LoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "chetan@gmail.com" and self.password == "Test123":
            print("You are logged in")
        else:
            print("Not Allowed to login")


email = input("Enter the email\n")
password = input("Enter the password\n")

login_object = LoginPage(email, password)
login_object.login_confirm()
