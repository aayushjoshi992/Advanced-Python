def httpsStatus(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown status"
print(httpsStatus(200))
print(httpsStatus(404))
print(httpsStatus(500))
print(httpsStatus(5007))
