---
title: strtoupper
description: Devuelve una string en mayúsculas
source_url: https://www.php.net/manual/es/function.strtoupper.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strtoupper.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 54ff7bf8e
order: 89490
---

strtoupper

Devuelve una string en mayúsculas

## Descripción

```php
strtoupper(string $string): string
```php

`strtoupper` devuelve `string`, después de haber convertido todos los caracteres alfabéticos a mayúsculas.

Los bytes en el rango `"a"` (0x61) a `"z"` (0x7a) serán convertidos a su letra mayúscula correspondiente restando 32 a cada valor de byte.

Esto puede ser utilizado para convertir caracteres ASCII en strings codificadas con UTF-8, ya que los caracteres UTF-8 multibyte serán ignorados. Para convertir caracteres no ASCII multibyte, utilice la función `mb_strtoupper`.

## Parámetros

`string`  
La string de entrada.

## Valores devueltos

Devuelve la string en mayúsculas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | La conversión de la casilla ya no depende de la configuración local definida con `setlocale`. Solo se convertirán los caracteres ASCII. |

## Ejemplos

Ejemplo con `strtoupper`

```
<?php
$str = "Marie A un Petit Agneau, et l'aime fORt.";
$str = strtoupper($str);
echo $str; // MARIE A UN PETIT AGNEAU, ET L'AIME FORT.

// Nota: Très habría sido convertido en TRÈS
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`strtolower`, `ucfirst`, `ucwords`, `mb_strtoupper`
