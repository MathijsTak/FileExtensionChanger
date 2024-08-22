import os
import av

def count_video_files(directory, include_subdirs):
    count = 0
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')  # Add more if needed
    for root, dirs, files in os.walk(directory):
        count += sum(1 for file in files if file.lower().endswith(video_extensions))
        if not include_subdirs:
            break
    return count

def check_video_file(file_path):
    try:
        with av.open(file_path) as container:
            # Check if the file has at least one video stream
            return any(stream.type == 'video' for stream in container.streams)
    except av.AVError as e:
        print(f"Error checking {file_path}: {str(e)}")
        return False

def check_files(directory, include_subdirs, progress_callback):
    checked_files = 0
    corrupted_files = []
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')  # Add more if needed
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(video_extensions):
                file_path = os.path.join(root, filename)
                if not check_video_file(file_path):
                    corrupted_files.append(file_path)
                checked_files += 1
                progress_callback(checked_files)
        if not include_subdirs:
            break
    return checked_files, corrupted_files