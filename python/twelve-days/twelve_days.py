def recite(start_verse, end_verse):
    christmas = [
        {"first": "a Partridge in a Pear Tree."},
        {"second": "two Turtle Doves"},
        {"third": "three French Hens"},
        {"fourth": "four Calling Birds"},
        {"fifth": "five Gold Rings"},
        {"sixth": "six Geese-a-Laying"},
        {"seventh": "seven Swans-a-Swimming"},
        {"eighth": "eight Maids-a-Milking"},
        {"ninth": "nine Ladies Dancing"},
        {"tenth": "ten Lords-a-Leaping"},
        {"eleventh": "eleven Pipers Piping"},
        {"twelfth": "twelve Drummers Drumming"}
    ]
    final_output = []
    for verse in range(start_verse, end_verse+1):
        start = "On the " + list(christmas[verse-1].keys())[0] + " day of Christmas my true love gave to me: "
        end = ""
        for i in range(verse):
            if i == 0:
                end = christmas[i][list(christmas[i].keys())[0]]
            elif i == 1:
                end = christmas[i][list(christmas[i].keys())[0]] + ", and " + end
            else:
                end = christmas[i][list(christmas[i].keys())[0]] + ", " + end
        output = start + end
        final_output.append(output)
    return final_output