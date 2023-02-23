import cv2
import os
import argparse

# obter o caminho do diretório de imagens
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--images', required=True, help='path to input directory of images')
args = vars(ap.parse_args())

# criar a pasta resized_images se não existir
if not os.path.exists('resized_images'):
    os.makedirs('resized_images')

# iterar cada imagem no diretório
for image in os.listdir(args['images']):
    # carregar a imagem
    img = cv2.imread(os.path.join(args['images'], image))
    # verificar se a imagem foi carregada com sucesso
    if img is not None:
        # redimensionar a imagem para 640x640
        res = cv2.resize(img, dsize=(640, 640), interpolation=cv2.INTER_AREA)
        # salvar a imagem redimensionada na pasta resized_images com o mesmo nome
        cv2.imwrite(os.path.join('resized_images', image), res)
        print(f'Image {image} resized successfully to 640x640')
    else:
        print(f'Image {image} not found')