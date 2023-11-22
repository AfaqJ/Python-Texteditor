def checkdiff(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False

print(checkdiff([1,2,2,3]))