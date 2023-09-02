from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'newDesktop':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" + year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Uncategorized",
#Audio
    '.aif' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.cda' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.mid' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.midi' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.mp3' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.mpa' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.ogg' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.wav' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.wma' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.wpl' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
    '.m3u' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Audio",
#Text
    '.txt' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.doc' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Microsoft/Word",
    '.docx' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Microsoft/Word",
    '.odt ' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.pdf': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/PDF",
    '.rtf': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.tex': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.wks ': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.wps': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.wpd': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/TextFiles",
#Video
    '.3g2': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.3gp': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.avi': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.flv': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.h264': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.m4v': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.mkv': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.mov': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.mp4': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.mpg': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.mpeg': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.rm': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.swf': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.vob': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
    '.wmv': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Video",
#Images
    '.ai': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.bmp': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.gif': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.ico': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.jpg': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.jpeg': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.png': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.ps': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.psd': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.svg': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.tif': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.tiff': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
    '.CR2': "/Users/Wolly/OneDrive/Desktop/newDesktop/Media/Images",
#Internet
    '.asp': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.aspx': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.cer': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.cfm': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.cgi': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.pl': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.css': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.htm': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.js': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.jsp': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.part': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.php': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.rss': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
    '.xhtml': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Internet",
#Compressed
    '.7z': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.arj': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.deb': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.pkg': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.rar': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.rpm': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.tar.gz': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.z': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.zip': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Compressed",
#Disc
    '.bin': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Disc",
    '.dmg': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Disc",
    '.iso': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Disc",
    '.toast': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Disc",
    '.vcd': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Disc",
#Data
    '.csv': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.dat': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.db': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.dbf': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.log': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.mdb': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.sav': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.sql': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.tar': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.xml': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
    '.json': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Database",
#Executables
    '.apk': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Executables",
    '.bat': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Executables",
    '.com': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Executables",
    '.exe': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Executables",
    '.gadget': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Executables",
    '.jar': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Executables",
    '.wsf': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Executables",
#Fonts
    '.fnt': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Fonts",
    '.fon': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Fonts",
    '.otf': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Fonts",
    '.ttf': "/Users/Wolly/OneDrive/Desktop/newDesktop/Other/Fonts",
#Presentations
    '.key': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.odp': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.pps': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.ppt': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.pptx': "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Presentations",
#Programming
    '.c': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/C&C++",
    '.class': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Java",
    '.dart': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Dart",
    '.py': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Python",
    '.sh': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Shell",
    '.swift': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/Swift",
    '.html': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/html",
    '.h': "/Users/Wolly/OneDrive/Desktop/newDesktop/Programming/html",
#Spreadsheets
    '.ods' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlr' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xls' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlsx' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cab' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cfg' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cpl' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cur' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.dll' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.dmp' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.drv' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.icns' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.ico' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.ini' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.lnk' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.msi' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.sys' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.tmp' : "/Users/Wolly/OneDrive/Desktop/newDesktop/Text/Other/System",
}

folder_to_track = '/Users/Wolly/OneDrive/Desktop/oldDesktop'
folder_destination = '/Users/Wolly/OneDrive/Desktop/newDesktop'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()