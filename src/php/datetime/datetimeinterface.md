---
title: La interfaz DateTimeInterface
source_url: https://www.php.net/manual/es/class.datetimeinterface.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimeinterface.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: e1e7f1f92
order: 10830
---

## Introducción

DateTimeInterface fue creada tanto como parametro de retorno, como para las declaraciones de tipo de propiedad puedan aceptar tanto `DateTimeImmutable` o `DateTime` como valor. No es posible que el usuario implemente esta interfaz en sus propias clases.

Las constantes comunes que permiten el formato de objetos `DateTimeImmutable` o `DateTime` mediante DateTimeImmutable::format y DateTime::format son también definidas en esta interfaz.

## Sinopsis de la clase

DateTimeInterface

Constantes

public

const

string

DateTimeInterface::ATOM

"Y-m-d\\TH:i:sP"

public

const

string

DateTimeInterface::COOKIE

"l, d-M-Y H:i:s T"

public

const

string

DateTimeInterface::ISO8601

"Y-m-d\\TH:i:sO"

public

const

string

DateTimeInterface::ISO8601_EXPANDED

"X-m-d\\TH:i:sP"

public

const

string

DateTimeInterface::RFC822

"D, d M y H:i:s O"

public

const

string

DateTimeInterface::RFC850

"l, d-M-y H:i:s T"

public

const

string

DateTimeInterface::RFC1036

"D, d M y H:i:s O"

public

const

string

DateTimeInterface::RFC1123

"D, d M Y H:i:s O"

public

const

string

DateTimeInterface::RFC7231

"D, d M Y H:i:s \\G\\M\\T"

public

const

string

DateTimeInterface::RFC2822

"D, d M Y H:i:s O"

public

const

string

DateTimeInterface::RFC3339

"Y-m-d\\TH:i:sP"

public

const

string

DateTimeInterface::RFC3339_EXTENDED

"Y-m-d\\TH:i:s.vP"

public

const

string

DateTimeInterface::RSS

"D, d M Y H:i:s O"

public

const

string

DateTimeInterface::W3C

"Y-m-d\\TH:i:sP"

Métodos

## Constantes predefinidas

`DateTimeInterface::ATOM` `string`; `DATE_ATOM`  
Atom (ejemplo: `2005-08-15T15:52:01+00:00`); compatible con ISO-8601, RFC 3339 y XML Schema

`DateTimeInterface::COOKIE` `string`; `DATE_COOKIE`  
HTTP Cookies (ejemplo: `Monday, 15-Aug-2005 15:52:01 UTC`)

`DateTimeInterface::ISO8601` `string`; `DATE_ISO8601`  
Similar a ISO-8601 (ejemplo: `2005-08-15T15:52:01+0000`)

> [!NOTE]
> Este formato no es compatible con el ISO-8601, aunque se deja por razones de retrocompatibilidad. Use `DateTimeInterface::ISO8601_EXPANDED`, `DateTimeInterface::ATOM` en su lugar para que sea compatible con el ISO-8601. (ref ISO8601:2004 section 4.3.3 clause d)

`DateTimeInterface::ISO8601_EXPANDED` `string`; `DATE_ISO8601_EXPANDED`  
ISO-8601 Extendido (ejemplo: `+10191-07-26T08:59:52+01:00`)

> [!NOTE]
> Este formato permite rangos de años fuera del rango normal de ISO-8601 de `0000`-`9999` al incluir siempre un carácter de signo. También asegura que la parte de la zona horaria (`+01:00`) sea compatible con ISO-8601.

`DateTimeInterface::RFC822` `string`; `DATE_RFC822`  
RFC 822 (ejemplo: `Mon, 15 Aug 05 15:52:01 +0000`)

`DateTimeInterface::RFC850` `string`; `DATE_RFC850`  
RFC 850 (ejemplo: `Monday, 15-Aug-05 15:52:01 UTC`)

`DateTimeInterface::RFC1036` `string`; `DATE_RFC1036`  
RFC 1036 (ejemplo: `Mon, 15 Aug 05 15:52:01 +0000`)

`DateTimeInterface::RFC1123` `string`; `DATE_RFC1123`  
RFC 1123 (ejemplo: `Mon, 15 Aug 2005 15:52:01 +0000`)

`DateTimeInterface::RFC7231` `string`; `DATE_RFC7231`  
RFC 7231 (desde PHP 7.0.19 y 7.1.5) (ejemplo: `Sat, 30 Apr 2016 17:52:13 GMT`)

`DateTimeInterface::RFC2822` `string`; `DATE_RFC2822`  
RFC 2822 (ejemplo: `Mon, 15 Aug 2005 15:52:01 +0000`)

`DateTimeInterface::RFC3339` `string`; `DATE_RFC3339`  
Igual que `DATE_ATOM`

`DateTimeInterface::RFC3339_EXTENDED` `string`; `DATE_RFC3339_EXTENDED`  
Formato RFC 3339 EXTENDED (ejemplo: `2005-08-15T15:52:01.000+00:00`)

`DateTimeInterface::RSS` `string`; `DATE_RSS`  
RSS (ejemplo: `Mon, 15 Aug 2005 15:52:01 +0000`).

`DateTimeInterface::W3C` `string`; `DATE_W3C`  
World Wide Web Consortium (ejemplo: `2005-08-15T15:52:01+00:00`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Las constantes `DATE_RFC7231` y `DateTimeInterface::RFC7231` han sido obsoletas. |
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 8.2.0 | Se ha añadido la constante `DateTimeInterface::ISO8601_EXPANDED`. |
| 7.2.0 | Las constantes de clase de `DateTime` ahora están definidas en DateTimeInterface. |
