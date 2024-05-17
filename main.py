def readBook():  
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def countWords():
    text = readBook()
    words = text.split()
    return len(words)

def countLetters():
    text=readBook().lower()
    letterCounters = {}
    for letter in text:
        if letter == " " or letter.isalpha() == False:
            continue
        if letter in letterCounters:
            letterCounters[letter] += 1
        else:
            letterCounters[letter] = 1
    
    return letterCounters

def itemList():
    items = countLetters().items()
    return items

def sortItems():
    items = itemList()
    newList = sorted(items,key=lambda x:x[1],reverse=True)
    return newList

def main():
    # print(countWords())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{countWords()} words found in the document")
    sortedCh = sortItems()
    for ch in sortedCh:
        print(f"The '{ch[0]}' character was found {ch[1]} times")
# The 'e' character was found 46043 times
# The 't' character was found 30365 times
# The 'a' character was found 26743 times
# The 'o' character was found 25225 times
# The 'i' character was found 24613 times
# The 'n' character was found 24367 times
# The 's' character was found 21155 times
# The 'r' character was found 20818 times
# The 'h' character was found 19725 times
# The 'd' character was found 16863 times
# The 'l' character was found 12739 times
# The 'm' character was found 10604 times
# The 'u' character was found 10407 times
# The 'c' character was found 9243 times
# The 'f' character was found 8731 times
# The 'y' character was found 7914 times
# The 'w' character was found 7638 times
# The 'p' character was found 6121 times
# The 'g' character was found 5974 times
# The 'b' character was found 5026 times
# The 'v' character was found 3833 times
# The 'k' character was found 1755 times
# The 'x' character was found 677 times
# The 'j' character was found 504 times
# The 'q' character was found 324 times
# The 'z' character was found 243 times
    print("--- End report ---")


main()