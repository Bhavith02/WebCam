import cv2
import os
import glob

images = glob.glob("*.jpg") #glob is used to find path names given some kind of pattern . Here this takes all images in the folder

for image in images:
    img = cv2.imread(image,1)  # if u want to read only one then : img = cv2.imread("photo2",0)
    path = 'resized'
    re = cv2.resize(img,(290,350))
    cv2.imshow("Gray",re)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(path,"resized_"+image),re)

# to print type of image                          : print(type(img))
# to pring img in terms of array(matrix) of bits  : print(img)
# to print resolution of image                    : print(img.shape)
