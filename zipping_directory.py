import pyminizip
import os

def get_paths_recursively(src_root_path):
    files = []
    if src_root_path is not None:
        for root, directories, filenames in os.walk(src_root_path):
            entries = []
            for filename in filenames:
                full_file_name = os.path.join(root, filename)
                if os.path.isfile(full_file_name) and not filename.startswith('.'):
                    files.append(os.path.join(root, filename))
    return files

def pyminizip_zipper(folder_path, output_path, password):
    paths = get_paths_recursively(folder_path)
    print(paths)
    roots = []
    for path in paths:
        roots.append(os.path.dirname(path.replace(os.path.dirname(folder_path), './')))
    print(roots)
    pyminizip.compress_multiple(paths, roots, output_path, password, 5)

def pyminizip_unzipper(zip_path, output_path, password):
    pyminizip.uncompress(zip_path, password, output_path, 5)
