# ContentSummarizerCLI

A command-line tool to summarize text and answer questions about the content using AI models.

## Features
- Summarize text using the `facebook/bart-large-cnn` model.
- Answer questions based on the content and summary using the `deepset/roberta-base-squad2` model.
- Load content from `content.txt` or enter directly via CLI.

## Installation
1. Clone the repository: git clone https://github.com/srisaiajay11/ContentSummarizerCLI.git
   cd ContentSummarizerCLI
2. Install dependencies:
    `pip install -r requirements.txt`

3. Run the application:
    `python summarizer.py`

## Requirements
- Python 3.6+
- See `requirements.txt` for dependencies.

## Usage
1. (Optional) Create a file named `content.txt` in the same directory as `summarizer.py` and add your content.
2. Run the script: python summarizer.py

3. If `content.txt` is not found, you will be prompted to enter the content directly (type `exit` to stop).
4. The script will display the content and its summary.
5. Ask questions about the content (type `exit` to stop).

## Limitations
- Maximum input text length: 2500 characters.
- No GUI or audio output.

## License
MIT License

