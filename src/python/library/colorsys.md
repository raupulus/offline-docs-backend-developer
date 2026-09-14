---
title: '"colorsys" --- Conversions between color systems'
source_url: https://docs.python.org/es/3
source_path: library/colorsys.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2020
---

# "colorsys" --- Conversions between color systems

**Código fuente:** Lib/colorsys.py

======================================================================

The "colorsys" module defines bidirectional conversions of color
values between colors expressed in the RGB (Red Green Blue) color
space used in computer monitors and three other coordinate systems:
YIQ, HLS (Hue Lightness Saturation) and HSV (Hue Saturation Value).
Coordinates in all of these color spaces are floating-point values.
In the YIQ space, the Y coordinate is between 0 and 1, but the I and Q
coordinates can be positive or negative.  In all other spaces, the
coordinates are all between 0 and 1.

Ver también:

  Puede encontrar más información sobre los espacios de color en
  http://poynton.ca/ColorFAQ.html y
  https://www.cambridgeincolour.com/tutorials/color-spaces.htm.

The "colorsys" module defines the following functions:

colorsys.rgb_to_yiq(r, g, b)

   Convierte el color de las coordenadas RGB en coordenadas YIQ.

colorsys.yiq_to_rgb(y, i, q)

   Convierte el color de las coordenadas YIQ en coordenadas RGB.

colorsys.rgb_to_hls(r, g, b)

   Convierte el color de las coordenadas RGB en coordenadas HLS.

colorsys.hls_to_rgb(h, l, s)

   Convierte el color de las coordenadas HLS en coordenadas RGB.

colorsys.rgb_to_hsv(r, g, b)

   Convierte el color de las coordenadas RGB en coordenadas HSV.

colorsys.hsv_to_rgb(h, s, v)

   Convierte el color de las coordenadas HSV en coordenadas RGB.

Ejemplo:

   >>> import colorsys
   >>> colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
   (0.5, 0.5, 0.4)
   >>> colorsys.hsv_to_rgb(0.5, 0.5, 0.4)
   (0.2, 0.4, 0.4)
