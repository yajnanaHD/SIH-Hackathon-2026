from ultralytics import YOLO

model = YOLO("yolo26n.pt") #loaded a pre trained model

#results = model.predict(source = 0, show = True, classes = [0]) 
#source 0 is a webcam, show = True will display the webcam feed with predictions, classes = [0] will filter for the person

#now attempting tracking on a video 

results = model.track(source=0, show=True, persist=True, classes=[0])

for r in results:
    print(r.boxes.id)
    print(r.boxes.xywh)