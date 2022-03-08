def main():
    bracketDict = {
        '{': '}',
        '[': ']',
        '(': ')',
    }
    sequence = input("Enter bracket sequence: ")
    balanced = True
    if (len(sequence) == 0):
        print("Balanced")
        return
    if (len(sequence) % 2 != 0):
        print("Unbalanced")
        return
    stack = []
    i = 0
    for bracket in sequence:
        i += 1
        if (i <= (len(sequence) / 2)):
            stack.append(bracket)
            continue
        poppedBracket = stack.pop()
        if (bracketDict[poppedBracket] != bracket):
            balanced = False
            break
    if (balanced):
        print("Balanced")
    else:
        print("Unbalanced")

if __name__ == "__main__":
    main()