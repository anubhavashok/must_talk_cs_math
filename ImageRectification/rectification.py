import numpy as np
import cv2

img = cv2.imread('img.jpg')
rows,cols,ch = img.shape

# mapping of coordinates in base image to coordinates in rectified image
pts1 = np.float32([[900,rows-186], [900, rows-70], [1300, rows-70]])
pts2 = np.float32([[0, cols],[0, 0],[rows, 0]])

M = cv2.getAffineTransform(pts1, pts2)
print M
dst = cv2.warpAffine(img, M, (cols,rows))
cv2.imwrite('dst_out.jpg', dst)

img2 = cv2.imread('img2.jpg')
rows,cols,ch = img.shape

# mapping of coordinates in base image to coordinates in rectified image
pts1 = np.float32([[300, cols-126], [279, cols-100], [571, cols-100]])
pts2 = np.float32([[0, cols],[0, 0],[rows, 0]])

M = cv2.getAffineTransform(pts1, pts2)
print M
dst2 = cv2.warpAffine(img, M, (cols,rows))
cv2.imwrite('dst2_out.jpg', dst2)
