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
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
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

        pl_list = sorted(self.playlists_lower)

        if pl_list:
            print("Showing all playlists:")
            for pl in pl_list:
                print(self.playlists[pl].playlist_name)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists_lower:
            print(f"Showing playlist: {playlist_name}")
            if self.playlists[playlist_name.lower()].videos:
                for video in self.playlists[playlist_name.lower()].videos:
                    print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")
            else:
                print("No videos here yet")
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if not playlist_name.lower() in self.playlists_lower:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        else:
            video = self._video_library.get_video(video_id)
            if video:
                if video in self.playlists[playlist_name.lower()].videos:
                    self.playlists[playlist_name.lower()].videos.remove(video)
                    print(f"Removed video from {playlist_name}: {video.title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if not playlist_name.lower() in self.playlists_lower:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self.playlists[playlist_name.lower()].videos = []
            print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if not playlist_name.lower() in self.playlists_lower:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            self.playlists_lower.remove(playlist_name.lower())
            self.playlists.pop(playlist_name.lower())
            print(f"Deleted playlist: {playlist_name}")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        search_results = {}
        for video in all_videos:
            if not video.title.lower().find(search_term.lower()) == -1:
                search_results[video.title] = video

        search_results = {key: value for key, value in sorted(search_results.items())}

        if search_results:
            print(f"Here are the results for {search_term}:")
            for i, video in enumerate(search_results.items()):
                print(f"{i+1}) {video[1].title} ({video[1].video_id}) [{' '.join(video[1].tags)}]", end="\n")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            idx = input("\n")
            # print(idx)
            try:
                idx = int(idx)
                if (idx-1) in range(len(search_results)):
                    self.play_video(list(search_results.items())[idx-1][1].video_id)
                    print(f"Playing video: {list(search_results.items())[idx-1][1].title}")
            except ValueError:
                pass
        else:
            print(f"No search results for {search_term}")
 

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        search_results = {}
        for video in all_videos:
            if video_tag.lower() in video.tags:
                search_results[video.title] = video

        search_results = {key: value for key, value in sorted(search_results.items())}

        if search_results:
            print(f"Here are the results for {video_tag}:")
            for i, video in enumerate(search_results.items()):
                print(f"{i+1}) {video[1].title} ({video[1].video_id}) [{' '.join(video[1].tags)}]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            idx = input("")
            # print(idx)
            try:
                idx = int(idx)
                if (idx-1) in range(len(search_results)):
                    self.play_video(list(search_results.items())[idx-1][1].video_id)
                    print(f"Playing video: {list(search_results.items())[idx-1][1].title}")
            except ValueError:
                pass
        else:
            print(f"No search results for {video_tag}")

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
