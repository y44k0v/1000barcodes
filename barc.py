import barcode

from barcode.writer import SVGWriter
from barcode.writer import ImageWriter

# kind of barcode 
EAN = barcode.get_barcode_class('ean13')


# first 9 digits of barcode out of 13
starter0 = "123456789"

for num in range(1000):
    starter = ""
    # 0 filler to have always 3 digits
    if num <10:
        starter = starter0 +"00"+ str(num)
    elif num <100:
        starter = starter0 +"0"+ str(num)
    else:
        starter = starter0 + str(num)
        
    # save SVG    
    my_ean = EAN(starter)
    my_ean.save(str(my_ean))   
    # Save PNG    
    my_ean2 = EAN(starter, writer=ImageWriter())
    my_ean2.save(str(my_ean2))
    
    # Save to FILE
    with open("barcodes.txt",'a') as file:
        file.write(str(my_ean)+"\n")
    
    
    

