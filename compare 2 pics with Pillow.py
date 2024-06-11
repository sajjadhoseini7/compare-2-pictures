from PIL import Image
import numpy as np

def compare_images(image1, image2):
  image_size = image1.size

  diff_image = np.abs(image1 - image2)

  sum_errors = np.sum(diff_image)
  
  avg = (sum_errors/image_size)
  
  return avg

image1 = Image.open('path/image.jpg')
image2 = Image.open('path/image.jpg')

#image1 = image1.convert('L')
#image2 = image2.convert('L')

image1=np.array(image1)
image2=np.array(image2)

image1=image1.astype('int')
image2=image2.astype('int')

difference_image = compare_images(image1, image2)

print(f'Totally, the average difference of 2 images per pixel is {difference_image}')

difference_percent = (difference_image/(255))*100
print(f'The difference of 2 images based on percentage is {difference_percent}%')



