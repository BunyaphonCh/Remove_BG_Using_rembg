from rembg import remove
from PIL import Image
from PIL import ImageFilter

input_path = 'C:/Users/user/Downloads/Delete_BG/image/remove_my_bg.jpg'
output_path = 'result.png'

input_image = Image.open(input_path)

output = remove(input_image)
output = output.filter(ImageFilter.GaussianBlur(radius=1))

white_bg = Image.new('RGB', output.size, (255, 255, 255))
white_bg.paste(output, mask=output.split()[-1])

white_bg.save(output_path)