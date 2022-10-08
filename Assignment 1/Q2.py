# Name: Ahmad Alqattan      ID:2192131011

def count_numbers(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

def check_Password(password):
    if len(password) < 8 or not password.isalnum() or count_numbers(password) < 2 or password[0].isdigit():
        return False
    else:
        return True

# print(check_Password("Hello123"))
# print(check_Password("Hello123%"))
# print(check_Password("123Hello"))
# True
# False
# False


