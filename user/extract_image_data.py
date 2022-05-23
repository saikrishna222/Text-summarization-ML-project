from PIL import Image
import pytesseract
import cv2
import os
from django.conf import settings

class ExtractsImagesData:
    def extract_data(self, filename):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        filepath = settings.MEDIA_ROOT + "\\" + filename
        # load the example image and convert it to grayscale
        image = cv2.imread(filepath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # cv2.imshow("Image", gray)

        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite("media/" + filename, gray)

        # img = cv2.imread("C:/Users/VISHAL/images/" + filename)
        # cv2.imshow(filename, img)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        src_path = "media/"
        text = pytesseract.image_to_string(Image.open(src_path + filename))
        os.remove("media/" + filename)
        # data = get_details(text)

        # show the output images
        # cv2.imshow("Image", image)
        # cv2.imshow("Output", gray)
        cv2.waitKey(0)

        return text


