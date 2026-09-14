---
title: Opciones de contexto Zip
description: Listado de opciones de contexto Zip
source_url: https://www.php.net/manual/es/context.zip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/context/zip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 0545e305c
order: 2050
---

Opciones de contexto Zip

Listado de opciones de contexto Zip

## Descripción

Las opciones de contexto Zip están disponibles para las envolturas (wrappers) `zip`.

## Opciones

`password`  
Utilizado para especificar una contraseña a utilizar para los archivos cifrados.

## Historial de cambios

| Versión                | Descripción                       |
|------------------------|-----------------------------------|
| 7.2.0, PECL zip 1.14.0 | Adición del parámetro `password`. |

## Ejemplos

Ejemplo con una utilización simple del parámetro `password`

```php
<?php
// Leer el archivo cifrado
$opts = array(
    'zip' => array(
        'password' => 'secret',
    ),
);
// crear el contexto...
$context = stream_context_create($opts);

// ...y utilizarlo para recuperar los datos
echo file_get_contents('zip://test.zip#test.txt', false, $context);

?>

    
```
