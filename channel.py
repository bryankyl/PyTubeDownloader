from pytube import Channel
from pytube import YouTube

def download():
    try:
        url = input("Enter the Channel URL : ")
        c = Channel(url)
    except:
        print("Not a valid Channel URL.")
    else:
        print("Download from the Channel: " + c.channel_name)
        print("There are " + str(len(c.videos)) + " videos in this channel.")

        start_date = 20220101
        end_date = 20220114

        for video_url in c:
            video = YouTube(video_url)
            date = video.publish_date.strftime("%Y%m%d")
            if (int(date) >= start_date) and (int(date) <= end_date):
                file_name = video.title + ".mp4"
                file_name = file_name.replace("/", ".")
                file_name = date + " - " + file_name
                video.streams.filter(type="video", subtype="mp4", progressive=True).order_by('resolution').desc()[
                    0].download(filename=file_name)
                print("Download " + file_name + " completed.")
                print(video_url)