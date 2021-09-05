import cv2
import torch
from PIL import Image

# Model
model1 = torch.hub.load('yolov5', 'custom',path='yolov5/weights/helmet_detection_best.pt',source='local',force_reload=True)
# model2 = torch.hub.load('yolov5', 'custom',path='yolov5/weights/license_plate_best.pt',source='local',force_reload=True)

# Inference
results1 = model1('3.jpg')# includes NMS
# results2 = model2('1.jpg')
# Results
results1.print()
# results1.crop(save_dir='detections/helmet')

point = results1.pandas().xyxy[0].values.tolist()

# for i in point:
#     if i[5] == 0:
#         im1 = im.crop((i[1],i[1]+i[3],i[0],i[0]+i[2]))
#         im.show()

# results2.print()  # or .show()
# for i in results1.pandas().xyxy[0].to_dict():
#     print(results1.pandas().xyxy[0].to_dict()[i][0])
# print(results1.xyxy[0])  # img1 predictions (tensor)
print(point)
# img1 predictions (pandas)
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie
