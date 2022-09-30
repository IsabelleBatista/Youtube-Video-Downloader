from pytube import YouTube

url = input(str("Insira a Url: "))
video = YouTube(url)

stream = video.streams.get_highest_resolution()

stream.download(output_path='C:/xampp/htdocs/_Video_Download/Videos')

