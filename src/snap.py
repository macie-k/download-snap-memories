import piexif
import piexif.helper
import src.download_memories as dm

from datetime import datetime
from urllib.parse import urlparse, parse_qs

class Snap:
    def __init__(self, json_data):
        self.timestamp = datetime.strptime(json_data['Date'], '%Y-%m-%d %H:%M:%S %Z')   # timestamp object from given date
        self.url = json_data['Download Link']                                           # download url
        self.base_name = f'{self.timestamp.strftime("%Y-%m-%d_%H-%M-%S")}'              # filename without path and extension
        self.extension = '.mp4' if json_data['Media Type'] == 'Video' else '.jpg'       # file extension based on type
        self.mid = parse_qs(urlparse(self.url).query)['mid'][0]                         # media_id value from url to uniquely identify photos

    # returns filename with path and extension
    def get_filename(self):
        return dm.target_dir + self.base_name + self.extension

    # saves exif information
    def save_exif(self):
        try:
            exif_dict = piexif.load(self.get_filename())
            piexif.remove(self.get_filename())
            new_date = self.timestamp.strftime("%Y:%m:%d %H:%M:%S")
            exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
            exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
            exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
            exif_dict['Exif'][piexif.ExifIFD.UserComment] = piexif.helper.UserComment.dump(self.mid)

            piexif.insert(piexif.dump(exif_dict), self.get_filename())
        except:
            return None

    def get_mid_exif(self):
        try:
            return piexif.helper.UserComment.load(piexif.load(self.get_filename())['Exif'][piexif.ExifIFD.UserComment])
        except:
            return None