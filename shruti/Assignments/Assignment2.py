'''Assignment No.02:   #Date - 10/09/2026
input file-
sample.txt

output file-
1)Char : No. of characters
2)Words : No. of words
3)SpecialCharacters : No. of SpecialCharacters
4)Lines : No. of lines
5)Numbers : No.of numbers
All in dictionary and in 1 file name sample_output.txt'''

from utility.file_data_helper import  input_file, count_special_char

def count(filedata):
    num = 0
    specialchar = 0

    characters = len(filedata)
    words = len(filedata.split())
    lines = len(filedata.splitlines())

    for line in filedata.splitlines():
        if line.isdigit():
            num += len(line)
        elif not line.isalnum() and not line.isalpha():
            specialchar += count_special_char(line)

    result = {
        "characters": characters,
        "words": words,
        "numeric": num,
        "special_characters": specialchar,
        "lines": lines
    }
    with open("sample_output.txt", "w") as fp:
        fp.write(str(result))

    return result


def main():
    filename = "sample.txt"
    data = input_file(filename)
    result = count(data)
    print(result)


if __name__ == '__main__':
    main()