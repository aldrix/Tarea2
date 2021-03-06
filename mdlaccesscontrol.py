# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Jean Carlos
'''
import uuid
import hashlib
import re
 
class clsAccessControl(object):
    def __init__(self):
        ohast=''
        
    def encript(self, value):
        # Verificar la longitud del password
        oHash=""
        olength_password=self.length_password(value)
        
        verificar = re.match('(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d)|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d)',value) 
        
        if verificar and olength_password>=8 and olength_password<=16:
            # uuid es usado para generar numeros random
            salt = uuid.uuid4().hex
            # hash
            oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
        else:
            print('El Password debe contener entre 8 y 16 caracteres. Debe contener al menos una mayúscula,')
            print(' un número y un caracter especial')
        return oHash   
    
    def check_password(self, oPassworkEncript, oCheckPassword):
        # Verificar la longitud del password
        olength_password=self.length_password(oCheckPassword)
        
        verificar = re.match('(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d)|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'+
                           '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d)',oCheckPassword) 
        
        if verificar and olength_password>=8 and olength_password<=16: 
            
            oPassworkEncript, salt = oPassworkEncript.split(':')
            return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
        else:
            print('El Password no posee el largo necesario o los caracteres especiales requeridos Ej: @.#$+*')
            return False
    
    def length_password(self, user_password):
        return len(user_password)

#Para encriptar un passwork  
#oPassword = input('Por favor ingrese su password: ')
#Se crea un objeto tipo clsAccessControl
#oAccessControl=clsAccessControl()
#oPassworkEncript = oAccessControl.encript(oPassword)
# #Para encriptar un passwork  
# oPassword = input('Por favor ingrese su password: ')
#  #Se crea un objeto tipo clsAccessControl
# oAccessControl=clsAccessControl()
# oPassworkEncript = oAccessControl.encript(oPassword)
# print('El Password almacenado en la memoria es: ' + oPassworkEncript)
# if oPassworkEncript:
#      #Para validar el passwork introducido
#     oCheckPassword = input('Para verificar su password, ingreselo nuevamente: ')
#     if oAccessControl.check_password(oPassworkEncript, oCheckPassword):
#         print('Ha introducido el password correcto')
#     else:
#         print('El password es diferente')
