# Importando a biblioteca
from pytube import YouTube

# Lista de resoluçoes disponiveis, testei todas e apenas estas funcionaram!
resolution = ['720p', '360p']

# Variavel que receberá o link do video
yt = YouTube(input('Digite a url do seu video aqui: '))


print('Video name: '+ yt.title)

print('Resoluções disponiveis: ')
print(resolution)

# variavel que receberá a resolução desejada
res = str(input('Digite a resolução que voce deseja baixar o video: '))
# Loop que garante que a resolução digitada é compativel com as resolucoes disponiveis para evitar que o programa quebre
while res not in resolution:
    res = str(input('Resolução indisponivel! Digite uma resolução da lista: '))

# variavel que determina a resolucao a ser baixada
stream = yt.streams.get_by_resolution(resolution=res)
print('downloading: '+ yt.title)
# Comando que efetua o download
stream.download()

print('The video "' + yt.title + '" was downloaded successfully!')