import requests
import json
URL = "https://www.way2sms.com/api/v1/sendCampaign"
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
    'apiKey':apiKey,
    'secret':secretKey,
    'useType':useType,
    'phone':phoneNo,
    'senderId':senderId,
    'message':textMessage
    }
    return requests.post(reqUrl, req_params)

response = sendPostRequest(URL,'KXKQXE0QHYMEH77DFPKN6RQIAMYUDZT6','KC74BU8URIT1SP0E','stage','7982135341','shanroy','Bhook lagi hai')
