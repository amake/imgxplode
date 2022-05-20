# imgxplode

Explode a composite image into individual pieces.

For example the following image is a composite of three opaque regions separated
by transparent pixels:

![](./test.png)

This tool would output three images corresponding to the three regions.

# Usage

1. Clone repo
2. Run `make test` in the repo root
3. Run `./.env/bin/python imgxplode.py /path/to/input.whatever`

Supported input formats are [whatever Pillow
supports](https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html).

# Caveats

It's very slow!

# License

MIT
