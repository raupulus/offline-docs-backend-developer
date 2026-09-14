---
title: La enumeración Uri\WhatWg\UrlValidationErrorType
source_url: https://www.php.net/manual/es/enum.uri-whatwg-urlvalidationerrortype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri.whatwg.urlvalidationerrortype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 8352249a8
order: 100170
---

## Introducción

Los posibles errores de validación definidos en el [estándar WHATWG URL](https://url.spec.whatwg.org/).

## Sinopsis del enum

Uri\WhatWg

UrlValidationErrorType

DomainToAscii

Error durante el proceso de conversión del nombre de dominio a una cadena ASCII.

DomainToUnicode

Error durante el proceso de conversión del nombre de dominio a una cadena Unicode.

DomainInvalidCodePoint

El host de la entrada contiene un punto de código de dominio prohibido.

HostInvalidCodePoint

Un host opaco (en una URL que no es especial) contiene un punto de código de host prohibido.

Ipv4EmptyPart

Una dirección IPv4 termina con un

U+002E

(

.

).

Ipv4TooManyParts

Una dirección IPv4 no consta exactamente de 4 partes.

Ipv4NonNumericPart

Una parte de la dirección IPv4 no es numérica.

Ipv4NonDecimalPart

La dirección IPv4 contiene números expresados con dígitos hexadecimales u octales.

Ipv4OutOfRangePart

Una parte de la dirección IPv4 supera

255

.

Ipv6Unclosed

A una dirección IPv6 le falta el cierre

U+005D

(

\]

).

Ipv6InvalidCompression

Una dirección IPv6 comienza con una compresión incorrecta.

Ipv6TooManyPieces

Una dirección IPv6 contiene más de 8 piezas.

Ipv6MultipleCompression

Una dirección IPv6 está comprimida en más de un lugar.

Ipv6InvalidCodePoint

Una dirección IPv6 contiene un punto de código que no es ni un dígito hexadecimal ASCII ni un

U+003A

(

:

). O termina de forma inesperada.

Ipv6TooFewPieces

Una dirección IPv6 sin compresión contiene menos de 8 piezas.

Ipv4InIpv6TooManyPieces

Una dirección IPv6 con sintaxis de dirección IPv4: la dirección IPv6 tiene más de 6 piezas.

Ipv4InIpv6InvalidCodePoint

Una dirección IPv6 con sintaxis de dirección IPv4.

Ipv4InIpv6OutOfRangePart

Una dirección IPv6 con sintaxis de dirección IPv4: una parte IPv4 supera

255

.

Ipv4InIpv6TooFewParts

Una dirección IPv6 con sintaxis de dirección IPv4: una dirección IPv4 contiene muy pocas partes.

InvalidUrlUnit

Se encontró un punto de código que no es una unidad de URL.

SpecialSchemeMissingFollowingSolidus

El esquema de la entrada no está seguido de

//

.

MissingSchemeNonRelativeUrl

La entrada carece de un esquema, porque no comienza con un carácter alfabético ASCII, y no se proporcionó una URL base o la URL base no puede utilizarse como URL base porque tiene una ruta opaca.

InvalidReverseSoldius

La URL tiene un esquema especial y utiliza

U+005C

(

\\

) en lugar de

U+002F

(

/

).

InvalidCredentials

La entrada incluye credenciales.

HostMissing

La entrada tiene un esquema especial, pero no contiene un host.

PortOutOfRange

El puerto de la entrada es demasiado grande.

PortInvalid

El puerto de la entrada es inválido.

FileInvalidWindowsDriveLetter

La entrada es una cadena de URL relativa que comienza con una letra de unidad Windows y el esquema de la URL base es

file

.

FileInvalidWindowsDriveLetterHost

El host de una URL

file:

es una letra de unidad Windows.
