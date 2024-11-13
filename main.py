import os 
import time
from tqdm import tqdm
from datetime import datetime
import argparse

# user_defined function
from utils.utils import downloadYouTube

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("--txt", type=str,required=True, help='.txt file path')
parser.add_argument("--resolution", type=str, required=True,default='1080p',  help='1080p, 720p, 480p, 360p, 240p, 144p')
parser.add_argument("--save_path", type=str,required=False, default='./youtube_video', help='save path')
args = parser.parse_args()


def main(args):
    start_time = time.time()
    date = datetime.now()

    txt = args.txt
    save_path = args.save_path
    resolution = args.resolution

    os.makedirs(save_path, exist_ok=True)

    youtube_txt = open(txt,"r+") 
    lines = youtube_txt.readlines()
    print('[INFO] START Download {:02d}M{:02d}D_{:02d}h{:02d}m'.format(date.month, date.day, date.hour, date.minute))
    for line in tqdm(lines):
        downloadYouTube(line, resolution=resolution, save_path=save_path)
    
    end = time.time()
    print(f"[INFO]| Done ... \nTotal duration:{end - start_time}")
    
if __name__== "__main__":
    main(args)
