favorite_places = {
        'victor': ['fuji','waikiki','nikko'],
        'veronica': ['bandai','alts','nikko'],
        'alex': ['new york','hawaii','bali'],
        }
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favourite places are: ")
    for place in places:
        print(f"{place.title()}")
