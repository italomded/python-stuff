import requests


def getName(url):
    try:
        name = url.split('/')
        name = name[len(name)-1]
        symbols = [':']
        for i in range(len(symbols)):
            print(symbols[i])
            name = name.replace(symbols[i], ';')
        return name
    except Exception:
        raise


def downloadOne(url):
    try:
        page = requests.get(url)
        name = getName(url)
        open(name, 'wb').write(page.content)
        print('Downloud concluído!')
    except Exception:
        raise  


while True:
    try:
        url = input('Digite o link: ')
        downloadOne(url)
    except Exception:
        print('ERROR: something went wrong!')
