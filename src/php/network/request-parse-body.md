---
title: request_parse_body
description: Lee y analiza el cuerpo de la petición y devuelve el resultado
source_url: https://www.php.net/manual/es/function.request-parse-body.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/request-parse-body.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: c78af136d
order: 56520
---

request_parse_body

Lee y analiza el cuerpo de la petición y devuelve el resultado

## Descripción

```php
request_parse_body([array $options]): array
```php

Esta función lee el cuerpo de la petición y lo analiza según la cabecera `Content-Type`. Actualmente, se admiten dos tipos de contenido:

- `application/x-www-form-urlencoded`

- `multipart/form-data`

Esta función se utiliza principalmente para analizar las peticiones `multipart/form-data` con verbos HTTP distintos de `POST` que no rellenan automáticamente las superglobales `$_POST` y `$_FILES`.

> [!CAUTION]
> El cuerpo de la petición solo puede consumirse una vez. `request_parse_body` consume el cuerpo de la petición sin almacenarlo en el búfer en el flujo `php://input`. Inversamente, si el cuerpo ya ha sido leído (por ejemplo a través de `php://input`), `request_parse_body` devolverá datos vacíos.

## Parámetros

`options`  
El argumento `options` acepta un array asociativo para sobrescribir los parámetros globales de `php.ini` siguientes para el análisis del cuerpo de la petición.

- `max_file_uploads`

- `max_input_vars`

- `max_multipart_body_parts`

- `post_max_size`

- `upload_max_filesize`

## Valores devueltos

`request_parse_body` devuelve un array con el equivalente de `$_POST` en el índice `0` y `$_FILES` en el índice `1`.

## Errores/Excepciones

Cuando el cuerpo de la petición no es válido según la cabecera `Content-Type`, se lanza una RequestParseBodyException.

Se lanza una ValueError cuando `options` contiene claves no válidas, o valores no válidos para la clave correspondiente.

## Ejemplos

Ejemplo de `request_parse_body`

```
<?php
// Analiza la petición y almacena el resultado en las superglobales $_POST y $_FILES.
[$_POST, $_FILES] = request_parse_body();
// Muestra el contenido de un fichero subido
echo file_get_contents($_FILES['file_name']['tmp_name']);
?>

   
```php

Ejemplo de `request_parse_body` con opciones personalizadas

```
<?php
// form.php

assert_logged_in();

// Solo para este formulario, se permite un tamaño de subida mayor.
[$_POST, $_FILES] = request_parse_body([
    'post_max_size' => '10M',
    'upload_max_filesize' => '10M',
]);

// Hacer algo con los ficheros subidos.
?>

   
```php
