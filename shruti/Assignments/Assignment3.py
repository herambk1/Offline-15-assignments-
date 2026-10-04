'''Assignment No.03: #Date - 10/09/2026
input file-
sample.txt-1

    output : 3 files
    1.mobile data -- mobile.txt
    2.email-- email.txt
    3.invalid data
    output : 3 files
    4.character data-- character.txt
    5.specialcharacter-- specialcharacter.txt
    6.numeric data-- numeric.txt'''

from utility import config
from utility.file_data_helper import  count_email_ids, count_mobile_num,input_file, count_special_char

def count(filedata):
    num = 0
    specialchar = 0
    characters = len(filedata)
    invalid_data = 0
    v_mobile = 0
    v_emails = 0
    for line in filedata.splitlines():
        v_emails += count_email_ids(line)
        v_mobile += count_mobile_num(line)
        if line.isdigit():
            num += len(line)
        elif not line.isalnum() and not line.isalpha():
            specialchar += count_special_char(line)

        else:
            invalid_data +=1


    result = {
        "characters": characters,
        "numeric": num,
        "special_characters": specialchar,
        "valid moblie num": v_mobile,
        "valid emails": v_emails,
        "invalid_data": invalid_data
    }
    with open(config.character_file,config.write_mode ) as fp:
        fp.write("characters:,\n"+ str(characters))
    with open(config.number_file,config.write_mode) as fp:
        fp.write("numbers:,\n"+ str(num))
    with open(config.special_char_file,config.write_mode) as fp:
        fp.write("special_char:,\n"+ str(specialchar))
    with open(config.mobile_file,config.write_mode) as fp:
        fp.write("mobilenumbers:,\n"+ str(v_mobile))
    with open(config.email_file,config.write_mode) as fp:
        fp.write("emails:,\n"+ str(v_emails))
    with open(config.invalid_file,config.write_mode) as fp:
        fp.write("invalid data:,\n"+ str(invalid_data))
    return result


def main():
    filename = config.input_file
    data = input_file(filename)
    result = count(data)
    print(result)


if __name__ == '__main__':
    main()