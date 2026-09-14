---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration83.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration83/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 4de6272a1
order: 1040
---

## Nuevas características

## Núcleo de PHP

### Modificación de solo lectura

Las clases anónimas ahora pueden marcarse como de solo lectura.

Las propiedades de solo lectura ahora pueden restablecerse durante la clonación.

### Constantes de clase tipificadas

Las constantes de clase, interfaz, rasgo y enumeración ahora admiten declaraciones de tipo.

### Cierres creados a partir de métodos mágicos

Los cierres creados a partir de métodos mágicos ahora pueden aceptar argumentos nombrados.

### El modificador final con un método de un rasgo

El modificador final ahora puede usarse al usar un método de un rasgo.

### El atributo Override

Se añadió el atributo \#\[\Override\] para verificar que un método existe en una clase padre o una interfaz implementada.

### Sintaxis de recuperación de constante de clase dinámicamente

Las constantes de clase ahora pueden accederse dinámicamente usando la sintaxis `C::{$name}`.

### Inicializadores de variables estáticas

Los inicializadores de variables estáticas ahora pueden contener expresiones arbitrarias.

### Sintaxis de valor de respaldo para variables ini

php.ini ahora soporta la sintaxis de valor de respaldo/valor por defecto.

```php
<?php
/*
/path/to/user.ini contiene el siguiente parámetro:

listen = localhost:${DRUPAL_FPM_PORT:-9000}
*/

$user_ini = parse_ini_file('/path/to/user.ini');
echo $user_ini['listen']; // localhost:9000

     
```

## CLI

Ahora es posible hacer linting de múltiples archivos.

## DOM

Se añadieron las propiedades DOMElement::\$className y DOMElement::\$id. Estas propiedades no son binarias en este momento debido a las limitaciones subyacentes de libxml2. Esto significa que los valores de las propiedades se truncarán a un byte NULO.

Se añadieron las propiedades DOMNode::\$isConnected y DOMNameSpaceNode::\$isConnected.

Se añadieron las propiedades DOMNode::\$parentElement y DOMNameSpaceNode::\$parentElement.

## FFI

Ahora es posible asignar `FFI\CData` a otros FFI\CData. Esto significa que los CData ahora pueden asignarse a estructuras y campos.

## Opcache

`opcache_get_status()['scripts'][n]['revalidate']` ahora contiene un timestamp Unix indicando cuándo se espera la próxima revalidación del timestamp de los scripts, dictada por la directiva INI [opcache.revalidate_freq](#ini.opcache.revalidate-freq).

## POSIX

`posix_getrlimit` ahora toma un argumento opcional `resource` para permitir la recuperación de un solo límite de recurso.

`posix_isatty` ahora lanza advertencias de tipo para enteros siguiendo la semántica ZPP habitual.

`posix_ttyname` ahora lanza advertencias de tipo para enteros siguiendo la semántica ZPP habitual y advertencias de valor para enteros de descriptor de archivo inválidos.

## Streams

Los streams ahora pueden emitir la notificación `STREAM_NOTIFY_COMPLETED`. Esto no estaba implementado anteriormente.
