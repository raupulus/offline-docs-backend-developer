---
title: nl2br
description: Inserta un salto de línea HTML en cada nueva línea
source_url: https://www.php.net/manual/es/function.nl2br.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/nl2br.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 88930
---

nl2br

Inserta un salto de línea HTML en cada nueva línea

## Descripción

```php
nl2br(string $string, [bool $use_xhtml]): string
```php

Devuelve `string` después de insertar `<br />` o `<br>` antes de todas las nuevas líneas (`\r\n`, `\n\r`, `\n` y `\r`).

## Parámetros

`string`  
El string de entrada.

`use_xhtml`  
Produce saltos de línea compatibles con XHTML o no.

## Valores devueltos

Devuelve el string modificado.

## Ejemplos

Ejemplo con `nl2br`

```
<?php
echo nl2br("foo isn't\n bar");
?>

    
```php

El ejemplo anterior mostrará:

    foo isn't<br />
     bar

Generación de código HTML válido con el argumento `use_xhtml`

```
<?php
echo nl2br("Welcome\r\nThis is my HTML document", false);
?>

    
```php

El ejemplo anterior mostrará:

    Welcome<br>
    This is my HTML document

Diversos separadores de nuevas líneas

```
<?php
$string = "Ceci\r\nest\n\rune\nchaîne\r";
echo nl2br($string);
?>

    
```php

El ejemplo anterior mostrará:

    Ceci<br />
    est<br />
    une<br />
    chaîne<br />

## Véase también

`htmlspecialchars`, `htmlentities`, `wordwrap`, `str_replace`
