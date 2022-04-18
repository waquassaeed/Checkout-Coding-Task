#import requests
import pip._vendor.requests
#from requests.structures import CaseInsensitiveDict
from pip._vendor.requests.structures import CaseInsensitiveDict
import json

url = "https://api.sandbox.checkout.com/payments"

#headers = CaseInsensitiveDict()
#headers["Accept"] = "application/json"
#headers["Authorization"] = "Bearer bbffa6216e6ced1d990e1f9383b37d3e874740b5a29cbd277905f9cd7d1518f8"
#headers["Content-Type"] = "application/json"

headers = {
  'Authorization': 'sk_test_0b9b5db6-f223-49d0-b68f-f6643dd4f808',
  'Cko-Idempotency-Key': 'CheckoutFrameRequest',
  'Content-Type': 'application/json'
}


payload = json.dumps({
  "source": {
    "type": "token",
    "token": "tok_s7u4yuor3q4uve6v6mbh3jpgo4"
  },
  "amount": 9,
  "currency": "EUR",
  "reference": "CheckoutFrameRequest",
   "customer": {
      "email": "checkouttest@gmail.com",
      "name": "Checkout Payment"
    }
})
#d = json.loads(data)

resp = pip._vendor.requests.post(url, headers=headers, data=payload)
resp_json = resp.json()

print(resp_json)
print(resp.status_code)
#print(resp.encoding)
#print(d)