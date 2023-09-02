from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from datetime import datetime
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'newDesktop':
                new_name = filename
                extension = 'noname'
                try:
                    extension = str(os.path.splitext(os.path.join(folder_to_track, filename))[1])
                except Exception:
                    extension = 'noname'
                
                now = datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")

                folder_destination_path = extensions_folders.get(extension.lower(), extensions_folders['no_name'])

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(folder_destination_path):
                    if folder_name == year:
                        folder_destination_path = os.path.join(folder_destination_path, year)
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = os.path.join(folder_destination_path, month, year)
                                month_exists = True

                if not year_exists:
                    os.mkdir(os.path.join(folder_destination_path, year))
                    folder_destination_path = os.path.join(folder_destination_path, year)
                if not month_exists:
                    os.mkdir(os.path.join(folder_destination_path, month))
                    folder_destination_path = os.path.join(folder_destination_path, month)

                file_exists = os.path.isfile(os.path.join(folder_destination_path, new_name))
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(os.path.join(folder_to_track, filename))[0] + str(i) + os.path.splitext(os.path.join(folder_to_track, filename))[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(os.path.join(folder_destination_path, new_name))
                src = os.path.join(folder_destination_path, filename)
                os.rename(src, new_name)


extensions_folders = {
    #no name
    'no_name' : "/Users/Wolly/Desktop/newDesktop/Other/Uncatorgarized",
    #audio
    '.aif' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.cda' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.mid' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.midi' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.mp3' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.mpa' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.ogg' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.wav' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.wma' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.wpl' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    '.m3u' : "/Users/Wolly/Desktop/newDesktop/Media/Audio",
    #text
    '.txt' : "/Users/Wolly/Desktop/newDesktop/Text/TextFiles",
    '.doc' : "/Users/Wolly/Desktop/newDesktop/Text/Microsoft/Word",
    '.docx' : "/Users/Wolly/Desktop/newDesktop/Text/Microsoft/Word",
    '.odt ' : "/Users/Wolly/Desktop/newDesktop/Text/TextFiles",
    '.pdf': "/Users/Wolly/Desktop/newDesktop/Text/PDF",
    '.rtf': "/Users/Wolly/Desktop/newDesktop/Text/TextFiles",
    '.tex': "/Users/Wolly/Desktop/newDesktop/Text/TextFiles",
    '.wks ': "/Users/Wolly/Desktop/newDesktop/Text/TextFiles",
    '.wps': "/Users/Wolly/Desktop/newDesktop/Text/TextFiles",
    '.wpd': "/Users/Wolly/Desktop/newDesktop/Text/TextFiles",
    #Video
    '.3g2': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.3gp': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.avi': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.flv': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.h264': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.m4v': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.mkv': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.mov': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.mp4': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.mpg': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.mpeg': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.rm': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.swf': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.vob': "/Users/Wolly/Desktop/newDesktop/Media/Video",
    '.wmv': "/Users/Wolly/Desktop/newDesktop/Media/Video",
#Images
    '.ai': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.bmp': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.gif': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.ico': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.jpg': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.jpeg': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.png': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.ps': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.psd': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.svg': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.tif': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.tiff': "/Users/Wolly/Desktop/newDesktop/Media/Images",
    '.CR2': "/Users/Wolly/Desktop/newDesktop/Media/Images",
#Internet
    '.asp': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.aspx': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.cer': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.cfm': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.cgi': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.pl': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.css': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.htm': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.js': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.jsp': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.part': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.php': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.rss': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
    '.xhtml': "/Users/Wolly/Desktop/newDesktop/Other/Internet",
#Compressed
    '.7z': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.arj': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.deb': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.pkg': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.rar': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.rpm': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.tar.gz': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.z': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
    '.zip': "/Users/Wolly/Desktop/newDesktop/Other/Compressed",
#Disc
    '.bin': "/Users/Wolly/Desktop/newDesktop/Other/Disc",
    '.dmg': "/Users/Wolly/Desktop/newDesktop/Other/Disc",
    '.iso': "/Users/Wolly/Desktop/newDesktop/Other/Disc",
    '.toast': "/Users/Wolly/Desktop/newDesktop/Other/Disc",
    '.vcd': "/Users/Wolly/Desktop/newDesktop/Other/Disc",
#Data
    '.csv': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.dat': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.db': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.dbf': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.log': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.mdb': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.sav': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.sql': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.tar': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.xml': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
    '.json': "/Users/Wolly/Desktop/newDesktop/Programming/Database",
#Executables
    '.apk': "/Users/Wolly/Desktop/newDesktop/Other/Executables",
    '.bat': "/Users/Wolly/Desktop/newDesktop/Other/Executables",
    '.com': "/Users/Wolly/Desktop/newDesktop/Other/Executables",
    '.exe': "/Users/Wolly/Desktop/newDesktop/Other/Executables",
    '.gadget': "/Users/Wolly/Desktop/newDesktop/Other/Executables",
    '.jar': "/Users/Wolly/Desktop/newDesktop/Other/Executables",
    '.wsf': "/Users/Wolly/Desktop/newDesktop/Other/Executables",
#Fonts
    '.fnt': "/Users/Wolly/Desktop/newDesktop/Other/Fonts",
    '.fon': "/Users/Wolly/Desktop/newDesktop/Other/Fonts",
    '.otf': "/Users/Wolly/Desktop/newDesktop/Other/Fonts",
    '.ttf': "/Users/Wolly/Desktop/newDesktop/Other/Fonts",
#Presentations
    '.key': "/Users/Wolly/Desktop/newDesktop/Text/Presentations",
    '.odp': "/Users/Wolly/Desktop/newDesktop/Text/Presentations",
    '.pps': "/Users/Wolly/Desktop/newDesktop/Text/Presentations",
    '.ppt': "/Users/Wolly/Desktop/newDesktop/Text/Presentations",
    '.pptx': "/Users/Wolly/Desktop/newDesktop/Text/Presentations",
#Programming
    '.c': "/Users/Wolly/Desktop/newDesktop/Programming/C&C++",
    '.class': "/Users/Wolly/Desktop/newDesktop/Programming/Java",
    '.dart': "/Users/Wolly/Desktop/newDesktop/Programming/Dart",
    '.py': "/Users/Wolly/Desktop/newDesktop/Programming/Python",
    '.sh': "/Users/Wolly/Desktop/newDesktop/Programming/Shell",
    '.swift': "/Users/Wolly/Desktop/newDesktop/Programming/Swift",
    '.html': "/Users/Wolly/Desktop/newDesktop/Programming/html",
    '.h': "/Users/Wolly/Desktop/newDesktop/Programming/html",
#Spreadsheets
    '.ods' : "/Users/Wolly/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlr' : "/Users/Wolly/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xls' : "/Users/Wolly/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlsx' : "/Users/Wolly/Desktop/newDesktop/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.cab' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.cfg' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.cpl' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.cur' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.dll' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.dmp' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.drv' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.icns' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.ico' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.ini' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.lnk' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.msi' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.sys' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",
    '.tmp' : "/Users/Wolly/Desktop/newDesktop/Text/Other/System",

}

folder_to_track = '/Users/Wolly/Desktop/oldDesktop'
folder_destination = '/Users/Wolly/Desktop/newDesktop'
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