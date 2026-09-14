---
title: strrchr
description: Encuentra la última ocurrencia de un carácter en un string
source_url: https://www.php.net/manual/es/function.strrchr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strrchr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 654ee5c8a
order: 89410
---

strrchr

Encuentra la última ocurrencia de un carácter en un string

## Descripción

```php
strrchr(string $haystack, string $needle, [bool $before_needle]): string
```php

Retorna el segmento del string `haystack` que comienza con la última ocurrencia de `needle`, hasta el final del string `haystack`.

## Parámetros

`haystack`  
El string en el que se debe buscar.

`needle`  
Si `needle` contiene más de un carácter, solo se utilizará el primero. Este comportamiento es diferente al de `strchr`.

Anterior a PHP 8.0.0, si `needle` no es una cadena de caracteres, se convierte en un entero y se aplica como valor ordinal de un carácter. Este comportamiento está obsoleto a partir de PHP 7.3.0, y confiar en él está fuertemente desaconsejado. Dependiendo del comportamiento esperado, `needle` debe ser explícitamente convertido a una cadena de caracteres, o debe realizarse una llamada explícita a `chr`.

`before_needle`  
Si `true`, `strrchr` retorna la parte del `haystack` antes de la última ocurrencia de `needle` (excluyendo esta última).

## Valores devueltos

Retorna la porción del string, o `false` si `needle` no es encontrado.

## Historial de cambios

| Versión | Descripción                                                     |
|---------|-----------------------------------------------------------------|
| 8.3.0   | El parámetro `before_needle` ha sido añadido.                   |
| 8.0.0   | `needle` acepta ahora una cadena vacía.                         |
| 8.0.0   | Pasar un `int` como `needle` ya no está soportado.              |
| 7.3.0   | Pasar un `int` como `before_needle` ha sido declarado obsoleto. |

## Ejemplos

Ejemplo con `strrchr`

```
<?php
$ext = strrchr('somefile.txt', '.');
echo "extensión de fichero: $ext \n";
$ext = $ext ? strtolower(substr($ext, 1)) : '';
echo "extensión de fichero: $ext";
?>

    
```php

Resultado del ejemplo anterior es similar a:

    extensión de fichero: .txt
    extensión de fichero: txt

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`strstr`, `strrpos`
