# Punjabi_Diet_Expert

An AI-powered chatbot providing personalized guidance on Canadian nutrition recommendations.

## Overview

This project implements a LLM chatbot focused on diet and nutrition. It uses advanced natural language processing to provide accurate, context-aware responses to dietary inquiries.

## Key Components

- LLM: HuggingFaceH4/zephyr-7b-beta
- Embedding: all-MiniLM-L6-v2 sentence transformer
- Vector Database: FAISS
- UI: Gradio
- Knowledge Base: Punjabi Diet Expert PDF

## Features

- RAG-enhanced responses for up-to-date nutritional advice
- Customizable chat parameters (max tokens, temperature, top-p)
- User-friendly interface for easy interaction

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure "Punjabi Diet Expert-pdf.pdf" is in the project directory
4. Run the application: `python app.py`

## Usage

The chatbot can answer questions about:
- Daily serving recommendations for different food groups
- Serving size examples
- Nutritional guidelines specific to Canada's Food Guide

## Technical Details
- User queries trigger a semantic search in the indexed documents
- Retrieved context is combined with the query for LLM processing
- Responses are generated considering both the query and relevant guide sections

## Limitations

This assistant is based on a specific nutritional guide and should not replace professional medical advice. It's intended for general information only.

## Future Improvements

- Expand the knowledge base with additional nutritional resources
- Implement multi-language support for broader accessibility
- Add visual aids for serving sizes and food groups

## Contribution

Contributions to improve the assistant's accuracy, expand its knowledge, or enhance its features are welcome. Please submit pull requests or open issues for discussion.

## Contact

For questions or feedback, please contact: ha4369939@alphacollege.me

---

Disclaimer: This project is for educational purposes and should not be used as a substitute for professional nutritional or medical advice.
