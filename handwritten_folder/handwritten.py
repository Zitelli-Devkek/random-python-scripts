import pywhatkit as kit  # pip install pywhatkid

# here goes the text
text = input(" Enter the text you want to handwrite:\n\n ")


# here goes the file's name
file_name = input("\n Enter what you would like the file's name to be:\n\n ")


# here you print the different colors you can choose
print("\n Which color you'd like? You can can choose:\n")
print("1.black")
print("2.white")
print("3.red")
print("4.lime")
print("5.blue")
print("6.yellow")
print("7.cyan")
print("8.magenta")
print("9.silver")
print("10.gray")
print("11.maroon")
print("12.olive")
print("13.green")
print("14.purple")
print("15.teal")
print("16.navy\n")


# here you ask for the specific color, using numbers
letter_color = int(input(" Please, just enter the number here:\n\n "))

rgb_color = (1, 1, 1)  # random values

# start colors
if (letter_color == 1):  # black
    rgb_color = (0, 0, 0)

elif(letter_color == 2):  # white
    rgb_color = (255, 255, 255)

elif(letter_color == 3):  # red
    rgb_color = (255, 0, 0)

elif(letter_color == 4):  # lime
    rgb_color = (0, 255, 0)

elif(letter_color == 5):  # blue
    rgb_color = (0, 0, 255)

elif(letter_color == 6):  # yellow
    rgb_color = (255, 255, 0)

elif(letter_color == 7):  # cyan, or aqua
    rgb_color = (0, 255, 255)

elif(letter_color == 8):  # magenta
    rgb_color = (255, 0, 255)

elif(letter_color == 9):  # silver
    rgb_color = (192, 192, 192)

elif(letter_color == 10):  # gray
    rgb_color = (128, 128, 128)

elif(letter_color == 11):  # maroon
    rgb_color = (128, 0, 0)

elif(letter_color == 12):  # olive
    rgb_color = (128, 128, 128)

elif(letter_color == 13):  # green
    rgb_color = (0, 128, 0)

elif(letter_color == 14):  # purple
    rgb_color = (128, 0, 128)

elif(letter_color == 15):  # teal
    rgb_color = (0, 128, 128)

elif(letter_color == 16):  # navy
    rgb_color = (0, 0, 128)
# end colors
else:

    # in case someone is as dumb as a rock
    print("Error. Try again using numbers from 1 to 16.")
    letter_color = input("Please, just enter the number here: ")


kit.text_to_handwriting(text, save_to=(file_name + ".png"), rgb=(rgb_color))
# text equals the text that is going to be handwritten. save_to has as a value the name of the file, to find it easier in the folder of the
# handwritten.py. and rgb has as a value the letter's color.
