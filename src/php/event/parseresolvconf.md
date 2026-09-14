---
title: EventDnsBase::parseResolvConf
description: Analiza el fichero resolv.conf
source_url: https://www.php.net/manual/es/eventdnsbase.parseresolvconf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventdnsbase/parseresolvconf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19800
---

EventDnsBase::parseResolvConf

Analiza el fichero resolv.conf

## Descripción

```php
public EventDnsBase::parseResolvConf(int $flags, string $filename): bool
```php

Analiza el fichero resolv.conf y lee todas las opciones presentes.

## Parámetros

`flags`  
Determina la información a analizar desde el fichero `resolv.conf`. Ver la página del manual del sistema del fichero `resolv.conf` para conocer su formato.

Las siguientes directivas no son analizadas en el fichero: `sortlist, rotate, no-check-names, inet6, debug`.

Si esta función encuentra un error, los valores devueltos posibles son: `1` = fallo al abrir el fichero, `2` = fallo al recuperar la información del fichero, `3` = fichero demasiado grande, `4` = exceso de memoria, `5` = lectura demasiado corta del fichero, `6` = ningún servidor de nombres listado en el fichero

`filename`  
Ruta hacia el fichero `resolv.conf`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
