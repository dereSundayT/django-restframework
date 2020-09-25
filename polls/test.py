# importing the requests library
import requests
# defining the api-endpoint
API_ENDPOINT = "https://api.paystack.co/transaction/initialize"
# your API key here
Authorization = "sk_test_b800aa0dcbd98dfa3f8265782f7b54b487b8411c"
# your source code here
# data to be sent to api
data = {
    'email': 'customer@email.com',
    'amount': '20000'}

headers = {"Content-Type": "application/json", "Authorization": Authorization}
#payload = {"trackingNumber": f"{tracking_id}", "service": "express", "limit": 1}
resp = requests.post(API_ENDPOINT, data=data, headers=headers)
# sending post request and saving response as response object
#r = requests.post(url=API_ENDPOINT, data=data)
print(resp.content)
# extracting response text
#pastebin_url = r.text
#print("The pastebin URL is:%s" % pastebin_url)
