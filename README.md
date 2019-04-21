# py-flatten-dict
Example of flatten dict with key complession without recursion

Usage:
```
json_data = {
    "a": {
        "s": "00",
        "d": {
            "f": "01",
            "g": {
                "h": {
                    "j": "02",
                    "k": "03",
                    "l": "04",
                    "c": {
                        "v": "05",
                        "b": "06"
                    },
                    "n": [
                        "07",
                        "08",
                        "09"
                    ]
                }
            }
        }
    },
    "z": "10",
}

print(flatten(json_data))
```

Output will be like:
```
{
  "a.s": "00",
  "a.d.f": "01",
  "a.d.g.h.j": "02",
  "a.d.g.h.k": "03",
  "a.d.g.h.l": "04",
  "a.d.g.h.n": "07,08,09",
  "a.d.g.h.c.v": "05",
  "a.d.g.h.c.b": "06"
  "z": "10",
}
```
