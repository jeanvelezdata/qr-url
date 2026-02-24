"""
Generate a non-expiring QR code for a URL.

Notes:
- The QR code itself does not expire. Only the target URL can stop working.
- Output is a PNG image by default.
"""

from __future__ import annotations

import argparse
from urllib.parse import urlparse

import qrcode


def validate_url(url: str) -> str:
    url = url.strip()
    parsed = urlparse(url)

    # Basic validation: require scheme + netloc for http(s) URLs
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError(
            "Invalid URL. Expected something like 'https://example.com/path'."
        )
    return url


def make_qr_png(url: str, out_path: str) -> None:
    qr = qrcode.QRCode(
        version=None,  # auto-fit
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # good balance
        box_size=20,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn a URL into a QR code PNG.")
    parser.add_argument("url", help="URL to encode (must start with http:// or https://)")
    parser.add_argument(
        "-o",
        "--out",
        default="qr.png",
        help="Output PNG path (default: qr.png)",
    )
    args = parser.parse_args()

    url = validate_url(args.url)
    print(url)
    make_qr_png(url, args.out)
    print(f"Saved QR code to: {args.out}")


if __name__ == "__main__":
    main()