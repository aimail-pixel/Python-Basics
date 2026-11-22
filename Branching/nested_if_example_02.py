"Core Basics example: Nested if (2)"

def main():
    logged_in, admin = True, False
    if logged_in:
        if admin:
            print("Manage")
        else:
            print("View")
    else:
        print("Sign in")


if __name__ == "__main__":
    main()
