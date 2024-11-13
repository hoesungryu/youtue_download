from pytubefix.cli import on_progress, download_by_resolution
from pytubefix import YouTube
import moviepy.editor as mpe
import os


def itags(yt, resolution='1080p'):
    max_audio = 0
    audio_value = 0
    for audio_stream in yt.streams.filter(only_audio=True):
        abr = int(audio_stream.abr.replace('kbps', ''))
        if abr > max_audio:
            max_audio = abr
            audio_value = audio_stream.itag
    streams = yt.streams
    try:
        video_tag = streams.filter(res=resolution, fps=60)[0].itag
        # print('60 FPS')
        fps=60
    except IndexError:
        video_tag = streams.filter(res=resolution, fps=30)
        if video_tag:
            video_tag = video_tag[0].itag
            # print('30 FPS')
            fps = 30
        else:
            video_tag = streams.filter(res=resolution, fps=24)[0].itag
            # print('24 FPS')
            fps = 24
    
    video_info = {
        'FPS': fps,
        'TITLE': yt.title
    }
    return audio_value, video_tag, video_info


def combine_audio(video_info, tmp_save_path, save_path):
    vidname = os.path.join(tmp_save_path, video_info["TITLE"] + '.mp4')
    audname = os.path.join(tmp_save_path, video_info["TITLE"] + '.m4a')
    fps = video_info["FPS"]
    outname = os.path.join(save_path, video_info["TITLE"] + '.mp4')

    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, fps=fps)

def downloadYouTube(url , resolution='144p', save_path='./youtube_video', tmp_save_path='./tmp'):
    os.makedirs(tmp_save_path, exist_ok=True)
    yt = YouTube(url, on_progress_callback=on_progress)
    audio, video, video_info = itags(yt, resolution)
    yt.streams.get_by_itag(audio).download(tmp_save_path)
    yt.streams.get_by_itag(video).download(tmp_save_path)
    combine_audio(video_info, tmp_save_path, save_path)
    # print(f'Downloaded {video_info["TITLE"]} at {resolution} {video_info["FPS"]} FPS')