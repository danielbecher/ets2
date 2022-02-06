#APP para fazer backup dos perfis do Euto Truck Simulator 2 no Windows 10/11.
#Importa as bibliotecas necessárias
import os
import glob
from time import sleep
from datetime import datetime
import shutil 

#Seta a hora da cópia para a criação do diretório
#Formato do diretório dentro do backup é DIA_MES_ANO_-_HORA_MINUTO_SEGUNDOS
hora = datetime.today().strftime('%d_%m_%Y_-_%H_%M_%S')

#Seta os diretórios dos profiles e destino
diretoriosteam = os.path.expanduser('~\\Documents\\Euro Truck Simulator 2\\steam_profiles')
diretoriolocal = os.path.expanduser('~\\Documents\\Euro Truck Simulator 2\\profiles')
diretoriodestino = "backup/" + hora

#Cria o diretório de backup
#os.mkdir(diretoriodestino)

#Faz a cópia dos profiles da steam
shutil.copytree(diretoriosteam,diretoriodestino+'/steam/')

#Faz a cópia dos profiles locais
shutil.copytree(diretoriolocal,diretoriodestino+'/local/')