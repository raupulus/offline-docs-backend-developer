---
title: pspell_config_create
description: Crea una configuración utilizada para abrir un diccionario
source_url: https://www.php.net/manual/es/function.pspell-config-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pspell/functions/pspell-config-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pspell
translation_status: ready
translation_reviewed: true
translation_revision: 549aa1c4f
order: 66390
---

pspell_config_create

Crea una configuración utilizada para abrir un diccionario

## Descripción

```php
pspell_config_create(string $language, [string $spelling], [string $jargon], [string $encoding]): PSpell\Config
```php

Crea una configuración utilizada para abrir un diccionario.

`pspell_config_create` tiene una sintaxis similar a la de `pspell_new`. De hecho, utilizar `pspell_config_create` seguido inmediatamente por `pspell_new_config` producirá exactamente el mismo resultado. Sin embargo, después de crear una nueva configuración, también pueden utilizarse las funciones `pspell_config_*` antes de llamar a `pspell_new_config` para aprovechar las funcionalidades avanzadas.

Para obtener más información y ejemplos, consúltese el manual en línea en el sitio de pspell : <http://aspell.net/>.

## Parámetros

`language`  
El argumento de lenguaje `language` es el código de idioma en dos letras, definido en la norma ISO 639, y dos letras opcionales ISO 3166, después de un guión o un subrayado (\_).

`spelling`  
El argumento de ortografía `spelling` es necesario para los idiomas que tienen más de una ortografía, como el inglés. Los valores reconocidos son entonces 'american' (americano), 'british' (inglés), y 'canadian' (canadiense).

`jargon`  
El argumento de jergas `jargon` contiene información adicional para distinguir dos diccionarios distintos para el mismo idioma y el mismo argumento de ortografía `spelling`.

`encoding`  
El argumento de codificación `encoding` indica la codificación esperada para la respuesta. Los valores válidos son : 'utf-8', 'iso8859-\*', 'koi8-r', 'viscii', 'cp1252', 'machine unsigned 16', 'machine unsigned 32'. Este argumento no ha sido probado de manera exhaustiva, por lo que se recomienda precaución.

## Valores devueltos

Devuelve una instancia de `PSpell\Config`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Ahora devuelve una instancia de `PSpell\Config` ; anteriormente, se devolvía un `resource`. |

## Ejemplos

`pspell_config_create`

```
<?php
$pspell_config = pspell_config_create("fr");
pspell_config_personal($pspell_config, "/var/dictionaries/custom.pws");
pspell_config_repl($pspell_config, "/var/dictionaries/custom.repl");
$pspell = pspell_new_personal($pspell_config, "fr");
?>

    
```php
