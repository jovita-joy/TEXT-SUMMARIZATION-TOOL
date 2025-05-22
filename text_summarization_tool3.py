from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

text = """
Artificial Intelligence (AI) is transforming industries across the globe. From automating customer service to predicting
disease outbreaks, AI's applications are vast and growing. In healthcare, AI helps with early diagnosis and treatment planning.
In finance, it enables fraud detection and algorithmic trading. However, with great power comes great responsibility.
Concerns over data privacy, algorithmic bias, and job displacement remain important challenges that need careful attention.
"""

inputs = tokenizer.encode(text, return_tensors='pt', max_length=1024, truncation=True)
summary_ids = model.generate(
    inputs,
    max_length=80,
    min_length=30,
    length_penalty=2.0,
    num_beams=4,
    early_stopping=True
)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Summary:")
print(summary)
