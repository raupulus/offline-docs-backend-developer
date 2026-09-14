---
title: ldap_explode_dn
description: Separa los diferentes componentes de un DN
source_url: https://www.php.net/manual/es/function.ldap-explode-dn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-explode-dn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: b95d28e6e
order: 43210
---

ldap_explode_dn

Separa los diferentes componentes de un DN

## Descripción

```php
ldap_explode_dn(string $dn, int $with_attrib): array
```php

Divide el DN devuelto por `ldap_get_dn` y lo descompone en sus componentes. Cada componente se denomina Nombre Distinguido Relativo (Relative Distinguished Name o RDN).

## Parámetros

`dn`  
El nombre DN de la entrada LDAP.

`with_attrib`  
Sirve para especificar si los RDN se devuelven solos, o bien con sus atributos. Para obtener los atributos junto con los RDN (en formato atributo=valor), se debe asignar a `with_attrib` el valor de `0` y, en caso contrario, se le debe asignar el valor de `1`.

## Valores devueltos

Devuelve un array de todos los componentes DN, o `false` si ocurre un error. El primer elemento del array tiene una clave `count` y representa el número de valores devueltos; los demás elementos son los componentes DN indexados numéricamente.
