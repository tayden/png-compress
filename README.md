# png-compress

Very effective lossy png image compression via k-means color clustering.

```bash
usage: compress_png.py [-h] -o OUTPUT [-k COLORS] [-c COMPRESSION] input

positional arguments:
  input                 Path to the input PNG image

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path/filename of output image
  -k COLORS, --colors COLORS
                        Number of quantized colors
  -c COMPRESSION, --compression COMPRESSION
                        Amount of PNG compression (0=none, 9=full)
```

A minimal GUI using Kivy is also available in src/.
It can be run by installing kivy ~1.10 and running `python src/main.py`