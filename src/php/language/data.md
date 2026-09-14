---
title: data://
description: Datos (RFC 2397)
source_url: https://www.php.net/manual/es/wrappers.data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 4620
---

data://

Datos (RFC 2397)

## Descripción

La envoltura de flujo `data:` ([RFC 2397](https://datatracker.ietf.org/doc/html/rfc2397)).

## Uso

- `data://text/plain;base64,`

## Opciones

| Atributo                                                    | Soportado |
|-------------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen)     | Sí        |
| Restringido por [allow_url_include](#ini.allow-url-include) | Sí        |
| Permite la lectura                                          | Sí        |
| Permite la escritura                                        | No        |
| Permite la adición                                          | No        |
| Permite la lectura y escritura simultáneamente              | No        |
| Soporte de la función `stat`                                | No        |
| Soporte de la función `unlink`                              | No        |
| Soporte de la función `rename`                              | No        |
| Soporte de la función `mkdir`                               | No        |
| Soporte de la función `rmdir`                               | No        |

Resumen de la envoltura {role="stream_wrapper"}

## Ejemplos

Mostrar un contenido data://

```php
<?php
// Muestra "I love PHP"
echo file_get_contents('data://text/plain;base64,SSBsb3ZlIFBIUAo=');
?>

   
```

Obtención del tipo de medio

```php
<?php
$fp   = fopen('data://text/plain;base64,', 'r');
$meta = stream_get_meta_data($fp);

// Muestra "text/plain"
echo $meta['mediatype'];
?>

   
```
