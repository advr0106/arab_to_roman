from arab_to_roman import convert_to_roman

while True:
    number = input("Introduce the number you want to convert to roman number (q = quit): ")
    if number.lower() == "q":
        break
    print(convert_to_roman(number))