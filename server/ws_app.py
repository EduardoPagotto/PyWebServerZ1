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

import socket

from datetime import datetime

from flask import Flask, render_template, jsonify, json, request

application = Flask(__name__)

# def gera_teste():
#     lista = []
#     dado1 = {}
#     dado1['nome'] = 'Eduardo'
#     dado1['idade'] = 47
#     dado1['sexo'] = True

#     dado2 = {}
#     dado2['nome'] = 'Locutus'
#     dado2['idade'] = 99
#     dado2['sexo'] = True

#     lista.append(dado1)
#     lista.append(dado2)
#     return lista

serial = 0

def le_dados(arquivo):
    with open(arquivo) as json_file:  
        data = json.load(json_file)
        return data

@application.route('/')
def api_root():
    return 'Welcome'
    #return render_template('index.html')

# @application.route('/getListItens', methods=['GET', 'POST'])
# def getListItens():
#     try:
#         lista = gera_teste()
#     except Exception as e:
#         return str(e)
#     return json.dumps(lista)

# @application.route('/adicione', methods=['POST'])
# def adicione():
#     try:

#         nova = request.json['lista_nova']

#         if not nova:
#             raise Exception('lista vazia')

#         print('Nome:{0}'.format(nova[0]))
#         resp = 'adicionado {0}'.format(nova[0])

#         return jsonify(status='OK', message=resp)

#     except Exception as e:
#         print('Error is ' + str(e))
#         return jsonify(status='ERROR', message=str(e))

@application.route('/begin', methods=['POST'])
def begin():
    if request.method=='POST':

        global serial
        serial += 1

        auth = request.headers['Authorization']
        host = request.headers['host']
        payload = request.get_json(silent=True)

        opp = {}
        batch = {}
        scanner = {}
        opp['command'] = 'BEGIN'
        opp['host'] = host
        opp['payload'] = payload
        opp['batch'] = batch
        opp['scanner'] = scanner
        batch['id'] = 'OBJETO_ID_UNICO'
        batch['path'] = '/{host:}_{agora:%Y%m%d%H%M%S}_{seq:04d}'.format(host=socket.gethostname(),
                                                                         agora=datetime.today(),
                                                                         seq=serial)
        batch['docs'] = []
        scanner['path'] = '/home/pagotto/images'

        # TODO: criar diretorio

        # TODO: Enviar comando para scanner comecar a aquisicao de imagens

        # TODO: envia opp para fila de processamento

        response = application.response_class(
            response=json.dumps(opp),
            status=200,
            mimetype='application/json'
        )
        return response

        # #erro
        # response = application.response_class(
        #     response=json.dumps(dado),
        #     status=404,
        #     mimetype='application/json'
        # )
    else:
        return("Erro")

@application.route('/teste_put', methods=['PUT'])
def teste_put():
    if request.method=='PUT':
        return "OK this is a PUT method"
    else:
        return("ok")
        #return('<form action="/teste_put" method="put"><input type="submit" value="Send" /></form>')

@application.route('/teste_get', methods=['GET'])
def teste_get():
    if request.method=='GET':
        return "OK this is a GET method"
    else:
        return("ok")
        #return('<form action="/teste_get" method="get"><input type="submit" value="Send" /></form>')

@application.route('/teste_post', methods=['POST'])
def teste_post():
    if request.method=='POST':
        return "OK this is a post method"
    else:
        return("ok")

@application.route('/teste_delete', methods=['DELETE'])
def teste_delete():
    if request.method=='DELETE':
        return "OK this is a DELETE method"
    else:
        return("ok")

# @application.route('/teste', methods=['GET', 'POST'])
# def teste():
#     if request.method=='GET':
#         return('<form action="/teste" method="post"><input type="submit" value="Send" /></form>')

#     elif request.method=='POST':
#         return "OK this is a post method"
#     else:
#         return("ok")

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)