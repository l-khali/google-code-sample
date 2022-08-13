"""A video player class."""

from .video_library import VideoLibrary
import random
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current = None
        self.playlists = {}
        self.playlists_lower = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        ordered_videos = []

        for video in self._video_library.get_all_videos():
            ordered_videos.append(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")
        
        ordered_videos.sort()

        print("Here's a list of all available videos:")
        for video in ordered_videos:
            print(f'\t {video}')

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        video = self._video_library.get_video(video_id)

        if video:
            if self.current:
                print(f"Stopping video: {self.current.title}")
                self.current.playing = 0
                self.current.paused = 0
            self.current = video
            video.playing = 1
            print(f"Playing video: {self.current.title}")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self.current:
            self.current.playing = 0
            print(f"Stopping video: {self.current.title}")
            self.current = None
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        if self.current:
            self.stop_video()
        random_video = random.choice(self._video_library.get_all_videos())
        self.current = random_video
        random_video.playing = 1
        print(f"Playing video: {random_video.title}")

    def pause_video(self):
        """Pauses the current video."""

        if self.current:
            if self.current.paused:
                print(f"Video already paused: {self.current.title}")
            else:
                self.current.playing = 0
                self.current.paused = 1
                print(f"Pausing video: {self.current.title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.current:
            if self.current.paused:
                self.current.paused = 0
                self.current.playing = 1
                print(f"Continuing video: {self.current.title}")
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self.current:
            if self.current.paused:
                print(f"Currently playing: {self.current.title} ({self.current.video_id}) [{' '.join(self.current.tags)}] - PAUSED")
            else:
                print(f"Currently playing: {self.current.title} ({self.current.video_id}) [{' '.join(self.current.tags)}]")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists_lower:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[playlist_name.lower()] = Playlist(playlist_name)
            self.playlists_lower.append(playlist_name.lower())
            print(f"Successfully created new playlist: {playlist_name}")


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        # playlist = self.playlists.get(playlist_name, None)
        # video = self._video_library.get_video(video_id, None)

        if not playlist_name.lower() in self.playlists_lower:
            print("Cannot add video to {playlist_name}: Playlist does not exist")
        else:
            video = self._video_library.get_video(video_id)
            if video:
                if video in self.playlists[playlist_name.lower()].videos:
                    print(f"Cannot add video to {playlist_name}: Video already added")
                else:
                    playlist = self.playlists[playlist_name.lower()]
                    playlist.videos.append(video)
                    print(f"Added video to {playlist_name}: {video.title}")
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        # # else:
        # #     video = self._video_library.get_video(video_id)
        # #     if video:
        # #         playlist = self._video_library.get_playlist(playlist_name)
        # #         playlist.videos.append(video)
        # #         print(f"Added video to {playlist_name}: {video.title}")
        # #     else:
        # #         print(f"Cannot add video to {playlist_name}: Video does not exist")
        # if playlist:
        #     if video:
        #         playlist.videos.append(video)
        #         print(f"Added video to {playlist_name}: {video.title}")
        #     else:
        #         print(f"Cannot add video to {playlist_name}: Video does not exist")
        # else:
        #     print("Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
