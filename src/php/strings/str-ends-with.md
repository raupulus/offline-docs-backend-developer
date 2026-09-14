---
title: str_ends_with
description: Determina si una cadena termina con un substring dado
source_url: https://www.php.net/manual/es/function.str-ends-with.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-ends-with.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 1bf3ed99f
order: 89120
---

str_ends_with

Determina si una cadena termina con un substring dado

## Descripción

```php
str_ends_with(string $haystack, string $needle): bool
```php

Realiza una verificación sensible a mayúsculas y minúsculas que indica si `haystack` (pajar) termina con `needle` (aguja).

## Parámetros

`haystack`  
El string en la que se realiza la búsqueda.

`needle`  
El substring a buscar en `haystack`.

## Valores devueltos

Devuelve `true` si `haystack` termina con `needle`, de lo contrario `false`.

## Ejemplos

Con un string vacío `''`

```
<?php
if (str_ends_with('abc', '')) {
    echo "Todas las cadenas terminan con la cadena vacía";
}
?>

    
```php

El ejemplo anterior mostrará:

```
Todas las cadenas terminan con la cadena vacía

    
```php

Demostración de la sensibilidad a mayúsculas y minúsculas

```
<?php
$string = 'The lazy fox jumped over the fence';

if (str_ends_with($string, 'fence')) {
    echo "La cadena termina con 'fence'\n";
}

if (str_ends_with($string, 'Fence')) {
    echo 'La cadena termina con "Fence"';
} else {
    echo '"Fence" no fue encontrado porque las mayúsculas y minúsculas no coinciden';
}

?>

    
```php

El ejemplo anterior mostrará:

```
La cadena termina con 'fence'
"Fence" no fue encontrado porque las mayúsculas y minúsculas no coinciden

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`str_contains`, `str_starts_with`, `stripos`, `strrpos`, `strripos`, `strstr`, `strpbrk`, `substr`, `preg_match`
