---
title: mb_ucfirst
description: Convierte una string con la primera letra en mayúscula
source_url: https://www.php.net/manual/es/function.mb-ucfirst.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ucfirst.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 154d93899
order: 45600
---

mb_ucfirst

Convierte una string con la primera letra en mayúscula

## Descripción

```php
mb_ucfirst(string $string, [string $encoding]): string
```php

Realiza una operación `ucfirst` segura para multi-octetos, y devuelve una string con la primera letra de `string` en mayúscula.

## Parámetros

`string`  
La string de entrada.

`encoding`  
La codificación de caracteres.

## Valores devueltos

Devuelve la string resultante.

## Notas

> [!NOTE]
> A diferencia de las funciones estándar de conversión de mayúsculas y minúsculas como `strtolower` y `strtoupper`, la conversión de mayúsculas y minúsculas se realiza en función de las propiedades de los caracteres Unicode. Por lo tanto, el comportamiento de esta función no se ve afectado por la configuración regional, y puede convertir todos los caracteres con la propiedad 'alfabético', como la diéresis sobre la "a" (ä).

Para obtener más información sobre las propiedades Unicode, consulte <http://www.unicode.org/reports/tr21/>.

## Véase también

mb_lcfirst

mb_convert_case

ucfirst
