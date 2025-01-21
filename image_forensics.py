import argparse
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_metadata_pillow(image_path):
    """Extract metadata using Pillow."""
    metadata = {}
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    gps_data = {}
                    for gps_id in value:
                        gps_tag = GPSTAGS.get(gps_id, gps_id)
                        gps_data[gps_tag] = value[gps_id]
                    metadata["GPSInfo"] = gps_data
                else:
                    metadata[tag] = value
        else:
            print(f"No EXIF metadata found in {image_path}.")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
    return metadata

def analyze_metadata(metadata):
    """Analyze metadata for signs of editing."""
    print("\nAnalyzing Metadata for Editing Clues...")
    suspicious_tags = ["Software", "ProcessingSoftware"]
    timestamps = ["DateTimeOriginal", "DateTimeDigitized", "DateTime"]

    editing_signs = False

    # Check for editing software
    for tag in suspicious_tags:
        if tag in metadata:
            print(f"Potential editing software detected: {metadata[tag]}")
            editing_signs = True

    # Check for timestamp inconsistencies
    date_values = {tag: metadata.get(tag) for tag in timestamps if tag in metadata}
    if len(date_values) > 1:
        print("Timestamp inconsistencies detected:")
        for key, value in date_values.items():
            print(f"  {key}: {value}")
        editing_signs = True

    if not editing_signs:
        print("No obvious signs of editing found in the metadata.")
    else:
        print("Metadata analysis suggests the image may have been edited.")

def display_metadata(metadata):
    """Display metadata in a readable format."""
    if not metadata:
        print("No metadata to display.")
        return
    for key, value in metadata.items():
        print(f"{key}: {value}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract and analyze metadata from an image file.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    args = parser.parse_args()

    # Check if the file exists
    if not os.path.exists(args.image_path):
        print("Invalid file path. Please check and try again.")
        return

    # Extract metadata
    print("\nExtracting Metadata...")
    metadata = extract_metadata_pillow(args.image_path)

    # Display metadata and analyze for editing clues
    if metadata:
        print("\nExtracted Metadata:")
        display_metadata(metadata)
        analyze_metadata(metadata)
    else:
        print("No metadata extracted.")

if __name__ == "__main__":
    main()
