---
title: Tipo singleton
source_url: https://www.php.net/manual/es/language.types.singleton.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/singleton.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 828980b61
order: 4530
---

## Tipo singleton

Los tipos singleton son aquellos que solo aceptan un único valor. PHP soporta dos tipos singleton: `false` desde PHP 8.0.0 y `true` desde PHP 8.2.0.

> [!WARNING]
> Antes de PHP 8.2.0, el tipo `false` solo podía ser utilizado en el contexto de un [tipo union](#language.types.type-system.composite.union).

> [!NOTE]
> No es posible definir tipos singleton personalizados. Considere el uso de una [enumeración](#language.types.enumerations) en su lugar.
