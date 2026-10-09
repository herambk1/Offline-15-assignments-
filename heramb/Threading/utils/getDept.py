def getdept(rows):
    found=[]
    for row in rows:
        dept = row[4]
        if dept not in found:
            found.append(dept)
    return found
