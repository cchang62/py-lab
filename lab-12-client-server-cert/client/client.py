import requests

# Ref. https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
# [Error] /Users/Jibamy/opt/miniconda3/lib/python3.8/site-packages/urllib3/connectionpool.py:1013: InsecureRequestWarning: Unverified HTTPS request is being made to host '127.0.0.1'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cert_file_path = "cert/demo-client.crt"
key_file_path = "cert/demo-client.key"

url = "https://127.0.0.1:5000/"
params = {"param_1": "value_1", "param_2": "value_2"}
cert = (cert_file_path, key_file_path)
# r = requests.get(url, params=params, cert=cert)
r = requests.get(url, params=params, cert=cert, verify=False)
# `export REQUESTS_CA_BUNDLE=./cert/demo-server.crt` to point cacert
# Linux default cacert path is `export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`
# Ref. https://stackoverflow.com/questions/42982143/python-requests-how-to-use-system-ca-certificates-debian-ubuntu
print(dir(r))
print(r.headers) 
# verify=False option : currently CN is incorrect and python request lib needs cacert for self-signed cert case

