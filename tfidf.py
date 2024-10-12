import os
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Chemin du dossier contenant les fichiers JSON
directory = './embedDB'

# Liste pour stocker le contenu des fichiers
documents = []
file_names = []

# Lire chaque fichier JSON dans le dossier
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Convertir les données en texte
            text = ' '.join([f"{word} " * count for word, count in data.items()])
            documents.append(text)
            file_names.append(filename)

# Créer le vecteur TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Créer un DataFrame pour afficher les résultats
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out(), index=file_names)

# Afficher le DataFrame
print("Matrice TF-IDF :")
print(tfidf_df)

# Enregistrer les résultats dans un fichier CSV (optionnel)
tfidf_df.to_csv('./tfidf_results.csv', index=True)

# Calculer les scores TF-IDF totaux pour chaque mot
tfidf_scores = tfidf_df.sum(axis=0)

# Créer un DataFrame pour les scores
scores_df = pd.DataFrame(tfidf_scores, columns=['Score']).reset_index()
scores_df.columns = ['Mot', 'Score']

# Obtenir les 100 mots avec les meilleurs scores
top_words = scores_df.nlargest(100, 'Score')

# Configurer pandas pour afficher toutes les lignes et colonnes
pd.set_option('display.max_rows', None)  # Afficher toutes les lignes
pd.set_option('display.max_columns', None)  # Afficher toutes les colonnes
pd.set_option('display.expand_frame_repr', False)  # Ne pas réduire l'affichage sur plusieurs lignes

# Afficher les 100 mots ayant le meilleur score
print("\n100 mots avec le meilleur score TF-IDF :")
print(top_words)

# Réinitialiser les options d'affichage (facultatif)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
