# Camera move by shot type (all 5 videos; shots<0.5s = short)
sign assumption: zoom-idx >0 = push-in (zoom in), <0 = pull-out

| code | n | locked% | push% | pull% | pan% | tilt% |
|---|---|---|---|---|---|---|
| W | 304 | 77 | 7 | 6 | 6 | 4 |
| M | 218 | 85 | 4 | 4 | 4 | 3 |
| C | 279 | 94 | 3 | 3 | 1 | 0 |
| X | 26 | 92 | 8 | 0 | 0 | 0 |
| O | 91 | 89 | 4 | 4 | 1 | 1 |
| H | 48 | 88 | 2 | 10 | 0 | 0 |
| U | 124 | 69 | 20 | 6 | 3 | 2 |
| T | 12 | 67 | 8 | 25 | 0 | 0 |
| D | 35 | 77 | 6 | 6 | 0 | 11 |
| E | 60 | 73 | 12 | 7 | 3 | 5 |
| B | 6 | 100 | 0 | 0 | 0 | 0 |
| ALL | 1203 | 83 | 6 | 5 | 3 | 2 |

## by flag
| flag | n | locked% | push% | pull% | pan% | tilt% |
|---|---|---|---|---|---|---|
| p | 106 | 69 | 10 | 8 | 8 | 6 |
| e | 93 | 95 | 3 | 2 | 0 | 0 |
| o | 87 | 97 | 1 | 1 | 1 | 0 |
| t | 102 | 89 | 2 | 4 | 4 | 1 |
| s | 74 | 72 | 7 | 8 | 8 | 5 |
| k | 18 | 78 | 6 | 11 | 0 | 6 |

- mean hold locked: 2.40s (n=1000)
- mean hold push: 3.24s (n=78)
- mean hold pull: 3.95s (n=58)
- mean hold pan: 2.59s (n=37)
- mean hold tilt: 2.66s (n=30)