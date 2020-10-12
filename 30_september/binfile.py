def main():
    with open("image (1).gif", "rb") as image_file:
        #image_file.seek(13)
        #for i in range(256):
        #  red = image_file.read(1)
        #    green = image_file.read(1)
        #   blue = image_file.read(1)
        #  print(i, red.hex(), green.hex(), blue.hex())

        with open("image (2).gif", "wb") as image_copy:
            data = image_file.read(19)
            image_copy.write(data)
            image_copy.write(bytearray([255, 0, 0]))
            image_file.seek(22, 0)
            data = image_file.read()
            image_copy.write(data)

if __name__ == '__main__':
    main()
