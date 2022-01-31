def run():
    print(is_palindrome("ana"))

def is_palindrome(string: str = "default") -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]
    

if __name__ =='__main__':
    run()
