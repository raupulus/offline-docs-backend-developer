---
title: basename
description: Devuelve el nombre del componente final de una ruta
source_url: https://www.php.net/manual/es/function.basename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/basename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 88c1f8d6c
order: 23270
---

basename

Devuelve el nombre del componente final de una ruta

## Descripción

```php
basename(string $path, [string $suffix]): string
```php

Toma como argumento `path`, la ruta de un fichero o directorio y proporciona el nombre del último componente.

> [!NOTE]
> `basename` actúa de manera ingenua y no tiene conocimiento del sistema de archivos subyacente o de los componentes de una ruta tales como "`..`".

> [!CAUTION]
> `basename` es sensible a la configuración local, por lo que si la ruta contiene caracteres multioctetos, la configuración local adecuada debe ser establecida mediante la función `setlocale`. Si `path` contiene caracteres que son inválidos para la configuración local actual, el comportamiento de `basename` es indefinido.

## Parámetros

`path`  
Una ruta.

En Windows, los caracteres slash (`/`) y backslash (`\`) se utilizan como separadores de directorio. En otros sistemas operativos, solo el carácter slash (`/`) se utiliza.

`suffix`  
Si `suffix` es proporcionado, el sufijo también será eliminado.

## Valores devueltos

Devuelve el nombre base de la ruta `path` dada.

## Ejemplos

Ejemplo con `basename`

```
<?php
echo "1) ".basename("/etc/sudoers.d", ".d").PHP_EOL;
echo "2) ".basename("/etc/sudoers.d").PHP_EOL;
echo "3) ".basename("/etc/passwd").PHP_EOL;
echo "4) ".basename("/etc/").PHP_EOL;
echo "5) ".basename(".").PHP_EOL;
echo "6) ".basename("/");
?>

    
```php

El ejemplo anterior mostrará:

    1) sudoers
    2) sudoers.d
    3) passwd
    4) etc
    5) .
    6)

## Véase también

`dirname`, `pathinfo`
