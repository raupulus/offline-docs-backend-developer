---
title: realpath
description: Retorna la ruta de acceso canónica absoluta
source_url: https://www.php.net/manual/es/function.realpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/realpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23980
---

realpath

Retorna la ruta de acceso canónica absoluta

## Descripción

```php
realpath(string $path): string
```php

`realpath` resuelve todos los enlaces simbólicos, y reemplaza todas las referencias `/./`, `/../` y `/` de `path` luego retorna la ruta de acceso canónica absoluta así encontrada.

## Parámetros

`path`  
La ruta de acceso a verificar.

> [!NOTE]
> Debe ser proporcionada una ruta de acceso, el valor puede ser una cadena de caracteres vacía. En estos casos, el valor es interpretado como el directorio actual.

## Valores devueltos

Retorna la ruta de acceso canónica absoluta así encontrada. El resultado no contiene ningún enlace simbólico, `/./` o `/../`. Los delimitadores de fin como `\` y `/` son igualmente eliminados.

`realpath` retorna `false` si ocurre un error, por ejemplo si el fichero no existe.

> [!NOTE]
> El script que se ejecuta debe tener los permisos de ejecución sobre todos los directorios de la estructura, de lo contrario, la función `realpath` retornará `false`.

> [!NOTE]
> Para los sistemas de archivos insensibles a mayúsculas/minúsculas, `realpath` puede o no normalizar la casilla de los caracteres.

> [!NOTE]
> La función `realpath` no funcionará para un fichero que se encuentra dentro de un phar ya que esta ruta sería una ruta de acceso virtual, no una real.

> [!NOTE]
> En Windows, las uniones y los enlaces simbólicos a los directorios son únicamente extendidos a un nivel.

> [!NOTE]
> Como el tipo entero de PHP es firmado y que muchas plataformas utilizan enteros de 32 bits, algunas funciones relacionadas con el sistema de archivos pueden retornar resultados extraños para ficheros de tamaño superior a 2 Go.

## Ejemplos

Ejemplo con `realpath`

```
<?php
chdir('/var/www/');
echo realpath('./../../etc/passwd') . PHP_EOL;

echo realpath('/tmp/') . PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    /etc/passwd
    /tmp

Ejemplo con `realpath` en Windows

En Windows, `realpath` cambiará las rutas de estilo Unix a rutas de estilo Windows.

```
<?php
echo realpath('/windows/system32'), PHP_EOL;

echo realpath('C:\Program Files\\'), PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    C:\WINDOWS\System32
    C:\Program Files

## Véase también

`basename`, `dirname`, `pathinfo`
