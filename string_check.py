from typing import Dict, List


class StringDict(object):
    def __init__(self):
        # type: () -> None
        self.words = {}   # type: Dict[str,List[str]]

    def add_string(self, w):
        # type: (str) -> None
        key = self.sort_word(w.lower())
        if key in self.words:
            self.words[key].append(w)
        else:
            self.words[key] = [w]

    @staticmethod
    def sort_word(w):
        # type: (str) -> str
        return ''.join(map(str, sorted(w)))

    def display(self, cutoff):
        # type: (int) -> None
        for key, val in self.words.items():
            if len(val) > cutoff:
                print key
                for v in val:
                    print "\t"+v


sd = StringDict()
'''
strings = ["racer","carer","strain","trains","German", "engram","Andrew","warden","wander","dawn","wand","tacos",
    "coast","coats","ascot","crate","react","trace","cater","scrape","recaps","spacer","casper","parse","reaps","spear",
    "spare","Tesla","steal","slate","stale","acres","scare","cares","races","negativism","timesaving","foster","softer",
    "forest","enlist","silent","listen","tinsel","sandworms","swordsman"]
for w in strings:
    sd.add_string(w)
'''
infile = open("scrabble_words.txt")
for word in infile:
    sd.add_string(word.strip())

sd.display(1)
