from log_utils.log_config import custom_log
logger = custom_log(str(__file__).split("\\")[-1])
def fetch_dept(data):
    dept = []
    try:
        for row in data:
            if row['Dept'] is not None and row['Dept'] not in dept:
                dept.append(row['Dept'])

        logger.info("Unique departments fetched: {}".format(dept))

        return dept

    except Exception as e:
        logger.error("Error while fetching departments: {}".format(e))
        print(e)
