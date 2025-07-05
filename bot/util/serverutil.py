from mcstatus import JavaServer

def getStatus():
    try:
        server = JavaServer.lookup("bliss")
        status = server.status()
        return status
    except:
        print("Server unreachable, or an error occured.")
        return None