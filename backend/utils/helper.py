def convertRowToObject( row):
    result = {}
    for column in row.__table__.columns:
      result[column.name] = getattr(row, column.name)
    
    return result

def convertTableToList( table):
    result = []
    for row in table:
        rowObj = convertRowToObject(row)
        result.append(rowObj)
    
    return result