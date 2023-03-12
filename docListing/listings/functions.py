def getCitationCount(value):
    return float(value["Citation count"])

def refactorDataKeys(dataSet):
    newDataSet = []
    for data in dataSet:
        newData = {}
        
        for key in data:
            list_string = key.split(' ')
        
            if(len(list_string) > 1):
                newKey = '_'.join(list_string)
            else:
                newKey = key
            
            newData[newKey] = data[key]
        
        newDataSet.append(newData)
            
    return newDataSet
            