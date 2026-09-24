
def unique_dept(fdata):
    uniqueDept = set()
    for data in fdata[1:]:
        uniqueDept.add(data[-1])
    return uniqueDept