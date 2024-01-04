![image](https://github.com/AlissonBlaas/b2labs-textextractor-api/assets/32876996/3a3e30c5-7a67-41ed-a28e-5394aaeb5f52)# B2LABS CODE CHALLENGE API
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

```bash
python main.py to execute locally
```

### Environment Variables

Refer to the .example.env file for environment variables.

## SOLID
i try to apply solid to this backend by made some classes and export those classes and their methods

### THE METHODOS THAT I USE
TextExtractor is an interface representing a strategy for extracting text.

PyMuPDFTextExtractor is a concrete implementation of the text extraction strategy using PyMuPDF.

OpenAITextGenerator is a concrete implementation of the text generation strategy using OpenAI.

TextProcessingService is a high-level module that uses the extracted text and generates additional text.

This separation adheres to SRP and DIP, making the code more modular and adherent to SOLID principles. 
The TextProcessingService can easily switch between different implementations of text extraction and generation without modifying its code, making it more flexible and maintainable.

## THIS BACKEND ARE DEPLOYED AT RENDER
![image](https://github.com/AlissonBlaas/b2labs-textextractor-api/assets/32876996/dda6647d-4f97-4568-88ff-7d9d2857cd80)
  
[FRONTEND](https://github.com/AlissonBlaas/b2labs-textextractor-web) ARE DEPLOYED AT VERCEL

WEB DEMO: https://b2labs-textextractor-web.vercel.app/

