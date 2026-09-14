---
title: Ejemplos
source_url: https://www.php.net/manual/es/zlib.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: eec6a4a36
order: 108700
---

## Ejemplos

Este ejemplo abre un archivo temporal y escribe una cadena de prueba en él, entonces muestra el contenido de este archivo dos veces.

Pequeño Ejemplo de Zlib

```php
<?php

$filename = tempnam('/tmp', 'zlibtest') . '.gz';
echo "<html>\n<head></head>\n<body>\n<pre>\n";
$s = "Sólo una prueba, prueba, prueba, prueba, prueba, prueba!\n";

// abre el archivo para escribir con compresión máxima
$zp = gzopen($filename, "w9");

// escribe la cadena en el archivo
gzwrite($zp, $s);

// cierra el archivo
gzclose($zp);

// abre el archivo para lectura
$zp = gzopen($filename, "r");

// lee el tercer carácter
echo gzread($zp, 3);

// salida hasta el fin del archivo y lo cierra
gzpassthru($zp);
gzclose($zp);

echo "\n";

// abre el archivo y muestra el contenido (por segunda vez).
if (readgzfile($filename) != strlen($s)) {
        echo "Error con funciones de zlib!";
}
unlink($filename);
echo "</pre>\n</body>\n</html>\n";

?>

  
```

Trabajando con la API de compresión y descompresión increemental

```php
<?php
// Perform GZIP compression:
$deflateContext = deflate_init(ZLIB_ENCODING_GZIP);
$compressed = deflate_add($deflateContext, "Data to compress", ZLIB_NO_FLUSH);
$compressed .= deflate_add($deflateContext, ", more data", ZLIB_NO_FLUSH);
$compressed .= deflate_add($deflateContext, ", and even more data!", ZLIB_FINISH);

// Perform GZIP decompression:
$inflateContext = inflate_init(ZLIB_ENCODING_GZIP);
$uncompressed = inflate_add($inflateContext, $compressed, ZLIB_NO_FLUSH);
$uncompressed .= inflate_add($inflateContext, NULL, ZLIB_FINISH);
echo $uncompressed;
?>

  
```

El ejemplo anterior mostrará:

    Data to compress, more data, and even more data!
