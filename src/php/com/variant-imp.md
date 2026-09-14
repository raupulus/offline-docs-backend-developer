---
title: variant_imp
description: Ejecuta una implicación a nivel de bits de dos variantes
source_url: https://www.php.net/manual/es/function.variant-imp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-imp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 31ab1b9a0
order: 7870
---

variant_imp

Ejecuta una implicación a nivel de bits de dos variantes

## Descripción

```php
variant_imp(mixed $left, mixed $right): variant
```php

Ejecuta una implicación a nivel de bits de dos variantes.

## Parámetros

`left`  
El operando de la izquierda.

`right`  
El operando de la derecha.

> [!NOTE]
> Al igual que para todas las funciones aritméticas, los parámetros para esta función pueden ser ya sea un tipo nativo de PHP (entero, string, float, bool o `null`), o una instancia de la clase COM, VARIANT o DOTNET. Los tipos nativos de PHP serán convertidos a VARIANT utilizando las mismas reglas que las encontradas en el constructor de la clase [???](#class.variant). Los objetos COM y DOTNET tendrán el valor de su propiedad predeterminada recuperado y utilizado como valor VARIANT.
>
> Las funciones aritméticas VARIANT están interfazadas con las funciones equivalentes de la biblioteca COM; para más información sobre estas funciones, consúltese la biblioteca MSDN. Las funciones PHP tienen nombres ligeramente diferentes: por ejemplo, `variant_add`, en PHP, corresponde a `VarAdd()` en la documentación MSDN.

## Valores devueltos

| Si `left` es | Si `right` es | entonces el resultado es |
|--------------|---------------|--------------------------|
| `true`       | `true`        | `true`                   |
| `true`       | `false`       | `false`                  |
| `true`       | `null`        | `true`                   |
| `false`      | `true`        | `true`                   |
| `false`      | `false`       | `true`                   |
| `false`      | `null`        | `true`                   |
| `null`       | `true`        | `true`                   |
| `null`       | `false`       | `null`                   |
| `null`       | `null`        | `null`                   |

Tabla de implicación de variantes

## Errores/Excepciones

Lanza una `com_exception` en caso de error.
