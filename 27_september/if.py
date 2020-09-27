def main():
    name = input("Enter your name :")
    if name.lower() == "jawid":
        print(f"Vilket superfint namn du har, {name}")
    else:
        if name[1] == "e":
            print("Yes du är bäst.")
        else:
            print("Jaha, någon ska ju ha det!")


if __name__ == '__main__':
    main()
