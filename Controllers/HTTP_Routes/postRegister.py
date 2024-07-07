from Models.DatabaseFunctions import register

def postRegister():
    query = register.register()
    return query