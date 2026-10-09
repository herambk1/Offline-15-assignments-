import json
import csv


def read_json_file(filename):
    with open("{}.json".format(filename), "r") as fp:
        return json.load(fp)


def get_columns(file):
    columns = {}

    for records in file:
        for key in records:
            columns[key] = 1

    return list(columns.keys())


def json_to_csv(keys, file):
    filename = "{}.csv".format("student_output")

    with open(filename, "w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=keys)
        writer.writeheader()
        writer.writerows(file)


def main():
    file = read_json_file(
        r"C:\Users\VISHAKHA MANE\PycharmProjects\databaseconn\student"
    )

    keys = get_columns(file)

    json_to_csv(keys, file)

    print(keys)


if __name__ == "__main__":
    main()

