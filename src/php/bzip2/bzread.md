---
title: bzread
description: Lectura binaria de un archivo bzip2
source_url: https://www.php.net/manual/es/function.bzread.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzread.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_reviewed: true
translation_revision: 5fdeb11b1
order: 6480
---

bzread

Lectura binaria de un archivo bzip2

## Descripción

```php
bzread(resource $bz, [int $length]): string
```php

`bzread` lee desde el puntero de archivo bzip2 dado.

La lectura se detiene cuando `length` (no comprimido) caracteres han sido leídos o si se alcanza el final del archivo, el primero de los dos que ocurra.

## Parámetros

`bz`  
El puntero de archivo. Debe ser válido y debe apuntar a un archivo abierto correctamente por la función `bzopen`.

`length`  
Si no se especifica, `bzread` leerá 1024 (no comprimidos) caracteres a la vez. Un máximo de 8192 caracteres no comprimidos serán leídos a la vez.

## Valores devueltos

Devuelve los datos no comprimidos o `false` si ocurre un error.

## Ejemplos

Ejemplo con `bzread`

```
<?php

$file = "/tmp/foo.bz2";
$bz = bzopen($file, "r") or die("Imposible abrir el archivo $file");

$decompressed_file = '';
while (!feof($bz)) {
  $decompressed_file .= bzread($bz, 4096);
}
bzclose($bz);

echo "El contenido del archivo $file es : <br />\n";
echo $decompressed_file;

?>

   
```php

## Véase también

bzwrite

feof

bzopen
