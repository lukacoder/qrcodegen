Generate QR codes.

For a standard install (which will include pillow for generating images), run:

pip install qrcode[pil]
What is a QR Code?
A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

Usage
From the command line, use the installed qr script:

qr "Some text" > test.png
Or in Python, use the make shortcut function:

import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
Advanced Usage
For more control, use the QRCode class. For example:

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
The version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). Set to None and use the fit parameter when making the code to determine this automatically.

fill_color and back_color can change the background and the painting color of the QR, when using the default image factory. Both parameters accept RGB color tuples.

img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
The error_correction parameter controls the error correction used for the QR Code. The following four constants are made available on the qrcode package:

ERROR_CORRECT_L
About 7% or less errors can be corrected.
ERROR_CORRECT_M (default)
About 15% or less errors can be corrected.
ERROR_CORRECT_Q
About 25% or less errors can be corrected.
ERROR_CORRECT_H.
About 30% or less errors can be corrected.
The box_size parameter controls how many pixels each “box” of the QR code is.

The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).

Other image factories
You can encode as SVG, or use a new pure Python image processor to encode to PNG images.

The Python examples below use the make shortcut. The same image_factory keyword argument is a valid option for the QRCode class for more advanced usage.

SVG
You can create the entire SVG or an SVG fragment. When building an entire SVG image, you can use the factory that combines as a path (recommended, and default for the script) or a factory that creates a simple set of rectangles.

From your command line:

qr --factory=svg-path "Some text" > test.svg
qr --factory=svg "Some text" > test.svg
qr --factory=svg-fragment "Some text" > test.svg
Or in Python:

import qrcode
import qrcode.image.svg

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make('Some data here', image_factory=factory)
Two other related factories are available that work the same, but also fill the background of the SVG with white:

qrcode.image.svg.SvgFillImage
qrcode.image.svg.SvgPathFillImage
Pure Python PNG
Install the following two packages:

pip install -e git+git://github.com/ojii/pymaging.git#egg=pymaging
pip install -e git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png
From your command line:

qr --factory=pymaging "Some text" > test.png
Or in Python:

import qrcode
from qrcode.image.pure import PymagingImage
img = qrcode.make('Some data here', image_factory=PymagingImage)
Styled Image
To apply styles to the QRCode, use the StyledPilImage image factory. This takes an optional module drawer to control the shape of the QR Code, an optional color mask to change the colors of the QR Code, and an optional image to embed in the center.

These QR Codes are not guaranteed to work with all readers, so do some experimentation and set the error correction to high (especially if embedding an image).

Examples to draw the QR code with rounded corners, radial gradiant and embedded image:

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('Some data')

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/image.png")
Other module_drawers:

doc/module_drawers.png
Other color masks:

doc/color_masks.png
Examples
Get the text content from print_ascii:

import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("Some text")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
The add_data method will append data to the current QR object. To add new data by replacing previous content in the same object, first use clear method:

import qrcode
qr = qrcode.QRCode()
qr.add_data('Some data')
img = qr.make_image()
qr.clear()
qr.add_data('New data')
other_img = qr.make_image()
Pipe ascii output to text file in command line:

qr --ascii "Some data" > "test.txt"
cat test.txt
Alternative to piping output to file to avoid PoweShell issues:

# qr "Some data" > test.png
qr --output=test.png "Some data"
