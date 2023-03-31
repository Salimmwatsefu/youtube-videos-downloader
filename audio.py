from pytube import YouTube


link = input("Enter a link to download")
yt = YouTube(link)

print("Title: ", yt.title) 

print("Views: ", yt.views)

yd = yt.streams.filter(only_audio=True).get_audio_only()
print("Downloading...")

yd.download("/home/salim/development/audio")
print("Done")