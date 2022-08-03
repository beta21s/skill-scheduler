import uuid
import cv2
import numpy as np
import pydicom as  dicom
from PIL import Image

class Dicom2Png:
    LEVER = 55
    WINDOWS = 120

    def translate(self, value, rescale_slope, rescale_intercept):
        return (value * rescale_slope) + rescale_intercept 

    def int12_to_int8(self, DicomImage, ds):
        rescale_slope = ds.RescaleSlope
        rescale_intercept = ds.RescaleIntercept
        img_array = []
        for eachRow in DicomImage:
            for eachPix in eachRow:
                img_array.append(self.translate(eachPix, rescale_slope, rescale_intercept))
        img_array = np.array(img_array)
        img_array = img_array.reshape(512,512)  
        return img_array

    def get_LUT_value(self, data, window, level):
        return np.piecewise(data, 
            [data <= (level - 0.5 - (window-1)/2),
                data > (level - 0.5 + (window-1)/2)],
                [0, 255, lambda data: ((data - (level - 0.5))/(window-1) + 0.5)*(255-0)])

    def toPNG(self, source, target):
        data = dicom.read_file(source)
        img = self.int12_to_int8(data.pixel_array, data)
        scaled_img = self.get_LUT_value(img, self.WINDOWS, self.LEVER)
        scaled_img = cv2.convertScaleAbs(scaled_img)
        cv2.imwrite(target + ".png", scaled_img)
        return target + ".png"