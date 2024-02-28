from PIL import Image

def resize_image(image_path, new_width, new_height):
    """
    Redimensiona uma imagem para as dimensões especificadas.

    Args:
    - image_path: Caminho para a imagem a ser redimensionada.
    - new_width: Nova largura desejada para a imagem.
    - new_height: Nova altura desejada para a imagem.

    Returns:
    - resized_image: Objeto de imagem redimensionado.
    """
    try:
        # Abre a imagem
        image = Image.open(image_path)
        
        # Redimensiona a imagem
        resized_image = image.resize((new_width, new_height))
        
        return resized_image
    except Exception as e:
        print("Erro ao redimensionar a imagem:", e)
        return None
