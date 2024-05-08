word = ""
while True:
    s = input("enter sign:")
    if s == "0":
        break
    if s in word:
        print(f"indentical characters are not allowed")
        break
    word += s 
