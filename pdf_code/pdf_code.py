import PyPDF2
from PyPDF2 import PdfReader

def pdf_code():
    file_path = "C:\\Users\\felix\\YandexDisk\\Уник\\Уник_4курс_\\Предметы\\Инжинерные исследования\\ghostwriter\\ghostwriter_gptApiFree\\pdf_documents\\7.32-2017.pdf"

    reader = PdfReader(file_path)

    for page in reader.pages:
        content = page.extract_text() # содержимое документ
        # print(content)

    return content