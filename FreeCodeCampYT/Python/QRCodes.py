# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:49:44 2022

@author: Frostmoon
"""
# QR Code encrypting & decrypting in Python

import qrcode

# data to be encoded as a QR code
data = "Don\'t forget to like, subscribe, and check me out on other platforms!"

# filepath to the folder where the QR code will be saved as an image file
savepath = "E:/Users/Administrator/Downloads/Other Coding Practice/FreeCodeCampYT/Python/"

def encode_into_qr(data, savepath, qrFit = True, vers = 1, b_size = 10, bord = 5, fillColor = "black", backgroundColor = "white"):
    # Changing properties/looks/styling of the QR code
    qr = qrcode.QRCode(version = vers, box_size = b_size, border = bord)
    qr.add_data(data)
    qr.make(fit = qrFit)
    
    # encoding the data
    img = qr.make_image(fill_color = fillColor, back_color = backgroundColor)
    
    # saving the resulting image file
    img.save(savepath + "myqrcode2.png")
    
# passing the data to the encoding function
#encode_into_qr(data, savepath, fillColor = "white", backgroundColor = "black")

from pyzbar.pyzbar import decode
from PIL import Image
from pprint import pprint

# decoding data from a QR code
def decode_from_qr(imagepath):
    img = Image.open(imagepath + "myqrcode.png")
    result = decode(img)
    pprint(result)
    
decode_from_qr(savepath)