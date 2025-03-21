import cv2
import pytesseract
import numpy as np

OCR_CONFIG = "--oem 3 --psm 6"

def preprocess_image(image):
    """Amélioration de l'image pour une meilleure reconnaissance OCR."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    kernel = np.ones((2, 2), np.uint8)
    denoised = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    return denoised

def extract_text_from_image(image):
    """Extrait du texte d'une image via OCR."""
    preprocessed_img = preprocess_image(image)
    return pytesseract.image_to_string(preprocessed_img, config=OCR_CONFIG)
