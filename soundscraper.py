
#please download chromedriver before running this file
from selenium import webdriver
import requests
import bs4
import os

#new, top, mix, track, artist
top_url = 'https://soundcloud.com/charts/top'
new_url = 'https://soundcloud.com/charts/new'
track_url ='https://soundcloud.com/search/sounds?q='
artist_url = 'https://soundcloud.com/search/people?q='
mix_url = '&filter.duration=epic'

#creating a selenium browser to init to click buttons and all
browser = webdriver.Chrome(r"C:\Users\lenovo\Downloads\chromedriver.exe")
browser.get('https://soundcloud.com')

while True:
    print("Menu")
    print("1. Search for a track")
    print("2. Search for a artist")
    print("3. Search for a mix")
    print("4. Search for a Top Charts")
    print("5. Search for a New Charts")
    print("0. Exit")
    print("")
    
    choice = int(input("Your choice:"))
    print()
    
    if choice == 0:
        browser.quit()
        break
    print()
    
    #search for track
    if choice == 1:
        name = input("Name of track: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name)
        continue
    
    if choice == 2:
        name = input("Name of artist: ")
        print()
        "%20".join(name.split(" "))
        browser.get(artist_url + name)
        continue
    
    if choice == 3:
        name = input("Name of mix: ")
        print()
        "%20".join(name.split(" "))
        browser.get(track_url + name + mix_url)
        continue
    
    # get the top 50 tracks for a genre
    if choice == 4:
        request = requests.get(top_url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        while True:
            print("Genre available")
            print()
            
            genres = soup.select("a[href*=genre]")[2:]
            
            genre_links = []
            #print out all of yhe available genre
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))
            
            print()
            choice = input("Your choice to go back to main menu")
            print()
            
            if choice == 'x':
                break
            else:
                choice = int(choice)
            
            
            url = 'https://soundcloud.com' + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")
            
            
            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []
            
            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index) + ": " + track.text)
                print()
            
            #song selection loop
            while True:
                choice = input("Your choice, (x to reselect)")
                print()
                
                if choice == "x":
                    break
                else:
                    choice = int(choice) 
                    
                print("Now Playing: " + track_names[choice])
                print()
                
                browser.get('https://soundcloud.com' + track_names[choice])

# new and hot tracks
    if choice == 5:
        request = requests.get(new_url)
        soup = bs4.BeautifulSoup(request.text, "lxml")
        while True:
            print("Genre available")
            print()
            
            genres = soup.select("a[href*=genre]")[2:]
            
            genre_links = []
            #print out all of yhe available genre
            for index, genre in enumerate(genres):
                print(str(index) + ": " + genre.text)
                genre_links.append(genre.get("href"))
            
            print()
            choice = input("Your choice to go back to main menu")
            print()
            
            if choice == 'x':
                break
            else:
                choice = int(choice)
            
            
            url = 'https://soundcloud.com' + genre_links[choice]
            request = requests.get(url)
            soup = bs4.BeautifulSoup(request.text, "lxml")
            
            
            tracks = soup.select("h2")[3:]
            track_links = []
            track_names = []
            
            for index, track in enumerate(tracks):
                track_links.append(track.a.get("href"))
                track_names.append(track.text)
                print(str(index) + ": " + track.text)
                print()
            
            #song selection loop
            while True:
                choice = input("Your choice, (x to reselect)")
                print()
                
                if choice == "x":
                    break
                else:
                    choice = int(choice) 
                    
                print("Now Playing: " + track_names[choice])
                print()
                
                browser.get('https://soundcloud.com' + track_names[choice])

    
print()
print("Goodbye")
    


















