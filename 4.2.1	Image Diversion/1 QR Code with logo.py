# import modules for image diversion
import qrcode
from PIL import Image

# Taking image which user wants
# in the QR code center
############################
Image_Path = 'INWK 6800.PNG'

Image_logo = Image.open(Image_Path)

# Taking base width for the qr code Structure
Width_Base = 150

# Adjust image and the encrypted logo size
wpercent = (Width_Base / float(Image_logo.size[0]))
hsize = int((float(Image_logo.size[1]) * float(wpercent)))
Image_logo = Image_logo.resize((Width_Base, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)
############################
# Taking url or text which should open once scanned
url = 'https://dal.brightspace.com/d2l/home/223837' # This is reference URL of the 6800 Seminar project IN BRIGHT SPACE

# Adding URL or text to QRcode
QRcode.add_data(url)

# Generating QR code
QRcode.make()

# Taking color name from user
####################################
QRcolor = 'black'

# adding color to QR code
QR_img = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QR_img.size[0] - Image_logo.size[0]) // 2,
	   (QR_img.size[1] - Image_logo.size[1]) // 2)
QR_img.paste(Image_logo, pos)

# save the QR code generated
####################################
QR_img.save('6800.png')

print('QR code generated!') # Confirms the Generated QR Code
