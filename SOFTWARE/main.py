from ultralytics import YOLO

model = YOLO("yolo26n.pt") #loaded a pre trained model

results = model.predict(source = 0, show = True, classes = [0]) 
#source 0 is a webcam, show = True will display the webcam feed with predictions, classes = [0] will filter for the person
