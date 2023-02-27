def calcT(temp):
    message = ''
    if temp > 90:
        message = 'very hot'

    if temp > 80:
        message = 'hot'
        
    if temp > 70:
        message = 'ok'
        
    if temp > 60:
        message = 'cool'

    return message
