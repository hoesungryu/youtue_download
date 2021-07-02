import os 
import time
import tqdm
from datetime import datetime
import argpars

# user_defined function
from utils.utils import downloadYouTube

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("--txt", type=str,required=True, help='.txt file path')
parser.add_argument("--save_path", type=str,required=False, help='save path')
args = parser.parse_args()


def main(args):
    start = time.time()
    date = datetime.now()
    
	youtube_txt = args.txt
	save_path = args.save_path

    lines = youtube_txt.readlines()
    print('[INFO] START Download {:02d}M{:02d}D_{:02d}h{:02d}m'.format(date.month, date.day, date.hour, date.minute)

    for line in tqdm(lines):
        downloadYouTube(line, save_path)
        
    end = time.time()
    print(f"[INFO]| Done ... \nTotal duration:{end_time - start_time}")
    

if __name__=='__main__':
	main(args)