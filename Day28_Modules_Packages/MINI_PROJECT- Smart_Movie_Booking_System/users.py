users_list = []


def add_user():

    user = {
        "user_id": input("Enter User ID: ").strip(),
        "name": input("Enter User Name: ").strip(),
        "phone_no": input("Enter Phone Number: ").strip(),
        "email": input("Enter Email: ").strip()
    }

    users_list.append(user)

    print(f"User '{user['name']}' added successfully!")


def view_users():

    if not users_list:
        print("No users found!")
        return

    print("\n----- Registered Users -----")

    for user in users_list:

        print(
            f"\nUser ID: {user['user_id']}"
            f"\nName: {user['name']}"
            f"\nPhone: {user['phone_no']}"
            f"\nEmail: {user['email']}"
        )

        print("-------------------------")