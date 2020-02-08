import os
import shutil
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler


audio = ['.aif', '.cda', '.mid', '.midi', '.mp3',
         '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.m3u']
documents = ['.txt', '.doc', '.docx', '.odt', '.pdf',
             '.rtf', '.tex', '.wks', '.wps', '.wpd', '.key', '.odp', '.pps',
             '.ppt', '.pptx', '.ods', '.xlr', '.xls', '.xlsx']
videos = ['.3g2', '.3gp', '.avi', '.flv', '.h264''.m4v', '.mkv',
          '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.webm']
compressed = ['.7z', '.arj', '.deb', '.pkg',
              '.rar', '.rpm', '.tar.gz', '.z', '.zip']
executables = ['.apk', '.bat', '.com', '.exe', '.jar', '.wsf']
pictures = ['.ai', '.bmp', '.gif', '.ico', '.jpg', '.jpeg',
            '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.CR2']

tutorials = ['tutorial', 'course', 'how to', 'python', 'build',
             'crash', 'course', 'html', 'css', 'django', 'beginner']

tv_series = ['s01', 's02', 's03', 's04', 's05', 's06', 's07']
playlist = ['.zpl', '.xspf']
folders_to_track = ["C:/Users/Feyton Inc/Downloads", "C:/Users/Feyton Inc/Music",
                    "C:/Users/Feyton Inc/Videos", "C:/Users/Feyton Inc/Desktop"]

for folder in folders_to_track:
    os.chdir(folder)
    folder_new = os.listdir()

    for f in folder_new:
        file_name, file_ext = os.path.splitext(f)
        if file_ext != '':
            try:
                if file_ext in executables:
                    shutil.move(f, "D:/SOFTWARE")

                elif file_ext in audio:
                    shutil.move(f, "D:/AUDIO")

                elif file_ext in compressed:
                    size = os.stat(f).st_size
                    # checking the size of compressed folder
                    if int(size) in range(0, 100000000):
                        shutil.move(f, "C:/Users/Feyton Inc/Documents")
                    elif int(size) in range(100000000, 700000000):
                        shutil.move(f, "C:/Users/Feyton Inc/Documents/Crack It")
                    else:
                        shutil.move(f, "C:/Users/Feyton Inc/Videos")

                elif file_ext in documents:
                    shutil.move(f, "C:/Users/Feyton Inc/Documents")

                elif file_ext in videos:
                    if file_ext == '.mkv':
                        size = os.stat(f).st_size
                        exist = any(sub in file_name.lower() for sub in tv_series)
                        if exist:
                            shutil.move(
                                f, "C:/Users/Feyton Inc/Documents/Videos")
                        else:
                            if int(size) in range(700000000, 9000000000):
                                shutil.move(f, "D:/MOVIES")
                            elif int(size) in range(100000000, 700000000):
                                shutil.move(
                                    f, "C:/Users/Feyton Inc/Videos")
                            else:
                                shutil.move(f, "D:/VIDEOS")
                    else:
                        filename_new = file_name.lower()
                        exist = any(sub in filename_new for sub in tutorials)
                        if exist:
                            shutil.move(
                                f, "C:/Users/Feyton Inc/Documents/Crack It")
                        else:
                            try:
                                shutil.move(f, "C:/Users/Feyton Inc/Videos")
                            except:
                                pass
                elif file_ext in pictures:
                    shutil.move(f, "C:/Users/Feyton Inc/Pictures")

                elif file_ext in playlist:
                    shutil.move(f, "C:/Users/Feyton Inc/Music/Playlists")
                else:
                    shutil.move(f, "C:/Users/Feyton Inc/Documents/Others")
            except shutil.Error:
                pass
        else:
            pass
