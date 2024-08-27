import requests

def hit_sender(card,message,chat_id):
    bot_token = '7417334652:AAFZiUC2mohOet-fm-E1A4DGP2ozwuCu_9I'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
