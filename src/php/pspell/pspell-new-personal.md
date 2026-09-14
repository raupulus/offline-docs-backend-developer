---
title: pspell_new_personal
description: Carga un nuevo diccionario con un diccionario personal
source_url: https://www.php.net/manual/es/function.pspell-new-personal.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-new-personal.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 81b23db05
order: 66490
---

pspell_new_personal

Carga un nuevo diccionario con un diccionario personal

## Descripción

```php
pspell_new_personal(string $filename, string $language, [string $spelling], [string $jargon], [string $encoding], [int $mode]): PSpell\Dictionary
```php

`pspell_new_personal` carga un nuevo diccionario con un diccionario personal. Este último puede ser modificado y guardado con `pspell_save_wordlist`. Sin embargo, las parejas de reemplazo no serán guardadas. Para ello, debe crearse una configuración que utilice `pspell_config_create`, seleccionarse el archivo de destino del diccionario personal con `pspell_config_personal`, seleccionarse el archivo de parejas de reemplazo con `pspell_config_repl` y abrirse un nuevo diccionario con `pspell_new_config`.

Para obtener más información y ejemplos, consúltese el manual en línea en el sitio web de pspell : <http://aspell.net/>.

## Parámetros

`filename`  
El archivo donde se añadirán las palabras del diccionario personal. Debe ser una ruta absoluta, que comience con '/' ya que, de lo contrario, será relativa a \$HOME, que es "/root" en la mayoría de los sistemas, y probablemente no sea lo deseado.

`language`  
El parámetro de idioma `language` es el código de idioma ISO 639 de dos letras, seguido de dos letras opcionales ISO 3166, después de un guión o un subrayado (\_).

`spelling`  
El parámetro de ortografía `spelling` es necesario para los idiomas que tienen más de una ortografía, como el inglés. Los valores reconocidos son entonces 'american' (americano), 'british' (británico), y 'canadian' (canadiense).

`jargon`  
Información adicional para distinguir dos diccionarios distintos para el mismo idioma y el mismo parámetro de ortografía `spelling`.

`encoding`  
La codificación esperada para la respuesta. Los valores válidos son : `utf-8`, `iso8859-*`, `koi8-r`, `viscii`, `cp1252`, `machine unsigned 16`, `machine unsigned 32`.

`mode`  
El modo de funcionamiento del corrector ortográfico. Varios modos están disponibles :

- `PSPELL_FAST` - Modo rápido (menos sugerencias)

- `PSPELL_NORMAL` - Modo normal (más sugerencias)

- `PSPELL_BAD_SPELLERS` - Modo lento (muchas más sugerencias)

- `PSPELL_RUN_TOGETHER` - Considera las palabras unidas como legales. De este modo, "lechat" será una palabra compuesta legal, aunque debería haber un espacio entre las dos palabras. Cambiar esta configuración solo afecta al resultado devuelto por `pspell_check`; `pspell_suggest` continuará devolviendo las sugerencias.

El modo es una máscara construida desde las diferentes constantes listadas a continuación. Sin embargo, las constantes `PSPELL_FAST`, `PSPELL_NORMAL` y `PSPELL_BAD_SPELLERS` son mutuamente excluyentes, por lo que solo debe seleccionarse una de ellas.

## Valores devueltos

Devuelve una instancia de `PSpell\Dictionary` en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PSpell\Dictionary`; anteriormente se devolvía un `resource`. |

## Ejemplos

`pspell_new_personal`

```
<?php
$pspell = pspell_new_personal ("/var/dictionaries/custom.pws",
        "en", "", "", "", PSPELL_FAST|PSPELL_RUN_TOGETHER);
?>

    
```php
