import requests, json
class ip():
    def ip_address(self, api_key):
        ip_address = '43.241.192.134'
        auth = api_key or '23c518e4-e589-46da-98cf-3b39102dda6c'
        url = 'https://ipfind.co/?auth=' + auth + '&ip=' + ip_address
        a = requests.get(url)
        data = json.loads(a.text)
        return data
