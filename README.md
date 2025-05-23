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

2.Tokenize Input Text
The text is tokenized with a maximum length of 1024 tokens (BART’s limit), and truncated if longer.

3.Generate Summary
Beam search is used to generate high-quality summaries. You can adjust parameters like max_length, min_length, num_beams, etc.

4.Decode Summary
The output token IDs are converted back into a readable string.

Why Use facebook/bart-large-cnn?

It is a fine-tuned version of Facebook's BART model, specifically designed for summarization tasks.

Produces fluent and human-like summaries.

Supports abstractive summarization, unlike traditional extractive methods.



