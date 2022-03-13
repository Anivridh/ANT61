def main():
    bracketDict = {
        '{': '}',
        '[': ']',
        '(': ')',
    }
    open_bracket_list = ['{', '[', '(']
    close_bracket_list = ['}', ']', ')']
    sequence = input("Enter bracket sequence: ")
    if (len(sequence) == 0):
        print("Balanced")
        return
    if (len(sequence) % 2 != 0):
        print("Unbalanced")
        return
    stack = []
    balanced = True
    for bracket in sequence:
        if (bracket in open_bracket_list):
            stack.append(bracket)
        else:
            if (len(stack) == 0):
                balanced = False
                break
            poppedBracket = stack.pop()
            if (bracketDict[poppedBracket] != bracket):
                balanced = False;
                break

    if (balanced):
        print("Balanced")
    else:
        print("Unbalanced")
if __name__ == "__main__":
    main()