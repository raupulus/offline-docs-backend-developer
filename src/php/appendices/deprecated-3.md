---
title: Funcionalidades obsoletas en PHP 7.1.x
source_url: https://www.php.net/manual/es/migration71.deprecated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration71/deprecated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 7583c04dd
order: 460
---

## Funcionalidades obsoletas en PHP 7.1.x

## ext/mcrypt

La extensión mcrypt fue declarada «abandonware» hace casi una década, y también era bastante compleja de utilizar. Por tanto, está obsoleta en favor de OpenSSL, y se eliminará del núcleo y se trasladará a PECL en PHP 7.2.

## Opción 'eval' para `mb_ereg_replace` y `mb_eregi_replace`

El modificador de patrón `e` está obsoleto para las funciones `mb_ereg_replace` y `mb_eregi_replace`.
