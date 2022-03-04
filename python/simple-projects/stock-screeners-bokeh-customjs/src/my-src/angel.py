import http.client

conn = http.client.HTTPSConnection(
    "apiconnect.angelbroking.com"
    )
payload = "{\n\"clientcode\":\"J0ugU36x\",\n\"password\":\"948ef137-85dc-40f4-88ad-272aec2f5c8f \"\n}"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
conn.request(
    "POST",
    "/rest/auth/angelbroking/user/v1/loginByPassword",
     payload,
     headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))