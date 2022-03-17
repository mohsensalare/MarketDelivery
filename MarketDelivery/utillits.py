import os
import random


def upload_path(instance, filepath, first_folder, type_file):
    rand_int = random.randint(1, 27634723542)
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    final_name = f"{instance.id}-{type_file}-{rand_int}{ext}"
    return f"{first_folder}/{final_name}"


