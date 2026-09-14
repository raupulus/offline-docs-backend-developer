---
title: variant_cmp
description: Compara dos variantes
source_url: https://www.php.net/manual/es/function.variant-cmp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-cmp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 7790
---

variant_cmp

Compara dos variantes

## Descripción

```php
variant_cmp(mixed $left, mixed $right, [int $locale_id], [int $flags]): int
```php

Compara `left` con `right`.

Esta función solo comparará valores escalares, no arrays ni registros variantes.

## Parámetros

`left`  
El operando de la izquierda.

`right`  
El operando de la derecha.

`locale_id`  
Identificador de configuración local válido a utilizar durante las comparaciones de strings (esto afecta la colación del string).

`flags`  
`flags` puede ser uno o varios de los siguientes valores, unidos con OR, y afecta las comparaciones de strings:

| Valor                 | Significado                                        |
|-----------------------|----------------------------------------------------|
| `NORM_IGNORECASE`     | Compara con sensibilidad a mayúsculas y minúsculas |
| `NORM_IGNORENONSPACE` | Ignora los caracteres no espaciadores              |
| `NORM_IGNORESYMBOLS`  | Ignora los símbolos                                |
| `NORM_IGNOREWIDTH`    | Ignora el ancho del string                         |
| `NORM_IGNOREKANATYPE` | Ignora el tipo Kana                                |
| `NORM_IGNOREKASHIDA`  | Ignora los caracteres árabes kashida               |

Opciones de comparación Variant

> [!NOTE]
> Al igual que para todas las funciones aritméticas, los parámetros para esta función pueden ser ya sea un tipo nativo de PHP (entero, string, float, bool o `null`), o una instancia de la clase COM, VARIANT o DOTNET. Los tipos nativos de PHP serán convertidos a VARIANT utilizando las mismas reglas que las encontradas en el constructor de la clase [???](#class.variant). Los objetos COM y DOTNET tendrán el valor de su propiedad predeterminada recuperado y utilizado como valor VARIANT.
>
> Las funciones aritméticas VARIANT están interfazadas con las funciones equivalentes de la biblioteca COM; para más información sobre estas funciones, consúltese la biblioteca MSDN. Las funciones PHP tienen nombres ligeramente diferentes: por ejemplo, `variant_add`, en PHP, corresponde a `VarAdd()` en la documentación MSDN.

## Valores devueltos

Devuelve uno de los siguientes valores:

| Valor         | Significado                        |
|---------------|------------------------------------|
| `VARCMP_LT`   | `left` es menor que `right`        |
| `VARCMP_EQ`   | `left` es igual a `right`          |
| `VARCMP_GT`   | `left` es mayor que `right`        |
| `VARCMP_NULL` | `left`, `right` o ambos son `null` |

Resultados de las comparaciones sobre variantes
