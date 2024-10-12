# I need to user it because archive already existe but not supposed to be used if not 
import hashlib
import os
import csv

def generate_file_hash(file_path, hash_algorithm='sha256'):
    """
    Génère un hash pour le fichier spécifié en utilisant l'algorithme donné (par défaut 'sha256').
    """
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def process_files_in_directory(directory, output_csv):
    """
    Parcourt tous les fichiers du répertoire donné, génère leurs hash et les stocke dans un fichier CSV.
    """
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Hash'])  # Entête du fichier CSV

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = generate_file_hash(file_path)
                writer.writerow([file_hash])

if __name__ == "__main__":
    archives_dir = "./archives/"
    output_csv = "./DBHashes.csv"
    process_files_in_directory(archives_dir, output_csv)
    print(f"Les hash des fichiers ont été enregistrés dans {output_csv}")
