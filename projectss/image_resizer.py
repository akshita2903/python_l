import cv2

img=cv2.imread('supervised ml.png')
width=img.shape[1]
height=img.shape[0]
print(f'Original Width is {width} ,\n Original Height is {height}')
print("original image")
# cv2.imshow('image',img)
width=(int)(input("Enter the new width"))
height=(int)(input("Enter new height"))
new_image=cv2.resize(img,(width,height))
print('Updated Image')
cv2.setWindowTitle('image','Updated Image')
cv2.imshow('image',new_image)
cv2.waitKey(0)
