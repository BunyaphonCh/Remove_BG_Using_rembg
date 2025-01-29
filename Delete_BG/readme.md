# Explain Code

## Input

![Input Image](image\remove_my_bg.jpg "This is a Input Image")

## Result
![Output Image](result.png "This is a Output Image")

## don't forget to use `pip install rembg` !!
My project is remove background, add blur effect and change image to white background

## Import library
```
from rembg import remove
from PIL import Image
from PIL import ImageFilter
```
### rembg is library for remove background
### PIL (Python Imaging Library) and ImageFilter for image manipulation and using filter such as blur

## Specifies location file
### First, i'm gonna use result.jpg but it have problem about RGBA because RGBA include transparency but format jpeg not support so i use result.png instead
```
input_path = 'C:/Users/user/Downloads/Delete_BG/image/remove_my_bg.jpg'
output_path = 'result.png'
```
### Open image location using PIL

```
input_image = Image.open(input_path)
```
### Remove background. The result is stored in output and using Gaussian Blur for make it appear smoother
```
output = remove(input_image)
output = output.filter(ImageFilter.GaussianBlur(radius=1))
```
### Create new white background and paste image to white background then save output
```
white_bg = Image.new('RGB', output.size, (255, 255, 255))
white_bg.paste(output, mask=output.split()[-1])
white_bg.save(output_path)
```