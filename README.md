# Image Processing Python Project

Este projeto consiste em um conjunto de scripts em Python para processamento de imagens. Ele inclui funcionalidades para redimensionamento de imagens e aplicação de filtros.

## Estrutura do Projeto

O projeto é organizado da seguinte maneira:

- `image_processing.py`: Este arquivo contém funções para redimensionamento de imagens.
- `image_filters.py`: Este arquivo contém funções para aplicação de filtros em imagens.

## Pré-requisitos

Certifique-se de ter instalado as seguintes bibliotecas Python:

- Pillow: `pip install Pillow`

## Como Usar

1. Importe as funções relevantes nos seus scripts Python.
2. Use as funções para processar suas imagens conforme necessário.

Exemplo de uso:

```python
from image_processing import resize_image
from image_filters import apply_filter

# Redimensionar uma imagem
resized_image = resize_image("input_image.jpg", 300, 200)
if resized_image:
    resized_image.save("resized_image.jpg")

# Aplicar um filtro a uma imagem
image = Image.open("input_image.jpg")
filtered_image = apply_filter(image, "BLUR")
if filtered_image:
    filtered_image.save("filtered_image.jpg")
