import subprocess
import os

# def convert_480p(source):
#     target = os.path.splitext(source)[0] + '_480p.mp4'
#     cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#     subprocess.run(cmd, capture_output=True)


def convert_480p(source):
     target = os.path.splitext(source)[0] + '_480p.mp4'
     cmd = [
         'ffmpeg',
         '-i', source,
         '-s', 'hd480',
         '-c:v', 'libx264',
         '-crf', '23',
         '-c:a', 'aac',
         '-strict', '-2',
         target
     ]
     result = subprocess.run(cmd, capture_output=True, text=True)
     if result.returncode != 0:
         print(f"Error: {result.stderr}")
     else:
         print(f"Successfully converted {source} to {target}")

