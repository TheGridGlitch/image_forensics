# Image Forensics Tool

A Python-based tool for extracting and analyzing metadata from image files to uncover potential signs of editing. This project uses the Pillow library for metadata extraction and provides insights into whether an image may have been edited.

## Features

- **Metadata Extraction**: Extracts EXIF metadata from image files, including details like camera make, model, GPS information, and timestamps.
- **Editing Analysis**: Analyzes metadata to detect potential signs of editing, such as:
  - Presence of editing software (e.g., Photoshop, Snapseed).
  - Inconsistencies in timestamps (e.g., `DateTimeOriginal` vs. `DateTime`).
- **User-Friendly Output**: Displays extracted metadata and analysis results in a readable format.

## Requirements

- Python 3.6+
- Pillow library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TheGridGlitch/image_forensics.git
   ```

2. Navigate to the project directory:
   ```bash
   cd image_forensics
   ```

3. Install the required dependencies:
   ```bash
   pip install Pillow
   ```

## Usage

Run the script with the path to an image file as an argument:

```bash
python image_forensics.py /path/to/image.jpg
```

### Example Output

#### For an Edited Image:
```
Extracted Metadata:
Software: Adobe Photoshop 2023
DateTimeOriginal: 2025:01:20 10:30:00
DateTime: 2025:01:21 12:45:00

Analyzing Metadata for Editing Clues...
Potential editing software detected: Adobe Photoshop 2023
Timestamp inconsistencies detected:
  DateTimeOriginal: 2025:01:20 10:30:00
  DateTime: 2025:01:21 12:45:00
Metadata analysis suggests the image may have been edited.
```

#### For an Unedited Image:
```
Extracted Metadata:
Make: Canon
Model: EOS 5D Mark IV
DateTimeOriginal: 2025:01:20 10:30:00

Analyzing Metadata for Editing Clues...
No obvious signs of editing found in the metadata.
```

## Limitations

- Only supports image formats that contain EXIF metadata, such as JPG and TIFF.
- Metadata can be intentionally removed or modified, making detection unreliable in some cases.
- Does not support PNG metadata extraction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of the Pillow library for providing powerful image processing tools.

