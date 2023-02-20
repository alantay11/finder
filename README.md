# finder
Python script to find missing indexes within a given range for use with yt-dlp to track undownloadable videos in playlists.

&nbsp;  
Videos must be named in `playlist_index. title` format.

Example:
`yt-dlp.exe -o "%(playlist_index)03d. %(title)s [%(id)s].%(ext)s"`

&nbsp;  
Outputting names of videos based on an text file is also possible if exported in this format:

`yt-dlp --flat-playlist -i --print-to-file playlist_index,title`

or anything that has title in the line after playlist_index:

`yt-dlp --flat-playlist -i --print-to-file playlist_index,title,duration_string,channel,webpage_url`
