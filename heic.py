import os
from PIL import Image
import imageio.v3 as iio

# Dossiers
directory = 'HEIC'
output_directory = 'PNG'

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Obtenir la liste des fichiers HEIF et HEIC dans le répertoire
files = [f for f in os.listdir(directory) if f.lower().endswith('.heic') or f.lower().endswith('.heif')]

# Convertir chaque fichier en PNG
for filename in files:
    heic_path = os.path.join(directory, filename)
    png_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.png')
    try:
        # Lire le fichier HEIC
        image = iio.imread(heic_path)
        # Convertir en image Pillow
        pil_image = Image.fromarray(image)
        # Sauvegarder en PNG
        pil_image.save(png_path, "PNG")
        print(f"Converted {filename} to PNG format")
    except Exception as e:
        print(f"Failed to convert {filename}: {e}")

print("Conversion terminée !")
