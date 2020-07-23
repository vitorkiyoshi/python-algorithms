import re
from modulo import *
def arvore(url_inicial,url='',espacos=0,regex=r'href=[\'"]?([^\'" >]+)',acum=[]):
    if url=='':
        url=url_inicial
    if url not in acum:
        print(" "*espacos + url)
        acum.append(url)
    html=obter_html(url)
    links=re.findall(regex, html)    #todos os links dentro da pagina
    for link in links:
        link=resolver_url(link, url)
        if eh_url_valida(link, url_inicial):
            if link not in acum:
                arvore(url_inicial,link,espacos+2,regex,acum)
    pass
def main():
    x=input()
    arvore(x)
main()
