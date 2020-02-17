import os
import shutil
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import random


def FilenameChange(file_to_rename):
    name, ext = os.path.splitext(file_to_rename)
    num = random.randint(1, 10)
    new_name = f'{name}{num}{ext}'
    return new_name


class MyCleaner(FileSystemEventHandler):
    def on_modified(self, event):
        for folder in folders_to_track:
            os.chdir(folder)
            folder_new = os.listdir()

            for f in folder_new:
                file_name, file_ext = os.path.splitext(f)
                if file_ext != '':
                    try:
                        if file_ext in executables:
                            try:
                                shutil.move(f, "D:/SOFTWARE")
                            except FileExistsError:
                                new_name = FilenameChange(f)
                                os.rename(f, new_name)
                                continue

                        elif file_ext in audio:
                            shutil.move(f, "D:/AUDIO")

                        elif file_ext in compressed:
                            size = os.stat(f).st_size
                            # checking the size of compressed folder
                            if int(size) in range(0, 100000000):
                                shutil.move(f, "C:/Users/Feyton Inc/Documents")
                            elif int(size) in range(100000000, 700000000):
                                shutil.move(
                                    f, "C:/Users/Feyton Inc/Documents/Crack It")
                            else:
                                shutil.move(f, "C:/Users/Feyton Inc/Videos")

                        elif file_ext in documents:
                            try:
                                shutil.move(f, "C:/Users/Feyton Inc/Documents")
                            except FileExistsError:
                                new_name = FilenameChange(f)
                                os.rename(f, new_name)
                                continue
                        elif file_ext in videos:
                            if file_ext == '.mkv':
                                size = os.stat(f).st_size
                                exist = any(sub in file_name.lower()
                                            for sub in tv_series)
                                if exist:
                                    shutil.move(
                                        f, "C:/Users/Feyton Inc/Videos")
                                else:
                                    if int(size) in range(700000000, 9000000000):
                                        try:
                                            shutil.move(f, "D:/MOVIES")
                                        except FileExistsError:
                                            new_name = FilenameChange(f)
                                            os.rename(f, new_name)
                                            continue
                                    elif int(size) in range(100000000, 700000000):
                                        shutil.move(
                                            f, "C:/Users/Feyton Inc/Videos")
                                    else:
                                        shutil.move(f, "D:/VIDEOS")
                            else:
                                filename_new = file_name.lower()
                                exist = any(
                                    sub in filename_new for sub in tutorials)
                                if exist:
                                    shutil.move(
                                        f, "C:/Users/Feyton Inc/Documents/Crack It")
                                else:
                                    try:
                                        shutil.move(
                                            f, "C:/Users/Feyton Inc/Videos")
                                    except FileExistsError:
                                        new_name = FilenameChange(f)
                                        os.rename(f, new_name)
                                        continue
                        elif file_ext in pictures:
                            shutil.move(f, "C:/Users/Feyton Inc/Pictures")

                        elif file_ext in playlist:
                            shutil.move(
                                f, "C:/Users/Feyton Inc/Music/Playlists")
                        elif file_ext in design:
                            shutil.move(
                                f, "C:/Users/Feyton Inc/Documents/Design")
                        elif file_ext in downloading:
                            pass
                        else:
                            shutil.move(
                                f, "C:/Users/Feyton Inc/Documents/Others")
                    except FileExistsError:
                        new_name = FilenameChange(f)
                        os.rename(f, new_name)
                        continue
                    except shutil.Error:
                        pass
                    except Exception:
                        try:
                            new_name = FilenameChange(f)
                            os.rename(f, new_name)
                            continue
                        except Exception:
                            pass
                else:
                    shutil.move(f, "C:/Users/Feyton Inc/Documents")


audio = ['.aif', '.cda', '.mid', '.midi', '.mp3',
         '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.m3u']
documents = ['.txt', '.doc', '.docx', '.odt', '.pdf',
             '.rtf', '.tex', '.wks', '.wps', '.wpd', '.key', '.odp', '.pps',
             '.ppt', '.pptx', '.ods', '.xlr', '.xls', '.xlsx', '.csv']

design = ['.xd', '.psd', '.html', '.css']
videos = ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
          '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv', '.webm', '.srt']
compressed = ['.7z', '.arj', '.deb', '.pkg',
              '.rar', '.rpm', '.tar.gz', '.z', '.zip']

executables = ['.apk', '.bat', '.com', '.exe', '.jar', '.wsf', '.msi']

pictures = ['.ai', '.bmp', '.gif', '.ico', '.jpg', '.jpeg',
            '.png', '.ps', '.svg', '.tif', '.tiff', '.CR2']

tutorials = ['tutorial', 'course', 'how to', 'python', 'build',
             'crash', 'course', 'html', 'css', 'django', 'beginner']

tv_series = ['s01', 's02', 's03', 's04', 's05', 's06', 's07']

playlist = ['.zpl', '.xspf']

downloading = ['.crdownload', '.download']

folders_to_track = ["C:/Users/Feyton Inc/Downloads"]

event_handler = MyCleaner()
observer = Observer()
observer.schedule(event_handler, folders_to_track[0], recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
