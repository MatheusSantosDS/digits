import matplotlib.pyplot as plt
import cv2 as cv
import glob

PATH = "data/*.jpg"

#usado para ver os histogramas
#file = "data/cdf0755_46_22_5.jpg"

def somar_pixels(img):
  #Soma das linhas e das colunas
  soma_horizontal = []
  soma_vertical = []

  #Preenche vetor coluna com 0's
  for x in range(len(img[0])):
    soma_vertical.append(0)

  for i in range(len(img)):
    sum = 0

    for j in range(len(img[i])):

      #binarizando o valor
      if(img[i][j] > 127):
        soma_vertical[j] += 1
        sum += 1

    soma_horizontal.append(sum)
    
  return soma_horizontal, soma_vertical

'''
#histogramas, para vizualizar as somas de pixels
def plotar_histograma(soma):
  plt.bar(range(len(soma)),soma,align='center')
  plt.show()
  return 0
'''

#Pegando as labels de cada imagem do arquivo files.txt
f = open("files.txt", "r")

text = f.read()
f.close()

filetxt = text.splitlines()
dict_labels = {}

#Dividindo arquivo em um dictionario com formato -> nome_da_imagem: label_da_imagem
for i in filetxt:
  dict_labels[i[5:-6]] = int(i[-1])

#ler as imagens, pegar os vetores de características e escrever no arquivo data.txt
for file in glob.glob(PATH):
    
    #le a imagem com o cv.imread, e da resize para o tamanho 40x40 usando 'nearest'
    imagem = cv.imread(file, cv.IMREAD_GRAYSCALE)
    imagem_resized = cv.resize(imagem, (40,40), interpolation = cv.INTER_NEAREST)
      
    soma_horizontal, soma_vertical = somar_pixels(imagem_resized)

    with open('datas.txt', 'a') as f:
        
        for item in soma_horizontal:
            f.write(str(item))
            f.write(" ")

        for item in soma_vertical:
            f.write(str(item))
            f.write(" ")

        f.write(str(dict_labels[file[5:-4]]))

        f.write("\n")





