import tweepy
import json
import yaml

with open('keys.yaml', 'r') as f:
    keys = yaml.load(f)


auth = tweepy.OAuthHandler(keys["t_con_key"],keys["t_con_secret_key"])
auth.set_access_token(keys["t_ass_tkn"],keys["t_ass_tkn_secret"])

api = tweepy.API(auth)

listas = api.lists_all() 

# pegar apenas uma lista
lista = listas[0]
print('Nome: %s | Descrição: %s' % (lista.name, lista.description))
for member in lista.members():
    lista_json = member._json
    print('User: %s - %s' % (member.screen_name, 
                             repr(lista_json['status']['text'])))
