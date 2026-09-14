---
title: stripos
description: Busca la posición de la primera ocurrencia en un string, sin distinguir
  mayúsculas de minúsculas
source_url: https://www.php.net/manual/es/function.stripos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/stripos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_revision: 4b72b2351
order: 89310
---

stripos

Busca la posición de la primera ocurrencia en un string, sin distinguir mayúsculas de minúsculas

## Descripción

```php
stripos(string $haystack, string $needle, [int $offset]): int
```php

Busca la posición numérica de la primera ocurrencia de `needle` en el string `haystack`.

A diferencia de la función `strpos`, `stripos` no distingue entre mayúsculas y minúsculas.

## Parámetros

`haystack`  
El string en el que se realiza la búsqueda.

`needle`  
El string a buscar.

Anterior a PHP 8.0.0, si `needle` no es una cadena de caracteres, se convierte en un entero y se aplica como valor ordinal de un carácter. Este comportamiento está obsoleto a partir de PHP 7.3.0, y confiar en él está fuertemente desaconsejado. Dependiendo del comportamiento esperado, `needle` debe ser explícitamente convertido a una cadena de caracteres, o debe realizarse una llamada explícita a `chr`.

`offset`  
Si se especifica, la búsqueda comenzará a partir de este número de caracteres, contados desde el inicio del string. Si la posición es negativa, la búsqueda comenzará utilizando este número de caracteres pero comenzando desde el final del string.

## Valores devueltos

Devuelve la posición de la primera ocurrencia en el string en relación con el inicio del string `haystack` (independientemente del offset). Asimismo, se debe tener en cuenta que la posición en el string comienza en 0, y no en 1.

Devuelve `false` si la ocurrencia no ha sido encontrada.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Errores/Excepciones

- Si `offset` es mayor que la longitud de `haystack`, se lanzará un `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El case folding ya no depende de la configuración local definida con `setlocale`. Solo se realizará el case folding ASCII. Los octetos no-ASCII serán comparados por su valor de octeto. |
| 8.0.0 | `needle` acepta ahora una cadena vacía. |
| 8.0.0 | Pasar un `int` como `needle` ya no está soportado. |
| 7.3.0 | Pasar un `int` como `before_needle` ha sido declarado obsoleto. |
| 7.1.0 | Se ha añadido soporte para números negativos en el parámetro `offset`. |

## Ejemplos

Ejemplo con `stripos`

```
<?php
$findme    = 'a';
$mystring1 = 'xyz';
$mystring2 = 'ABC';

$pos1 = stripos($mystring1, $findme);
$pos2 = stripos($mystring2, $findme);

// No, 'a' no forma parte de 'xyz'
if ($pos1 === false) {
    echo "El string '$findme' no ha sido encontrado en el string '$mystring1'", PHP_EOL;
}

// Observe el uso de !==. Un simple != no daría el resultado esperado
// ya que la letra 'a' está en la posición 0 (la primera).
if ($pos2 !== false) {
    echo "El string '$findme' ha sido encontrado en el string '$mystring2'", PHP_EOL;
    echo " en la posición $pos2";
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`mb_stripos`, `str_contains`, `str_ends_with`, `str_starts_with`, `strpos`, `strrpos`, `strripos`, `stristr`, `substr`, `str_ireplace`
