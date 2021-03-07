import base64
# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
import http.client as http_client
import logging

import requests


def debug():
    http_client.HTTPConnection.debuglevel = 1
    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


endpoint = "https://us-central1-mcpabe.cloudfunctions.net/test"


def encodeStringToBytes(s: str):
    message_bytes = s.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes


def decodeBytesToString(base64_bytes):
    return base64_bytes.decode('utf-8')


# turn binary bytes into a string to send
def readBinaryFile(filePath: str):
    with open(filePath, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        return base64_encoded_data.decode('utf-8')


def writeBinaryFile(filePath: str, byteString: str):
    fileBytes = byteString.encode('utf-8')
    with open(filePath, 'wb') as binary_file:
        binary_file_data = base64.decodebytes(fileBytes)
        binary_file.write(binary_file_data)


def setup(attributeUniverse: list, public_key_loc="public_key.txt", master_key_loc="master_key.txt"):
    post_date = {'method': 'setup', 'attributeUniverse': attributeUniverse}
    r = requests.post(endpoint, json=post_date)
    print(r.status_code)
    resp = r.json()
    writeBinaryFile(public_key_loc, resp['publicKey'])
    writeBinaryFile(master_key_loc, resp['masterKey'])


def keygen(userAttributes: str, user_share_1_loc: str, user_share_2_loc: str, public_key_loc="public_key.txt",
           master_key_loc="master_key.txt"):
    public_key = readBinaryFile(public_key_loc)
    master_key = readBinaryFile(master_key_loc)
    post_date = {'method': 'keygen', 'userAttributes': userAttributes, 'masterKey': master_key, 'publicKey': public_key}
    r = requests.post(endpoint, json=post_date)
    resp = r.json()
    writeBinaryFile(user_share_1_loc, resp['share1'])
    writeBinaryFile(user_share_2_loc, resp['share2'])


def encrypt(policy: str, input_file_loc: str, encrypted_file_loc="", public_key_loc="public_key.txt"):
    public_key = readBinaryFile(public_key_loc)
    input_file = readBinaryFile(input_file_loc)
    post_date = {'method': 'encrypt', 'policy': policy,
                 'inputFile': input_file, 'publicKey': public_key}
    r = requests.post(endpoint, json=post_date)
    resp = r.json()
    if encrypted_file_loc == "":
        encrypted_file_loc = input_file_loc + "_ENCRYPTED"
    writeBinaryFile(encrypted_file_loc, resp['encryptedFile'])


def halfDecrypt(user_share_1_loc: str, encrypted_file_loc: str, professionalID: str, half_decrypted_file_loc="",
                public_key_loc="public_key.txt"):
    public_key = readBinaryFile(public_key_loc)
    user_share_1 = readBinaryFile(user_share_1_loc)
    encrypted_file = readBinaryFile(encrypted_file_loc)
    post_date = {'method': 'halfDecrypt', 'share1': user_share_1, 'professionalId': professionalID,
                 'encryptedFile': encrypted_file, 'publicKey': public_key}
    r = requests.post(endpoint, json=post_date)
    resp = r.json()
    if half_decrypted_file_loc == "":
        half_decrypted_file_loc = encrypted_file_loc + "_mDECRYPTED"
    writeBinaryFile(half_decrypted_file_loc, resp['mDecryptedFile'])


def decrypt(user_share_2_loc: str, encrypted_file_loc: str, professionalID: str, half_decrypted_file_loc="",
            decrypted_file_loc="", public_key_loc="public_key.txt"):
    public_key = readBinaryFile(public_key_loc)
    user_share_2 = readBinaryFile(user_share_2_loc)
    encrypted_file = readBinaryFile(encrypted_file_loc)
    if half_decrypted_file_loc == "":
        half_decrypted_file_loc = encrypted_file_loc + "_mDECRYPTED"
    mDecrypted_file = readBinaryFile(half_decrypted_file_loc)
    post_date = {'method': 'decrypt', 'share2': user_share_2, 'professionalId': professionalID,
                 'encryptedFile': encrypted_file, 'mDecryptedFile': mDecrypted_file, 'publicKey': public_key}
    r = requests.post(endpoint, json=post_date)
    resp = r.json()
    if decrypted_file_loc == "":
        decrypted_file_loc = encrypted_file_loc + "_DECRYPTED"
    writeBinaryFile(decrypted_file_loc, resp['decryptedFile'])


def test():
    attributeUniverse = ["doctor", "windsor", "detroit", "heart_surgeon", "emergency"]
    userAttributes = "heart_surgeon doctor detroit"
    policy = "(doctor AND detroit AND heart_surgeon)"
    inputFile = "sensitivePatientFile.jpg"
    encrypted_file_loc = "ENCRYPTED_" + inputFile
    half_decrypted_file_loc = "mDECRYPTED_" + inputFile
    decrypted_file_loc = "DECRYPTED_" + inputFile
    user_share_1_loc = "userShare1.txt"
    user_share_2_loc = "userShare2.txt"
    professionalID = "professionalID"
    setup(attributeUniverse)
    encrypt(policy, inputFile, encrypted_file_loc)
    keygen(userAttributes, user_share_1_loc, user_share_2_loc)
    halfDecrypt(user_share_1_loc, encrypted_file_loc, professionalID, half_decrypted_file_loc)
    decrypt(user_share_2_loc, encrypted_file_loc, professionalID, half_decrypted_file_loc, decrypted_file_loc)


# debug()
test()
