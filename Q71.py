# Quiz 7: Olivia Busk
def count_hashtags(string):
    total=0
    index=0
    while index < len(string):
        for ch in string:
            if ch == "#":
                total += 1
                index += 1
            else:
                index += 1
        return total

print(count_hashtags("#My name is #Olivia #Busk"))
