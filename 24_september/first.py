def main():
    times = []
    while True:
        while True:
            minuets = input("Enter minutes for this run :")
            if minuets.isdigit():
                minuets = int(minuets)
                break

        while True:
            seconds = input("Enter seconds for this run :")
            if seconds.isdigit():
                seconds = int(seconds)
                break

        if minuets == 0 and seconds == 0:
            break

        time = minuets * 60 + seconds
        times.append(time)

    avg = sum(times) / len(times)
    minuets = int(avg // 60)
    print(avg, "seconds")

    #eller för second
    #seconds = avg - minuets * 60
    #print(seconds)
    print(minuets, "minutes")




if __name__ == '__main__':
    main()
