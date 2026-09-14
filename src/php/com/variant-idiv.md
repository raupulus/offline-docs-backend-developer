---
title: variant_idiv
description: Convierte variants en valores enteros y realiza una división
source_url: https://www.php.net/manual/es/function.variant-idiv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/variant-idiv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 31ab1b9a0
order: 7860
---

variant_idiv

Convierte variants en valores enteros y realiza una división

## Descripción

```php
variant_idiv(mixed $left, mixed $right): variant
```php

Convierte `left` y `right` en valores enteros y realiza una división entera.

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

| Si | Entonces |
|----|----|
| Ambas expresiones son strings, fechas, caracteres, bool | División y entero devueltos |
| Una expresión es un string y la otra es un carácter | División |
| Una expresión es numérica y la otra es un string | División |
| Ambas expresiones son numéricas | División |
| Una de las expresiones es NULL | NULL es devuelto |
| Ambas expresiones están vacías | Se lanza una `com_exception` con código `DISP_E_DIVBYZERO` |

Reglas de divisiones internas de variants

## Errores/Excepciones

Lanza una `com_exception` en caso de fallo.

## Véase también

`variant_div`
