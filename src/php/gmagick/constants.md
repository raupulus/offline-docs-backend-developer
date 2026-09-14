---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/gmagick.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmagick/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmagick
translation_status: ready
translation_reviewed: false
translation_revision: c34257b72
order: 26430
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`Gmagick::COLOR_BLACK` (`int`)  
Negro

`Gmagick::COLOR_BLUE` (`int`)  
Azul

`Gmagick::COLOR_CYAN` (`int`)  
Cian

`Gmagick::COLOR_GREEN` (`int`)  
Verde

`Gmagick::COLOR_RED` (`int`)  
Rojo

`Gmagick::COLOR_YELLOW` (`int`)  
Amarillo

`Gmagick::COLOR_MAGENTA` (`int`)  
Magenta

`Gmagick::COLOR_OPACITY` (`int`)  
Opacidad

`Gmagick::COLOR_ALPHA` (`int`)  
Alpha

`Gmagick::COLOR_FUZZ` (`int`)  
Fuzz

<!-- -->

`Gmagick::COMPOSITE_DEFAULT` (`int`)  
El operador compuesto por defecto

`Gmagick::COMPOSITE_UNDEFINED` (`int`)  
Operador compuesto indefinido

`Gmagick::COMPOSITE_NO` (`int`)  
Ningún operador compuesto definido

`Gmagick::COMPOSITE_ADD` (`int`)  
El resultado de una imagen + una imagen

`Gmagick::COMPOSITE_ATOP` (`int`)  
El resultado es la misma forma que una imagen; donde la imagen compuesta oscurece la imagen, la imagen de la forma la superpone.

`Gmagick::COMPOSITE_BLEND` (`int`)  
Mezcla la imagen

`Gmagick::COMPOSITE_BUMPMAP` (`int`)  
Idéntico a COMPOSITE_MULTIPLY, excepto que la fuente se convierte primero a niveles de gris.

`Gmagick::COMPOSITE_CLEAR` (`int`)  
Hace que la imagen de destino sea transparente

`Gmagick::COMPOSITE_COLORBURN` (`int`)  
Oscurece la imagen de destino para reflejar la imagen fuente

`Gmagick::COMPOSITE_COLORDODGE` (`int`)  
Aclara la imagen de destino para reflejar la imagen fuente

`Gmagick::COMPOSITE_COLORIZE` (`int`)  
Colorea la imagen de destino utilizando la imagen compuesta

`Gmagick::COMPOSITE_COPYBLACK` (`int`)  
Copia los negros desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_COPYBLUE` (`int`)  
Copia los azules desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_COPY` (`int`)  
Copia la imagen fuente sobre la imagen de destino

`Gmagick::COMPOSITE_COPYCYAN` (`int`)  
Copia el cian desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_COPYGREEN` (`int`)  
Copia el verde desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_COPYMAGENTA` (`int`)  
Copia el magenta desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_COPYOPACITY` (`int`)  
Copia la opacidad desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_COPYRED` (`int`)  
Copia el rojo desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_COPYYELLOW` (`int`)  
Copia el amarillo desde la fuente hacia la imagen de destino

`Gmagick::COMPOSITE_DARKEN` (`int`)  
Oscurece la imagen de destino

`Gmagick::COMPOSITE_DSTATOP` (`int`)  
La parte de la imagen de destino que está dentro de la fuente se compone sobre la fuente y reemplaza la imagen de destino

`Gmagick::COMPOSITE_DST` (`int`)  
La imagen de destino se conserva sin modificación

`Gmagick::COMPOSITE_DSTIN` (`int`)  
La parte de la fuente reemplaza la imagen de destino

`Gmagick::COMPOSITE_DSTOUT` (`int`)  
La parte fuera de la fuente reemplaza la imagen de destino

`Gmagick::COMPOSITE_DSTOVER` (`int`)  
La imagen de destino reemplaza la fuente

`Gmagick::COMPOSITE_DIFFERENCE` (`int`)  
Resta el color más oscuro de los dos colores elementales del más claro

`Gmagick::COMPOSITE_DISPLACE` (`int`)  
Desplaza los píxeles de la imagen de destino según lo definido por la fuente

`Gmagick::COMPOSITE_DISSOLVE` (`int`)  
Disuelve la fuente en la imagen de destino

`Gmagick::COMPOSITE_EXCLUSION` (`int`)  
Produce un efecto similar a Gmagick::COMPOSITE_DIFFERENCE, pero aparece con un contraste más bajo

`Gmagick::COMPOSITE_HARDLIGHT` (`int`)  
Multiplica o superpone los colores, dependiendo del valor de color de la fuente

`Gmagick::COMPOSITE_HUE` (`int`)  
Modifica el tono de la imagen de destino según lo definido por la fuente

`Gmagick::COMPOSITE_IN` (`int`)  
Realiza una composición de la fuente en la imagen de destino

`Gmagick::COMPOSITE_LIGHTEN` (`int`)  
Aclara la imagen de destino según lo definido por la fuente

`Gmagick::COMPOSITE_LUMINIZE` (`int`)  
Ilumina la imagen de destino según lo definido por la fuente

`Gmagick::COMPOSITE_MINUS` (`int`)  
Resta la fuente de la imagen de destino

`Gmagick::COMPOSITE_MODULATE` (`int`)  
Modula la luminosidad, saturación y tono de la imagen de destino según lo definido por la fuente

`Gmagick::COMPOSITE_MULTIPLY` (`int`)  
Multiplica la imagen de destino por la fuente

`Gmagick::COMPOSITE_OUT` (`int`)  
Realiza una composición de las partes exteriores de la fuente sobre la imagen de destino

`Gmagick::COMPOSITE_OVER` (`int`)  
Realiza una composición sobre la imagen de destino

`Gmagick::COMPOSITE_OVERLAY` (`int`)  
Superpone la fuente sobre la imagen de destino

`Gmagick::COMPOSITE_PLUS` (`int`)  
Añade la fuente a la imagen de destino

`Gmagick::COMPOSITE_REPLACE` (`int`)  
Reemplaza la imagen de destino por la fuente

`Gmagick::COMPOSITE_SATURATE` (`int`)  
Satura la imagen de destino según lo definido por la fuente

`Gmagick::COMPOSITE_SCREEN` (`int`)  
La fuente y la imagen de destino son complementadas, luego multiplicadas, luego reemplazan la imagen de destino

`Gmagick::COMPOSITE_SOFTLIGHT` (`int`)  
Oscurece o aclara los colores, siguiendo la fuente

`Gmagick::COMPOSITE_SRCATOP` (`int`)  
La parte de la fuente que se encuentra dentro de la imagen de destino se compone sobre la imagen de destino

`Gmagick::COMPOSITE_SRC` (`int`)  
La fuente se copia hacia la imagen de destino

`Gmagick::COMPOSITE_SRCIN` (`int`)  
La parte de la fuente que se encuentra dentro de la imagen de destino reemplaza la imagen de destino

`Gmagick::COMPOSITE_SRCOUT` (`int`)  
La parte de la fuente que se encuentra fuera de la imagen de destino reemplaza la imagen de destino

`Gmagick::COMPOSITE_SRCOVER` (`int`)  
La fuente reemplaza la imagen de destino

`Gmagick::COMPOSITE_SUBTRACT` (`int`)  
Resta los colores de la imagen fuente en la imagen de destino

`Gmagick::COMPOSITE_THRESHOLD` (`int`)  
La fuente se compone de la imagen de destino, según lo definido por la fuente

`Gmagick::COMPOSITE_XOR` (`int`)  
La parte de la fuente que se encuentra fuera de la imagen de destino se combina con la parte de la imagen de destino que se encuentra fuera de la fuente

<!-- -->

`Gmagick::MONTAGEMODE_FRAME` (`int`)  

`Gmagick::MONTAGEMODE_UNFRAME` (`int`)  

`Gmagick::MONTAGEMODE_CONCATENATE` (`int`)  

<!-- -->

`Gmagick::STYLE_NORMAL` (`int`)  

`Gmagick::STYLE_ITALIC` (`int`)  

`Gmagick::STYLE_OBLIQUE` (`int`)  

`Gmagick::STYLE_ANY` (`int`)  

<!-- -->

`Gmagick::FILTER_UNDEFINED` (`int`)  

`Gmagick::FILTER_POINT` (`int`)  

`Gmagick::FILTER_BOX` (`int`)  

`Gmagick::FILTER_TRIANGLE` (`int`)  

`Gmagick::FILTER_HERMITE` (`int`)  

`Gmagick::FILTER_HANNING` (`int`)  

`Gmagick::FILTER_HAMMING` (`int`)  

`Gmagick::FILTER_BLACKMAN` (`int`)  

`Gmagick::FILTER_GAUSSIAN` (`int`)  

`Gmagick::FILTER_QUADRATIC` (`int`)  

`Gmagick::FILTER_CUBIC` (`int`)  

`Gmagick::FILTER_CATROM` (`int`)  

`Gmagick::FILTER_MITCHELL` (`int`)  

`Gmagick::FILTER_LANCZOS` (`int`)  

`Gmagick::FILTER_BESSEL` (`int`)  

`Gmagick::FILTER_SINC` (`int`)  

<!-- -->

`Gmagick::IMGTYPE_UNDEFINED` (`int`)  

`Gmagick::IMGTYPE_BILEVEL` (`int`)  

`Gmagick::IMGTYPE_GRAYSCALE` (`int`)  

`Gmagick::IMGTYPE_GRAYSCALEMATTE` (`int`)  

`Gmagick::IMGTYPE_PALETTE` (`int`)  

`Gmagick::IMGTYPE_PALETTEMATTE` (`int`)  

`Gmagick::IMGTYPE_TRUECOLOR` (`int`)  

`Gmagick::IMGTYPE_TRUECOLORMATTE` (`int`)  

`Gmagick::IMGTYPE_COLORSEPARATION` (`int`)  

`Gmagick::IMGTYPE_COLORSEPARATIONMATTE` (`int`)  

`Gmagick::IMGTYPE_OPTIMIZE` (`int`)  

<!-- -->

`Gmagick::RESOLUTION_UNDEFINED` (`int`)  

`Gmagick::RESOLUTION_PIXELSPERINCH` (`int`)  

`Gmagick::RESOLUTION_PIXELSPERCENTIMETER` (`int`)  

<!-- -->

`Gmagick::COMPRESSION_UNDEFINED` (`int`)  

`Gmagick::COMPRESSION_NO` (`int`)  

`Gmagick::COMPRESSION_BZIP` (`int`)  

`Gmagick::COMPRESSION_FAX` (`int`)  

`Gmagick::COMPRESSION_GROUP4` (`int`)  

`Gmagick::COMPRESSION_JPEG` (`int`)  

`Gmagick::COMPRESSION_JPEG2000` (`int`)  

`Gmagick::COMPRESSION_LOSSLESSJPEG` (`int`)  

`Gmagick::COMPRESSION_LZW` (`int`)  

`Gmagick::COMPRESSION_RLE` (`int`)  

`Gmagick::COMPRESSION_ZIP` (`int`)  

<!-- -->

`Gmagick::PAINT_POINT` (`int`)  

`Gmagick::PAINT_REPLACE` (`int`)  

`Gmagick::PAINT_FLOODFILL` (`int`)  

`Gmagick::PAINT_FILLTOBORDER` (`int`)  

`Gmagick::PAINT_RESET` (`int`)  

<!-- -->

`Gmagick::GRAVITY_NORTHWEST` (`int`)  

`Gmagick::GRAVITY_NORTH` (`int`)  

`Gmagick::GRAVITY_NORTHEAST` (`int`)  

`Gmagick::GRAVITY_WEST` (`int`)  

`Gmagick::GRAVITY_CENTER` (`int`)  

`Gmagick::GRAVITY_EAST` (`int`)  

`Gmagick::GRAVITY_SOUTHWEST` (`int`)  

`Gmagick::GRAVITY_SOUTH` (`int`)  

`Gmagick::GRAVITY_SOUTHEAST` (`int`)  

<!-- -->

`Gmagick::STRETCH_NORMAL` (`int`)  

`Gmagick::STRETCH_ULTRACONDENSED` (`int`)  

`Gmagick::STRETCH_CONDENSED` (`int`)  

`Gmagick::STRETCH_SEMICONDENSED` (`int`)  

`Gmagick::STRETCH_SEMIEXPANDED` (`int`)  

`Gmagick::STRETCH_EXPANDED` (`int`)  

`Gmagick::STRETCH_EXTRAEXPANDED` (`int`)  

`Gmagick::STRETCH_ULTRAEXPANDED` (`int`)  

`Gmagick::STRETCH_ANY` (`int`)  

<!-- -->

`Gmagick::ALIGN_UNDEFINED` (`int`)  

`Gmagick::ALIGN_LEFT` (`int`)  

`Gmagick::ALIGN_CENTER` (`int`)  

`Gmagick::ALIGN_RIGHT` (`int`)  

<!-- -->

`Gmagick::DECORATION_NO` (`int`)  

`Gmagick::DECORATION_UNDERLINE` (`int`)  

`Gmagick::DECORATION_OVERLINE` (`int`)  

`Gmagick::DECORATION_LINETROUGH` (`int`)  

<!-- -->

`Gmagick::NOISE_UNIFORM` (`int`)  

`Gmagick::NOISE_GAUSSIAN` (`int`)  

`Gmagick::NOISE_MULTIPLICATIVEGAUSSIAN` (`int`)  

`Gmagick::NOISE_IMPULSE` (`int`)  

`Gmagick::NOISE_LAPLACIAN` (`int`)  

`Gmagick::NOISE_POISSON` (`int`)  

<!-- -->

`Gmagick::CHANNEL_UNDEFINED` (`int`)  

`Gmagick::CHANNEL_RED` (`int`)  

`Gmagick::CHANNEL_GRAY` (`int`)  

`Gmagick::CHANNEL_CYAN` (`int`)  

`Gmagick::CHANNEL_GREEN` (`int`)  

`Gmagick::CHANNEL_MAGENTA` (`int`)  

`Gmagick::CHANNEL_BLUE` (`int`)  

`Gmagick::CHANNEL_YELLOW` (`int`)  

`Gmagick::CHANNEL_ALPHA` (`int`)  

`Gmagick::CHANNEL_OPACITY` (`int`)  

`Gmagick::CHANNEL_MATTE` (`int`)  

`Gmagick::CHANNEL_BLACK` (`int`)  

`Gmagick::CHANNEL_INDEX` (`int`)  

`Gmagick::CHANNEL_ALL` (`int`)  

<!-- -->

`Gmagick::METRIC_UNDEFINED` (`int`)  

`Gmagick::METRIC_MEANABSOLUTEERROR` (`int`)  

`Gmagick::METRIC_MEANSQUAREERROR` (`int`)  

`Gmagick::METRIC_PEAKABSOLUTEERROR` (`int`)  

`Gmagick::METRIC_PEAKSIGNALTONOISERATIO` (`int`)  

`Gmagick::METRIC_ROOTMEANSQUAREDERROR` (`int`)  

<!-- -->

`Gmagick::PIXEL_CHAR` (`int`)  

`Gmagick::PIXEL_DOUBLE` (`int`)  

`Gmagick::PIXEL_FLOAT` (`int`)  

`Gmagick::PIXEL_INTEGER` (`int`)  

`Gmagick::PIXEL_LONG` (`int`)  

`Gmagick::PIXEL_QUANTUM` (`int`)  

`Gmagick::PIXEL_SHORT` (`int`)  

<!-- -->

`Gmagick::COLORSPACE_UNDEFINED` (`int`)  

`Gmagick::COLORSPACE_RGB` (`int`)  

`Gmagick::COLORSPACE_GRAY` (`int`)  

`Gmagick::COLORSPACE_TRANSPARENT` (`int`)  

`Gmagick::COLORSPACE_OHTA` (`int`)  

`Gmagick::COLORSPACE_LAB` (`int`)  

`Gmagick::COLORSPACE_XYZ` (`int`)  

`Gmagick::COLORSPACE_YCBCR` (`int`)  

`Gmagick::COLORSPACE_YCC` (`int`)  

`Gmagick::COLORSPACE_YIQ` (`int`)  

`Gmagick::COLORSPACE_YPBPR` (`int`)  

`Gmagick::COLORSPACE_YUV` (`int`)  

`Gmagick::COLORSPACE_CMYK` (`int`)  

`Gmagick::COLORSPACE_SRGB` (`int`)  

`Gmagick::COLORSPACE_HSB` (`int`)  

`Gmagick::COLORSPACE_HSL` (`int`)  

`Gmagick::COLORSPACE_HWB` (`int`)  

`Gmagick::COLORSPACE_REC601LUMA` (`int`)  

`Gmagick::COLORSPACE_REC709LUMA` (`int`)  

`Gmagick::COLORSPACE_LOG` (`int`)  

<!-- -->

`Gmagick::VIRTUALPIXELMETHOD_UNDEFINED` (`int`)  

`Gmagick::VIRTUALPIXELMETHOD_BACKGROUND` (`int`)  

`Gmagick::VIRTUALPIXELMETHOD_CONSTANT` (`int`)  

`Gmagick::VIRTUALPIXELMETHOD_EDGE` (`int`)  

`Gmagick::VIRTUALPIXELMETHOD_MIRROR` (`int`)  

`Gmagick::VIRTUALPIXELMETHOD_TILE` (`int`)  

`Gmagick::VIRTUALPIXELMETHOD_TRANSPARENT` (`int`)  

<!-- -->

`Gmagick::PREVIEW_UNDEFINED` (`int`)  

`Gmagick::PREVIEW_ROTATE` (`int`)  

`Gmagick::PREVIEW_SHEAR` (`int`)  

`Gmagick::PREVIEW_ROLL` (`int`)  

`Gmagick::PREVIEW_HUE` (`int`)  

`Gmagick::PREVIEW_SATURATION` (`int`)  

`Gmagick::PREVIEW_BRIGHTNESS` (`int`)  

`Gmagick::PREVIEW_GAMMA` (`int`)  

`Gmagick::PREVIEW_SPIFF` (`int`)  

`Gmagick::PREVIEW_DULL` (`int`)  

`Gmagick::PREVIEW_GRAYSCALE` (`int`)  

`Gmagick::PREVIEW_QUANTIZE` (`int`)  

`Gmagick::PREVIEW_DESPECKLE` (`int`)  

`Gmagick::PREVIEW_REDUCENOISE` (`int`)  

`Gmagick::PREVIEW_ADDNOISE` (`int`)  

`Gmagick::PREVIEW_SHARPEN` (`int`)  

`Gmagick::PREVIEW_BLUR` (`int`)  

`Gmagick::PREVIEW_THRESHOLD` (`int`)  

`Gmagick::PREVIEW_EDGEDETECT` (`int`)  

`Gmagick::PREVIEW_SPREAD` (`int`)  

`Gmagick::PREVIEW_SOLARIZE` (`int`)  

`Gmagick::PREVIEW_SHADE` (`int`)  

`Gmagick::PREVIEW_RAISE` (`int`)  

`Gmagick::PREVIEW_SEGMENT` (`int`)  

`Gmagick::PREVIEW_SWIRL` (`int`)  

`Gmagick::PREVIEW_IMPLODE` (`int`)  

`Gmagick::PREVIEW_WAVE` (`int`)  

`Gmagick::PREVIEW_OILPAINT` (`int`)  

`Gmagick::PREVIEW_CHARCOALDRAWING` (`int`)  

`Gmagick::PREVIEW_JPEG` (`int`)  

<!-- -->

`Gmagick::RENDERINGINTENT_UNDEFINED` (`int`)  

`Gmagick::RENDERINGINTENT_SATURATION` (`int`)  

`Gmagick::RENDERINGINTENT_PERCEPTUAL` (`int`)  

`Gmagick::RENDERINGINTENT_ABSOLUTE` (`int`)  

`Gmagick::RENDERINGINTENT_RELATIVE` (`int`)  

<!-- -->

`Gmagick::FILLRULE_UNDEFINED` (`int`)  

`Gmagick::FILLRULE_EVENODD` (`int`)  

`Gmagick::FILLRULE_NONZERO` (`int`)  

<!-- -->

`Gmagick::PATHUNITS_UNDEFINED` (`int`)  

`Gmagick::PATHUNITS_USERSPACE` (`int`)  

`Gmagick::PATHUNITS_USERSPACEONUSE` (`int`)  

`Gmagick::PATHUNITS_OBJECTBOUNDINGBOX` (`int`)  

<!-- -->

`Gmagick::LINECAP_UNDEFINED` (`int`)  

`Gmagick::LINECAP_BUTT` (`int`)  

`Gmagick::LINECAP_ROUND` (`int`)  

`Gmagick::LINECAP_SQUARE` (`int`)  

<!-- -->

`Gmagick::LINEJOIN_UNDEFINED` (`int`)  

`Gmagick::LINEJOIN_MITER` (`int`)  

`Gmagick::LINEJOIN_ROUND` (`int`)  

`Gmagick::LINEJOIN_BEVEL` (`int`)  

<!-- -->

`Gmagick::RESOURCETYPE_UNDEFINED` (`int`)  

`Gmagick::RESOURCETYPE_AREA` (`int`)  

`Gmagick::RESOURCETYPE_DISK` (`int`)  

`Gmagick::RESOURCETYPE_FILE` (`int`)  

`Gmagick::RESOURCETYPE_MAP` (`int`)  

`Gmagick::RESOURCETYPE_MEMORY` (`int`)  

<!-- -->

`Gmagick::ORIENTATION_UNDEFINED` (`int`)  

`Gmagick::ORIENTATION_TOPLEFT` (`int`)  

`Gmagick::ORIENTATION_TOPRIGHT` (`int`)  

`Gmagick::ORIENTATION_BOTTOMRIGHT` (`int`)  

`Gmagick::ORIENTATION_BOTTOMLEFT` (`int`)  

`Gmagick::ORIENTATION_LEFTTOP` (`int`)  

`Gmagick::ORIENTATION_RIGHTTOP` (`int`)  

`Gmagick::ORIENTATION_RIGHTBOTTOM` (`int`)  

`Gmagick::ORIENTATION_LEFTBOTTOM` (`int`)  

<!-- -->

`Gmagick::INTERLACE_UNDEFINED` (`int`)  

`Gmagick::INTERLACE_NO` (`int`)  

`Gmagick::INTERLACE_NONE` (`int`)  

`Gmagick::INTERLACE_LINE` (`int`)  

`Gmagick::INTERLACE_PLANE` (`int`)  

`Gmagick::INTERLACE_PARTITION` (`int`)
