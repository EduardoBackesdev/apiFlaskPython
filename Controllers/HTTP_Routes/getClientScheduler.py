from Models.DatabaseFunctions import clientScheduler

def getClientScheduler():
    query = clientScheduler.clientScheduler()
    return query
