# Imports 
import io
import os
from google.cloud import vision
import google.auth
from google.oauth2 import service_account
import cv2
import numpy as np 
from google.protobuf.json_format import MessageToJson
import re 

# image path 
path = './test/test5.webp'

# Image Load 
image = cv2.imread(path)


# # Preprocessing =======================================
# generates inputImage


# # Simple thresholding --------------------------------------------
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# threshImg = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# inputImage = cv2.cvtColor(threshImg,cv2.COLOR_BGR2RGB)
# cv2.imwrite('cloudInput.jpg',inputImage)



# # Better for date parsing -------------------------------------------------
# imageBw = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# ret, bw = cv2.threshold(imageBw, 150,255,cv2.THRESH_BINARY_INV)
# connectivity = 10
# nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(bw, connectivity, cv2.CV_32S)
# sizes = stats[1:, -1]; nb_components = nb_components - 1
# min_size = 50 #threshhold value for small noisy components
# img2 = np.zeros((output.shape), np.uint8)
# for i in range(0, nb_components):
#     if sizes[i] >= min_size:
#         img2[output == i + 1] = 255
# trans = cv2.bitwise_not(img2)
# inputImage = cv2.cvtColor(trans,cv2.COLOR_BGR2RGB)
# cv2.imwrite('cloudInput.jpg',inputImage)



# # Shaprening ------------------------------------------ Better for blur Images, makes only black text pop 
# kernel = np.array([[-1,-1,-1], [-1,10,-1], [-1,-1,-1]])
# trans = cv2.filter2D(image, -1, kernel)
# inputImage = cv2.cvtColor(trans,cv2.COLOR_BGR2RGB)
# cv2.imwrite('cloudInput.jpg',inputImage)





# # No Preprocessing --------------------------------- 
inputImage = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imwrite('cloudInput.jpg',inputImage)

# # Preprocessing ======================================= END END END END END END END END END END




# # Getting Cloud Vision Outputs =====================================
# Add secret key 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/mnt/c/Users/Samarth Negi/Desktop/engine/documentParser/secret/documentParserSecret.json'

client = vision.ImageAnnotatorClient()
with io.open('./cloudInput.jpg', 'rb') as image_file:
    content = image_file.read()
imageCloud = vision.Image(content=content)
response = client.document_text_detection(image=imageCloud)



def checkPassport(response):
    corpus = []
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    corpus.append(word_text)

    corpus = [x.lower() for x in corpus]

    tests = 0 

    if 'nationality' in corpus:
        tests = tests + 1 
    if 'passport' in corpus:
        tests = tests + 1 
    if 'ind' in corpus:
        tests = tests + 1 

    joined = ''.join(corpus)
    lessThan = joined.count('<')

    if lessThan > 10:
        tests = tests + 3 

    if tests > 3 :
        return True
    else:
        return False


def checkAadhar(response):
    corpus = []
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    corpus.append(word_text)

    corpus = [x.lower() for x in corpus]
    globs = [] 
    trig = 0 
    current_glob = []
    for ind,snap in enumerate(corpus) : 
        if snap.isnumeric():
            if len(snap)==4:
                globs.append([snap,corpus[ind+1],corpus[ind+2]])

    regex = ("^[2-9]{1}[0-9]{3}\\" +"s[0-9]{4}\\s[0-9]{4}$")
    for glob in globs:
        joined = ' '.join(glob)
        p = re.compile(regex)
        if(re.search(p, joined)):
            return True
        else:
            pass
    return False

print(f'CheckPassport,{checkPassport(response)}')
print(f'checkAadhar,{checkAadhar(response)}')




# with io.open(path, 'rb') as image_file:
#     content = image_file.read()

# def detect_document(path):
#     """Detects document features in an image."""
#     

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.Image(content=content)

#     response = client.document_text_detection(image=image)

#     for page in response.full_text_annotation.pages:
#         for block in page.blocks:
#             print('\nBlock confidence: {}\n'.format(block.confidence))

#             for paragraph in block.paragraphs:
#                 print('Paragraph confidence: {}'.format(
#                     paragraph.confidence))

#                 for word in paragraph.words:
#                     word_text = ''.join([
#                         symbol.text for symbol in word.symbols
#                     ])
#                     print('Word text: {} (confidence: {})'.format(
#                         word_text, word.confidence))

#                     for symbol in word.symbols:
#                         print('\tSymbol: {} (confidence: {})'.format(
#                             symbol.text, symbol.confidence))

#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))



# -------------------------

# from google.cloud.vision import ImageAnnotatorClient
# import os
# import base64
# 

# # def encode_image(image_path):
# #     with open(image_path, "rb") as f:
# #         image_content = f.read()
# #         return base64.b64encode(image_content)

# client = vision.ImageAnnotatorClient()


# with io.open(path, 'rb') as image_file:
#     content = image_file.read()

# image = vision.Image(content=content)

# response = client.document_text_detection(image=image)
# print(response)