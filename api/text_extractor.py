import fitz

class TextExtractor:
    def extract_text(self, file_path):
        pass

class PyMuPDFTextExtractor(TextExtractor):
    def extract_text(self, file_data):
        try:
            doc = fitz.open("pdf", file_data)

            text = ''
            for page_number in range(doc.page_count):
                page = doc[page_number]
                text += page.get_text()

            return {'text': text}

        except Exception as e:
            return {'error': f"Error extracting text: {str(e)}"}
        finally:
            if 'doc' in locals():
                doc.close()