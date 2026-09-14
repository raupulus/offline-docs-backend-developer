---
title: fileperms
description: Lee los permisos de un fichero
source_url: https://www.php.net/manual/es/function.fileperms.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fileperms.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23560
---

fileperms

Lee los permisos de un fichero

## Descripción

```php
fileperms(string $filename): int
```php

Lee los permisos del fichero dado.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve los permisos del fichero en formato numérico. Los bits de menor peso son los mismos que los de los permisos en `chmod`, sin embargo algunas plataformas incluyen en el retorno información sobre el tipo de fichero dado en `filename`. Los ejemplos siguientes muestran cómo probar el valor de retorno en cuanto a los permisos y el tipo de fichero en sistemas POSIX como Linux o macOS.

Para ficheros locales, se utiliza el valor específico `st_mode` de la estructura C devuelta por la función `stat`. Los bits afectados pueden cambiar según la plataforma y se debe investigar al respecto si se deben analizar los bits que no concernen a la permisión.

Devuelve `false` en caso de error.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Mostrar los permisos en valor octal

```
<?php
echo substr(sprintf('%o', fileperms('/tmp')), -4);
echo substr(sprintf('%o', fileperms('/etc/passwd')), -4);
?>

    
```php

El ejemplo anterior mostrará:

    1777
    0644

Mostrar todos los permisos

```
<?php
$perms = fileperms('/etc/passwd');

switch ($perms & 0xF000) {
    case 0xC000: // Socket
        $info = 's';
        break;
    case 0xA000: // Enlace simbólico
        $info = 'l';
        break;
    case 0x8000: // Regular
        $info = 'r';
        break;
    case 0x6000: // Especial de bloque
        $info = 'b';
        break;
    case 0x4000: // Directorio
        $info = 'd';
        break;
    case 0x2000: // Especial de carácter
        $info = 'c';
        break;
    case 0x1000: // Pipe FIFO
        $info = 'p';
        break;
    default: // Desconocido
        $info = 'u';
}

// Propietario
$info .= (($perms & 0x0100) ? 'r' : '-');
$info .= (($perms & 0x0080) ? 'w' : '-');
$info .= (($perms & 0x0040) ?
            (($perms & 0x0800) ? 's' : 'x' ) :
            (($perms & 0x0800) ? 'S' : '-'));

// Grupo
$info .= (($perms & 0x0020) ? 'r' : '-');
$info .= (($perms & 0x0010) ? 'w' : '-');
$info .= (($perms & 0x0008) ?
            (($perms & 0x0400) ? 's' : 'x' ) :
            (($perms & 0x0400) ? 'S' : '-'));

// Todos
$info .= (($perms & 0x0004) ? 'r' : '-');
$info .= (($perms & 0x0002) ? 'w' : '-');
$info .= (($perms & 0x0001) ?
            (($perms & 0x0200) ? 't' : 'x' ) :
            (($perms & 0x0200) ? 'T' : '-'));

echo $info;
?>

    
```php

El ejemplo anterior mostrará:

    -rw-r--r--

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`chmod`, `is_readable`, `stat`
