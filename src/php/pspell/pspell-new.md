---
title: pspell_new
description: Carga un nuevo diccionario
source_url: https://www.php.net/manual/es/function.pspell-new.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-new.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 46364d741
order: 66500
---

pspell_new

Carga un nuevo diccionario

## Descripción

```php
pspell_new(string $language, [string $spelling], [string $jargon], [string $encoding], [int $mode]): PSpell\Dictionary
```php

`pspell_new` abre un nuevo diccionario y devuelve una instancia de `PSpell\Dictionary`, para ser utilizada con otras funciones pspell.

Para más información y ejemplos, consúltese el sitio <http://aspell.net/>.

## Parámetros

`language`  
El argumento de idioma `spelling` se compone de las dos letras del código de idioma ISO 639, y del código opcional de país ISO 3166, separados por un '\_'.

`spelling`  
Este argumento es necesario para los idiomas que tienen más de una ortografía, como el inglés o el francés. Los valores reconocidos son 'american', 'british', y 'canadian'.

`jargon`  
El argumento `jargon` contiene información adicional para distinguir dos listas de palabras que tienen el mismo marcado de idioma y ortografía.

`encoding`  
El argumento `encoding` es el tipo de codificación de las palabras. Los valores válidos son 'utf-8', 'iso8859-\*', 'koi8-r', 'viscii', 'cp1252', 'machine unsigned 16', 'machine unsigned 32'. Este argumento no ha sido probado de forma exhaustiva, por lo que se recomienda precaución al utilizarlo.

`mode`  
El argumento `mode` es el modo de funcionamiento del corrector ortográfico. Varios modos están disponibles :

- `PSPELL_FAST` - Modo rápido (menos sugerencias)

- `PSPELL_NORMAL` - Modo normal (más sugerencias)

- `PSPELL_BAD_SPELLERS` - Modo lento (muchas más sugerencias)

- `PSPELL_RUN_TOGETHER` - Considera que palabras unidas forman un compuesto válido. Así, "lechat" será un compuesto válido. Esta opción modifica únicamente los resultados devueltos por `pspell_check`; `pspell_suggest` siempre devolverá sugerencias.

`mode` es una máscara construida a partir de las constantes listadas anteriormente. Sin embargo, `PSPELL_FAST`, `PSPELL_NORMAL` y `PSPELL_BAD_SPELLERS` son mutuamente excluyentes : no se deben utilizar a la vez.

## Valores devueltos

Devuelve una instancia de `PSpell\Dictionary` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PSpell\Dictionary` ; anteriormente se devolvía un `resource`. |

## Ejemplos

`pspell_new`

```
<?php
$pspell = pspell_new("en", "", "", "",
                     (PSPELL_FAST|PSPELL_RUN_TOGETHER));
?>

    
```php
