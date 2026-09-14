---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/datetime.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: b53f03f24
order: 10190
---

## Constantes predefinidas

Las contantes `DATE_*` están definidas y ofrecen representaciones de fecha estándar que pueden ser empleadas por funciones de formato de fecha (como `date`).

`SUNFUNCS_RET_TIMESTAMP` (`int`)  
Timestamp

`SUNFUNCS_RET_STRING` (`int`)  
Horas:minutos (ejemplo: `08:02`)

`SUNFUNCS_RET_DOUBLE` (`int`)  
Horas como número con decimales (ejemplo `8.75`)

<!-- -->

`DATE_ATOM` (`string`)  
Atom (ejemplo: `2005-08-15T15:52:01+00:00`); compatible con ISO-8601, RFC 3339 y XML Schema

`DATE_COOKIE` (`string`)  
HTTP Cookies (ejemplo: `Monday, 15-Aug-2005 15:52:01 UTC`)

`DATE_ISO8601` (`string`)  
Similar a ISO-8601 (ejemplo: `2005-08-15T15:52:01+0000`)

> [!NOTE]
> Este formato no es compatible con el ISO-8601, aunque se deja por razones de retrocompatibilidad. Use `DATE_ISO8601_EXPANDED`, `DATE_ATOM` en su lugar para que sea compatible con el ISO-8601. (ref ISO8601:2004 section 4.3.3 clause d)

`DATE_ISO8601_EXPANDED` (`string`)  
ISO-8601 Extendido (ejemplo: `+10191-07-26T08:59:52+01:00`)

> [!NOTE]
> Este formato permite rangos de años fuera del rango normal de ISO-8601 de `0000`-`9999` al incluir siempre un carácter de signo. También asegura que la parte de la zona horaria (`+01:00`) sea compatible con ISO-8601.

`DATE_RFC822` (`string`)  
RFC 822 (ejemplo: `Mon, 15 Aug 05 15:52:01 +0000`)

`DATE_RFC850` (`string`)  
RFC 850 (ejemplo: `Monday, 15-Aug-05 15:52:01 UTC`)

`DATE_RFC1036` (`string`)  
RFC 1036 (ejemplo: `Mon, 15 Aug 05 15:52:01 +0000`)

`DATE_RFC1123` (`string`)  
RFC 1123 (ejemplo: `Mon, 15 Aug 2005 15:52:01 +0000`)

`DATE_RFC7231` (`string`)  
RFC 7231 (desde PHP 7.0.19 y 7.1.5) (ejemplo: `Sat, 30 Apr 2016 17:52:13 GMT`)

`DATE_RFC2822` (`string`)  
RFC 2822 (ejemplo: `Mon, 15 Aug 2005 15:52:01 +0000`)

`DATE_RFC3339` (`string`)  
Igual que `DATE_ATOM`.

`DATE_RFC3339_EXTENDED` (`string`)  
Formato RFC 3339 EXTENDED (ejemplo: `2005-08-15T15:52:01.000+00:00`)

`DATE_RSS` (`string`)  
RSS (ejemplo: `Mon, 15 Aug 2005 15:52:01 +0000`). Alias de `DATE_RFC1123`.

`DATE_W3C` (`string`)  
World Wide Web Consortium (ejemplo: `2005-08-15T15:52:01+00:00`). Alias de `DATE_RFC3339`.
