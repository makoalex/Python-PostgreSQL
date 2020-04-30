import requests

uri = requests.get('https://developers.facebook.com/docs/apis-and-sdks/#facebook-apis')
print(uri.content)