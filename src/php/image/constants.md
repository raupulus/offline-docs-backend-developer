---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/image.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: false
translation_revision: f8bab1dfb
order: 31350
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`GD_VERSION` (`string`)  
La versión de GD con la que se compiló PHP.

`GD_MAJOR_VERSION` (`int`)  
La versión principal de GD con la que se compiló PHP.

`GD_MINOR_VERSION` (`int`)  
La versión secundaria de GD con la que se compiló PHP.

`GD_RELEASE_VERSION` (`int`)  
La versión de lanzamiento de GD con la que se compiló PHP.

`GD_EXTRA_VERSION` (`string`)  
La versión "extra" de GD (beta/rc..) con la que se compiló PHP.

`GD_BUNDLED` (`int`)  
Cuando se usa la versión incluida de GD este valor es 1, de lo contrario se establece en 0.

`IMG_AVIF` (`int`)  
Utilizado como valor de retorno por `imagetypes`

(disponible a partir de PHP 8.1.0)

`IMG_BMP` (`int`)  
Utilizado como valor de retorno por `imagetypes`

`IMG_GIF` (`int`)  
Utilizado como valor de retorno por `imagetypes`

`IMG_JPG` (`int`)  
Utilizado como valor de retorno por `imagetypes`

`IMG_JPEG` (`int`)  
Utilizado como valor de retorno por `imagetypes`

> [!NOTE]
> Esta constante tiene el mismo valor que `IMG_JPG`

`IMG_PNG` (`int`)  
Utilizado como valor de retorno por `imagetypes`

`IMG_TGA` (`int`)  
Utilizado como valor de retorno por `imagetypes`

(disponible a partir de PHP 7.4.0)

`IMG_WBMP` (`int`)  
Utilizado como valor de retorno por `imagetypes`

`IMG_XPM` (`int`)  
Utilizado como valor de retorno por `imagetypes`

`IMG_WEBP` (`int`)  
Utilizado como valor de retorno por `imagetypes`

(disponible a partir de PHP 7.0.10)

`IMG_WEBP_LOSSLESS` (`int`)  
(disponible a partir de PHP 8.1.0)

`IMG_COLOR_TILED` (`int`)  
Opción de color especial que puede utilizarse en lugar de un color asignado con `imagecolorallocate` o `imagecolorallocatealpha`.

`IMG_COLOR_STYLED` (`int`)  
Opción de color especial que puede utilizarse en lugar de un color asignado con `imagecolorallocate` o `imagecolorallocatealpha`.

`IMG_COLOR_BRUSHED` (`int`)  
Opción de color especial que puede utilizarse en lugar de un color asignado con `imagecolorallocate` o `imagecolorallocatealpha`.

`IMG_COLOR_STYLEDBRUSHED` (`int`)  
Opción de color especial que puede utilizarse en lugar de un color asignado con `imagecolorallocate` o `imagecolorallocatealpha`.

`IMG_COLOR_TRANSPARENT` (`int`)  
Opción de color especial que puede utilizarse en lugar de un color asignado con `imagecolorallocate` o `imagecolorallocatealpha`.

`IMG_AFFINE_TRANSLATE` (`int`)  
Constante de tipo de transformación afín utilizada por la función `imageaffinematrixget`.

`IMG_AFFINE_SCALE` (`int`)  
Constante de tipo de transformación afín utilizada por la función `imageaffinematrixget`.

`IMG_AFFINE_ROTATE` (`int`)  
Constante de tipo de transformación afín utilizada por la función `imageaffinematrixget`.

`IMG_AFFINE_SHEAR_HORIZONTAL` (`int`)  
Constante de tipo de transformación afín utilizada por la función `imageaffinematrixget`.

`IMG_AFFINE_SHEAR_VERTICAL` (`int`)  
Constante de tipo de transformación afín utilizada por la función `imageaffinematrixget`.

`IMG_ARC_ROUNDED` (`int`)  
Constante de estilo utilizada por la función `imagefilledarc`.

> [!NOTE]
> Esta constante tiene el mismo valor que `IMG_ARC_PIE`

`IMG_ARC_PIE` (`int`)  
Constante de estilo utilizada por la función `imagefilledarc`.

`IMG_ARC_CHORD` (`int`)  
Constante de estilo utilizada por la función `imagefilledarc`.

`IMG_ARC_NOFILL` (`int`)  
Constante de estilo utilizada por la función `imagefilledarc`.

`IMG_ARC_EDGED` (`int`)  
Constante de estilo utilizada por la función `imagefilledarc`.

`IMG_GD2_RAW` (`int`)  
Constante de tipo utilizada por la función `imagegd2`.

`IMG_GD2_COMPRESSED` (`int`)  
Constante de tipo utilizada por la función `imagegd2`.

`IMG_EFFECT_REPLACE` (`int`)  
Efecto de mezcla alfa utilizado por la función `imagelayereffect`.

`IMG_EFFECT_ALPHABLEND` (`int`)  
Efecto de mezcla alfa utilizado por la función `imagelayereffect`.

`IMG_EFFECT_NORMAL` (`int`)  
Efecto de mezcla alfa utilizado por la función `imagelayereffect`.

`IMG_EFFECT_OVERLAY` (`int`)  
Efecto de mezcla alfa utilizado por la función `imagelayereffect`.

`IMG_EFFECT_MULTIPLY` (`int`)  
Efecto de mezcla alfa utilizado por la función `imagelayereffect`.

`IMG_FILTER_NEGATE` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_GRAYSCALE` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_BRIGHTNESS` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_CONTRAST` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_COLORIZE` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_EDGEDETECT` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_GAUSSIAN_BLUR` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_SELECTIVE_BLUR` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_EMBOSS` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_MEAN_REMOVAL` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_SMOOTH` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_PIXELATE` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

`IMG_FILTER_SCATTER` (`int`)  
Filtro GD especial utilizado por la función `imagefilter`.

(disponible a partir de PHP 7.4.0)

`IMAGETYPE_GIF` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_JPEG` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_JPEG2000` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_PNG` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_SWF` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_PSD` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_BMP` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_WBMP` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_XBM` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_TIFF_II` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_TIFF_MM` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_IFF` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_JB2` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_JPC` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_JP2` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_JPX` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_SWC` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_ICO` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_WEBP` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

(disponible a partir de PHP 7.1.0)

`IMAGETYPE_AVIF` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

(disponible a partir de PHP 8.1.0)

`IMAGETYPE_HEIF` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

(disponible a partir de PHP 8.5.0)

`IMAGETYPE_UNKNOWN` (`int`)  
Constante de tipo de imagen utilizada por las funciones `image_type_to_mime_type` y `image_type_to_extension`.

`IMAGETYPE_COUNT` (`int`)  
El número de constantes de tipo de imagen (incluyendo el tipo "desconocido") compatibles con las funciones `image_type_to_mime_type` y `image_type_to_extension`

`PNG_NO_FILTER` (`int`)  
Filtro PNG especial, utilizado por la función `imagepng`.

`PNG_FILTER_NONE` (`int`)  
Filtro PNG especial, utilizado por la función `imagepng`.

`PNG_FILTER_SUB` (`int`)  
Filtro PNG especial, utilizado por la función `imagepng`.

`PNG_FILTER_UP` (`int`)  
Filtro PNG especial, utilizado por la función `imagepng`.

`PNG_FILTER_AVG` (`int`)  
Filtro PNG especial, utilizado por la función `imagepng`.

`PNG_FILTER_PAETH` (`int`)  
Filtro PNG especial, utilizado por la función `imagepng`.

`PNG_ALL_FILTERS` (`int`)  
Filtro PNG especial, utilizado por la función `imagepng`.

`IMG_FLIP_VERTICAL` (`int`)  
Utilizado junto con `imageflip`, disponible a partir de PHP 5.5.0.

`IMG_FLIP_HORIZONTAL` (`int`)  
Utilizado junto con `imageflip`, disponible a partir de PHP 5.5.0.

`IMG_FLIP_BOTH` (`int`)  
Utilizado junto con `imageflip`, disponible a partir de PHP 5.5.0.

`IMG_BELL` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_BESSEL` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_BILINEAR_FIXED` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_BICUBIC` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_BICUBIC_FIXED` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_BLACKMAN` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_BOX` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_BSPLINE` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_CATMULLROM` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_GAUSSIAN` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_GENERALIZED_CUBIC` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_HERMITE` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_HAMMING` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_HANNING` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_MITCHELL` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_POWER` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_QUADRATIC` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_SINC` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_NEAREST_NEIGHBOUR` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_WEIGHTED4` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_TRIANGLE` (`int`)  
Utilizado junto con `imagesetinterpolation`, disponible a partir de PHP 5.5.0.

`IMG_CROP_BLACK` (`int`)  
Recorta el fondo negro.

`IMG_CROP_DEFAULT` (`int`)  
Igual que `IMG_CROP_TRANSPARENT`. Antes de PHP 7.4.0, la librería GD incluida recurría a `IMG_CROP_SIDES`, si la imagen no tenía color transparente.

`IMG_CROP_SIDES` (`int`)  
Usa las 4 esquinas de la imagen para intentar detectar el fondo a recortar.

`IMG_CROP_THRESHOLD` (`int`)  
Recorta una imagen usando el `umbral` y el `color` dados.

`IMG_CROP_TRANSPARENT` (`int`)  
Recorta el fondo transparente.

`IMG_CROP_WHITE` (`int`)  
Recorta el fondo blanco.
