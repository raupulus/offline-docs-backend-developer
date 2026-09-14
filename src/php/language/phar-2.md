---
title: phar://
description: Archivo PHP
source_url: https://www.php.net/manual/es/wrappers.phar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/phar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 4680
---

phar://

Archivo PHP

## Descripción

La envoltura de flujo `phar://`. Véase [envoltura de flujo Phar](#phar.using.stream) para una descripción detallada.

## Uso

- `phar://`

## Opciones

| Atributo                                                    | Soportado |
|-------------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen)     | No        |
| Restringido por [allow_url_include](#ini.allow-url-include) | No        |
| Permite la lectura                                          | Sí        |
| Permite la escritura                                        | Sí        |
| Permite la adición                                          | No        |
| Permite la lectura y escritura simultáneamente              | Sí        |
| Soporte de la función `stat`                                | Sí        |
| Soporte de la función `unlink`                              | Sí        |
| Soporte de la función `rename`                              | Sí        |
| Soporte de la función `mkdir`                               | Sí        |
| Soporte de la función `rmdir`                               | Sí        |

Resumen de la envoltura {role="stream_wrapper"}

## Véase también
