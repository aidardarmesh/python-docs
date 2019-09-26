def decorator(fn):
    def wrapper(arg1, arg2):
        print("Look what I've found")
        fn(arg1, arg2)

    return wrapper

@decorator
def print_full_name(first_name, last_name):
    print(first_name, last_name)

print_full_name("Aidar", "Darmesh")