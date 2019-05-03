def sanitizeInput(valid_responses,text):
    response = ""
    while response.lower() not in [x.lower() for x in valid_responses]:
        response = input(text)
    return response

def caseInsensitiveIndex(x,arr):
    return ([i.lower() for i in arr].index(x.lower()))

def caseInsensitiveIn(x,arr):
    return (x.lower() in [i.lower() for i in arr])