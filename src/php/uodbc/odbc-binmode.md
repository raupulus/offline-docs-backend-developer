---
title: odbc_binmode
description: Modifica la gestión de columnas de datos binarios
source_url: https://www.php.net/manual/es/function.odbc-binmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-binmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98640
---

odbc_binmode

Modifica la gestión de columnas de datos binarios

## Descripción

```php
odbc_binmode(Odbc\Result $statement, int $mode): true
```php

`odbc_binmode` controla la gestión de las columnas de datos binarios. Los tipos ODBC SQL afectados son `BINARY`, `VARBINARY` y `LONGVARBINARY`. El modo predeterminado puede definirse utilizando la directiva `php.ini` [uodbc.defaultbinmode](#ini.uodbc.defaultbinmode)

Cuando un dato SQL se convierte en carácter C, (`ODBC_BINMODE_CONVERT`) los 8 bits del carácter fuente se representan por dos caracteres ASCII. Estos caracteres son representaciones ASCII de los números en formato hexadecimal. Por ejemplo, el binario `00000001` se convierte en `"01"` y el binario `11111111` se convierte en `"FF"`.

Mientras que la gestión de las columnas `BINARY` y `VARBINARY` depende únicamente del binmode, la gestión de las columnas `LONGVARBINARY` depende también de longreadlen, como se muestra a continuación:

| Modo                    | Longitud | Resultado  |
|-------------------------|----------|------------|
| `ODBC_BINMODE_PASSTHRU` | 0        | `passthru` |
| `ODBC_BINMODE_RETURN`   | 0        | `passthru` |
| `ODBC_BINMODE_CONVERT`  | 0        | `passthru` |
| `ODBC_BINMODE_PASSTHRU` | \>0      | `passthru` |
| `ODBC_BINMODE_RETURN`   | \>0      | Tal cual   |
| `ODBC_BINMODE_CONVERT`  | \>0      | Carácter   |

Conversión de `LONGVARBINARY`

Si se utiliza `odbc_fetch_into`, `passthru` significa que se devolverá una cadena vacía para estas columnas. Si se utiliza la función `odbc_result`, passthru significa que los datos se envían directamente al cliente (es decir, se imprimen).

## Parámetros

`statement`  
The ODBC result object.

`mode`  
Valores posibles para el parámetro `mode`:

- `ODBC_BINMODE_PASSTHRU`: devolver los datos en binario

- `ODBC_BINMODE_RETURN`: devolver sin conversión

- `ODBC_BINMODE_CONVERT`: convertir en carácter

> [!NOTE]
> La gestión de columnas de tipo binary long también se ve afectada por la función `odbc_longreadlen`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |
