---
title: addslashes
description: Añade barras invertidas en un string
source_url: https://www.php.net/manual/es/function.addslashes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/addslashes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 45042fef6
order: 88600
---

addslashes

Añade barras invertidas en un string

## Descripción

```php
addslashes(string $string): string
```php

Devuelve el string `str` después de haber escapado todos los caracteres que deben serlo. Estos caracteres son: comillas simples (`'`), comillas dobles (`"`), barra invertida (`\`), NUL (el byte NUL)

Un caso de uso de `addslashes` es escapar los caracteres mencionados en un string que debe ser evaluada por PHP:

Caracteres de escape

```
<?php
$str = "O'Reilly?";
eval("echo '" . addslashes($str) . "';");
?>

    
```php

`addslashes` es a veces utilizado incorrectamente para prevenir las [Inyecciones SQL](#security.database.sql-injection). En su lugar, las funciones de escape específicas de la base de datos y/o las declaraciones preparadas deberían ser utilizadas.

## Parámetros

`string`  
El string a escapar.

## Valores devueltos

Devuelve el string escapada.

## Ejemplos

Ejemplo con `addslashes`

```
<?php
$str = "¿Su nombre es O'reilly?";

// Muestra: ¿Su nombre es O\'reilly?
echo addslashes($str);
?>

    
```php

## Véase también

`stripcslashes`, `stripslashes`, `addcslashes`, `htmlspecialchars`, `quotemeta`, `get_magic_quotes_gpc`
