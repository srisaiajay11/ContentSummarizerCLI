from transformers import pipeline

# Load content from file or prompt user
try:
    with open("content.txt", "r") as file:
        content = file.read().strip()
    if not content:
        raise ValueError("Content file is empty!")
except FileNotFoundError:
    print("Error: content.txt not found!")
    content = input("Enter the content to summarize (type 'exit' to stop): ")
    if content.lower() == 'exit':
        print("Exiting.")
        exit()
    if not content.strip():
        print("Error: Content cannot be empty!")
        exit()

# Summary generation
def generate_summary(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    if len(text) > 2500:
        raise ValueError("Text exceeds 2500 characters. Please shorten it.")
    summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
    return summary[0]['summary_text']

# Chatbot Q&A
def answer_question(question, context, summary):
    qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
    full_context = context + " " + summary
    answer = qa_pipeline(question=question, context=full_context)
    return answer['answer']

# Test Run
if __name__ == "__main__":
    print("Content:", content)
    try:
        summary = generate_summary(content)
        print("Summary:", summary)
    except Exception as e:
        print(f"Error generating summary: {e}")
        exit()

    # Loop for multiple questions
    while True:
        question = input("Ask a question about the content (type 'exit' to stop): ")
        if question.lower() == 'exit':
            print("Exiting question loop.")
            break
        if not question.strip():
            print("Error: Please enter a valid question!")
            continue
        try:
            answer = answer_question(question, content, summary)
            print("Question:", question)
            print("Answer:", answer)
        except Exception as e:
            print(f"Error answering question: {e}")