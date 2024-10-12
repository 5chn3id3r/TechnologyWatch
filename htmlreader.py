import html2text
import nltk
from collections import Counter
from nltk.corpus import stopwords

# Télécharger les stop words si ce n'est pas déjà fait
nltk.download('stopwords')

def convert_html_to_text(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    text_content = html2text.html2text(html_content)
    
    return denoiser(text_content)

def denoiser(raw_text):
    # Récupérer les stop words en anglais et en français
    stop_words_en = set(stopwords.words('english'))
    stop_words_fr = set(stopwords.words('french'))

    def is_clean(word):
        non_alpha_chars = sum(1 for char in word if not char.isalpha())
        if len(word) == 0 or len(word) > 30:
            return False
        non_alpha_ratio = non_alpha_chars / len(word)
        
        return non_alpha_ratio <= 0.2

    # Filtrer les mots pour exclure les stop words et nettoyer le texte
    clean_text = " ".join(
        [word for word in raw_text.split(" ") if is_clean(word) and word.lower() not in stop_words_en and word.lower() not in stop_words_fr]
    )
    
    return clean_text

def html_to_stats(input_file):
    text = convert_html_to_text(input_file)
    words = text.split()
    word_frequencies = Counter(words)
    stats = dict(word_frequencies)

    return stats

if __name__ == "__main__":
    query = 'random query bellec'
    text_content = convert_html_to_text("./archives/binary-fuzzing-strategies-what-works.html")
    stats = html_to_stats(text_content)
    print(stats)  # Affiche les statistiques des mots
