---
title: Ejemplos
source_url: https://www.php.net/manual/es/bzip2.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_revision: 5fdeb11b1
order: 6390
---

## Ejemplos

Este ejemplo abre un fichero temporal y escribe una cadena de prueba en el, muestra el contenido del fichero.

Pequeño ejemplo de bzip2

```php
<?php

$filename = "/tmp/testfile.bz2";
$str = "Esto es una cadena de prueba.\n";

// Abriendo fichero para escribir
$bz = bzopen($filename, "w");

// escribe la cadena en el fichero
bzwrite($bz, $str);

// cierra el fichero
bzclose($bz);

// abre el fichero para escritura
$bz = bzopen($filename, "r");

// lee 10 caracteres
echo bzread($bz, 10);

// muestra salida hasta el final del fichero (o los siguientes 1024 caracteres) y lo cierra.
echo bzread($bz);

bzclose($bz);

?>

  
```
