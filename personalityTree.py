import json

# Load the JSON object
with open('user_data.json', 'r') as f:
  data = json.load(f)

name = data["user"].get("name", "Not specified")
bio = data["user"].get("bio", "Not specified")
birth_date = data["user"].get("birth_date", "Not specified").split("T")[0]
gender = "Not specified" if data["user"].get(
  "gender", -1) == -1 else "Male" if data["user"]["gender"] == 0 else "Female"

jobs = [f"{job['company'].get('name', 'Not specified')} - {job['title'].get('name', 'Not specified')}" for job in data["user"].get("jobs", [])]


schools = ", ".join([
  school.get("name", "Not specified")
  for school in data["user"].get("schools", [])
])
city = data["user"]["city"].get(
  "name", "Not specified") if data["user"].get("city") else "Not specified"
distance = str(data.get("distance_mi", "Not specified")) + " miles away"
zodiac = next(
  (d["choice_selections"][0]["name"]
   for d in data["user"].get("selected_descriptors", []) if d["id"] == "de_1"),
  "Not specified")
education = next(
  (d["choice_selections"][0]["name"]
   for d in data["user"].get("selected_descriptors", []) if d["id"] == "de_9"),
  "Not specified")
pets = next((d["choice_selections"][0]["name"] for d in data["user"].get("selected_descriptors", []) if d["id"] == "de_3"), "Not specified")
drinking = next((d["choice_selections"][0]["name"] for d in data["user"].get("selected_descriptors", []) if d["id"] == "de_22"), "Not specified")
personality = next((d["choice_selections"][0]["name"] for d in data["user"].get("selected_descriptors", []) if d["id"] == "de_13"), "Not specified")
workout = next((d["choice_selections"][0]["name"] for d in data["user"].get("selected_descriptors", []) if d["id"] == "de_10"), "Not specified")

relationship_intent = data.get("user", {}).get("relationship_intent", {})
descriptor_choice = relationship_intent.get("descriptor_choice_id", "Not specified")
emoji = relationship_intent.get("emoji", "Not specified")
image_url = relationship_intent.get("image_url", "Not specified")
title_text = relationship_intent.get("title_text", "Not specified")
body_text = relationship_intent.get("body_text", "Not specified")
spotify_connected = data.get("spotify", {}).get("spotify_connected", False)
spotify_top_artists = data.get("spotify", {}).get("spotify_top_artists", [])
spotify_theme_track = data.get("spotify", {}).get("spotify_theme_track", {})
spotify_name = spotify_theme_track.get("name", "Not specified")
spotify_artists = ", ".join([
  artist.get("name", "Not specified")
  for artist in spotify_theme_track.get("artists", [])
])
spotify_album = spotify_theme_track.get("album",
                                        {}).get("name", "Not specified")
spotify_album_id = spotify_theme_track.get("album",
                                           {}).get("id", "Not specified")
spotify_preview_url = spotify_theme_track.get("preview_url", "Not specified")
spotify_uri = spotify_theme_track.get("uri", "Not specified")
user_interests = ", ".join([
  interest.get("name", "Not specified")
  for interest in data.get("experiment_info", {}).get(
    "user_interests", {}).get("selected_interests", [])
])

# Print the extracted fields
print("Name:", name)
print("Bio:", bio)
print("Birth date:", birth_date)
print("Gender:", gender)
print("Jobs:", ", ".join(jobs))
print("Schools:", schools)
print("City:", city)
print("Distance:", distance)
print("Selected descriptors:")
print("    Zodiac:", zodiac)
print("    Education:", education)
print("    Drinking:", drinking)
print("    Workout:", workout)
print("    Pets:", pets)
print("    Personality:", personality)
print("Relationship intent:")
print("    Descriptor choice:", descriptor_choice)
print("    Emoji:", emoji)
print("    Image URL:", image_url)
print("    Title text:", title_text)
print("    Body text:", body_text)
print("Spotify:")
print(" Spotify top artists:", spotify_top_artists)
print(" Spotify theme track:")
print(" Name:", spotify_name)
print(" Artists:", spotify_artists)

print("Experiment info:")
print(" User interests:", user_interests)
