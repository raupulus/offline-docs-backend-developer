---
title: mailparse_uudecode_all
description: Procesa los datos desde un apuntador a archivo y extrae cada archivo
  embebido con codificación uu
source_url: https://www.php.net/manual/es/function.mailparse-uudecode-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-uudecode-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_revision: 01bd007b0
order: 44440
---

mailparse_uudecode_all

Procesa los datos desde un apuntador a archivo y extrae cada archivo embebido con codificación uu

## Descripción

```php
mailparse_uudecode_all(resource $fp): array
```php

Lee los datos del apuntador de archivo dado y extrae cada archivo codificado mediante uuencode embebido en un archivo temporal.

## Parámetros

`fp`  
Un apuntador de archivo válido.

## Valores devueltos

Devuelve una matriz de matrices asociativas, listando la información de cada archivo.

|  |  |
|----|----|
| `filename` | Ruta al nombre de archivo temporal creado |
| `origfilename` | El nombre de archivo original, solo para partes codificadas mediante uuencode |

La primera entrada es el cuerpo del mensaje. Las siguientes son los archivos uuencode decodificados.

## Ejemplos

Ejemplo de `mailparse_uudecode_all`

```
<?php

$texto = <<<EOD
To: fred@example.com

hola, esto es un texto cualquiera.
bla bla bla.

begin 644 test.txt
/=&AI<R!I<R!A('1E<W0*
`
end

EOD;

$aa = tmpfile();
fwrite($aa, $texto);

$datos = mailparse_uudecode_all($aa);

echo "CUERPO\n";
readfile($datos[0]["filename"]);
echo "UUE ({$datos[1]['origfilename']})\n";
readfile($datos[1]["filename"]);

// Limpiar
unlink($datos[0]["filename"]);
unlink($datos[1]["filename"]);

?>

   
```php

El ejemplo anterior mostrará:

    CUERPO
    To: fred@example.com

    hola, esto es un texto cualquiera.
    bla bla bla.

    UUE (test.txt)
    this is a test
