from PIL import Image
from processing.image_processing import resize_image
from processing.image_filters import apply_filter

# Exemplo de uso de redimensionamento
resized_image = resize_image("input_image.jpg", 300, 200)
if resized_image:
    resized_image.save("resized_image.jpg")

# Exemplo de uso de aplicação de filtro
image = Image.open("input_image.jpg")
filtered_image = apply_filter(image, "BLUR")
if filtered_image:
    filtered_image.save("filtered_image.jpg")
