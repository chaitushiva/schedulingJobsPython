import requests

s=requests.Session()

url = 'https://github.com/login'

with requests.Session() as c:
    USERNAME = 'shivaldap@gmail.com'
    PASSWORD = 'shiva@ldap1'
    c.get(url)
    print c.cookies
    login_data = dict(login = USERNAME,password = PASSWORD)
    authenticity_token = c.cookies['_gh_sess']
    c.post(url,data = login_data, headers = {'Referer':'https://github.com/'})
    page = c.get('https://github.com/issues')
    print page.content