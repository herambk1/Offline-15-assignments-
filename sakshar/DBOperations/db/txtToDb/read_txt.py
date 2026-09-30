def read_txt_file(fileName):
    with open(fileName) as fp:
        data = fp.readlines()
        return [line.strip() for line in data]

def create_insert_list(data):
    ins_lst = []
    for i in range(0,len(data),1):
        values = data[i].split(',')
        id_val = values[0]
        first_name = f"'{values[1]}'" if values[1] != 'N/A' else 'NULL'
        last_name = f"'{values[2]}'" if values[2] != 'N/A' else 'NULL'
        maiden_name = f"'{values[3]}'" if values[3] != 'N/A' else 'NULL'
        age = values[4]
        gender = f"'{values[5]}'" if values[5] != 'N/A' else 'NULL'
        query = f"insert into emp_txt_data (id, first_name, last_name, maiden_name, age, gender) values({id_val}, {first_name}, {last_name}, {maiden_name}, {age}, {gender})"
        ins_lst.append(query)
    return ins_lst