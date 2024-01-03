from text_extractor import TextExtractor
from text_generator import TextGenerator

class TextProcessingService:
    def __init__(self, text_extractor: TextExtractor, text_generator: TextGenerator):
        self.text_extractor = text_extractor
        self.text_generator = text_generator

    def process_text(self, file_data):
        extraction_result = self.text_extractor.extract_text(file_data)
        if 'error' in extraction_result:
            return extraction_result

        extracted_text = extraction_result.get('text', '')

        prompt = f"Given the following PDF text:\n{extracted_text}\nGenerate a relevant text:"
        generation_result = self.text_generator.generate_text(prompt)

        return {'generated_text': generation_result}