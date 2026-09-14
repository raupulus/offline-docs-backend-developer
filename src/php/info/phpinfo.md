---
title: phpinfo
description: Muestra numerosas informaciones sobre la configuración de PHP
source_url: https://www.php.net/manual/es/function.phpinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/phpinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: f78180344
order: 39170
---

phpinfo

Muestra numerosas informaciones sobre la configuración de PHP

## Descripción

```php
phpinfo([int $flags]): true
```php

Muestra numerosas informaciones sobre PHP, relativas a su configuración actual: opciones de compilación, extensiones, versión, informaciones sobre el servidor, y el entorno (cuando es compilado como módulo), entorno PHP, informaciones sobre el sistema, rutas, valores generales y locales de configuración, encabezados HTTP y la licencia PHP.

Como todos los sistemas están configurados de manera diferente, `phpinfo` sirve generalmente para verificar la [configuración](#configuration) así como las [variables predefinidas](#language.variables.predefined), para una plataforma dada.

`phpinfo` es una buena herramienta de depuración, ya que muestra el contenido de todas las variables EGPCS (Entorno, GET, POST, Cookie, Servidor).

## Parámetros

`flags`  
La visualización puede ser personalizada utilizando una o varias de las *constantes siguientes*. Estas son combinables con el [operador a nivel de bits](#language.operators.bitwise), y deben ser pasadas en el argumento `flags`. También se pueden sumar estas constantes.

| Nombre de la constante | Valor | Descripción |
|----|----|----|
| INFO_GENERAL | 1 | La línea de configuración, la ruta del `php.ini`, la fecha de compilación, el servidor web, el sistema, etc. |
| INFO_CREDITS | 2 | Los créditos de PHP. Ver también `phpcredits`. |
| INFO_CONFIGURATION | 4 | Valores actuales locales y generales de las directivas PHP. Ver también la función `ini_get`. |
| INFO_MODULES | 8 | Módulos cargados y su configuración específica. Ver también la función `get_loaded_extensions`. |
| INFO_ENVIRONMENT | 16 | Informaciones sobre las variables de entorno, que están disponibles en la variable `$_ENV`. |
| INFO_VARIABLES | 32 | Muestra todas las [variables predefinidas](#language.variables.predefined), provenientes del entorno, el método GET, el método POST, las cookies y el servidor. |
| INFO_LICENSE | 64 | La licencia PHP. Ver también [la FAQ de la licencia](https://www.php.net/license/). |
| INFO_ALL | -1 | Muestra todas las informaciones mencionadas. |

Opciones de `phpinfo`

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo con `phpinfo`

```
<?php

// Muestra todas las informaciones, como lo haría INFO_ALL
phpinfo();

// Muestra únicamente el módulo de información.
// phpinfo(8) proporcionaría las mismas informaciones.
phpinfo(INFO_MODULES);

?>

    
```php

## Notas

> [!NOTE]
> En las versiones anteriores a PHP 5.5, parte de las informaciones mostradas están desactivadas si la directiva [expose_php](#ini.expose-php) está configurada con el valor `off`. Esto incluye los logos PHP y Zend, así como los créditos.

> [!NOTE]
> `phpinfo` muestra texto en lugar de HTML cuando se utiliza la versión CLI.

## Véase también

`phpversion`, `phpcredits`, `ini_get`, `ini_set`, `get_loaded_extensions`, [las variables predefinidas](#language.variables.predefined)
