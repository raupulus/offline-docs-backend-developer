---
title: exif_read_data
description: Lee los encabezados EXIF en las imágenes
source_url: https://www.php.net/manual/es/function.exif-read-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exif/functions/exif-read-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exif
translation_status: ready
translation_reviewed: true
translation_revision: 330a38c4d
order: 20680
---

exif_read_data

Lee los encabezados

EXIF

en las imágenes

## Descripción

```php
exif_read_data(resource $file, [string $required_sections], [bool $as_arrays], [bool $read_thumbnail]): array
```php

`exif_read_data` lee los encabezados EXIF de las imágenes. Con esta función, se pueden leer los datos meta generados por las cámaras digitales.

Los encabezados EXIF tienden a estar presentes en las imágenes JPEG/TIFF generadas por las cámaras digitales, pero desafortunadamente, cada cámara digital tiene una idea diferente de cómo sus imágenes deben ser marcadas, por lo que no siempre se puede contar con un encabezado EXIF específico, aunque esté presente.

Los parámetros `Height` y `Width` se calculan de la misma manera que para la función `getimagesize`, por lo que sus valores no formarán parte de ningún encabezado devuelto. De igual manera, el índice `html` es la representación textual de la altura/ancho utilizada en una etiqueta de imagen HTML clásica.

Cuando un encabezado EXIF contiene una nota de Copyright, este encabezado puede contener a su vez dos valores. Como esta solución es inconsistente con los estándares EXIF 2.10, la sección `COMPUTED` devolverá los dos encabezados, `Copyright.Photographer` y `Copyright.Editor`, mientras que las secciones `IFD0` contienen el array de bytes con caracteres NULL para separar las dos entradas; o bien, solo la primera entrada si el tipo de datos era incorrecto (comportamiento por defecto de EXIF). La sección `COMPUTED` también contendrá una entrada `Copyright`, que será ya sea la cadena original de copyright, o una lista de valores separados por comas de fotos y copyright del autor.

La etiqueta `UserComment` presenta el mismo problema que la etiqueta Copyright. Puede almacenar dos valores: primero, el juego de caracteres utilizado, luego el valor en sí. Si es así, la sección `IFD` contendrá solo el juego de caracteres, o un array de bytes. La sección `COMPUTED` almacenará las dos entradas `UserCommentEncoding` y `UserComment`. El índice `UserComment` está disponible en ambos casos, y es preferible usarlo, en lugar del valor de la sección `IFD0`.

`exif_read_data` valida los datos de las etiquetas EXIF de acuerdo con la especificación EXIF (<http://exif.org/Exif2-2.PDF>, página 20).

## Parámetros

`file`  
La ubicación del archivo de imagen. Puede ser ya sea una ruta de acceso al archivo (los wrappers de flujo también son soportados como de costumbre), o un flujo `resource`.

`required_sections`  
Lista de valores separados por comas de las secciones que deben presentarse en el array de resultado. Si ninguna de las secciones solicitadas se encuentra, el valor devuelto es `false`.

|  |  |
|----|----|
| FILE | FileName (nombre del archivo), FileSize (tamaño del archivo), FileDateTime (fecha de modificación del archivo), SectionsFound (secciones encontradas) |
| COMPUTED | Atributo Html, ancho, altura, color o blanco y negro y más si está disponible. El ancho y la altura se calculan de la misma manera que la función `getimagesize`, por lo que sus valores nunca deberían diferir. De igual manera, el índice `html` es la representación textual de la altura/ancho utilizada en una etiqueta de imagen HTML clásica. |
| ANY_TAG | Toda la información concerniente a esta etiqueta, como `IFD0`, `EXIF`, ... |
| IFD0 | Todas las etiquetas `IFD0`. En imágenes normales, contienen las dimensiones de la imagen, etc. |
| THUMBNAIL | Un archivo que contiene una miniatura, si hay un segundo `IFD`. Toda la información etiquetada sobre esta miniatura será almacenada en esta sección. |
| COMMENT | Encabezado de comentario de las imágenes JPEG. |
| EXIF | La sección EXIF es una subsección de la sección `IFD0`. Ella contiene información más detallada sobre las imágenes. La mayoría de estos índices están relacionados con las cámaras digitales. |

`as_arrays`  
Especifica si cada sección debe convertirse en un array o no. Las `required_sections` `COMPUTED`, `THUMBNAIL` y `COMMENT` siempre serán convertidas en arrays, ya que contienen nombres que podrían entrar en conflicto.

`read_thumbnail`  
Cuando se define como `true`, la miniatura misma es leída. De lo contrario, solo se leen los datos contenidos en el archivo.

## Valores devueltos

Devuelve un array asociativo donde los índices son los nombres de los encabezados y los valores son los valores asociados a estos encabezados. Si no se puede devolver ningún dato, `exif_read_data` devolverá `false`.

## Errores/Excepciones

Pueden generarse errores de nivel `E_WARNING` y/o `E_NOTICE` para etiquetas no soportadas u otras condiciones de error potencial, pero la función intenta leer toda la información comprensible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `required_sections` ahora es nullable. |
| 7.2.0 | Se ha añadido el soporte para los siguientes formatos EXIF: Samsung, DJI, Panasonic, Sony, Pentax, Minolta, Sigma/Foveon, AGFA, Kyocera, Ricoh, Epson |

## Ejemplos

Ejemplo con `exif_read_data`

```
<?php
echo "test1.jpg:<br />\n";
$exif = exif_read_data('tests/test1.jpg', 'IFD0');
echo $exif===false ? "No se encontraron encabezados de datos.<br />\n" : "La imagen contiene encabezados<br />\n";

$exif = exif_read_data('tests/test2.jpg', 0, true);
echo "test2.jpg:<br />\n";
foreach ($exif as $key => $section) {
    foreach ($section as $name => $val) {
        echo "$key.$name: $val<br />\n";
    }
}
?>

   
```php

La primera llamada falla porque la imagen no tiene encabezado de información.

Resultado del ejemplo anterior es similar a:

```
test1.jpg:
No se encontraron encabezados de datos.
test2.jpg:
FILE.FileName: test2.jpg
FILE.FileDateTime: 1017666176
FILE.FileSize: 1240
FILE.FileType: 2
FILE.SectionsFound: ANY_TAG, IFD0, THUMBNAIL, COMMENT
COMPUTED.html: width="1" height="1"
COMPUTED.Height: 1
COMPUTED.Width: 1
COMPUTED.IsColor: 1
COMPUTED.ByteOrderMotorola: 1
COMPUTED.UserComment: Exif test image.
COMPUTED.UserCommentEncoding: ASCII
COMPUTED.Copyright: Photo (c) M.Boerger, Edited by M.Boerger.
COMPUTED.Copyright.Photographer: Photo (c) M.Boerger
COMPUTED.Copyright.Editor: Edited by M.Boerger.
IFD0.Copyright: Photo (c) M.Boerger
IFD0.UserComment: ASCII
THUMBNAIL.JPEGInterchangeFormat: 134
THUMBNAIL.JPEGInterchangeFormatLength: 523
COMMENT.0: Comment #1.
COMMENT.1: Comment #2.
COMMENT.2: Comment #3end
THUMBNAIL.JPEGInterchangeFormat: 134
THUMBNAIL.Thumbnail.Height: 1
THUMBNAIL.Thumbnail.Height: 1

   
```php

`exif_read_data` con flujos disponibles desde PHP 7.2.0

```
<?php
// Abrir el archivo, esto debería ser en modo binario
$fp = fopen('/path/to/image.jpg', 'rb');

if (!$fp) {
    echo 'Error: No se pudo abrir la imagen para lectura';
    exit;
}

// Intentar leer los encabezados EXIF
$headers = exif_read_data($fp);

if (!$headers) {
    echo 'Error: No se pudieron leer los encabezados exif';
    exit;
}

// Mostrar los encabezados 'COMPUTED'
echo 'EXIF Headers:' . PHP_EOL;

foreach ($headers['COMPUTED'] as $header => $value) {
    printf(' %s => %s%s', $header, $value, PHP_EOL);
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

```
EXIF Headers:
 Height => 576
 Width => 1024
 IsColor => 1
 ByteOrderMotorola => 0
 ApertureFNumber => f/5.6
 UserComment =>
 UserCommentEncoding => UNDEFINED
 Copyright => Denis
 Thumbnail.FileType => 2
 Thumbnail.MimeType => image/jpeg

   
```php

## Notas

> [!NOTE]
> Si [mbstring](#ref.mbstring) está activado, EXIF intentará tratar el Unicode y elegir un juego de caracteres como se especifica por [exif.decode_unicode_motorola](#ini.exif.decode-unicode-motorola) y [exif.decode_unicode_intel](#ini.exif.decode-unicode-intel). La extensión EXIF no intentará determinar el codificado por sí misma, y es responsabilidad del usuario especificar correctamente el codificado a usar para el decodificado definiendo una de las dos directivas INI antes de llamar a `exif_read_data`.

> [!NOTE]
> Si el parámetro `file` se usa para pasar un flujo a la función, entonces el flujo debe ser reposicionable. Tenga en cuenta que la posición del puntero de un archivo no se modifica después del retorno de esta función.

## Véase también

exif_thumbnail

getimagesize
