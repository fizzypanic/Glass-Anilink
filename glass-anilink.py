import webbrowser

print(r''' _____ _                  ___        _ _ _       _    
|  __ \ |                / _ \      (_) (_)     | |   
| |  \/ | __ _ ___ ___  / /_\ \_ __  _| |_ _ __ | | __
| | __| |/ _` / __/ __| |  _  | '_ \| | | | '_ \| |/ /
| |_\ \ | (_| \__ \__ \ | | | | | | | | | | | | |   < 
 \____/_|\__,_|___/___/ \_| |_/_| |_|_|_|_|_| |_|_|\__|''')

streaming = int(input("Welcome to Glass Anilink! Do you use either Youtube Music or Spotify?\nIf so, type 1 for Youtube Music or 2 for Spotify: "))
if streaming == 1:
    print("So you use Youtube Music! Got it!")
elif streaming == 2:
    print("So you use Spotify! Got it!")
else:
    print("Maybe you're in the wrong place...")

while True:
    album = int(input("Now, which of their albums do you wanna listen to?\n1. ILYSFM\n2. Dreamland\n3. How To Be a Human Being\n4. ZABA\n5. Exit Anilink! \nInput the number of the album! "))
    if streaming == 1 and album == 1:
        print("Opening Glass Animals' ILYSFM on Youtube Music...")
        webbrowser.open('https://www.youtube.com/playlist?list=OLAK5uy_lBs1atmfjuHSWrT3bCgk-pBQ8q57-ywKQ')
    elif streaming == 1 and album == 2:
        print("Opening Glass Animals 'Dreamland on Youtube Music...")
        webbrowser.open('https://www.youtube.com/playlist?list=OLAK5uy_nmBg68iVZ75jRs9LtfPZ0vBfHPjlnFtcQ')
    elif streaming == 1 and album == 3:
        print("Opening Glass Animals' How To Be a Human Being on Youtube Music...")
        webbrowser.open('https://www.youtube.com/playlist?list=OLAK5uy_kQFJ4qYA5p8MBj_4W9fLsWIU5v-ps0KDM')
    elif streaming == 1 and album == 4:
        print("Opening Glass Animals' ZABA on Youtube Music...")
        webbrowser.open('https://www.youtube.com/playlist?list=OLAK5uy_k12nU61mtYTc3VS3YErh5QD16eCtlLDxQ')
    elif album == 5:
        print("Thanks for trying out Anilink! See you next time!")
        break
    else:
        print("Invalid album! Maybe it'll exist in the coming years...")

    if streaming == 2 and album == 1:
        print("Opening Glass Animals' ILYSFM on Spotify...")
        webbrowser.open('https://open.spotify.com/album/5i6LJyHq9wxLSecf0N2Iuw')
    elif streaming == 2 and album == 2:
        print("Opening Glass Animals' Dreamland on Spotify...")
        webbrowser.open('https://open.spotify.com/album/5bfpRtBW7RNRdsm3tRyl3R')
    elif streaming == 2 and album == 3:
        print("Opening Glass Animals' How To Be a Human Being on Spotify...")
        webbrowser.open('https://open.spotify.com/album/6qb9MDR0lfsN9a2pw77uJy')
    elif streaming == 2 and album == 4:
        print("Opening Glass Animals' ZABA on Spotify...")
        webbrowser.open('https://open.spotify.com/album/14IOe7ahxQPTwUYUQX3IFi')
    elif album == 5:
        print("Thanks for trying out Anilink! See you next time!")
        break
    else:
        print("Invalid album! Maybe it'll exist in the coming years...")

    print()