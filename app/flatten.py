from dataclasses import dataclass, field
from queue import Queue
from typing import Any


@dataclass(order=True)
class DictData:
    parent_key: str
    item: Any = field(compare=False)


def flatten(dct):
    q = Queue()
    q.put(
        DictData(
            parent_key="",
            item=iter(dct.items())
        )
    )

    job = q.get_nowait()

    results = []

    while job:
        parent_key = job.parent_key
        item = job.item

        for k, v in item:
            p_key = k if not parent_key else f"{parent_key}.{k}"

            if isinstance(v, dict):
                q.put_nowait(DictData(
                    parent_key=p_key,
                    item=iter(v.items())))
            elif isinstance(v, list):
                results.append((p_key, ",".join(v)))
            else:
                results.append((p_key, v))

        else:
            if not q.empty():
                job = q.get_nowait()
            else:
                return dict(results)


if __name__ == '__main__':
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
    
    """
    Output will be like:
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
    """
