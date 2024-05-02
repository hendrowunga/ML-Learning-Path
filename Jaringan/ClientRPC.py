import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
x1 = input('masukkan 1 angka : ')
x2 = input('Masukkan 2 angka : ')
r = proxy.doit(int(x1), int (x2))
print(f"r: {r}")