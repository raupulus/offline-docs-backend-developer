---
title: apache_note
description: Muestra o asigna la tabla de notas de Apache
source_url: https://www.php.net/manual/es/function.apache-note.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-note.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: a331ac8a8
order: 4780
---

apache_note

Muestra o asigna la tabla de notas de Apache

## Descripción

```php
apache_note(string $note_name, [string $note_value]): string
```php

Esta función es una abstracción de los comandos `table_get` y `table_set` de Apache. Edita la tabla de notas que existe durante una petición. El propósito de esta tabla es permitir que los módulos de Apache se comuniquen.

La utilidad de la función `apache_note` es pasar información de un módulo a otro, durante la misma petición.

## Parámetros

`note_name`  
El nombre de la nota.

`note_value`  
El valor de la nota.

## Valores devueltos

Si `note_value` es omitido o `null`, devuelve el valor actual de la variable `note_name`. De lo contrario, asigna a la nota `note_name` el valor `note_value` y devolverá el valor anterior de la variable `note_name`. Si la nota no puede ser recuperada, `false` es devuelto.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | `note_value` ahora es nullable. |

## Ejemplos

Pasaje de información entre PHP y Perl

```
<?php

apache_note('name', 'Fredrik Ekengren');

// Llamada al script Perl
virtual("/perl/some_script.pl");

$result = apache_note("resultdata");
?>

    
```php

```
## Recuperación del objeto de petición Apache
my $r = Apache->request()->main();

## Recuperación de los datos pasados
my $name = $r->notes('name');

## Procesamiento

## Envío del resultado hacia PHP
$r->notes('resultdata', $result);

    
```php

Valores de identificación en el archivo access.log

```
<?php

apache_note('sessionID', session_id());

?>

    
```php

```
## "%{sessionID}n" puede ser utilizado en la directiva LogFormat

    
```php

## Véase también

`virtual`
