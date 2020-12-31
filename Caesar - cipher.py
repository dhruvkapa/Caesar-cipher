
print("Caesar Cipher Right and Left Shift\n------------------------------")

letters = "abcdefghijklmnopqrstuvwxyz"

# shift -- 4 and index = 1
encryptedWord = input("Enter the encrypted word: ")
index = 0



def left_shift():
    isTrue = True

    def encrypted_word_known_shift(shift, encrypted_word):
        decrypted_word = ""
        for letter in list(encrypted_word):
            if letter in letters:
                if letters.index(letter) + shift > len(letters) -1 :
                    getSubString = letters[letters.index(letter) + 1: len(letters)]
                    getLengthOfSubString = len(getSubString)
                    decrypted_word += letters[shift -1 - getLengthOfSubString]
                else:
                    decrypted_word += letters[(letters.index(letter)) + shift]

            else:
                decrypted_word += letter

        return decrypted_word




    def encrypted_word_unknown_shift(encrypted_word):
        global index

        while index < len(letters):
            decrypted_word = ""
            for letter in list(encrypted_word):
                if letter in letters:
                    if letters.index(letter) + index > len(letters) - 1 :
                        getSubString = letters[letters.index(letter) + 1 : len(letters)]
                        getLengthOfSubString = len(getSubString)
                        decrypted_word += letters[index - 1 - getLengthOfSubString]
                    else:
                        decrypted_word += letters[letters.index(letter) + index]
                else:
                    decrypted_word += letter
            print("Shift By {} : {}".format(index,decrypted_word))
            if index > len(letters)-1:
                isTrue = False
                break

            index += 1



    input_if_known_shift = input("Do you know the shift number? (Y/N): ")
    if input_if_known_shift.lower() == "y":
        inputShift = int(input("Enter the known shift of the cipher: "))
        print(encrypted_word_known_shift(inputShift,encryptedWord))

    elif input_if_known_shift.lower() == "n":
        while isTrue:
            encrypted_word_unknown_shift(encryptedWord)



def right_shift():
    isTrue = True

    def encrypted_word_known_shift(shift, encrypted_word):
        decrypted_word = ""
        for letter in list(encrypted_word):
            if letter in letters:
                if letters.index(letter) - shift < 0:
                    getSubString = letters[0: letters.index(letter)]
                    getLengthOfSubString = len(getSubString)
                    decrypted_word += letters[(-1 * shift) + getLengthOfSubString]
                else:
                    decrypted_word += letters[(letters.index(letter)) - shift]

            else:
                decrypted_word += letter

        return decrypted_word

    def encrypted_word_unknown_shift(encrypted_word):
        global index

        while index < len(letters):
            decrypted_word = ""
            for letter in list(encrypted_word):
                if letter in letters:
                    if letters.index(letter) - index < 0:
                        getSubString = letters[0: letters.index(letter)]
                        getLengthOfSubString = len(getSubString)
                        decrypted_word += letters[(-1 * index) + getLengthOfSubString]
                    else:
                        decrypted_word += letters[letters.index(letter) - index]
                else:
                    decrypted_word += letter
            print("Shift By {} : {}".format(index, decrypted_word))
            if index < (len(letters) -1) * -1:
                isTrue = False
                break

            index += 1

    input_if_known_shift = input("Do you know the shift number? (Y/N): ")
    if input_if_known_shift.lower() == "y":
        inputShift = int(input("Enter the known shift of the cipher: "))
        print(encrypted_word_known_shift(inputShift, encryptedWord))

    elif input_if_known_shift.lower() == "n":
        while isTrue:
            encrypted_word_unknown_shift(encryptedWord)



input_left_shift_or_right = input("Is the this a left shift or a right shift?: (R/L): ")
if input_left_shift_or_right.lower() == "l":
    left_shift()
elif input_left_shift_or_right.lower() =="r":
    right_shift()