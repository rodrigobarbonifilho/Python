import urllib.error
import urllib.request

try:
    global site
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\n\033[1;31mO site pudim não está acessível no momento.\033[m')
else:
    print('\n\033[1;33mConsegui acessar o site pudim com sucesso.\033[m')
finally:
    esc = input('Quer o código HTML? ').strip().upper()[0]
    if esc in 'SIM':
        print(site.read())
