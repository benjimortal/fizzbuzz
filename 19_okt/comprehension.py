def main():
    values = []
    for i in range(10):
        if i < 7:

            values.append(i * 2)
        #elif i > 7:
         #   values.append(i *3)
        else:
            values.append(i * 3)
    print(values)

    values = [i*2  if i < 7 else i*3 for i in range(10) if i < 8]
    print(values)
    x = 6
    msg = "low" if x < 6 else "high"
    print(msg)

    values = [i*2 for i in range(10)] # det här är en comprehension metod. och enkel sät ärn den där uppe.
    print(values)

    values = []
    for i in range(10):
        if i < 7:
            values.append(i * 2) # en vanlig for loop

    #en  comprehension metod
    values = [i *2 for i in range(100)]
    print(values)



if __name__ == '__main__':
    main()
