# File Operations

This Python script provides a graphical user interface (GUI) for changing file extensions and checking video file integrity in a specified directory. It was created using Claude-3.5-sonnet, an AI language model, based on user requirements and questions.

## Features

- Change file extensions in a selected directory
- Check the integrity of video files in a selected directory
- Option to include subdirectories in both processes
- Simple and intuitive graphical interface
- Progress bars for both operations to provide visual feedback

## Requirements

- Python 3.x
- tkinter library (usually comes pre-installed with Python)
- av library for video file checking (install via `pip install av`)

## Usage

1. Run the script:
   ```
   python GUI.py
   ```

2. The GUI window will appear with the following options:
   - **Directory**: Enter or browse for the target directory
   - **Old Extension**: Enter the current file extension (e.g., ".txt")
   - **New Extension**: Enter the desired new file extension (e.g., ".md")
   - **Include Subdirectories**: Check this box to process files in subdirectories for both functionalities

3. Click the "Change Extensions" button to start changing file extensions. A progress bar will indicate the progress of the operation.

4. Click the "Check Video Files" button to start checking the integrity of video files. A progress bar will also indicate the progress of this operation.

5. Success messages will display the number of files changed or checked.

## Note

Always make sure to back up your files before running this script, as the file extension changes might be irreversible.

## Credits

This script was created with the assistance of an AI language model, based on user requirements and questions. This also means that there is no copyright on this program, and you are free to use it any way you like.