def run():
    # squares = []
    # primeros = 100
    # for i in range(1, primeros+1, 1):
    #     if i%3 == 0:
    #         continue
    #     else:
    #         squares.append(i**2)
    
    squares = [i for i in range(1,100000) if i%36 == 0]

    

    print(squares)
    # for i in squares:
    #     print(i)

    

if __name__=='__main__':
        run()
