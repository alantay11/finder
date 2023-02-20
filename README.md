# finder
Python script to find missing indexes within a given range, made for use with yt-dlp downloads to make it easier to track which videos are undownloadable in playlists.


Outputting names of videos based on an text file is also possible if exported in this format (or anything that has title in the line after playlist_index):

`yt-dlp --flat-playlist -i --print-to-file playlist_index,title,duration_string,channel,webpage_url`
