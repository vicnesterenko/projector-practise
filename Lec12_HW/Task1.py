def is_admin(func):
    def wrapper(**kwargs):
        user_type = kwargs.get("user_type")
        if user_type == "admin":
            return func(**kwargs)
        else:
            try:
                raise ValueError("Permission denied")
            except ValueError as e:
                print(f"ValueError: {e}")

    return wrapper


@is_admin
def show_customer_receipt(user_type: str) -> str:
    receipt = "2 pills aspirin per 1 week"
    print(f"User with role '{user_type}' gets receipt: {receipt}")


show_customer_receipt(user_type="admin")
# User with role 'admin' gets receipt: 2 pills aspirin per 1 weeks
show_customer_receipt(user_type="user")
# ValueError: Permission denied
