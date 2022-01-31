def remove_duplicates(some_list):
    return set(some_list)

def run():
    my_list = [1, 1, 2, 2, 3, 4, 3]
    print(my_list)
    my_list = remove_duplicates(my_list)
    print(my_list) 

run()


