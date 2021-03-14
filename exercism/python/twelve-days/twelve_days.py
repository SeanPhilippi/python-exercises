# whiteboard this one... I'm already very inefficient
def recite(start_verse, end_verse):
    song_hash = {
        "first": "and a Partridge in a Pear Tree.",
        "second": "two Turtle Doves,",
        "third": "three French Hens,",
        "fourth": "four Calling Birds,",
        "fifth": "five Gold Rings,",
        "sixth": "six Geese-a-Laying,",
        "seventh": "seven Swans-a-Swimming,",
        "eighth": "eight Maids-a-Milking,",
        "ninth": "nine Ladies Dancing,",
        "tenth": "nine Ladies Dancing,",
        "eleventh": "eleven Pipers Piping,",
        "twelfth": "twelve Drummers Drumming,",
    }

    verses = len(range(start_verse, end_verse + 1))
    print("verses", verses)
    
    day = ""
    present = ""
    result = f"On the {} day of Christmas my true love gave to me: {}."
    while count < verses:
        for key, value in song_hash.items():
            # print f"On the 
            print("key", key)
            print("value", value)
            count += 1
    return result

print(recite(3, 5))
