from ultralytics import YOLO

model = YOLO("yolo26n.pt") #loaded a pre trained model

#results = model.predict(source = 0, show = True, classes = [0]) 
#source 0 is a webcam, show = True will display the webcam feed with predictions, classes = [0] will filter for the person

#now attempting tracking on a video 

results = model.track(source=0, show=True, persist=True, classes=[0], stream = True)

path_history = {}
frame_count = 0

for r in results:
    frame_count += 1
    if r.boxes.id is not None: #if the model detected a person
        ids = r.boxes.id.tolist() #converts the id tensors to a list
        centers = r.boxes.xywh.tolist() #converts coordinates tensor data to a list
        for track_id, box in zip(ids, centers): #track id is a single number, an assigned id for one specific person, it never changes
#zip() is a python tool that walks through 2 or more lists at the same time, then pairs up items that share the same position (refer to claude chat for specific example
            track_id = int(track_id)
            x, y, = box[0], box[1]

            if track_id not in path_history: #similar to adding elements to a list based upon conditions in python
                path_history[track_id] = []
            path_history[track_id].append((x, y, frame_count))