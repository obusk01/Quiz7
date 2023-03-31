# Quiz 7: Olivia Busk
def hash_spam(string):
    total = 0
    index = 0
    while index < len(string):
        for ch in string:
            if ch == "#":
                total += 1
                index += 1
            else:
                index += 1
        return total
    if total >= 4:
        print("This tweet will be considered as a spam!")


print(hash_spam("#My n#ame# is #Olivia# #Bus#k"))
print(hash_spam("#My name is Olivia# #Bus#k"))
