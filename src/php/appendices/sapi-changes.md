---
title: Modificaciones de los módulos SAPI
source_url: https://www.php.net/manual/es/migration70.sapi-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/sapi-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 310b9d492
order: 420
---

## Modificaciones de los módulos SAPI

## [FPM](#book.fpm)

### Los puertos de [escucha](#listen) sin especificar ahora escuchan tanto en IPv4 como en IPv6

En PHP 5, una directiva de [escucha](#listen) con solo un número de puerto escuchaba en todas las interfaces, pero solo en IPv4. PHP 7 ahora aceptará solicitudes realizadas tanto a través de IPv4 como de IPv6.

Esto no afecta a las directivas que incluyen direcciones IP específicas; estas continuarán escuchando solo en esa dirección y protocolo.
