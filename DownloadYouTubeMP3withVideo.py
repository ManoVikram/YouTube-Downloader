#! python3
# This program will download a MP3 format of a YouTube video

import os, subprocess

try:
	from selenium import webdriver
except:
	print("Installing required package...")
	os.system("python -m pip install selenium")
	# Comment the above line and uncomment the below line if on Linux
	# os.system("python3 -m pip3 install selenium")

try:
	from pytube import YouTube
except:
	print("Installing required package...")
	os.system("python -m pip install pytube3")
	# Comment the above line and uncomment the below line if on Linux
	# os.system("python3 -m pip3 install pytube3")

while True:
	songName = input("Enter the name of the song(enter 0 to quit): ")

	if songName == "0":
		break

	browser = webdriver.Chrome()
	browser.get("https://www.youtube.com/results?search_query=" + songName)

	searchResults = browser.find_elements_by_id("video-title")

	allDetails = []
	num = 0
	for data in searchResults:
		videoDetails = []
		num += 1

		videoDetails.append(data.get_attribute("aria-label"))
		videoDetails.append(data.get_attribute("href"))

		if videoDetails[0] == None or videoDetails[1] == None:
			continue

		allDetails.append(videoDetails)

		if (num >= 5):
			break

	# print(allDetails)

	num = 0
	print("0. Quit\n")
	for data in allDetails:
		num += 1

		print(str(num) + ". TILE => " + data[0])
		print("\t\t" + data[1] + "\n")
	num += 1
	print(str(num) + ". Select different song\n")

	choice = int(input("Enter the Number of the song in the list: "))
	print("\n")
	if choice == 0:
		break
	elif choice == num:
		continue
	choice -= 1

	# allDetails[choice].click()

	youtubeFile = YouTube(allDetails[choice][1])
	# streams = youtubeFile.streams.filter(only_audio=True)
	streams = youtubeFile.streams.filter(subtype="mp4").filter(progressive=True).order_by("resolution").desc()

	num = 0
	print("0. Quit\n")
	for stream in streams:
		num += 1
		print(str(num) + ". ", stream, "\n")
	num += 1
	print(str(num) + ". Select different song\n")

	selectStream = int(input("Enter the number of the stream: "))
	print("\n")
	if selectStream == 0:
		break
	elif selectStream == num:
		continue
	selectStream -= 1

	location = input("Enter the location path where the file needs to be saved: ")
	print("\n")
	streams[selectStream].download(location)

	audioFileName = input("Enter the audio file name: ")
	audioFileName += ".mp3"

	defaultFilename = streams[selectStream].default_filename

	subprocess.call(["ffmpeg", "-i", os.path.join(location, defaultFilename), os.path.join(location, audioFileName)])

	print("Completed")

# searchBox = browser.find_element_by_tag_name("input")
# searchBox.send_keys(songName)
# searchBox.submit()

# resultsPage = requests.get("https://www.youtube.com/results?search_query=" + songName)
# resultsPage.raise_for_status()

# soup = bs4.BeautifulSoup(resultsPage.text, features="html.parser")
# videosList = soup.select('a[id="video-title"]')
# videosList = soup.find_all("a", class_="ytd-video-renderer")

# print(videosList)

# searchResults = []
# for i in range(5):
# 	videoDetails = []

# 	title = videosList[i].get("title")
# 	link = "https://www.youtube.com" + videosList[i].get("href")

# 	videoDetails.append(title)
# 	videoDetails.append(link)

# 	searchResults.append(videoDetails)

# print(searchResults)
