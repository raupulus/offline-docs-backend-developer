---
title: strpos
description: Busca la posición de la primera ocurrencia en un string
source_url: https://www.php.net/manual/es/function.strpos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strpos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 4b72b2351
order: 89400
---

strpos

Busca la posición de la primera ocurrencia en un string

## Descripción

```php
strpos(string $haystack, string $needle, [int $offset]): int
```php

Busca la posición numérica de la primera ocurrencia de `needle` en el `string` `haystack`.

## Parámetros

`haystack`  
El string en el que se debe buscar.

`needle`  
El string a buscar.

Anterior a PHP 8.0.0, si `needle` no es una cadena de caracteres, se convierte en un entero y se aplica como valor ordinal de un carácter. Este comportamiento está obsoleto a partir de PHP 7.3.0, y confiar en él está fuertemente desaconsejado. Dependiendo del comportamiento esperado, `needle` debe ser explícitamente convertido a una cadena de caracteres, o debe realizarse una llamada explícita a `chr`.

`offset`  
Si se especifica, la búsqueda comenzará a partir de este número de caracteres contados desde el inicio del string. Si este número es negativo, la búsqueda comenzará utilizando este número de caracteres pero comenzando desde el final del string.

## Valores devueltos

Devuelve la posición numérica de la ocurrencia en relación con el inicio del string `haystack` (independientemente del `offset`). Nótese también que la posición en el string comienza en `0`, y no en `1`.

Devuelve `false` si la ocurrencia no ha sido encontrada.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `needle` acepta ahora una cadena vacía. |
| 8.0.0 | Pasar un `int` como `needle` ya no está soportado. |
| 7.3.0 | Pasar un `int` como `before_needle` ha sido declarado obsoleto. |
| 7.1.0 | Se ha añadido soporte para números negativos en el parámetro `offset`. |

## Ejemplos

Con `===`

```
<?php
$mystring = 'abc';
$findme   = 'a';
$pos = strpos($mystring, $findme);

// Note nuestra utilización de ===.  == no funcionaría como esperado
// ya que la posición de 'a' es el carácter 0 (primero).
if ($pos === false) {
    echo "El string '$findme' no se encuentra en el string '$mystring'";
} else {
    echo "El string '$findme' ha sido encontrado en el string '$mystring'";
    echo " y comienza en la posición $pos";
}
?>

    
```php

Con !==

```
<?php
$mystring = 'abc';
$findme   = 'a';
$pos = strpos($mystring, $findme);

// Note nuestra utilización de !==.  != no funcionaría como esperado
// ya que la posición de 'a' es el carácter 0 (primero).
if ($pos !== false) {
    echo "El string '$findme' ha sido encontrado en el string '$mystring'";
    echo " y comienza en la posición $pos";
} else {
    echo "El string '$findme' no se encuentra en el string '$mystring'";
}
?>

    
```php

Utilizar un offset

```
<?php
// Podemos buscar el carácter, e ignorar todo lo que está antes del offset
$newstring = 'abcdef abcdef';
$pos = strpos($newstring, 'a', 1); // $pos = 7, no 0
echo $pos, PHP_EOL;
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`stripos`, `str_contains`, `str_ends_with`, `str_starts_with`, `strrpos`, `strripos`, `strstr`, `strpbrk`, `substr`, `preg_match`
