---
title: str_starts_with
description: Determina si un string comienza con un substring dado
source_url: https://www.php.net/manual/es/function.str-starts-with.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-starts-with.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 9737e4b25
order: 89220
---

str_starts_with

Determina si un string comienza con un substring dado

## Descripción

```php
str_starts_with(string $haystack, string $needle): bool
```php

Realiza una verificación sensible a mayúsculas y minúsculas que indica si `haystack` (pajar) comienza con `needle` (aguja).

## Parámetros

`haystack`  
El string en la que se realiza la búsqueda.

`needle`  
El substring a buscar en `haystack`.

## Valores devueltos

Devuelve `true` si `haystack` comienza con `needle`, de lo contrario `false`.

## Ejemplos

Con un string vacío `''`

```
<?php
if (str_starts_with('abc', '')) {
    echo "Todas los strings comienzan con el string vacía";
}
?>

    
```php

El ejemplo anterior mostrará:

```
Todas los strings comienzan con el string vacía

    
```php

Demostración de la sensibilidad a mayúsculas y minúsculas

```
<?php
$string = 'The lazy fox jumped over the fence';

if (str_starts_with($string, 'The')) {
    echo "El string comienza con 'The'\n";
}

if (str_starts_with($string, 'the')) {
    echo 'El string comienza con "the"';
} else {
    echo '"the" no fue encontrado porque las mayúsculas y minúsculas no coinciden';
}

?>

    
```php

El ejemplo anterior mostrará:

```
El string comienza con 'The'
"the" no fue encontrado porque las mayúsculas y minúsculas no coinciden

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`str_contains`, `str_ends_with`, `stripos`, `strrpos`, `strripos`, `strstr`, `strpbrk`, `substr`, `preg_match`
