# Client And Server Cert Spec

## Prerequisites

Python 3.8.5

## Generate client and server certificates

```sh
############ Server Side ############

# Step1 產生一組沒有加密的 2048 bits 私密金鑰（PK: Private Key）
openssl genrsa -out 1-demo-server.key 2048

# Step2 產生憑證簽署請求（CSR: Certificate Signing Request）
# /C=Country 國別 
# /ST=State 州
# /L=Location 地區
# /O=Organization 組織
# /OU=Organizational Unit 組織部門單位
# /CN=Common Name 網域名稱
openssl req -sha512 -new -key 1-demo-server.key -out 1-demo-server.csr -subj "/C=TW/ST=Taipei/L=Taipei/O=example/OU=Personal/CN=www.example.com"
# 1-demo-server.crt is under 127.0.0.1, and the expire date of server cert is 2031/09/11

# Step3 檢查 CSR，列出請求內部資料（可省略）
openssl req -in 1-demo-server.csr -noout -text

# Step4 建立自我簽署的憑證（Self-Sign Certificate）
openssl x509 -sha512 -req -days 3650 -in 1-demo-server.csr -signkey 1-demo-server.key -out 1-demo-server.crt

# Step5 私密金鑰加密（可省略）
# -a 表示檔案使用 base64 編碼
# -salt 加鹽，增加安全性
openssl aes-256-cbc -a -salt -in 1-demo-server.key -out 1-demo-server.encrypt.key
```

```sh
############ Client Side ############

# Step1 建立用戶端私密金鑰以及簽署請求
openssl genrsa -out 1-demo-client.key 2048
openssl req -sha512 -new -key 1-demo-client.key -out 1-demo-client.csr -subj "/C=TW/ST=Taipei/L=Taipei/O=example/OU=Client/CN=client.example.com"

# Step2 簽署用戶端憑證
openssl x509 -sha512 -req -days 3650 -CA 1-demo-server.crt -CAkey 1-demo-server.key -CAserial 1-demo-server.srl -CAcreateserial -in 1-demo-client.csr -out 1-demo-client.crt

# Step3 驗證簽署（可省略）
openssl verify -CAfile 1-demo-server.crt 1-demo-client.crt

# Step4 打包加密 PKCS#12 (Public-Key Cryptography Standards)，用於部署到用戶端手機以及瀏覽器
openssl pkcs12 -export -out 1-demo-client.p12 -inkey 1-demo-client.key -in 1-demo-client.crt -certfile 1-demo-server.crt
```

## Run service

```sh

```

## Client test

```sh
# CURL 
curl -k --cert-type P12 --cert cert/1-demo-client.p12 https://127.0.0.1:5000/  
# -k | --insecure option which allows curl to make insecure connections, that is cURL does not verify the certificate.

curl --cert-type P12 --cert cert/1-demo-client.p12 --cacert cert/demo-server.crt https://127.0.0.1:5000/  
# Work!! But CN is not aligned, like
# curl: (60) SSL: certificate subject name 'www.example.com' does not match target host name '127.0.0.1'
# More details here: https://curl.haxx.se/docs/sslcerts.html

```

## Ref.

1. [Create client and server certs](https://dev.twsiyuan.com/2016/01/self-sign-certificate.html
2. [Simple Flask with cert](https://medium.com/@charming_rust_oyster_221/)flask-%E9%85%8D%E7%BD%AE-https-%E7%B6%B2%E7%AB%99-ssl-%E5%AE%89%E5%85%A8%E8%AA%8D%E8%AD%89-36dfeb609fa8)
3. [Simple Python client with cert](https://stackoverflow.com/questions/17576324/python-requests-ssl-error-for-client-side-cert)
4. [cURL with cacert and cert -0](https://smallstep.com/hello-mtls/doc/client/curl)
5. [cURL with cacert and cert -1 ](https://stackoverflow.com/questions/32253909/curl-with-a-pkcs12-certificate-in-a-bash-script)
6. [cURL with cacert and cert -2 ](https://blog.miniasp.com/post/2020/08/23/curl-and-self-signed-certificated-or-CA-certificate)
7. [cURL with cert and -k ](https://stackoverflow.com/questions/24611640/curl-60-ssl-certificate-problem-unable-to-get-local-issuer-certificate)
8. [verify-ca.py source code](https://gist.github.com/nebulak/6d865ddd768fb905a562d6026cdd508a)
