---
title: strpbrk
description: Busca un conjunto de caracteres en un string
source_url: https://www.php.net/manual/es/function.strpbrk.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strpbrk.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89390
---

strpbrk

Busca un conjunto de caracteres en un string

## Descripción

```php
strpbrk(string $string, string $characters): string
```php

`strpbrk` busca el conjunto de caracteres `characters` en el string `string`.

## Parámetros

`string`  
El string en el que se busca `characters`.

`characters`  
Este argumento distingue entre mayúsculas y minúsculas.

## Valores devueltos

Devuelve un string, comenzando en el primer carácter encontrado, o `false` si no se ha encontrado ninguno.

## Ejemplos

Ejemplo con `strpbrk`

```
<?php

$text = 'This is a Simple text.';

// Esto mostrará "is is a Simple text." porque 'i' coincide con el primero
echo strpbrk($text, 'mi'), PHP_EOL;

// Esto mostrará "Simple text." porque los caracteres distinguen mayúsculas y minúsculas
echo strpbrk($text, 'S'), PHP_EOL;
?>

    
```php

## Véase también

`strpos`, `strstr`, `preg_match`
