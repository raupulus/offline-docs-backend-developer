---
title: dir
description: Devuelve una instancia de la clase Directory
source_url: https://www.php.net/manual/es/function.dir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/dir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_reviewed: false
translation_revision: b0b19b661
order: 12030
---

dir

Devuelve una instancia de la clase Directory

## Descripción

```php
dir(string $directory, [resource $context]): Directory
```php

Un mecanismo pseudo-objeto permite la lectura de un directorio. El argumento `directory` es abierto.

## Parámetros

`directory`  
El directorio a abrir

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Devuelve una instancia de la clase `Directory` en caso de éxito, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `context` ahora es nullable. |

## Ejemplos

Ejemplo con `dir`

Observe cómo se verifica el valor de retorno de `Directory::read` en el siguiente ejemplo. Se comprueba si el valor es idéntico (igual y del mismo tipo que -- véase [operadores de comparación](#language.operators.comparison) para más detalles) `false` de lo contrario, cualquier entrada en el nombre se evaluaría a `false` causaría la interrupción del ciclo.

```
<?php
$d = dir("/etc/php5");
echo "Manejador : " . $d->handle . "\n";
echo "Ruta : " . $d->path . "\n";
while (false !== ($entry = $d->read())) {
   echo $entry."\n";
}
$d->close();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Manejador : Resource id #2
    Ruta : /etc/php5
    .
    ..
    apache
    cgi
    cli

## Notas

> [!NOTE]
> El orden en el que las entradas del directorio son devueltas con el método read depende del sistema.
