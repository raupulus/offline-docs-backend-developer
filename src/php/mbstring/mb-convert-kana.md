---
title: mb_convert_kana
description: Convierte un "kana" en otro ("zen-kaku", "han-kaku" y más)
source_url: https://www.php.net/manual/es/function.mb-convert-kana.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-convert-kana.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 34f90a659
order: 45000
---

mb_convert_kana

Convierte un "kana" en otro ("zen-kaku", "han-kaku" y más)

## Descripción

```php
mb_convert_kana(string $string, [string $mode], [string $encoding]): string
```php

Realiza una conversión "han-kaku" - "zen-kaku" en la cadena `string`. Esta función es únicamente útil para los japoneses.

## Parámetros

`string`  
La cadena a convertir.

`mode`  
La opción de conversión.

Especifique las conversiones combinando los siguientes valores.

| Opción | Significado |
|----|----|
| `r` | Convierte el alfabeto "zen-kaku" en "han-kaku" |
| `R` | Convierte el alfabeto "han-kaku" en "zen-kaku" |
| `n` | Convierte los números "zen-kaku" en "han-kaku" |
| `N` | Convierte los números "han-kaku" en "zen-kaku" |
| `a` | Convierte los números y alfabeto "zen-kaku" en "han-kaku" |
| `A` | Convierte los números y alfabeto "zen-kaku" en "han-kaku". (Los caracteres incluidos en las opciones "a", "A" son U+0021 - U+007E excluyendo U+0022, U+0027, U+005C, U+007E) |
| `s` | Convierte "zen-kaku" en "han-kaku" (U+3000 -\> U+0020) |
| `S` | Convierte "han-kaku" en "zen-kaku" (U+0020 -\> U+3000) |
| `k` | Convierte "zen-kaku kata-kana" en "han-kaku kata-kana" |
| `K` | Convierte "han-kaku kata-kana" en "zen-kaku kata-kana" |
| `h` | Convierte "zen-kaku hira-gana" en "han-kaku kata-kana" |
| `H` | Convierte "han-kaku kata-kana" en "zen-kaku hira-gana" |
| `c` | Convierte "zen-kaku kata-kana" en "zen-kaku hira-gana" |
| `C` | Convierte "zen-kaku hira-gana" en "zen-kaku kata-kana" |
| `V` | Elimina las notaciones vocales y las convierte en caracteres. Usar con "K","H" |

Opciones de conversión disponibles

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

La cadena convertida.

## Errores/Excepciones

Genera un `ValueError` si la combinación de diferentes `mode` no es válida. Por ejemplo `"sS"`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Ahora se genera un `ValueError` si la combinación de diferentes `mode`s no es válida. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Ejemplos

Ejemplo con `mb_convert_kana`

```
<?php
/* Convierte todos los "han-kaku" "kata-kana" en "zen-kaku" "hira-gana" */
echo mb_convert_kana('ﾔﾏﾀﾞ ﾊﾅｺ', "HV") . "\n";

/* Convierte "han-kaku" "kata-kana" en "zen-kaku" "kata-kana"
   y "zen-kaku" alfanumérico en "han-kaku" */
echo mb_convert_kana('ｺｳｻﾞﾊﾞﾝｺﾞｳ ０１２３４５６', "KVa") . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    やまだ はなこ
    コウザバンゴウ 0123456
