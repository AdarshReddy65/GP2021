import os

with open(os.path.expanduser('inil.txt'),'r') as f:
    read = f.readlines()
    for i in range(len(read)):
        read[i] = read[i][:-1]
    print(read)


# # from os import read
# # import cv2
# # import pytesseract
# # import numpy as np

# # pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# # cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

# # def extract_num(img_name):
# #     global read
# #     s = ''
# #     img = cv2.imread(img_name)
# #     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #     nplate = cascade.detectMultiScale(gray,1.1,4)
# #     for (x,y,w,h) in nplate:
# #         a,b = (int(0.02*img.shape[0]),int(0.025*img.shape[1]))
# #         plate = img[y+a:y+h-a,x+b:x+w-b,:]
# #         kernel = np.ones((1,1), np.uint8)
# #         plate = cv2.dilate(plate,kernel,iterations=1)
# #         plate = cv2.erode(plate,kernel,iterations=1)
# #         plate_gray = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
# #         (thresh,plate) = cv2.threshold(plate_gray,127,255,cv2.THRESH_BINARY)

# #         read = pytesseract.image_to_string(plate)
# #         read = ''.join(e for e in read if e.isalnum())
# #         s = read[:2]
# #     print(read)
        
# # img = "2.jpg"

# # extract_num(img)

# import cv2
# import torch
# import pytesseract
# from PIL import Image
# from os import walk

# pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# model = torch.hub.load('yolov5', 'custom', path='yolov5/weights/license_plate_best.pt', source='local', force_reload=True)

# # model.conf = 0.4  # confidence threshold (0-1)
# # model.classes = [0]

# result = model('1.jpg')
# result.print()
# print(result.pandas().xyxy[0])
# result.crop(save_dir='./detect/license/')

# license_src = next(walk('./detect/license/crops/numberplate'), (None, None, []))[2]  # [] if no file
# print(license_src)
# for i in range(len(license_src)):
#     license_src[i] = "./detect/license/crops/numberplate/"+license_src[i]

# for i in license_src:
#     read = pytesseract.image_to_string(Image.open(i))
#     print(read)


# # result.crop(save_dir='./detect/license/')

# # cap = cv2.VideoCapture("./src/vid1.mp4")
# # c = 1
# # timeRate = 2 # The time interval to capture video frames (here is a frame every 10 seconds)
# # k=0

# # while(True):
# #     ret, frame = cap.read()
# #     FPS = cap.get(5)
# #     if ret:
# #         frameRate = int(FPS) * timeRate # Because the number of frames obtained by cap.get(5) is not an integer, it needs to be rounded up (int for rounding down, round for rounding up, ceil( of math module for rounding up) ) Method)
# #         if(c % frameRate == 0):
# #             k+=1
# #             print("Start to capture video:" + str(k) + ".jpg")
# # 			 # Here you can do some operations: display the captured frame picture, save the captured frame to the local
# #             cv2.imwrite("./dest/" + str(k) +'.jpg', frame) # here is to save the captured image locally
# #         c += 1
# #         cv2.waitKey(0)
# #     else:
# #         print(k,"frames have been saved")
# #         break
# # cap.release()


# # helmet_src = next(walk('./src/'), (None, None, []))[2]  # [] if no file

# # for i in range(len(helmet_src)):
# #     helmet_src[i] = "./src/"+helmet_src[i]


# # model = torch.hub.load('yolov5', 'custom', path='yolov5/weights/helmet_detection_best.pt', source='local', force_reload=True)

# # model.conf = 0.4  # confidence threshold (0-1)
# # model.classes = [0]

# # result = model(helmet_src)
# # result.crop(save_dir='./detect/helmet/')

# # helmet_dest = next(walk('./detect/helmet/crops/0/'), (None, None, []))[2]  # [] if no file

# # for i in range(len(helmet_dest)):
# #     helmet_dest[i] = "./detect/helmet/crops/0/"+helmet_dest[i]

# # model.classes = [1,2]
# # model.conf = 0.25

# # helmet_result = model(helmet_dest,640)# includes NMS
# # helmet_result.save(save_dir='./detect/helmet/dest/')

# # ref = next(walk('./detect/helmet/dest/'), (None, None, []))[2]
# # license_src = []
# # for i in range(len(helmet_result.pandas().xyxy)):
# #     for j in helmet_result.pandas().xyxy[i].values.tolist():
# #         if j[5] == 2:
# #             license_src.append(ref[i])
# # for i in range(len(license_src)):
# #     license_src[i] = "./detect/helmet/dest/"+license_src[i]

# # print(license_src)


# # # for i in range(len(filenames)):
# # #     print(result.pandas().xyxy[i])
# # #     print()


# # # point = results1.pandas().xyxy[0].values.tolist()

# # # for i in point:
# # #     if i[5] == 0:
# # #         im1 = im.crop((i[1],i[1]+i[3],i[0],i[0]+i[2]))
# # #         im.show()

# # # results2.print()  # or .show()
# # # for i in results1.pandas().xyxy[0].to_dict():
# # #     print(results1.pandas().xyxy[0].to_dict()[i][0])
# # # print(results1.xyxy[0])  # img1 predictions (tensor)
# # # print(point)
# # # img1 predictions (pandas)
# # #      xmin    ymin    xmax   ymax  confidence  class    name
# # # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# # # 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# # # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# # # 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
