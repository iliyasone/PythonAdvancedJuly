print("program start")


def choose_action(exp: int):
    print("choose action call")
    
    def custom_power(x):
        print("custom power call")
        return x**exp
    return custom_power

super_function = choose_action(5)
loh_function = choose_action(4)

print(super_function.__closure__)