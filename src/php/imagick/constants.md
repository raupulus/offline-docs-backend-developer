---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/imagick.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 3bbb0751e
order: 32580
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`imagick::COLOR_BLACK` (`int`)  
Color negro

`imagick::COLOR_BLUE` (`int`)  
Color azul

`imagick::COLOR_CYAN` (`int`)  
Color cian

`imagick::COLOR_GREEN` (`int`)  
Color verde

`imagick::COLOR_RED` (`int`)  
Color rojo

`imagick::COLOR_YELLOW` (`int`)  
Color amarillo

`imagick::COLOR_MAGENTA` (`int`)  
Color magenta

`imagick::COLOR_OPACITY` (`int`)  
Color de la opacidad

`imagick::COLOR_ALPHA` (`int`)  
Color del alpha

`imagick::COLOR_FUZZ` (`int`)  
Color del fuzz

<!-- -->

`imagick::DISPOSE_UNRECOGNIZED` (`int`)  
Tipo de disposición no reconocido

`imagick::DISPOSE_UNDEFINED` (`int`)  
Tipo de disposición no definido

`imagick::DISPOSE_NONE` (`int`)  
Ningún tipo de disposición

`imagick::DISPOSE_BACKGROUND` (`int`)  
Disposición del fondo

`imagick::DISPOSE_PREVIOUS` (`int`)  
Disposición previa

<!-- -->

`imagick::COMPOSITE_DEFAULT` (`int`)  
El operador de composición por defecto.

`imagick::COMPOSITE_UNDEFINED` (`int`)  
Operador de composición indefinido

`imagick::COMPOSITE_NO` (`int`)  
No hay operador de composición definido

`imagick::COMPOSITE_ADD` (`int`)  
El resultado de imagen + imagen

`imagick::COMPOSITE_ATOP` (`int`)  
El resultado tiene la misma forma que la imagen, con la imagen compuesta que llena la imagen donde la forma de la imagen se superpone a la imagen

`imagick::COMPOSITE_BLEND` (`int`)  
Combina las imágenes imagen (mezcla)

`imagick::COMPOSITE_BUMPMAP` (`int`)  
Lo mismo que COMPOSITE_MULTIPLY, excepto que la fuente se convierte primero a niveles de gris

`imagick::COMPOSITE_CLEAR` (`int`)  
Hace que la imagen de destino sea transparente

`imagick::COMPOSITE_COLORBURN` (`int`)  
Oscurece la imagen de destino para reflejar la imagen fuente

`imagick::COMPOSITE_COLORDODGE` (`int`)  
Aclara la imagen de destino para reflejar la imagen fuente

`imagick::COMPOSITE_COLORIZE` (`int`)  
Colorea la imagen de destino con la imagen compuesta

`imagick::COMPOSITE_COPYBLACK` (`int`)  
Copia el negro de la fuente al destino

`imagick::COMPOSITE_COPYBLUE` (`int`)  
Copia el azul de la fuente al destino

`imagick::COMPOSITE_COPY` (`int`)  
Copia la fuente al destino

`imagick::COMPOSITE_COPYCYAN` (`int`)  
Copia el cian de la fuente al destino

`imagick::COMPOSITE_COPYGREEN` (`int`)  
Copia el verde de la fuente al destino

`imagick::COMPOSITE_COPYMAGENTA` (`int`)  
Copia el magenta de la fuente al destino

`imagick::COMPOSITE_COPYOPACITY` (`int`)  
Copia la opacidad de la fuente al destino

`imagick::COMPOSITE_COPYRED` (`int`)  
Copia el rojo de la fuente al destino

`imagick::COMPOSITE_COPYYELLOW` (`int`)  
Copia el amarillo de la fuente al destino

`imagick::COMPOSITE_DARKEN` (`int`)  
Oscurece la imagen de destino

`imagick::COMPOSITE_DSTATOP` (`int`)  
La parte de la imagen de destino que está dentro de la fuente se compone con la fuente y se coloca en el destino.

`imagick::COMPOSITE_DST` (`int`)  
El destino se deja intacto

`imagick::COMPOSITE_DSTIN` (`int`)  
La parte dentro de la fuente reemplaza el destino

`imagick::COMPOSITE_DSTOUT` (`int`)  
La parte fuera de la fuente reemplaza el destino

`imagick::COMPOSITE_DSTOVER` (`int`)  
El destino reemplaza la fuente

`imagick::COMPOSITE_DIFFERENCE` (`int`)  
Resta el color oscuro del color claro

`imagick::COMPOSITE_DISPLACE` (`int`)  
Desplaza los píxeles del destino según lo definido por la fuente

`imagick::COMPOSITE_DISSOLVE` (`int`)  
Disuelve la fuente en el destino

`imagick::COMPOSITE_EXCLUSION` (`int`)  
Produce un efecto similar a imagick::COMPOSITE_DIFFERENCE, pero con un contraste más bajo

`imagick::COMPOSITE_HARDLIGHT` (`int`)  
Multiplica o proyecta los colores, dependiendo del valor del color fuente

`imagick::COMPOSITE_HUE` (`int`)  
Modifica el matiz del destino, según lo definido por la fuente

`imagick::COMPOSITE_IN` (`int`)  
Compone la fuente en el destino

`imagick::COMPOSITE_LIGHTEN` (`int`)  
Aclara el destino, según lo definido por la fuente

`imagick::COMPOSITE_LUMINIZE` (`int`)  
Ilumina el destino según lo definido por la fuente

`imagick::COMPOSITE_MINUS` (`int`)  
Resta la fuente del destino

`imagick::COMPOSITE_MODULATE` (`int`)  
Modula la claridad del destino, su saturación y su matiz según lo definido por el destino

`imagick::COMPOSITE_MULTIPLY` (`int`)  
Multiplica el destino con la fuente

`imagick::COMPOSITE_OUT` (`int`)  
Compone el exterior de la fuente en el destino

`imagick::COMPOSITE_OVER` (`int`)  
Compone la fuente sobre el destino

`imagick::COMPOSITE_OVERLAY` (`int`)  
Superpone la fuente sobre el destino

`imagick::COMPOSITE_PLUS` (`int`)  
Añade la fuente sobre el destino

`imagick::COMPOSITE_REPLACE` (`int`)  
Reemplaza el destino con la fuente

`imagick::COMPOSITE_SATURATE` (`int`)  
Satura el destino según lo definido por la fuente

`imagick::COMPOSITE_SCREEN` (`int`)  
La fuente y el destino se complementan, luego se multiplican y finalmente reemplazan el destino

`imagick::COMPOSITE_SOFTLIGHT` (`int`)  
Oscurece o aclara los colores, según la fuente

`imagick::COMPOSITE_SRCATOP` (`int`)  
La parte de la fuente que está en el destino y compuesta sobre el destino

`imagick::COMPOSITE_SRC` (`int`)  
La fuente se copia sobre el destino

`imagick::COMPOSITE_SRCIN` (`int`)  
La parte de la fuente que está en el destino, reemplaza el destino.

`imagick::COMPOSITE_SRCOUT` (`int`)  
La parte de la fuente que está fuera del destino reemplaza el destino

`imagick::COMPOSITE_SRCOVER` (`int`)  
La fuente reemplaza el destino

`imagick::COMPOSITE_SUBTRACT` (`int`)  
Resta los colores en la fuente en el destino

`imagick::COMPOSITE_THRESHOLD` (`int`)  
La fuente se compone sobre el destino, según lo definido por los umbrales de la fuente

`imagick::COMPOSITE_XOR` (`int`)  
La parte de la fuente que está fuera del destino y combinada con la parte del destino que está fuera de la fuente

<!-- -->

`imagick::MONTAGEMODE_FRAME` (`int`)  

`imagick::MONTAGEMODE_UNFRAME` (`int`)  

`imagick::MONTAGEMODE_CONCATENATE` (`int`)  

<!-- -->

`imagick::STYLE_NORMAL` (`int`)  

`imagick::STYLE_ITALIC` (`int`)  

`imagick::STYLE_OBLIQUE` (`int`)  

`imagick::STYLE_ANY` (`int`)  

<!-- -->

`imagick::FILTER_UNDEFINED` (`int`)  

`imagick::FILTER_POINT` (`int`)  

`imagick::FILTER_BOX` (`int`)  

`imagick::FILTER_TRIANGLE` (`int`)  

`imagick::FILTER_HERMITE` (`int`)  

`imagick::FILTER_HANNING` (`int`)  

`imagick::FILTER_HAMMING` (`int`)  

`imagick::FILTER_BLACKMAN` (`int`)  

`imagick::FILTER_GAUSSIAN` (`int`)  

`imagick::FILTER_QUADRATIC` (`int`)  

`imagick::FILTER_CUBIC` (`int`)  

`imagick::FILTER_CATROM` (`int`)  

`imagick::FILTER_MITCHELL` (`int`)  

`imagick::FILTER_LANCZOS` (`int`)  

`imagick::FILTER_BESSEL` (`int`)  

`imagick::FILTER_SINC` (`int`)  

<!-- -->

`imagick::IMGTYPE_UNDEFINED` (`int`)  

`imagick::IMGTYPE_BILEVEL` (`int`)  

`imagick::IMGTYPE_GRAYSCALE` (`int`)  

`imagick::IMGTYPE_GRAYSCALEMATTE` (`int`)  

`imagick::IMGTYPE_PALETTE` (`int`)  

`imagick::IMGTYPE_PALETTEMATTE` (`int`)  

`imagick::IMGTYPE_TRUECOLOR` (`int`)  

`imagick::IMGTYPE_TRUECOLORMATTE` (`int`)  

`imagick::IMGTYPE_COLORSEPARATION` (`int`)  

`imagick::IMGTYPE_COLORSEPARATIONMATTE` (`int`)  

`imagick::IMGTYPE_OPTIMIZE` (`int`)  

<!-- -->

`imagick::RESOLUTION_UNDEFINED` (`int`)  

`imagick::RESOLUTION_PIXELSPERINCH` (`int`)  

`imagick::RESOLUTION_PIXELSPERCENTIMETER` (`int`)  

<!-- -->

`imagick::COMPRESSION_UNDEFINED` (`int`)  

`imagick::COMPRESSION_NO` (`int`)  

`imagick::COMPRESSION_BZIP` (`int`)  

`imagick::COMPRESSION_FAX` (`int`)  

`imagick::COMPRESSION_GROUP4` (`int`)  

`imagick::COMPRESSION_JPEG` (`int`)  

`imagick::COMPRESSION_JPEG2000` (`int`)  

`imagick::COMPRESSION_LOSSLESSJPEG` (`int`)  

`imagick::COMPRESSION_LZW` (`int`)  

`imagick::COMPRESSION_RLE` (`int`)  

`imagick::COMPRESSION_ZIP` (`int`)  

`imagick::COMPRESSION_DXT1` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.0 o superior.

`imagick::COMPRESSION_DXT3` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.0 o superior.

`imagick::COMPRESSION_DXT5` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.0 o superior.

<!-- -->

`imagick::PAINT_POINT` (`int`)  

`imagick::PAINT_REPLACE` (`int`)  

`imagick::PAINT_FLOODFILL` (`int`)  

`imagick::PAINT_FILLTOBORDER` (`int`)  

`imagick::PAINT_RESET` (`int`)  

<!-- -->

`imagick::GRAVITY_NORTHWEST` (`int`)  

`imagick::GRAVITY_NORTH` (`int`)  

`imagick::GRAVITY_NORTHEAST` (`int`)  

`imagick::GRAVITY_WEST` (`int`)  

`imagick::GRAVITY_CENTER` (`int`)  

`imagick::GRAVITY_EAST` (`int`)  

`imagick::GRAVITY_SOUTHWEST` (`int`)  

`imagick::GRAVITY_SOUTH` (`int`)  

`imagick::GRAVITY_SOUTHEAST` (`int`)  

<!-- -->

`imagick::STRETCH_NORMAL` (`int`)  

`imagick::STRETCH_ULTRACONDENSED` (`int`)  

`imagick::STRETCH_CONDENSED` (`int`)  

`imagick::STRETCH_SEMICONDENSED` (`int`)  

`imagick::STRETCH_SEMIEXPANDED` (`int`)  

`imagick::STRETCH_EXPANDED` (`int`)  

`imagick::STRETCH_EXTRAEXPANDED` (`int`)  

`imagick::STRETCH_ULTRAEXPANDED` (`int`)  

`imagick::STRETCH_ANY` (`int`)  

<!-- -->

`imagick::ALIGN_UNDEFINED` (`int`)  

`imagick::ALIGN_LEFT` (`int`)  

`imagick::ALIGN_CENTER` (`int`)  

`imagick::ALIGN_RIGHT` (`int`)  

<!-- -->

`imagick::DECORATION_NO` (`int`)  

`imagick::DECORATION_UNDERLINE` (`int`)  

`imagick::DECORATION_OVERLINE` (`int`)  

`imagick::DECORATION_LINETROUGH` (`int`)  

<!-- -->

`imagick::NOISE_UNIFORM` (`int`)  

`imagick::NOISE_GAUSSIAN` (`int`)  

`imagick::NOISE_MULTIPLICATIVEGAUSSIAN` (`int`)  

`imagick::NOISE_IMPULSE` (`int`)  

`imagick::NOISE_LAPLACIAN` (`int`)  

`imagick::NOISE_POISSON` (`int`)  

`imagick::NOISE_RANDOM` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

<!-- -->

`imagick::CHANNEL_UNDEFINED` (`int`)  

`imagick::CHANNEL_RED` (`int`)  

`imagick::CHANNEL_GRAY` (`int`)  

`imagick::CHANNEL_CYAN` (`int`)  

`imagick::CHANNEL_GREEN` (`int`)  

`imagick::CHANNEL_MAGENTA` (`int`)  

`imagick::CHANNEL_BLUE` (`int`)  

`imagick::CHANNEL_YELLOW` (`int`)  

`imagick::CHANNEL_ALPHA` (`int`)  

`imagick::CHANNEL_OPACITY` (`int`)  

`imagick::CHANNEL_MATTE` (`int`)  

`imagick::CHANNEL_BLACK` (`int`)  

`imagick::CHANNEL_INDEX` (`int`)  

`imagick::CHANNEL_ALL` (`int`)  

`imagick::CHANNEL_DEFAULT` (`int`)  

<!-- -->

`imagick::METRIC_UNDEFINED` (`int`)  

`imagick::METRIC_MEANABSOLUTEERROR` (`int`)  

`imagick::METRIC_MEANSQUAREERROR` (`int`)  

`imagick::METRIC_PEAKABSOLUTEERROR` (`int`)  

`imagick::METRIC_PEAKSIGNALTONOISERATIO` (`int`)  

`imagick::METRIC_ROOTMEANSQUAREDERROR` (`int`)  

<!-- -->

`imagick::PIXEL_CHAR` (`int`)  

`imagick::PIXEL_DOUBLE` (`int`)  

`imagick::PIXEL_FLOAT` (`int`)  

`imagick::PIXEL_INTEGER` (`int`)  
Solo disponible con ImageMagick \< 7.

`imagick::PIXEL_LONG` (`int`)  

`imagick::PIXEL_QUANTUM` (`int`)  

`imagick::PIXEL_SHORT` (`int`)  

<!-- -->

`imagick::EVALUATE_UNDEFINED` (`int`)  

`imagick::EVALUATE_ADD` (`int`)  

`imagick::EVALUATE_AND` (`int`)  

`imagick::EVALUATE_DIVIDE` (`int`)  

`imagick::EVALUATE_LEFTSHIFT` (`int`)  

`imagick::EVALUATE_MAX` (`int`)  

`imagick::EVALUATE_MIN` (`int`)  

`imagick::EVALUATE_MULTIPLY` (`int`)  

`imagick::EVALUATE_OR` (`int`)  

`imagick::EVALUATE_RIGHTSHIFT` (`int`)  

`imagick::EVALUATE_SET` (`int`)  

`imagick::EVALUATE_SUBTRACT` (`int`)  

`imagick::EVALUATE_XOR` (`int`)  

`imagick::EVALUATE_POW` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_LOG` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_THRESHOLD` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_THRESHOLDBLACK` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_THRESHOLDWHITE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_GAUSSIANNOISE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_IMPULSENOISE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_LAPLACIANNOISE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_MULTIPLICATIVENOISE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_POISSONNOISE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_UNIFORMNOISE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_COSINE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_SINE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

`imagick::EVALUATE_ADDMODULUS` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.4 o superior.

<!-- -->

`imagick::COLORSPACE_UNDEFINED` (`int`)  

`imagick::COLORSPACE_RGB` (`int`)  

`imagick::COLORSPACE_GRAY` (`int`)  

`imagick::COLORSPACE_TRANSPARENT` (`int`)  

`imagick::COLORSPACE_OHTA` (`int`)  

`imagick::COLORSPACE_LAB` (`int`)  

`imagick::COLORSPACE_XYZ` (`int`)  

`imagick::COLORSPACE_YCBCR` (`int`)  

`imagick::COLORSPACE_YCC` (`int`)  

`imagick::COLORSPACE_YIQ` (`int`)  

`imagick::COLORSPACE_YPBPR` (`int`)  

`imagick::COLORSPACE_YUV` (`int`)  

`imagick::COLORSPACE_CMYK` (`int`)  

`imagick::COLORSPACE_SRGB` (`int`)  

`imagick::COLORSPACE_HSB` (`int`)  

`imagick::COLORSPACE_HSL` (`int`)  

`imagick::COLORSPACE_HWB` (`int`)  

`imagick::COLORSPACE_REC601LUMA` (`int`)  

`imagick::COLORSPACE_REC709LUMA` (`int`)  

`imagick::COLORSPACE_LOG` (`int`)  

`imagick::COLORSPACE_CMY` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.2 o superior.

<!-- -->

`imagick::VIRTUALPIXELMETHOD_UNDEFINED` (`int`)  

`imagick::VIRTUALPIXELMETHOD_BACKGROUND` (`int`)  

`imagick::VIRTUALPIXELMETHOD_CONSTANT` (`int`)  

`imagick::VIRTUALPIXELMETHOD_EDGE` (`int`)  

`imagick::VIRTUALPIXELMETHOD_MIRROR` (`int`)  

`imagick::VIRTUALPIXELMETHOD_TILE` (`int`)  

`imagick::VIRTUALPIXELMETHOD_TRANSPARENT` (`int`)  

`imagick::VIRTUALPIXELMETHOD_MASK` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.2 o superior.

`imagick::VIRTUALPIXELMETHOD_BLACK` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.2 o superior.

`imagick::VIRTUALPIXELMETHOD_GRAY` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.2 o superior.

`imagick::VIRTUALPIXELMETHOD_WHITE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.2 o superior.

`imagick::VIRTUALPIXELMETHOD_HORIZONTALTILE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.3 o superior.

`imagick::VIRTUALPIXELMETHOD_VERTICALTILE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.3 o superior.

<!-- -->

`imagick::PREVIEW_UNDEFINED` (`int`)  

`imagick::PREVIEW_ROTATE` (`int`)  

`imagick::PREVIEW_SHEAR` (`int`)  

`imagick::PREVIEW_ROLL` (`int`)  

`imagick::PREVIEW_HUE` (`int`)  

`imagick::PREVIEW_SATURATION` (`int`)  

`imagick::PREVIEW_BRIGHTNESS` (`int`)  

`imagick::PREVIEW_GAMMA` (`int`)  

`imagick::PREVIEW_SPIFF` (`int`)  

`imagick::PREVIEW_DULL` (`int`)  

`imagick::PREVIEW_GRAYSCALE` (`int`)  

`imagick::PREVIEW_QUANTIZE` (`int`)  

`imagick::PREVIEW_DESPECKLE` (`int`)  

`imagick::PREVIEW_REDUCENOISE` (`int`)  

`imagick::PREVIEW_ADDNOISE` (`int`)  

`imagick::PREVIEW_SHARPEN` (`int`)  

`imagick::PREVIEW_BLUR` (`int`)  

`imagick::PREVIEW_THRESHOLD` (`int`)  

`imagick::PREVIEW_EDGEDETECT` (`int`)  

`imagick::PREVIEW_SPREAD` (`int`)  

`imagick::PREVIEW_SOLARIZE` (`int`)  

`imagick::PREVIEW_SHADE` (`int`)  

`imagick::PREVIEW_RAISE` (`int`)  

`imagick::PREVIEW_SEGMENT` (`int`)  

`imagick::PREVIEW_SWIRL` (`int`)  

`imagick::PREVIEW_IMPLODE` (`int`)  

`imagick::PREVIEW_WAVE` (`int`)  

`imagick::PREVIEW_OILPAINT` (`int`)  

`imagick::PREVIEW_CHARCOALDRAWING` (`int`)  

`imagick::PREVIEW_JPEG` (`int`)  

<!-- -->

`imagick::RENDERINGINTENT_UNDEFINED` (`int`)  

`imagick::RENDERINGINTENT_SATURATION` (`int`)  

`imagick::RENDERINGINTENT_PERCEPTUAL` (`int`)  

`imagick::RENDERINGINTENT_ABSOLUTE` (`int`)  

`imagick::RENDERINGINTENT_RELATIVE` (`int`)  

<!-- -->

`imagick::INTERLACE_UNDEFINED` (`int`)  

`imagick::INTERLACE_NO` (`int`)  

`imagick::INTERLACE_LINE` (`int`)  

`imagick::INTERLACE_PLANE` (`int`)  

`imagick::INTERLACE_PARTITION` (`int`)  

`imagick::INTERLACE_GIF` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.4 o superior.

`imagick::INTERLACE_JPEG` (`int`)  

`imagick::INTERLACE_PNG` (`int`)  

<!-- -->

`imagick::FILLRULE_UNDEFINED` (`int`)  

`imagick::FILLRULE_EVENODD` (`int`)  

`imagick::FILLRULE_NONZERO` (`int`)  

<!-- -->

`imagick::PATHUNITS_UNDEFINED` (`int`)  

`imagick::PATHUNITS_USERSPACE` (`int`)  

`imagick::PATHUNITS_USERSPACEONUSE` (`int`)  

`imagick::PATHUNITS_OBJECTBOUNDINGBOX` (`int`)  

<!-- -->

`imagick::LINECAP_UNDEFINED` (`int`)  

`imagick::LINECAP_BUTT` (`int`)  

`imagick::LINECAP_ROUND` (`int`)  

`imagick::LINECAP_SQUARE` (`int`)  

<!-- -->

`imagick::LINEJOIN_UNDEFINED` (`int`)  

`imagick::LINEJOIN_MITER` (`int`)  

`imagick::LINEJOIN_ROUND` (`int`)  

`imagick::LINEJOIN_BEVEL` (`int`)  

<!-- -->

`imagick::RESOURCETYPE_UNDEFINED` (`int`)  

`imagick::RESOURCETYPE_AREA` (`int`)  
Define el ancho y la altura máximos de una imagen que puede almacenarse en la caché de píxeles.

`imagick::RESOURCETYPE_DISK` (`int`)  
Define el tamaño máximo de espacio en disco permitido para almacenar la caché de píxeles.

`imagick::RESOURCETYPE_FILE` (`int`)  
Define el número máximo de archivos de caché de píxeles abiertos.

`imagick::RESOURCETYPE_MAP` (`int`)  
Define el tamaño máximo de memoria en bytes a asignar a la caché de píxeles.

`imagick::RESOURCETYPE_MEMORY` (`int`)  
Define el tamaño máximo de la memoria, en bytes, a asignar a la caché de píxeles.

`imagick::RESOURCETYPE_THREAD` (`int`)  
Define el número máximo de hilos paralelos. Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.7.8 o superior.

<!-- -->

`imagick::LAYERMETHOD_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_COALESCE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_COMPAREANY` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_COMPARECLEAR` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_COMPAREOVERLAY` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_DISPOSE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_OPTIMIZE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_OPTIMIZEPLUS` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.2.9 o superior.

`imagick::LAYERMETHOD_OPTIMIZEIMAGE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::LAYERMETHOD_OPTIMIZETRANS` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::LAYERMETHOD_REMOVEDUPS` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::LAYERMETHOD_REMOVEZERO` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::LAYERMETHOD_COMPOSITE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::LAYERMETHOD_MERGE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.7 o superior.

`imagick::LAYERMETHOD_FLATTEN` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.7 o superior.

`imagick::LAYERMETHOD_MOSAIC` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.7 o superior.

<!-- -->

`imagick::ORIENTATION_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_TOPLEFT` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_TOPRIGHT` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_BOTTOMRIGHT` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_BOTTOMLEFT` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_LEFTTOP` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_RIGHTTOP` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_RIGHTBOTTOM` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

`imagick::ORIENTATION_LEFTBOTTOM` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.0 o superior.

<!-- -->

`imagick::DISTORTION_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_AFFINE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_AFFINEPROJECTION` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_ARC` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_BILINEAR` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_PERSPECTIVE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_PERSPECTIVEPROJECTION` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_SCALEROTATETRANSLATE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.6 o superior.

`imagick::DISTORTION_POLYNOMIAL` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DISTORTION_POLAR` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DISTORTION_DEPOLAR` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DISTORTION_BARREL` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DISTORTION_BARRELINVERSE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DISTORTION_SHEPARDS` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DISTORTION_SENTINEL` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

<!-- -->

`imagick::ALPHACHANNEL_ACTIVATE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

`imagick::ALPHACHANNEL_DEACTIVATE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

`imagick::ALPHACHANNEL_RESET` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

`imagick::ALPHACHANNEL_SET` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.8 o superior.

`imagick::ALPHACHANNEL_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::ALPHACHANNEL_COPY` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::ALPHACHANNEL_EXTRACT` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::ALPHACHANNEL_OPAQUE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::ALPHACHANNEL_SHAPE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::ALPHACHANNEL_TRANSPARENT` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::ALPHACHANNEL_BACKGROUND` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.5.3 o superior.

`imagick::ALPHACHANNEL_REMOVE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.7.8 o superior.

`imagick::ALPHACHANNEL_ASSOCIATE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.9.0 o superior.

`imagick::ALPHACHANNEL_DISSOCIATE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.9.0 o superior.

`imagick::ALPHACHANNEL_ON` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 7.0.0 o superior.

`imagick::ALPHACHANNEL_OFF` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 7.0.0 o superior.

`imagick::ALPHACHANNEL_DISCRETE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 7.0.0 o superior.

<!-- -->

`imagick::SPARSECOLORMETHOD_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::SPARSECOLORMETHOD_BARYCENTRIC` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::SPARSECOLORMETHOD_BILINEAR` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::SPARSECOLORMETHOD_POLYNOMIAL` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::SPARSECOLORMETHOD_SPEPARDS` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::SPARSECOLORMETHOD_VORONOI` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

<!-- -->

`imagick::FUNCTION_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.9 o superior.

`imagick::FUNCTION_POLYNOMIAL` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.9 o superior.

`imagick::FUNCTION_SINUSOID` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.9 o superior.

<!-- -->

`imagick::INTERPOLATE_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_AVERAGE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_BICUBIC` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_BILINEAR` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_FILTER` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_INTEGER` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_MESH` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_NEARESTNEIGHBOR` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.2 o superior.

`imagick::INTERPOLATE_SPLINE` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.3.4 o superior.

<!-- -->

`imagick::DITHERMETHOD_UNDEFINED` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DITHERMETHOD_NO` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DITHERMETHOD_RIEMERSMA` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.

`imagick::DITHERMETHOD_FLOYDSTEINBERG` (`int`)  
Esta constante solo está disponible si Imagick ha sido compilado con ImageMagick versión 6.4.6 o superior.
