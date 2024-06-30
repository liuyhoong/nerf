import subprocess
import os

def extract_frames_ffmpeg(video_path, output_folder, frame_rate=4):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 构建FFmpeg命令
    command = [
        'ffmpeg',
        '-i', video_path,                # 输入文件
        '-vf', f'fps={frame_rate}',      # 每秒抽取的帧数
        os.path.join(output_folder, 'frame_%04d.jpg')  # 输出文件格式
    ]
    
    # 运行FFmpeg命令
    subprocess.run(command)
    print("Frames extracted successfully.")

# 示例使用
video_path = 'D:/FDU/graduate/研一下/神网/期末作业/video1.mp4'
output_folder = 'D:/FDU/graduate/研一下/神网/期末作业/images'
frame_rate = 4  # 每秒抽取4帧
extract_frames_ffmpeg(video_path, output_folder, frame_rate)
