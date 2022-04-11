def run():

    #Reto1
    #squeares = [i**2 for i in range(1,101) if i%3 != 0]
    #print(squeares)

    #Reto2
    multiplos = [i for i in range(1,100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(multiplos)

if __name__ == '__main__':
    run()
