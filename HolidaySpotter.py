import requests

url1="http://ip-api.com/json/"                                   #detecting user's country and countryCode by IP Address
resp1=requests.get(url1)
data1=resp1.json()

if resp1.status_code==200:
    print("Your current location details are:")
    for x in data1.keys():
        if x=="country":
            country=data1.get(x)
            print('country:',data1.get(x))
        elif x=="countryCode":
            countryCode=data1[x]
            print('countryCode:',data1.get(x),'\n')
    print("Would you like to change this?")

    str =input("Enter(Yes/No):")
    if str=="Yes":                                                  #getting country code, in case the user decides to check for another country
        country = input('Entry Country:')
        url2 = 'https://api.first.org/data/v1/countries'
        resp2 = requests.get(url2)
        data2 = resp2.json()
        for (x, y) in data2.items():
            dic = {}
            if x == 'data':
                dic[x] = y
                break
        d = dic['data']
        for code, details in d.items():
            for x1, y1 in details.items():
                if y1 == country:
                    countryCode = code
                    print('\nYour Updated country is:',country)
                    print('Your Updated countryCode:', countryCode,'\n')
                    break
else:
    print("Invalid")
                                                                   #asking the user to input date
print('Enter date below:\n')
year=input("Enter the year:")
month=input("Enter the month:")
day=input("Enter the day:")
api_key=""                          #Replace with your api key

base_url="https://holidays.abstractapi.com/v1/?"                    #checking if a holiday was celebrated in the country
url3=base_url+f'api_key={api_key}&country={countryCode}&year={year}&month={month}&day={day}'

resp3 = requests.get(url3)
data3=resp3.json()
print(resp3.status_code)
if data3==[]:
    print('No holiday was celebrated on this day in',country)
else:
    data=data3[0]
    print(data.get('name'),' was celebrated on ',day,'/',month,'/',year,' in ',country,'.',sep='')