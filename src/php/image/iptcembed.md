---
title: iptcembed
description: Incorpora datos binarios IPTC en una imagen JPEG
source_url: https://www.php.net/manual/es/function.iptcembed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/image/functions/iptcembed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: image
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 32500
---

iptcembed

Incorpora datos binarios IPTC en una imagen JPEG

## Descripción

```php
iptcembed(string $iptc_data, string $filename, [int $spool]): string
```php

`iptcembed` incorpora datos binarios IPTC en una imagen JPEG.

## Parámetros

`iptc_data`  
Los datos a escribir.

`filename`  
Ruta hacia el fichero JPEG.

`spool`  
El flag de la bobina. Si la bobina es inferior a 2, entonces el fichero JPEG será devuelto en forma de `string`. De lo contrario el fichero JPEG será enviado a STDOUT.

## Valores devueltos

Si `spool` es inferior a 2, el fichero JPEG será devuelto, o `false` si ocurre un error. De lo contrario devuelve `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `iptcembed`

```
<?php

// Función iptc_make_tag() por Thies C. Arntzen
function iptc_make_tag($rec, $data, $value)
{
    $length = strlen($value);
    $retval = chr(0x1C) . chr($rec) . chr($data);

    if($length < 0x8000)
    {
        $retval .= chr($length >> 8) .  chr($length & 0xFF);
    }
    else
    {
        $retval .= chr(0x80) .
                   chr(0x04) .
                   chr(($length >> 24) & 0xFF) .
                   chr(($length >> 16) & 0xFF) .
                   chr(($length >> 8) & 0xFF) .
                   chr($length & 0xFF);
    }

    return $retval . $value;
}

// Ruta hacia el fichero JPEG
$path = './phplogo.jpg';

// Define las etiquetas IPTC
$iptc = array(
    '2#120' => 'Test image',
    '2#116' => 'Copyright 2008-2009, The PHP Group'
);

// Conversión de las etiquetas IPTC a código binario
$data = '';

foreach($iptc as $tag => $string)
{
    $tag = substr($tag, 2);
    $data .= iptc_make_tag(2, $tag, $string);
}

// Incorporación de los datos IPTC
$content = iptcembed($data, $path);

// Escribe los datos de la nueva imagen en un fichero.
$fp = fopen($path, "wb");
fwrite($fp, $content);
fclose($fp);
?>

   
```php

## Notas

> [!NOTE]
> Esta función no requiere la biblioteca GD.
