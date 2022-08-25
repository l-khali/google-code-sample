# Google Python Code Sample

While attending Bright Network's 'Technology Internship Experience', I completed this coding challenge from Google using object oriented programming.

The task involved creating a command-line application simulating Youtube which allowed user interaction. The majority of the methods I implemented can be found in [video_player.py](https://github.com/l-khali/google-code-sample/blob/main/python/src/video_player.py), as well as [video.py](https://github.com/l-khali/google-code-sample/blob/main/python/src/video.py).

Some examples of the functionality of the package are shown here (although there are many more!):

```
YT> PLAY amazing_cats_video_id
Playing video: Amazing Cats

YT> SHOW_PLAYING
Currently playing: Amazing Cats (amazing_cats_video_id) [#cat #animal]

YT> PAUSE
Pausing video: Amazing Cats

YT> SHOW_PLAYING
Currently playing: Amazing Cats (amazing_cats_video_id) [#cat #animal] - PAUSED

YT> STOP
Stopping video: Amazing Cats

YT> SHOW_PLAYING
No video is currently playing
```

```
YT> CREATE_PLAYLIST my_playlist
Successfully created new playlist: my_playlist

YT> ADD_TO_PLAYLIST my_playlist amazing_cats_video_id
Added video to my_playlist: Amazing Cats

YT> CLEAR_PLAYLIST my_playlist
Successfully removed all videos from my_playlist

YT> SHOW_PLAYLIST my_playlist
Showing playlist: my_playlist
  No videos here yet.
 
YT> CLEAR_PLAYLIST another_playlist
Cannot clear playlist another_playlist: Playlist does not exist
```

```
YT> SEARCH_VIDEOS cat
Here are the results for cat:
  1) Amazing Cats (amazing_cats_video_id) [#cat #animal]
  2) Another Cat Video (another_cat_video_id) [#cat #animal]
Would you like to play any of the above? If yes, specify the number of the video.
If your answer is not a valid number, we will assume it's a no.
Nope!

YT> SEARCH_VIDEOS cat
Here are the results for cat:
  1) Amazing Cats (amazing_cats_video_id) [#cat #animal]
  2) Another Cat Video (another_cat_video_id) [#cat #animal]
Would you like to play any of the above? If yes, specify the number of the video.
If your answer is not a valid number, we will assume it's a no.
2
Playing video: Another Cat Video

YT> SEARCH_VIDEOS blah
No search results for blah
```
