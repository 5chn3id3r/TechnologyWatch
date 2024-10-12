import os
import json
from htmlreader import html_to_stats
from pdfreader import pdf_to_stats


def process_html_file(file_path):
    stats = html_to_stats(file_path)
    
    # Crée un fichier .json dans le dossier embedDB avec les stats
    file_name = os.path.basename(file_path)
    embed_file = f"./embedDB/{file_name}.json"
    with open(embed_file, 'w', encoding='utf-8') as embed:
        json.dump(stats, embed, ensure_ascii=False, indent=4)  # Sauvegarde en format JSON

def process_pdf_file(file_path):
    stats = pdf_to_stats(file_path)
    
    # Crée un fichier .json dans le dossier embedDB avec les stats
    file_name = os.path.basename(file_path)
    embed_file = f"./embedDB/{file_name}.json"
    with open(embed_file, 'w', encoding='utf-8') as embed:
        json.dump(stats, embed, ensure_ascii=False, indent=4)  # Sauvegarde en format JSON

def list_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Vérifie l'extension du fichier
            if file.lower().endswith(('.html', '.htm')):
                process_html_file(file_path)
            elif file.lower().endswith('.pdf'):
                process_pdf_file(file_path)

if __name__ == "__main__":
    archives_dir = "./archives"
    list_files_in_directory(archives_dir)
