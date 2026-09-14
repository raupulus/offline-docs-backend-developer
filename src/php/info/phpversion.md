---
title: phpversion
description: Devuelve el número de la versión actual de PHP
source_url: https://www.php.net/manual/es/function.phpversion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/phpversion.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 39180
---

phpversion

Devuelve el número de la versión actual de PHP

## Descripción

```php
phpversion([string $extension]): string
```php

Devuelve el número de la versión actual de PHP.

## Parámetros

`extension`  
Un nombre de extensión, opcional.

## Valores devueltos

Devuelve la versión actual de PHP como un `string`. Si se proporciona un argumento `string` al parámetro `extension`, `phpversion` devuelve la versión de esta extensión, o `false` si no hay información de versión asociada o esta extensión no está activada.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `extension` ahora es nullable. |

## Ejemplos

Ejemplo con `phpversion`

```
<?php

// muestra el número de versión actual de PHP.
echo 'Versión actual de PHP: ' . phpversion();

// muestra por ejemplo '1.22.3' o nada si esta extensión no está activa
echo phpversion('tidy');
?>

    
```php

Ejemplo con `PHP_VERSION_ID`

```
<?php

/**
 * PHP_VERSION_ID se define como un número, donde a mayor número,
 * más reciente es la versión de PHP utilizada. Se define como en
 * la expresión anterior:
 *
 * $version_id = $major_version * 10000 + $minor_version * 100 + $release_version;
 *
 * Ahora, con PHP_VERSION_ID, se pueden verificar las funcionalidades
 * que esta versión de PHP puede tener, lo que evita usar version_compare()
 * cada vez que se verifica si la versión actual de PHP puede no
 * soportar una funcionalidad.
 *
 * Por ejemplo, aquí se pueden definir las constantes PHP_*_VERSION que no
 * están disponibles en versiones a partir de 5.2.7.
 */

if (PHP_VERSION_ID < 50207) {
    define('PHP_MAJOR_VERSION',   $version[0]);
    define('PHP_MINOR_VERSION',   $version[1]);
    define('PHP_RELEASE_VERSION', $version[2]);

    // etc.

}

?>

    
```php

## Notas

> [!NOTE]
> Esta información también está disponible a través de la constante predefinida `PHP_VERSION`. Más información sobre versiones, con las constantes `PHP_VERSION_*`.

> [!NOTE]
> Algunas extensiones pueden definir su propio número de versión. Sin embargo, la mayoría de las extensiones incluidas utilizarán la versión de PHP como número de versión.

## Véase también

[las constantes PHP_VERSION](#reserved.constants.core), `version_compare`, `phpinfo`, `phpcredits`, `zend_version`
