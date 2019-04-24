import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import scipy.misc

def remove_bgd(img_bgr, input_folder, target_folder, i):
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    rectangle = (5, 5, 250, 250)

    #initial mask
    mask = np.zeros(img_rgb.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    #grabcut
    cv2.grabCut(img_rgb, mask, rectangle, bgdModel, fgdModel, 5, #no. of iterations
                cv2.GC_INIT_WITH_RECT) #initialization
    mask_2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    img_rgb_nobgd = img_rgb * mask_2[:, :, np.newaxis]

    scipy.misc.imsave('/home/user/Documents/final_year_project/data/'+target_folder+'/'+input_folder+'_'+str(i)+'.jpg', img_rgb_nobgd)
    print(i)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def main():
    count = int(input('enter the no. of folders to convert : '))
    for i in range(0, count):
        input_folder = ['bacterial_spot','blight','healthy','leaf_mold','yellowleaf_curl_virus']
        target_folder = ['bacterial_spot_nobgd','blight_nobgd','healthy_nobgd','leaf_mold_nobgd','yellowleaf_curl_virus_nobgd']
        images = load_images_from_folder('/home/user/Documents/final_year_project/data/'+input_folder[i])
        j = 0
        for img in images:
            j += 1
            remove_bgd(img, input_folder[i], target_folder[i], j)

if __name__ == '__main__':
    main()

