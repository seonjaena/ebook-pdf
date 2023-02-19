import os, shutil
folder1 = 'C:/Users/sky11/OneDrive/Desktop/tests/images'
folder2 = 'C:/Users/sky11/OneDrive/Desktop/tests/pdf'
for filename in os.listdir(folder1):
    file_path = os.path.join(folder1, filename)
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)

for filename in os.listdir(folder2):
    file_path = os.path.join(folder2, filename)
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)