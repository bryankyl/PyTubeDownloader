from pytube import YouTube

def download():
    url = input("Enter the Video URL : ")
    video = YouTube(url)
    date = video.publish_date.strftime("%Y%m%d")
    file_name = video.title + ".mp4"
    file_name = file_name.replace("/", ".")
    file_name = date + " - " + file_name
    video.streams.filter(type="video", subtype="mp4", progressive=True).order_by('resolution').desc()[0].download(filename=file_name)
    print("Download " + file_name + " completed.")
    print(url)