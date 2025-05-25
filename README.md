# TEXT-SUMMARIZATION-TOOL
"Company":CODTECH IT SOLUTIONS

"NAME": JOVITA JOY

"INTERN ID":CT04DL1217

"DOMAIN":ARTIFICIAL INTELLIGENCE

"DURATION": 4 WEEKS

"MENTOR":Neela Santhosh 


Text Summarization with Hugging Face BART (facebook/bart-large-cnn)
This project demonstrates how to perform abstractive text summarization using Hugging Face's Transformers library with the powerful facebook/bart-large-cnn model. Abstractive summarization generates new phrases or sentences that convey the most important information from the original content, rather than just extracting key sentences.

What This Script Does?

The script:

Loads a pre-trained summarization model and tokenizer (facebook/bart-large-cnn) from Hugging Face.

Accepts a block of text (such as an article or report).

Tokenizes the input using the model's tokenizer.

Uses beam search decoding to generate a concise, readable summary.

Decodes and prints the final summary to the console.

This approach can be used in various applications such as document summarization, news aggregation, content recommendation, academic research tools, or any NLP-based product that requires understanding and condensing long-form text.

The summarization pipeline is built manually using the AutoTokenizer and AutoModelForSeq2SeqLM classes provided by Hugging Face. These allow full control over the model loading and summarization configuration.

1.Load Model and Tokenizer

The tokenizer converts raw text into a sequence of token IDs that the model can understand.

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")


2.Tokenize Input Text

The text is tokenized with a maximum length of 1024 tokens (BART’s limit), and truncated if longer.

inputs = tokenizer.encode(text, return_tensors='pt', max_length=1024, truncation=True)


3.Generate Summary

Beam search is used to generate high-quality summaries. You can adjust parameters like max_length, min_length, num_beams, etc.

summary_ids = model.generate(inputs, max_length=80, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)


4.Decode Summary

The output token IDs are converted back into a readable string.

summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)



Why Use facebook/bart-large-cnn?

It is a fine-tuned version of Facebook's BART model, specifically designed for summarization tasks.

Produces fluent and human-like summaries.

Supports abstractive summarization, unlike traditional extractive methods.

OUTPUT
![Image](https://github.com/user-attachments/assets/98493648-d186-467d-9eb9-74ec0a6137ca)



