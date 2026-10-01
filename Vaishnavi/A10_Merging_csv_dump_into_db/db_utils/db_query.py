from log_utils.log_config_data import log_config

logger = log_config(str(__file__).split("\\")[-1])


def DB_query(data):
    logger.info("Creating insert query for employee: {}".format(data['emp_id']))

    query = "insert into employee_data values({},'{}',{},'{}','{}',{})".format(data['emp_id'],data['name'],data['age'],data['city'],data['department'],data['salary'])

    logger.info("Insert query created successfully")
    return query
