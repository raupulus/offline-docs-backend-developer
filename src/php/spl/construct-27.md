---
title: SplTempFileObject::__construct
description: Construir un nuevo objeto de fichero temporal
source_url: https://www.php.net/manual/es/spltempfileobject.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/spltempfileobject/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 85530
---

SplTempFileObject::\_\_construct

Construir un nuevo objeto de fichero temporal

## Descripción

```php
public SplTempFileObject::__construct([int $maxMemory])
```php

Construir un nuevo objeto de fichero temporal.

## Parámetros

`maxMemory`  
La cantidad máxima de memoria (en bytes, por omisión es 2 MB) para el fichero temporal a usar. Su el fichero temporal supera este tamaño, Este será movido a un archivo en el directorio temporal del sistema.

Si `maxMemory` es negativo, se usará memoria. Si `maxMemory` es cero, no se usará memoria.

## Errores/Excepciones

Lanza una `RuntimeException` si un error ocurre.

## Ejemplos

Ejemplo de SplTempFileObject

Este ejemplo escribe un fichero temporal en la memoria mientras se puede escribir y leer en este.

```
<?php
$temp = new SplTempFileObject();
$temp->fwrite("Esta es la primera línea\n");
$temp->fwrite("Y esta es la segunda.\n");
echo "Escrito " . $temp->ftell() . " bytes al fichero temporal.\n\n";

// Rebobina y lee lo que fué escrito
$temp->rewind();
foreach ($temp as $line) {
    echo $line;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Escrito 47 bytes al fichero temporal.

    Esta es la primera línea
    Y esta es la segunda.

## Véase también

`SplFileObject`, [PHP input/output streams](#wrappers.php) (para `php://temp` y `php://memory`)
