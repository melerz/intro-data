import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials


"""
we will get all the features from spotify, by song name and artist name.
this function will create a json file with all the data
"""
def get_song_features_and_info_json(song_name, artist_name):

    # getting credentials to request special API
    credenials = SpotifyClientCredentials(client_id="5659eaf41b194134866170761e2fb293",client_secret="17e2a9fa37c2466baa2ba05752896cdc")

    # getting the client
    spotify_client = spotipy.Spotify(client_credentials_manager=credenials)

    # getting the song id in order to retrieve features, limiting to 1 since it sorts the results by popularity
    song_results = spotify_client.search(q='artist:' + artist_name + ' track:' + song_name, type='track',limit=1)
    print(song_results)
    tracks = song_results['tracks']['items']
    if len(tracks)==0:
        print("***no results for the requested track***")
        return
    result_dict = tracks[0]

    # creating dict for track
    song_dict = creating_song_dictionary(artist_name, result_dict, spotify_client)

    # writing to file
    name = artist_name+'_'+song_name
    with open(name+'.json', 'w') as outfile:
        json.dump(song_dict, outfile)


def creating_song_dictionary(artist_name, result_dict, spotify_client):
    song_dict = {}
    song_dict['artist'] = artist_name
    song_id = [result_dict['uri']]
    song_dict['uri'] = song_id
    song_dict['year'] = result_dict['album']['release_date'][:4]
    song_dict['artist id'] = result_dict['artists'][0]['id']
    song_dict['track id'] = result_dict['id']
    song_dict['name'] = spotify_client.track(song_dict['track id'])['name']
    song_dict['popularity'] = result_dict['popularity']
    song_dict['preview link'] = result_dict['preview_url']
    features = spotify_client.audio_features(song_id)
    song_dict['main features'] = features[0]

    # todo - need this? a big analysis, maybe will be helpful
    # analysis = spotify_client._get(features[0]['analysis_url'])
    #
    # song_dict['analysis'] = analysis

    return song_dict


get_song_features_and_info_json("if i were a boy","Beyonce")