import requests

a = raw_input('Enter currency to convert from?')
a = a.upper()

b = raw_input('Enter currency to convert to?')
b = b.upper()

c = float(raw_input('Enter value to convert?'))

url = ('https://currency-api.appspot.com/api/%s/%s.json') % (a, b)
print url

r = requests.get(url)
rate= r.json()['rate']
print "rate => "+str(rate)

value= c*float(r.json()['rate'])
print "value => "+str(value)
