PAD = 0
BOS = 1
EOS = 2

phoneme_symbols = [
    "[PAD]",
    "[BOS]",
    "[EOS]",
    "pau",
    "N",
    "a",
    "b",
    "by",
    "ch",
    "cl",
    "d",
    "dy",
    "e",
    "f",
    "g",
    "gw",
    "gy",
    "h",
    "hy",
    "i",
    "j",
    "k",
    "kw",
    "ky",
    "m",
    "my",
    "n",
    "ny",
    "o",
    "p",
    "py",
    "r",
    "ry",
    "s",
    "sh",
    "t",
    "ts",
    "ty",
    "u",
    "v",
    "w",
    "y",
    "z",
]

phoneme_to_id = {s: i for i, s in enumerate(phoneme_symbols)}
id_to_phoneme = {i: s for i, s in enumerate(phoneme_symbols)}
