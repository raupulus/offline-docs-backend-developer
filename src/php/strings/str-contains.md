---
title: str_contains
description: Determina si una cadena contiene un substring dado
source_url: https://www.php.net/manual/es/function.str-contains.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-contains.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 9737e4b25
order: 89100
---

str_contains

Determina si una cadena contiene un substring dado

## Descripción

```php
str_contains(string $haystack, string $needle): bool
```php

Realiza una verificación sensible a mayúsculas y minúsculas para indicar si `needle` (aguja) está contenida en `haystack` (pajar).

## Parámetros

`haystack`  
El string en el que se realiza la búsqueda.

`needle`  
El substring a buscar en `haystack`.

## Valores devueltos

Devuelve `true` si `needle` está en `haystack`, de lo contrario `false`.

## Ejemplos

Con un string vacío `''`

```
<?php
if (str_contains('abc', '')) {
    echo "Verificar la existencia de la cadena vacía siempre devolverá true";
}
?>

    
```php

El ejemplo anterior mostrará:

```
Verificar la existencia de la cadena vacía siempre devolverá true

    
```php

Demostración de la sensibilidad a mayúsculas y minúsculas

```
<?php
$string = 'The lazy fox jumped over the fence';

if (str_contains($string, 'lazy')) {
    echo "La cadena 'lazy' fue encontrada en la cadena\n";
}

if (str_contains($string, 'Lazy')) {
    echo 'La cadena "Lazy" fue encontrada en la cadena';
} else {
    echo '"Lazy" no fue encontrada porque las mayúsculas y minúsculas no coinciden';
}

?>

    
```php

El ejemplo anterior mostrará:

```
La cadena 'lazy' fue encontrada en la cadena
"Lazy" no fue encontrada porque las mayúsculas y minúsculas no coinciden

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`str_ends_with`, `str_starts_with`, `stripos`, `strrpos`, `strripos`, `strstr`, `strpbrk`, `substr`, `preg_match`
