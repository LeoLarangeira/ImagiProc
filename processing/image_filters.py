from PIL import ImageFilter

def apply_filter(image, filter_name):
    """
    Aplica um filtro à imagem.

    Args:
    - image: Objeto de imagem a ser filtrado.
    - filter_name: Nome do filtro a ser aplicado.

    Returns:
    - filtered_image: Imagem após a aplicação do filtro.
    """
    try:
        # Converte o nome do filtro para o objeto de filtro correspondente
        filter_function = getattr(ImageFilter, filter_name)
        
        # Aplica o filtro à imagem
        filtered_image = image.filter(filter_function)
        
        return filtered_image
    except AttributeError:
        print("Filtro não encontrado. Certifique-se de que o nome do filtro está correto.")
        return None
    except Exception as e:
        print("Erro ao aplicar o filtro:", e)
        return None
