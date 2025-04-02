import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

# 🔑 Set up Spotify API Credentials
SPOTIFY_CLIENT_ID = "your client id"
SPOTIFY_CLIENT_SECRET = "your client secret"

# 🎵 Initialize Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def play_music(query="Relaxing music"):
    """Searches for relaxing music on Spotify and opens the song/playlist in a web browser."""
    try:
        # First, search for a track
        results = sp.search(q=query, limit=1, type="track")
        if results["tracks"]["items"]:
            track_url = results["tracks"]["items"][0]["external_urls"]["spotify"]
            print(f"🎶 Playing: {query}\n🔗 Open: {track_url}")
            webbrowser.open(track_url)
            return
        
        # If no track is found, search for a playlist
        results = sp.search(q=query, limit=1, type="playlist")
        if results["playlists"]["items"]:
            playlist_url = results["playlists"]["items"][0]["external_urls"]["spotify"]
            print(f"🎵 Playing Playlist: {query}\n🔗 Open: {playlist_url}")
            webbrowser.open(playlist_url)
            return

        print("⚠️ No music found. Try another search.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n🎵 Welcome to the Music Player!")
    search_query = input("🔍 Enter the type of music you want to listen to (e.g., meditation, classical, stress relief): ")
    play_music(search_query)
