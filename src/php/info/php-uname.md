---
title: php_uname
description: Devuelve información sobre el sistema operativo
source_url: https://www.php.net/manual/es/function.php-uname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/php-uname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 03db4883c
order: 39150
---

php_uname

Devuelve información sobre el sistema operativo

## Descripción

```php
php_uname([string $mode]): string
```php

`php_uname` devuelve una descripción del sistema operativo en el que se ejecuta PHP. Es la misma cadena que se ve al principio de `phpinfo`. Si solo se desea conocer el nombre del sistema operativo, puede utilizarse la constante `PHP_OS`, pero debe tenerse en cuenta que esta constante contiene el nombre del sistema en el que PHP fue *compilado*.

En algunas antiguas plataformas Unix, no es posible determinar las informaciones corrientes del SO, en cuyo caso esta función se limita a devolver el nombre del SO en el que PHP fue compilado. Esto solo ocurrirá si la biblioteca `uname()` no existe o no funciona.

## Parámetros

`mode`  
`mode` es un solo carácter que define qué información se devolverá:

- `'a'`: Este es el valor por omisión. Devuelve las mismas informaciones que los modos individuales `'s'`, `'n'`, `'r'`, `'v'`, `'m'` separadas por espacios.

- `'s'`: nombre del sistema operativo. Por ejemplo, `FreeBSD`.

- `'n'`: nombre del host. Por ejemplo, `localhost.example.com`.

- `'r'`: nombre de la versión. Por ejemplo, `5.1.2-RELEASE`.

- `'v'`: información sobre la versión. Varía enormemente según el sistema operativo.

- `'m'`: tipo de máquina. Por ejemplo, `i386`.

## Valores devueltos

Devuelve la descripción, en forma de `string`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Levanta una excepción `ValueError` cuando se especifica un `mode` inválido. |

## Ejemplos

Ejemplos con `php_uname`

```
<?php
echo php_uname();
echo PHP_OS;

/* Salidas posibles:
Linux localhost 2.4.21-0.13mdk #1 Fri Mar 14 15:08:06 EST 2003 i686
Linux

FreeBSD localhost 3.2-RELEASE #15: Mon Dec 17 08:46:02 GMT 2001
FreeBSD

Windows NT XN1 5.1 build 2600
WINNT
*/

if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
    echo 'El servidor se ejecuta en Windows !';
} else {
    echo 'El servidor no se ejecuta en Windows !';
}

?>

    
```php

Existen también algunas [constantes PHP predefinidas](#language.constants.predefined) relacionadas que pueden resultar útiles, por ejemplo:

Ejemplos con algunas constantes relacionadas con el sistema

```
<?php
// *nix
echo DIRECTORY_SEPARATOR; // /
echo PHP_SHLIB_SUFFIX;    // so
echo PATH_SEPARATOR;      // :

// Win*
echo DIRECTORY_SEPARATOR; // \
echo PHP_SHLIB_SUFFIX;    // dll
echo PATH_SEPARATOR;      // ;
?>

    
```php

## Véase también

`phpversion`, `php_sapi_name`, `phpinfo`
