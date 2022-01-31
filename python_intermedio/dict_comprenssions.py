def run():

    my_dict = {i: i**(1/2) for i in range(1,1001) }

    for k, v in my_dict.items():
        print(k , " : " , v, sep = "")

if __name__=="__main__":
    run()