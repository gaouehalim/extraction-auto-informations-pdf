from PyPDF2 import PdfReader
from pdf2image import convert_from_bytes
from ocr import extract_text_from_image

def extract_text_from_pdf(pdfs):
    """Extrait du texte des PDFs en utilisant PyPDF2 et OCR pour les images."""
    if pdfs is None:
        return None

    docs = []
    
    for pdf in pdfs:
        try:
            reader = PdfReader(pdf)
            pdf_text = ""

            for i, page in enumerate(reader.pages, start=1):
                text = page.extract_text()

                if text:
                    pdf_text += f"\n--- Page {i} ---\n{text}"
                else:
                    images = convert_from_bytes(pdf.read())
                    ocr_text = ""
                    
                    for img in images:
                        img_cv = np.array(img)
                        extracted_text = extract_text_from_image(img_cv)
                        ocr_text += extracted_text + "\n"
                    
                    pdf_text += f"\n--- Page {i} (OCR) ---\n{ocr_text}"

            docs.append(pdf_text)
        
        except Exception as e:
            continue

    return docs
