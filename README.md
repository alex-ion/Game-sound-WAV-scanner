# Game-sound-WAV-scanner
Last year I decided to add some sounds to my Wall-E Robot and wanted so bad to include some from the Worms Game and Starcraft 1, games that I used to play when I was a kid.
The only thing is that the bit resolution and sampling rate of each sound file must have been modified in order to be recognised by my Arduino Mega microcontroller. I used https://audio.online-convert.com/convert-to-wav where you can upload up to 10 files once and download them as an archive when the transforming process is finished. After downloading, I had to manually extract the files from the archive, which is very time consuming if you consider the fact that there were more than 100 archives.

Therefore, I decided to make an automatic tool in Python which should do the job for me. Basically, the script was always scanning a folder for new archives and if an archive was found, it should extract the files from archive and place them into a special folder.
