from pafy import new
video = new(input("enter link here:"))
stream = video.getbest()
stream.download()



