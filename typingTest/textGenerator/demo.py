from textGenerator_nGram import NGramTextGenerator

def clean_text(text: str) -> str:
    import re
    text = re.sub(r'\s+', ' ', text)  # collapse whitespace
    return text.strip()

with open("warandpeace.txt", encoding="utf-8") as f:
    corpus = f.read()

corpus = clean_text(corpus)



generator = NGramTextGenerator(n=3)
generator.build_model(corpus)

print("📜 Generated samples:\n")

for i in range(5):
    print(f"{i+1}. {generator.generate(length=20)}\n")
