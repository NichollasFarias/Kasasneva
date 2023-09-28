import sqlite3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

BD = sqlite3.connect('Kasasneva.db')
cursor = BD.cursor()
BD.execute('CREATE TABLE IF NOT EXISTS imoveis(ID integer PRIMARY KEY AUTOINCREMENT, Cidade text, Tipo text, Negocio text, Valor decimal)')


class Tela(ScreenManager):
    pass

class Kasasneva(App):
    def build(self):
        return Tela()

    def verificar(self,user,senha,play):
        if(user.text == '182348'):
            userver = True
            user.background_color = [1,1,1,1]
        else:
            userver = False
            user.background_color = [1,0,0,1]

        if(senha.text == '182348'):
            senhaver = True
            senha.background_color = [1,1,1,1]
        else:
            senhaver = False
            senha.background_color = [1,0,0,1]

        if(userver == True and senhaver == True):
            play.current = 'Menu'

    def AddDados(self,cid,tip,neg,val):
        adcidade = cid.text
        adtipo = tip.text
        adnegocio = neg.text
        advalor = float(val.text)

        if(advalor >= 1000):
            aprovado = True
        else:
            aprovado = False
        
        if(aprovado == True):
            BD.execute('INSERT INTO imoveis VALUES(NULL,?,?,?,?)',(adcidade,adtipo,adnegocio,advalor))
            BD.commit()
            cid.text = ""
            tip.text = ""
            neg.text = ""
            val.text = ""
        else:
            cid.text = ""
            tip.text = ""
            neg.text = ""
            val.text = ""

    def Pesquisar(self,btncid,btntip,btnneg,barratxt,tab):

        tab.clear_widgets()
        if(btncid.state == 'down'):
            Dado = barratxt.text
            cursor.execute('SELECT * FROM imoveis WHERE Cidade= :name', {'name': Dado})
            re = cursor.fetchall()
            for row in re:
                tab.add_widget(Label(text = str(row), font_size = 30, size_hint_y = None, height = 35))

        elif(btntip.state == 'down'):
            Dado = barratxt.text
            cursor.execute('SELECT * FROM imoveis WHERE Tipo= :name', {'name': Dado})
            re = cursor.fetchall()
            for row in re:
                tab.add_widget(Label(text = str(row), font_size = 30, size_hint_y = None, height = 35))

        elif(btnneg.state == 'down'):
            Dado = barratxt.text
            cursor.execute('SELECT * FROM imoveis WHERE Negocio= :name', {'name': Dado})
            re = cursor.fetchall()
            for row in re:
                tab.add_widget(Label(text = str(row), font_size = 30, size_hint_y = None, height = 35))

    def Analise(self,btncid,btntip,btnneg,barratxt,tab):
        
        if(btncid.state == 'down'):
            tab.clear_widgets()
            barratxt.text = 'Pesquisar por nome da Cidade...'
        elif(btntip.state == 'down'):
            tab.clear_widgets()
            barratxt.text = 'Pesquisar por Tipo do imovel...'
        elif(btnneg.state == 'down'):
            tab.clear_widgets()
            barratxt.text = 'Pesquisar por finalidade do imovel...'
    
            
            
                    
            
        
        
        
        

Kasasneva().run()
