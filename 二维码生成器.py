import qrcode
s=input("请输入您需要转化的网址：")
qr = qrcode.QRCode(     
    version=1,     
    error_correction=qrcode.constants.ERROR_CORRECT_L,     
    box_size=10,     
    border=4, 
) 
qr.add_data(s) 
qr.make(fit=True)  
img = qr.make_image()
img.save('网站二维码.jpg')
