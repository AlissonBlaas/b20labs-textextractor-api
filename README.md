# B2LABS CODE CHALLENGE API
## Description

The B2LABS API support Web and Mobile Applications.

## Code Standards

## Setup

Create .env file based on .env.example with the appropriate configurations.

## Prerequisites

you will need python installed in your machine

### To Run Locally:

1. Install dependencies using pip or other package manager.

2. Run the server after installing the dependencies:
 - to execute locally
```bash
python api/main.py
```

### Environment Variables

Refer to the .example.env file for environment variables.

## SOLID
i try to apply solid to this backend by made some classes and export those classes and their methods

### THE METHODOS THAT I USE
### [FILE](https://github.com/AlissonBlaas/b2labs-textextractor-api/blob/main/api/text_extractor.py) contains TextExtractor
- TextExtractor is an interface representing a strategy for extracting text.


### [FILE](https://github.com/AlissonBlaas/b2labs-textextractor-api/blob/main/api/text_extractor.py) contains PyMuPDFTextExtractor
- PyMuPDFTextExtractor is a concrete implementation of the text extraction strategy using PyMuPDF.
```
## PyMuPDF Library:
PyMuPDF is used to open and read the PDF document (fitz.open("pdf", file_data)).
The document is processed page by page using a loop (for page_number in range(doc.page_count):).

## Text Extraction:
For each page in the PDF, the text content is extracted using page.get_text().
The extracted text from each page is concatenated to form the complete text content of the PDF.

## Error Handling:
Exception handling is implemented to capture any errors that may occur during the text extraction process.
If an error occurs, it is caught, and an error message is returned in the result dictionary ({'error': f"Error extracting text: {str(e)}"}).
```

### [FILE](https://github.com/AlissonBlaas/b2labs-textextractor-api/blob/main/api/text_generator.py) contains OpenAITextGenerator
- OpenAITextGenerator is a concrete implementation of the text generation strategy using OpenAI.
```
The OpenAITextGenerator class is responsible for interacting with the OpenAI API to generate text based on a given prompt.
The class is initialized with the OpenAI API key, which is typically kept confidential and should be stored securely.

## Generation Method:
The generate_text method of the OpenAITextGenerator class takes a prompt as input.
The prompt is constructed using the extracted text from the PDF content in the TextProcessingService class.
In the provided example, the prompt is constructed with the message "Given the following PDF text:\n{extracted_text}\nGenerate a relevant text:".

## API Request:
The OpenAI API key and prompt are used to make a request to the OpenAI API using the openai.Completion.create method.
The prompt and other relevant parameters are passed to the API, and the response is received.
```


### [FILE](https://github.com/AlissonBlaas/b2labs-textextractor-api/blob/main/api/text_processing.py) contains TextProcessingService
- TextProcessingService is a high-level module that uses the extracted text and generates additional text.
```
Initialization:

The class is initialized with instances of TextExtractor and TextGenerator.
These instances are provided through dependency injection, allowing the class to work with different implementations of text extraction and text generation.
Process Text Method:

The main method of the class is process_text(file_data).
It takes the raw content of a PDF document (file_data) as input.
Text Extraction:

It calls the extract_text method of the injected TextExtractor to extract text from the provided PDF content.
The result of text extraction is stored in the extraction_result variable.
```


This separation adheres to SRP and DIP, making the code more modular and adherent to SOLID principles. 
The TextProcessingService can easily switch between different implementations of text extraction and generation without modifying its code, making it more flexible and maintainable.



## WHERE THIS CAN BE USED

### Use Case: Summarizing legal contracts, agreements, or court documents.

Benefit: Helps legal professionals quickly identify key terms, obligations, and legal implications.
News Article Summarization:

### Use Case: Summarizing news articles for readers.

Benefit: Provides a brief summary of news stories, enabling users to stay informed without reading every article.



## THIS BACKEND ARE DEPLOYED AT RENDER
![image](https://github.com/AlissonBlaas/b2labs-textextractor-api/assets/32876996/dda6647d-4f97-4568-88ff-7d9d2857cd80)
  
[FRONTEND](https://github.com/AlissonBlaas/b2labs-textextractor-web) ARE DEPLOYED AT VERCEL

WEB DEMO: https://b2labs-textextractor-web.vercel.app/

