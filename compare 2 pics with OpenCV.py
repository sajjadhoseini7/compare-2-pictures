import cv2
import numpy as np

def compare_images(image1, image2):
  image_size = image1.size

  diff_image = cv2.absdiff(image1, image2)
  #diff_image = np.abs(image1 - image2)

  sum_errors = np.sum(diff_image)
  
  avg = sum_errors/image_size
  
  return avg

image1 = cv2.imread('path/image.jpg')
image2 = cv2.imread('path/image.jpg')

#image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

image1=image1.astype('int')
image2=image2.astype('int')

difference_image = compare_images(image1, image2)

print(f'Totally, the average difference of 2 images per pixel is {difference_image}')

difference_percent = (difference_image/(255))*100
print(f'The difference of 2 images based on percentage is {difference_percent}%')



