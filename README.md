# URL → QR Code (Python)

Creates a permanent, high-resolution QR code PNG from any `http://` or `https://` URL.
The QR code itself does not expire — it is just an image encoding your URL. Whether the
code still works in the future depends entirely on whether the target URL remains live.

---

## Requirements

- Python 3.8+
- [`qrcode`](https://pypi.org/project/qrcode/) with PIL support

---

## Install

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourname/yourrepo.git
cd yourrepo
pip install -r requirements.txt
```

The only required package is:

```
qrcode[pil]
```

If you don't have a `requirements.txt`, you can install directly:

```bash
pip install "qrcode[pil]"
```

---

## Usage

### Basic usage

```bash
python qr_generator.py https://example.com
```

This will generate a file called `qr.png` in the current directory.

### Custom output path

```bash
python qr_generator.py https://example.com -o my_qrcode.png
```

### Full syntax

```
python qr_generator.py <url> [-o OUTPUT_PATH]

positional arguments:
  url                   URL to encode (must start with http:// or https://)

options:
  -o, --out OUTPUT      Output PNG file path (default: qr.png)
```

---

## Examples

Generate a QR code for a Zenodo dataset and save it to a custom path:

```bash
python qr_generator.py https://zenodo.org/records/3992359 -o zenodo_qr.png
```

Generate a QR code for a GitHub repository:

```bash
python qr_generator.py https://github.com/yourname/yourrepo -o repo_qr.png
```

---

## Output

The script produces a single PNG image file. Default settings:

| Setting | Value |
|---------|-------|
| Format | PNG |
| Box size | 20 px per module |
| Border | 1 module (quiet zone) |
| Error correction | Medium (recovers up to ~15% damage) |
| Version | Auto-fit to content length |
| Fill / background | Black on white |

The auto-fit version means the QR code will be as compact as possible while still
encoding your full URL reliably.

---

## URL Validation

The script validates the URL before generating the QR code. It requires:

- A scheme of `http://` or `https://` — bare domains like `example.com` will be rejected
- A non-empty host/netloc component

If the URL is invalid, the script will exit with a descriptive error message before
creating any file.

---

## Notes

- **The QR code does not expire.** QR codes are static images — there is no server,
  no token, and no expiry mechanism. The only way a QR code stops working is if the
  URL it encodes goes offline or changes.
- **URL shorteners.** If you encode a shortened URL (e.g. `bit.ly/...`), the QR code
  depends on that shortener's service remaining live. For maximum permanence, encode
  the final destination URL directly.
- **Print size.** At box size 20, the output image is large enough for clean printing
  at standard poster or flyer sizes. If you need a smaller file, reduce `box_size`
  in `make_qr_png()`.

---

## License

MIT