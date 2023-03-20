import json

# Load the JSON object
with open('user_data.json', 'r') as f:
    data = json.load(f)

name = data["user"]["name"]
bio = data["user"]["bio"]
birth_date = data["user"]["birth_date"].split("T")[0]
gender = "Not specified" if data["user"]["gender"] == -1 else "Male" if data["user"]["gender"] == 0 else "Female"
jobs = data["user"]["jobs"]
schools = ", ".join([school["name"] for school in data["user"]["schools"]])
#city = data["user"]["city"]["name"] if data["user"]["city"] else "Not specified"
distance = str(data["distance_mi"]) + " miles away"
zodiac = next((d["choice_selections"][0]["name"] for d in data["user"]["selected_descriptors"] if d["id"] == "de_1"), None)
education = next((d["choice_selections"][0]["name"] for d in data["user"]["selected_descriptors"] if d["id"] == "de_9"), None)
#relationship_intent = data["user"]["relationship_intent"]
descriptor_choice = relationship_intent["descriptor_choice_id"]
emoji = relationship_intent["emoji"]
image_url = relationship_intent["image_url"]
title_text = relationship_intent["title_text"]
body_text = relationship_intent["body_text"]
spotify_connected = data["spotify"]["spotify_connected"]
spotify_top_artists = data["spotify"]["spotify_top_artists"]
spotify_theme_track = data["spotify"]["spotify_theme_track"]
spotify_name = spotify_theme_track["name"]
spotify_artists = ", ".join([artist["name"] for artist in spotify_theme_track["artists"]])
spotify_album = spotify_theme_track["album"]["name"]
spotify_album_id = spotify_theme_track["album"]["id"]
spotify_preview_url = spotify_theme_track["preview_url"]
spotify_uri = spotify_theme_track["uri"]
user_interests = ", ".join([interest["name"] for interest in data["experiment_info"]["user_interests"]["selected_interests"]])

# Print the extracted fields
print("Name:", name)
print("Bio:", bio)
print("Birth date:", birth_date)
print("Gender:", gender)
print("Jobs:", jobs)
print("Schools:", schools)
print("City:", city)
print("Distance:", distance)
print("Selected descriptors:")
print("    Zodiac:", zodiac)
print("    Education:", education)
print("Relationship intent:")
print("    Descriptor choice:", descriptor_choice)
print("    Emoji:", emoji)
print("    Image URL:", image_url)
print("    Title text:", title_text)
print("    Body text:", body_text)
print("Spotify:")
print("    Spotify connected:", spotify_connected)
print("    Spotify top artists:", spotify_top_artists)
print("    Spotify theme track:")
print("        Name:", spotify_name)
print("        Artists:", spotify_artists)
print("        Album:", spotify_album)
print("        Album ID:", spotify_album_id)
print("        Preview URL:", spotify_preview_url)
print("        URI:", spotify_uri)
print("Experiment info:")
print("    User interests:", user_interests)