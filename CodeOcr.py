from PIL import Image,ImageEnhance,ImageFilter
import pytesseract
im = Image.open("code.png")
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('code2.png')
text = pytesseract.image_to_string(im)
print(text)