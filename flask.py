#Com Flask, você pode rapidamente criar uma API básica com poucas linhas de código, 
#sendo uma excelente opção para prototipagem rápida, como mostrado no código a seguir:

from flask import Flask

app = Flask(__name__)

@app.route('/api')
def ola_mundo():
    return 'Olá Mundo!'

if __name__ == '__main__':
    app.run()


#Apesar de ser um framework mais pesado em comparação com Flask, 
#o Django oferece uma solução abrangente para desenvolvimento web. 
#Um exemplo de como criar uma API simples em Django está no código a seguir:

from django.http import JsonResponse
from django.views import View

class MinhaAPI(View):
    def get(self, request):
        return JsonResponse({'message': 'Olá mundo!'})
    
#FastAPI é uma escolha moderna, otimizada para alta performance e fácil utilização. 
#Ele utiliza a tipagem de dados do Python 3.7+ para oferecer uma documentação automática 
#excepcional, facilitando a compreensão e utilização da API.

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def ola_mundo():
    return {"message": "Olá Mundo!"}