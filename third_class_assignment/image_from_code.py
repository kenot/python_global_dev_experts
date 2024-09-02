from PIL import Image, ImageDraw

image_size = (200, 200)

image = Image.new("RGB", image_size, "white")

draw = ImageDraw.Draw(image)

draw.rectangle([50, 50, 150, 150], outline="blue", fill="lightblue")

draw.ellipse([75, 75, 125, 125], outline="red", fill="pink")

image.save("simple_image.png")

print("Image created and saved as 'simple_image.png'")
