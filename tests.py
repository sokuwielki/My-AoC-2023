from PIL import Image 
import pytesseract 

# If you're on windows, you will need to point pytesseract to the path 
# where you installed Tesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\smok5\AppData\Local\Programs\Python\Python310\Scripts'
 
# Open the image file 
# replace 'test.png' with your image file 
img = Image.open(r'C:\Users\smok5\Desktop\penis.jpg')
 
# Use pytesseract to convert the image data to text 
text = pytesseract.image_to_string(img)
 
# Print the text print(text)
print(text)