from Jsontocsv_utilty.json_to_csv_helper import input_json_file, write_jsontocsv_file


def main():
    filename = input_json_file("emp2.json")
    write_jsontocsv_file(filename)


if __name__ == "__main__":
    main()