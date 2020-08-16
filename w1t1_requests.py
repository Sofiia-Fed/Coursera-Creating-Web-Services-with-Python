import requests
import json
import datetime

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
API_URL = 'https://api.vk.com/method/'
version = '5.71'

def calc_age(uid):
	today = datetime.date.today().year

	vk_request1 = requests.get(f'{API_URL}users.get', params={
		'access_token': ACCESS_TOKEN,
		'user_id': uid,
		'v': version,
	})
	user_id = json.loads(vk_request1.text)['response'][0]['id']

	vk_request2 = requests.get(f'{API_URL}friends.get', params={
		'access_token': ACCESS_TOKEN,
		'user_id': user_id,
		'fields': 'bdate',
		'v': version,
	})
	friends = json.loads(vk_request2.text)['response']['items']

	all_bdates = [user['bdate'] for user in friends if 'bdate' in user]
	dates_with_years = list(filter(lambda date: date.count('.') == 2, all_bdates))
	ages = sorted(list(map(lambda date: today - int(date.split('.')[-1]), dates_with_years)))
	friends_ages = sorted({age: ages.count(age) for age in ages}.items(), 
						  key=lambda item: item[1], reverse=True)

	return friends_ages


