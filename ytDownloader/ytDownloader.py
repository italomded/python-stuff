from pytube import YouTube
from pydub import AudioSegment
import os

audio_dir = './audio/'
video_dir = './video/'
temp_dir = './temp/'

def downloadVideo(youtube):
    try:
        print('MSG: downloading...')
        youtube.streams.filter(progressive=True).order_by('resolution')[-1].download(video_dir)
    except Exception:
        raise
    else:
        print('MSG: finished!')

def downloadAudio(youtube):
    try:
        print('MSG: downloading...')
        audio = youtube.streams.get_audio_only()
        audio_title = audio.title
        audio_subtype = audio.subtype
        audio_path = temp_dir +  audio_title + '.' + audio_subtype
        audio.download(temp_dir)
        convertAudio(audio_path, audio_subtype, audio_title)
        deleteFile(audio_path)
    except Exception:
        raise
    else:
        print('MSG: finished!')


def convertAudio(path, a_format, title):
    try:
        print('MSG: converting...')
        audio = AudioSegment.from_file(path, a_format)
        audio.export(audio_dir + title + '.mp3', 'mp3')
    except Exception:
        raise
        

def deleteFile(path):
    try:
        print('MSG: deleting demo file...')
        os.remove(path)
    except Exception:
        raise


def createDir():
    if (not os.path.exists(audio_dir)):
            os.mkdir(audio_dir)
    if (not os.path.exists(temp_dir)):
            os.mkdir(temp_dir)
    if (not os.path.exists(video_dir)):
            os.mkdir(video_dir)


createDir()
while True:
    try:
        option = input('OPTIONS: 1. audio | 2. video | 3. exit | INPUT: ')
        if option == '1':
            url = input('URL: ')
            youtube = YouTube(url)
            downloadAudio(youtube)
        elif option == '2':
            url = input('URL: ')
            youtube = YouTube(url)
            downloadVideo(youtube)
        else:
            print('MSG: goodbye!')
            break
    except Exception:
        print('ERROR: something went wrong!')