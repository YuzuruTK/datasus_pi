from PIL import Image
import os
from pathlib import Path

def compress_image(input_path, quality=50):
    """
    Compresses an image file using Pillow with a lower quality setting for more aggressive compression.
    """
    img = Image.open(input_path)
    output_path = input_path.with_name(f"{input_path.stem}_compressed{input_path.suffix}")
    img.save(output_path, quality=quality)
    return output_path

def process_images_in_folder(max_size_mb=1):
    """
    Processes images in the current working directory recursively, compressing images larger than max_size_mb.
    """
    current_directory = Path.cwd()  # Get current working directory
    for path in current_directory.glob("**/*"):
        if path.is_file():
            if path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:  # Add more formats if needed
                size_mb = path.stat().st_size / (1024 * 1024)
                if size_mb > max_size_mb:
                    print(f"Compressing {path.name} ({size_mb:.2f} MB)...")
                    compressed_path = compress_image(path, quality=50)  # Adjust quality here (e.g., 50 for more aggressive)
                    os.remove(path)  # Delete original image
                    os.rename(compressed_path, path)  # Rename compressed image to original name
                    print(f"Compression complete for {path.name}")
                    print("---------------------------------")

# Exemplo de uso:
process_images_in_folder()
