import cv2 as cv
import numpy as np
from PIL import Image
import os
def generate_dataset():
    faceclassifier = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    def face_crop(img):
        grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = faceclassifier.detectMultiScale(grayscale, 1.3, 5)
        # 1.3 for scaling 
        # KNN neigh = 5
        if len(faces) == 0:
            return None
        for (x, y, w, h) in faces:
            crop_face = img[y:y+h, x:x+w]
        return crop_face
    
    cap = cv.VideoCapture(0)
    id = 4
    img_id = 0
    while True:
        ret, frame = cap.read()
        if face_crop(frame) is not None:
            img_id+=1
            face = cv.resize(face_crop(frame),(200,200))
            face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
            filenaming = "data/user."+str(id)+"."+str(img_id)+".jpg"
            cv.imwrite(filenaming,face)
            cv.putText(face, str(img_id), (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            #5050 is the text placement
            #front scale = 1
            #boarder thickness = 2

            cv.imshow("Cropped face",face)
            if cv.waitKey(1)==13 or int(img_id)==600:
                break
    cap.release()
    cv.destroyAllWindows()
    print("Collecting Samples Completed.")
#This funtion call will get image dataset of the user
generate_dataset()

def train_classifier(data_dir):
    path = [os.path.join(data_dir,f) for f in os.listdir(data_dir)]
    faces = []
    ids = []
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img,'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        
        faces.append(imageNp)
        ids.append(id)
    ids = np.array(ids)

    #Training classifier and saving
    clf = cv.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")

#to make a classifier anda train it
#train_classifier("data")


def draw_boundary(image, classifier, scalefactor, minNeighbors, color, text, clf):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    feat = classifier.detectMultiScale(gray, scalefactor, minNeighbors)

    coords = []

    for (x, y, w, h) in feat:
        cv.rectangle(image, (x, y), (x+w, y+h), color, 2)
        id, pred = clf.predict(gray[y:y+h, x:x+w])
        confidence = int(100*(1-pred/300))

        if confidence > 70:
            if id == 1:
                cv.putText(image, "Joshua", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv.LINE_AA)
            if id == 2:
                cv.putText(image, "Duran", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv.LINE_AA)
            if id == 3:
                cv.putText(image, "Gache", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv.LINE_AA)
            if id == 4:
                cv.putText(image, "Dagle", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, color, 1, cv.LINE_AA)
        else:
            cv.putText(image, "MAGNANAKAW!", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 1, cv.LINE_AA)
            
        coords.append([x, y, w, h])  # Append the coordinates of each detected face

    return coords
def recognize(img,clf,faceCascade):
    coords = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
    return img
faceCascade =  cv.CascadeClassifier("haarcascade_frontalface_default.xml")
clf = cv.face.LBPHFaceRecognizer_create()
clf.read("classifier.xml")

vid_cap= cv.VideoCapture(0)

# while True:
#     ret,img = vid_cap.read()
#     img = recognize(img,clf,faceCascade)
#     cv.imshow("face decetion",img)

#     if cv.waitKey(1)==13:
#         break
# vid_cap.release()
# cv.destroyAllWindows()