def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
            "firstname": "Facundo",
            "lastname": "Garcia"
            }
    for i, v in my_dict.items():
        print(i + ": " + v)

    super_list = [
        {"firstname": "Facundo","lastname": "Garcia"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "Jose", "lastname": "Garcia"},
    ]
    i=0
    for i in super_list:
        for key, values in i.items():
            print(key,"\t:", values)

    #for i in super_list:
	#    print(i.items())

    super_dict = {

        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating nums": [1.1, 4.5, 6.43]
    }

    for i in range(largo):
        for key, value in super_dict.items():
            print(key , " -- ", value[i])

    for key, value in super_dict.items():
        print(key , " -- ", value)

if __name__ == '__main__':
    run()
