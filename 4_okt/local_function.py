#LEGB   L = Local.  E = Enclosing (en function som är innuti en annan function). G = Global. B = Buildin

value = 10  #global value


def function():
    value = 11 # local i function
    print(value)

    def inner():
        value = 12
        print(value)

    inner()


def main():
    print(value)
    function()



if __name__ == '__main__':
    main()
