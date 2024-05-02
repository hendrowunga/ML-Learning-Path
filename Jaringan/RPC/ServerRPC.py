from xmlrpc.server import SimpleXMLRPCServer

def doit(a, b):
    return a + b

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(doit, "doit")
server.serve_forever()