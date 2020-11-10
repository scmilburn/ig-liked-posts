import instaloader
import json
l = instaloader.Instaloader()
l.load_session_from_file("smilburn_")
del l.context._session.headers['Host']
del l.context._session.headers['Origin']
del l.context._session.headers['X-Instagram-AJAX']
del l.context._session.headers['X-Requested-With']
l.context._session.headers['User-Agent'] = 'Instagram 10.26.0 (iPhone7,2; iPhone OS 10_1_1; en_US; en-US; scale=2.00; gamut=normal; 750x1334) AppleWebKit/420+'

params = {}
done = False
while not done:
	data = l.context.get_json(path='api/v1/feed/liked/', host='i.instagram.com', params=params)
	for item in data['items']:
		p = instaloader.Post.from_shortcode(l.context, item['code'])
		if not l.download_post(p, ':liked'):
			done = True
			break
	if not data['more_available']:
		break
	params['max_id'] = data['next_max_id']
