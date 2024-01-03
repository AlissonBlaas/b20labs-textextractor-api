import fitz

class TextExtractor:
    def extract_text(self, file_path):
        pass

class PyMuPDFTextExtractor(TextExtractor):
    def extract_text(self, file_path):
        text = ""
        try:
            doc = fitz.open(file_path)
            for page_number in range(doc.page_count):
                page = doc[page_number]
                text += page.get_text()
        except Exception as e:
            return {'error': str(e)}
        finally:
            if 'doc' in locals():
                doc.close()
        return {'text': text}