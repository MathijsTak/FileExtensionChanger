import os

def count_files_with_extension(directory, extension, include_subdirs):
    count = 0
    for root, dirs, files in os.walk(directory):
        count += sum(1 for file in files if file.endswith(extension))
        if not include_subdirs:
            break
    return count

def change_extensions(directory, old_ext, new_ext, include_subdirs, progress_callback):
    changed_files = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(old_ext):
                old_path = os.path.join(root, filename)
                new_filename = os.path.splitext(filename)[0] + new_ext
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                changed_files += 1
                progress_callback(changed_files)
        if not include_subdirs:
            break
    return changed_files