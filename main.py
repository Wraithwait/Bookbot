def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

        # Count Words
        word_count = len(file_contents.split())
        #print(word_count)

        #Count Characters
        letter_count = count_characters(file_contents)

        #Generate Report
        generate_report(word_count, letter_count)


def count_characters(input_string):
    letter_count = {}
    
    for letter in input_string:
        if letter.isalpha(): #or letter == ' ':
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    print("Letter Counts:")
    for letter, count in letter_count.items():
        print(letter_count)
        return letter_count

def generate_report(word_count, letter_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Word count: {word_count}")
    print("Character counts:")

    for char, count in sorted(letter_count.items()):
        #if char != ' ': # Exclude spaces from report
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()