"""'Explode' each input image into many images.

The output images are rectangular subregions separated by transparent pixels.

"""

from PIL import Image
from os import path


def _process_one(img_path):
    print(f'Processing {img_path}')
    base, ext = path.splitext(img_path)
    img = Image.open(img_path).convert('RGBA')
    groups = _compute_groups(img)
    print(f'Detected {len(groups)} groups')
    for n, group in enumerate(groups):
        box = _compute_box(group)
        cropped = img.crop(box)
        outpath = f'{base}-{n:03d}{ext}'
        cropped.save(outpath)
        print(f'Wrote {outpath}')


def _compute_groups(img):
    groups = []
    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:
                for group in reversed(groups):
                    if (x - 1, y) in group or (x, y - 1) in group:
                        group.add((x, y))
                        break
                else:
                    groups.append(set([(x, y)]))
    return groups


def _compute_box(group):
    left = min(x for x, y in group)
    upper = min(y for x, y in group)
    right = max(x for x, y in group)
    lower = max(y for x, y in group)
    return (left, upper, right, lower)


def main():
    """Process args."""
    import sys

    for arg in sys.argv[1:]:
        _process_one(arg)


if __name__ == '__main__':
    main()
