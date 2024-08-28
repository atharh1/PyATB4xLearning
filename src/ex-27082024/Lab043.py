def decorator(cust):
    def pre_program():
        cust()
        print("Its needed before ui")
        cust()
        print("close")
        cust()

    return pre_program()


@decorator
def sample_test():
    print("Sample test")