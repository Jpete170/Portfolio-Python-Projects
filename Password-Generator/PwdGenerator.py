import string
import random

if __name__=="__main__":
    stringLower = string.ascii_lowercase
    stringUpper = string.ascii_uppercase
    stringDigits = string.digits
    stringPunctuation = string.punctuation

    plen = int(input("Enter desirable password length: "))

    s_array = []
    s_array.extend(list(stringLower))
    s_array.extend(list(stringUpper))
    s_array.extend(list(stringDigits))
    s_array.extend(list(stringPunctuation))

    print("".join(random.sample(s_array, plen)))