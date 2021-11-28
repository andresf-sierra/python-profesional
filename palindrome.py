def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1] #Slices


def run():
    print(is_palindrome(1000)) #Error ingresado a propósito


if __name__=="__main__":
    run()
