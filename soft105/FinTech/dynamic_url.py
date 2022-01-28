def updateRouteConfig(path,fileName):
    fptr = open("./routerUpdateConfig.txt","w")
    fptr.write(f"{path}\n{fileName}")
    fptr.close()
def downloadRouteConfig():
    try:
        res = []
        fptr = open("./routerUpdateConfig.txt","r")
        for line in fptr.readlines():
            res.append(line)
        fptr.close()
        return res
    except:
        fptr = open("./routerUpdateConfig.txt","w")
        fptr.close()
        return downloadRouteConfig()
def clearRouteConfig():
    fptr = open("./routerUpdateConfig.txt","w")
    fptr.close()