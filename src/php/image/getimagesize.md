---
title: getimagesize
description: Devuelve el tamaño de una imagen
source_url: https://www.php.net/manual/es/function.getimagesize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/getimagesize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 31380
---

getimagesize

Devuelve el tamaño de una imagen

## Descripción

```php
getimagesize(string $filename, [array $image_info]): array
```php

`getimagesize` determina el tamaño de cualquier imagen soportada proporcionada y devuelve las dimensiones, el tipo de imagen y una cadena tipo `height/width` para colocar en una etiqueta HTML IMG normal y el tipo de contenido HTTP correspondiente.

`getimagesize` puede también devolver más información en el argumento `image_info`.

> [!CAUTION]
> Esta función espera que `filename` sea un fichero de imagen válido. Si se proporciona un fichero no imagen, puede ser detectado incorrectamente como imagen y la función devolverá con éxito, pero el array puede contener valores absurdos.
>
> No se debe utilizar `getimagesize` para verificar que un fichero dado es una imagen válida. En su lugar, debe utilizarse una solución diseñada para ello como la extensión [FileInfo](#book.fileinfo).

> [!NOTE]
> Se debe tener en cuenta que JPC y JP2 pueden tener componentes con diferentes profundidades de bit. En este caso, el valor de "bits" es la mayor profundidad de bit encontrada. Asimismo, los ficheros JP2 disponen de soporte para `multiple JPEG 2000 codestreams`. En este caso, `getimagesize` devuelve los valores para el primer codestream encontrado en la raíz del fichero.

> [!NOTE]
> La información sobre iconos se recupera desde el icono con mayor resolución.

> [!NOTE]
> Las imágenes GIF consistentes en uno o varios fotogramas, donde cada fotograma puede ocupar únicamente una parte de la imagen. El tamaño de la imagen que es reportado por `getimagesize` es el tamaño global (leído desde el descriptor lógico de la pantalla).

## Parámetros

`filename`  
Este argumento especifica el fichero del cual se desean obtener las informaciones. Puede ser un fichero local o (dependiendo de la configuración), un fichero remoto utilizando uno de los [flujos soportados](#wrappers).

`image_info`  
Este argumento opcional permite extraer información adicional del fichero de imagen. Actualmente, esta opción devuelve diferentes marcadores JPG APP en un array asociativo. Algunos programas utilizan estos marcadores APP para especificar información en las etiquetas HTML. Un marcador común es el marcador APP13, descrito en [IPTC](http://www.iptc.org/). Puede utilizarse la función `iptcparse` para analizar este marcador, y obtener información legible.

> [!NOTE]
> `image_info` soporta únicamente los ficheros JFIF.

## Valores devueltos

Devuelve un array que contiene hasta 7 elementos. No todos los tipos de imágenes incluyen los elementos `channels` y `bits`.

El índice 0 contiene el ancho. El índice 1 contiene la altura.

> [!NOTE]
> Algunos formatos pueden no contener ninguna imagen, o bien varias. En estos casos, `getimagesize` puede no ser capaz de determinar correctamente el tamaño de la imagen. `getimagesize` devuelve entonces cero como tamaño de altura y ancho.

> [!NOTE]
> `getimagesize` es independiente de las metadatos de la imagen. Por ejemplo, si la bandera Exif `Orientation` está definida en un valor que gira la imagen 90 o 270 grados, los índices 0 y 1 son intercambiados, es decir, contienen respectivamente la altura y el ancho.

El índice 2 es una constante entre `IMAGETYPE_*`, indicando el tipo de la imagen.

El índice 3 contiene la cadena para colocar en las etiquetas IMG: `height="xxx" width="yyy"`.

`mime` corresponde al tipo MIME de una imagen. Esta información puede ser utilizada para enviar el encabezado HTTP `Content-type` correcto:

`getimagesize` y tipos MIME

```
<?php
$size = getimagesize($filename);
$fp = fopen($filename, "rb");
if ($size && $fp) {
    header("Content-type: {$size['mime']}");
    fpassthru($fp);
    exit;
} else {
    // error
}
?>

    
```php

`channels` será 3 para imágenes RGB y 4 para imágenes CMYK.

`bits` es el número de bytes para cada color.

Sin embargo, la presencia de los valores de `channels` y de `bits` puede llevar a la confusión. Por ejemplo, una imagen GIF utiliza siempre tres canales por píxel, pero el número de bits por píxel no puede ser calculado en el caso de una imagen animada GIF con una tabla de colores global.

Si ocurre un error, `false` es devuelto.

## Errores/Excepciones

Si el acceso a `filename` es imposible, `getimagesize` generará un error de nivel `E_WARNING`. Si ocurre un error durante la lectura, `getimagesize` generará un error de nivel `E_NOTICE`.

A partir de PHP 8.0.0, se lanza una excepción ValueError si `filename` está vacío.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Devuelve las dimensiones actuales de la imagen, bits y canales de imágenes AVIF; previamente, las dimensiones eran reportadas como `0x0`, y bits y canales no eran reportados en absoluto. |
| 8.0.0 | Ahora se lanza una excepción ValueError si `filename` está vacío; anteriormente se generaba un `E_WARNING` y la función devolvía `false`. |
| 7.1.0 | Añadido el soporte para WebP. |

## Ejemplos

Ejemplo con `getimagesize`

```
<?php
list($width, $height, $type, $attr) = getimagesize("img/flag.jpg");
echo "<img src=\"img/flag.jpg\" $attr alt=\"Ejemplo con getimagesize()\" />";
?>

    
```php

`getimagesize` con una URL

```
<?php
$size = getimagesize("http://www.example.com/gifs/logo.gif");

// Si el nombre del fichero contiene espacios, codifíquelo!
$size = getimagesize("http://www.example.com/gifs/lo%20go.gif");

?>

    
```php

`getimagesize` que devuelve IPTC

```
<?php
$size = getimagesize("testimg.jpg", $info);
if (isset($info["APP13"])) {
    $iptc = iptcparse($info["APP13"]);
    var_dump($iptc);
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función no requiere la biblioteca GD.

## Véase también

image_type_to_mime_type

exif_imagetype

exif_read_data

exif_thumbnail

imagesx

imagesy
