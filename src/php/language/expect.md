---
title: expect://
description: Flujos de Interacción de Procesos
source_url: https://www.php.net/manual/es/wrappers.expect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/expect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 4630
---

expect://

Flujos de Interacción de Procesos

## Descripción

Los flujos que se hayan abierto con la envoltura `expect://`, darán acceso a stdin, stdout y stderr (entrada, salida y errores estándar respectivamente) de los procesos, vía PTY.

> [!NOTE]
> Para poder usar la envoltura `expect://` se debe instalar la extensión [Expect](https://pecl.php.net/package/expect) disponible en [PECL](https://pecl.php.net/).

`expect://` (PECL)

## Uso

- `expect://command`

## Opciones

| Atributo                                                | Permitido |
|---------------------------------------------------------|-----------|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen) | No        |
| Permites Lecturas                                       | Sí        |
| Permite Escrituras                                      | No        |
| Permite Añadir contenido                                | Sí        |
| Permite Lecturas y Escrituras Simultáneas               | No        |
| Permite usar la función `stat`                          | No        |
| Permite usar la función `unlink`                        | No        |
| Permite usar la función `rename`                        | No        |
| Permite usar la función `mkdir`                         | No        |
| Permite usar la función `rmdir`                         | No        |

Resumen de la Envoltura {role="stream_wrapper"}
