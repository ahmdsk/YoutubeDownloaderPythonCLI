import os
import random

from pytube import YouTube
from pytube import Playlist


print("""===== Youtube Downloader =====
Menu List:
1. Single Download
2. Playlist Download
3. Keluar
==============================
""")
menu = int(input("Pilih Menu: "))
current_dir = os.getcwd()

if menu == 1:
    url = input("Masukan URL Video: ")
    yt_single = YouTube(url)
    videos = []
    
    for index, stream in enumerate(yt_single.streams.order_by('resolution').filter(adaptive=True, file_extension='mp4'), start=1):
        videos.append(stream)
        
        print(f"""
        {index}. {yt_single.title} | {yt_single.author}
        Resolusi: {stream.resolution}
        """)

    resolution = int(input("Pilih Resolusi: "))
    result = videos[resolution - 1]

    # Download Video
    print("Menunggu Video Di Download...")
    new_file_name = f"{yt_single.title}-{random.randint(1, 1000)}.mp4"
    result.download(filename=new_file_name)
    print("Video Berhasil Di Download.. :D")
elif menu == 2:
    url = input("Masukan Playlist Video: ")
    yt_playlist = Playlist(url)

    print(f"""
    Pilihan Resolusi:
    1. 144p
    2. 240p
    3. 360p
    4. 480p
    5. 720p
    6. 1080p
    """)
    set_res = int(input("Pilih Resolusi: "))

    if set_res == 1:
        res_input = "144p"
    elif set_res == 2:
        res_input = "240p"
    elif set_res == 3:
        res_input = "360p"
    elif set_res == 4:
        res_input = "480p"
    elif set_res == 5:
        res_input = "720p"
    elif set_res == 6:
        res_input = "1080p"
    else:
        print("Resolusi Pilihan Belum Tersedia!")
        exit()

    print("Menunggu Semua Video Di Download...")
    new_folder = f"{current_dir}/{yt_playlist.title}"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Ubah Ke Folder Baru
    os.chdir(new_folder)

    # Download Playlist
    for link in yt_playlist:
        for stream in YouTube(link).streams.order_by('resolution').filter(adaptive=True, file_extension='mp4', res=res_input):
            stream.download()

    print("Berhasil Mendownload Playlist")
elif menu == 3:
    print("Good Bye...")
    exit()
else:
    print("Menu Tidak Tersedia")