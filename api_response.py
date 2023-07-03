import requests


def lets_try(categorization):
    classification_gender = {}
    classification_period = {}

    database = {}

    url = "https://dataderden.cbs.nl/ODataApi/OData/72035ned"
    classification_gender_url = url + '/Geslacht'
    classification_period_url = url + '/Perioden'
    addon = '/TypedDataSet'
    url += addon

    r = requests.get(classification_gender_url)
    r = r.json()
    for item in r['value']:
        classification_gender[item['Title']] = item['Key']

    r = requests.get(classification_period_url)
    r = r.json()
    for item in r['value']:
        classification_period[item['Key']] = item['Title']
        database[item['Title']] = 0
    "0 = both genders, -1 = men, 1 = women"
    r = requests.get(url)
    r = r.json()
    for item in r['value']:
        if categorization == 0:
            calc = item['TotaalDelicten_1']
            for num, items in enumerate(database):
                if item['ID'] == num:
                    database[items] = calc
        elif categorization == 1:
            if item['Geslacht'] == classification_gender['Vrouwen']:
                calc = item['TotaalDelicten_1']
                if item['Migratieachtergrond'] == 'T001040' and str(item['Leeftijd']) == '52020':
                    personal_timeline = item['Perioden']
                    database[classification_period[personal_timeline]] = calc
        elif categorization == -1:
            if item['Geslacht'] == classification_gender['Mannen']:
                calc = item['TotaalDelicten_1']
                if item['Migratieachtergrond'] == 'T001040' and str(item['Leeftijd']) == '52020':
                    personal_timeline = item['Perioden']
                    database[classification_period[personal_timeline]] = calc

    x, y = [], []
    for item in database:
        x.append(item)
        y.append(database[item])
    return x, y

if __name__ == '__main__':
    print('men')
    x, y = lets_try(-1)
    print(x)
    print(y)
    print('total')
    x, y = lets_try(0)
    print(x)
    print(y)
    print('women')
    x, y = lets_try(1)
    print(x)
    print(y)
