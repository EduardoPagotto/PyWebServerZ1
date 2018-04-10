#!/usr/bin/env python3
'''
Created on 20180410
Update on 20180410
@author: Eduardo Pagotto
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913

import requests

import json

def get_data(url_acc):
    r = requests.get(url=url_acc)
    if r.ok is True:
        return r.json()
    else:
        if r.reason is not None:
            raise Exception(str(r.reason))
        
        raise Exception('Erro Desconhecido')

def set_data(url_acc, transacoes):
    dados = json.dumps(transacoes)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url_acc, data=dados, headers=headers)
    if response.ok is False:
        raise Exception('WebServer respondeu com erro: %s', str(response._content))


if __name__ == "__main__":

    #chamar em linha de comando
    #curl -X PATCH http://127.0.0.1:5000/teste

    #derrubar
    #fuser -k 8080/tcp

    try:

        dados = get_data('http://127.0.0.1:5000/getListItens')

        novo = {}
        novo['nome'] = 'DEDALUS'

        dados.append(novo)

        set_data('http://127.0.0.1:5000/adicione', dados)

        print('FIM')
    except Exception as exp:
        print(str(exp))