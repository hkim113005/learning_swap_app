from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(file_path):
    """Get metadata from an image file."""
    with Image.open(file_path) as img:
        exif_data = img._getexif()
        if not exif_data:
            return None
        metadata = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
        return metadata

# Example usage:
metadata = get_image_metadata('unnamed.jpg')
if metadata:
    print(metadata.get('DateTimeOriginal'))
else:
    print('No metadata found.')