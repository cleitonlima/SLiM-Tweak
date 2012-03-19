#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Interface do SLiM Tweak, feita em PyQt4
#Desenvolvido por Cleiton Lima <cleitonlima@cleitonlima.com.br> - 2012
#Licença: GPLv3

##############################################
#    Este arquivo é parte do programa SLiM Tweak

#    SLiM Tweak é um software livre; você pode redistribui-lo e/ou 

#    modifica-lo dentro dos termos da Licença Pública Geral GNU como 

#    publicada pela Fundação do Software Livre (FSF); na versão 2 da 

#    Licença, ou (na sua opnião) qualquer versão.


#    Este programa é distribuido na esperança que possa ser  util, 

#    mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer

#    MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a

#    Licença Pública Geral GNU para maiores detalhes.


#   Você deve ter recebido uma cópia da Licença Pública Geral GNU

#   junto com este programa, se não, escreva para a Fundação do Software

#   Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
###################################################

from PyQt4 import QtCore, QtGui
from os import environ, system, path, listdir
import sys

class MainWindow(QtGui.QWidget):
    
	def __init__(self):
		super(MainWindow, self).__init__()
        
		self.initUI()
        
	def initUI(self):
	
		self.resize(533, 342)
		self.setWindowTitle(QtGui.QApplication.translate("Form", "SLiM Tweak", None, QtGui.QApplication.UnicodeUTF8))
		self.setMaximumSize(QtCore.QSize(533, 342))
		
		self.preview = QtGui.QLabel(self)
		self.preview.setGeometry(QtCore.QRect(10, 90, 231, 141))
		self.preview.setText("")
		self.preview.setPixmap(QtGui.QPixmap("/usr/share/slim/themes/default/background.jpg"))
		self.preview.setScaledContents(True)
		self.preview.setObjectName("preview")
		
		self.themes = QtGui.QComboBox(self)
		self.themes.setGeometry(QtCore.QRect(10, 30, 381, 31))
		self.themes.setObjectName("themes")
		
		self.label = QtGui.QLabel(self)
		self.label.setGeometry(QtCore.QRect(10, 10, 171, 21))
		self.label.setObjectName("label")
		self.label.setText(QtGui.QApplication.translate("Form", "Selecione o Tema:", None, QtGui.QApplication.UnicodeUTF8))
		
		self.label_2 = QtGui.QLabel(self)
		self.label_2.setGeometry(QtCore.QRect(10, 70, 171, 21))
		self.label_2.setObjectName("label_2")
		self.label_2.setText(QtGui.QApplication.translate("Form", "Previsão do Tema", None, QtGui.QApplication.UnicodeUTF8))
		
		self.numlock = QtGui.QCheckBox(self)
		self.numlock.setGeometry(QtCore.QRect(390, 270, 141, 20))
		self.numlock.setObjectName("numlock")
		self.numlock.setText(QtGui.QApplication.translate("Form", "Habilitar Numlock", None, QtGui.QApplication.UnicodeUTF8))

		self.userDefine = QtGui.QLineEdit(self)
		self.userDefine.setGeometry(QtCore.QRect(10, 270, 231, 24))
		self.userDefine.setObjectName("userDefine")
		
		self.label_3 = QtGui.QLabel(self)
		self.label_3.setGeometry(QtCore.QRect(10, 240, 171, 21))
		self.label_3.setObjectName("label_3")
		self.label_3.setText(QtGui.QApplication.translate("Form", "Definir Usuário Padrão", None, QtGui.QApplication.UnicodeUTF8))

		self.login = QtGui.QCheckBox(self)
		self.login.setGeometry(QtCore.QRect(250, 270, 141, 20))
		self.login.setObjectName("login")
		self.login.setText(QtGui.QApplication.translate("Form", "Login Automático", None, QtGui.QApplication.UnicodeUTF8))
		
		self.pushButton = QtGui.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(200, 300, 91, 31))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.setText(QtGui.QApplication.translate("Form", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))

		self.list_themes()
		
		self.themes.currentIndexChanged.connect(self.change_preview)
		
		self.pushButton.clicked.connect(self.apply_changes)
		
		self.show()
		
	def list_themes(self):
		#Lista os temas instalados na pasta do SLiM
		themes_dir = str("/usr/share/slim/themes/")
		theme_list = listdir(themes_dir)
		for item in theme_list:
			self.themes.addItem(item)
	
	def change_general(self, cfg, value):
		#Modifica as opções presentes no aplicativo
		config = open("/etc/slim.conf").readlines()
		for line in config:
			if cfg in line:
				if cfg == "numlock":
					if "on|off" in line:
						pass
					else:
						lns = config.index(line)
						config[lns] = str(cfg)+str("   ")+str(value)+str('\n')
						open("/etc/slim.conf", "w").writelines(config)
				else:
						lns = config.index(line)
						config[lns] = str(cfg)+str("   ")+str(value)+str('\n')
						open("/etc/slim.conf", "w").writelines(config)
	
	def change_preview(self):
		#Muda a Imagem em Preview ao se alterar o tema na ComboBox
		themes_dir = str("/usr/share/slim/themes/")
		theme_list = listdir(themes_dir)
		current_index = self.themes.currentIndex()
		current_theme = str(theme_list[current_index])
		if path.isfile(themes_dir+current_theme+str("/preview.jpg")):
			self.preview.setPixmap(QtGui.QPixmap(themes_dir+current_theme+str("/preview.jpg")))
		elif path.isfile(themes_dir+current_theme+str("/preview.png")):
			self.preview.setPixmap(QtGui.QPixmap(themes_dir+current_theme+str("/preview.png")))
		elif path.isfile(themes_dir+current_theme+str("/screenshot.png")):
			self.preview.setPixmap(QtGui.QPixmap(themes_dir+current_theme+str("/screenshot.png")))
		elif path.isfile(themes_dir+current_theme+str("/screenshot.jpg")):
			self.preview.setPixmap(QtGui.QPixmap(themes_dir+current_theme+str("/screenshot.jpg")))
		elif path.isfile(themes_dir+current_theme+str("/background.png")):
			self.preview.setPixmap(QtGui.QPixmap(themes_dir+current_theme+str("/background.png")))
		else:
			self.preview.setPixmap(QtGui.QPixmap(themes_dir+current_theme+str("/background.jpg")))
		
	def apply_changes(self):
		#Função que aplica as modificações feitas no aplicativo
		
		#Configura o usuário padrão do SLiM, se o usuário definiu
		print(self.userDefine.text())
		if self.userDefine.text() == "":
			config = open("/etc/slim.conf").readlines()
			for line in config:
				if "default_user" in line:
					lns = config.index(line)
					config[lns] = str("# ")+str(line)
					open("/etc/slim.conf", "w").writelines(config)
		else:
			self.change_general("default_user", str(self.userDefine.text()))
		
		#Configura o login automático, se o usuário definiu assim.
		print(self.login.checkState())
		if self.login.checkState() == 0:
			self.change_general("auto_login", "no")
		else:
			self.change_general("auto_login", "yes")
		
		#Configura a ativação por padrão da tecla "numlock"
		print(self.numlock.checkState())
		if self.numlock.checkState() == 0:
			self.change_general("numlock", "off")
		else:
			self.change_general("numlock", "on")
		
		#Configura o tema padrão definido pelo usuário
		themes_dir = str("/usr/share/slim/themes/")
		theme_list = listdir(themes_dir)
		current_index = self.themes.currentIndex()
		current_theme = str(theme_list[current_index])
		self.change_general("current_theme", current_theme)
		
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
