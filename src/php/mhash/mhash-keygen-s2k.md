---
title: mhash_keygen_s2k
description: Genera una clave
source_url: https://www.php.net/manual/es/function.mhash-keygen-s2k.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mhash/functions/mhash-keygen-s2k.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mhash
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 46960
---

mhash_keygen_s2k

Genera una clave

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] mhash_keygen_s2k(int $algo, string $password, string $salt, int $length): string
```php

Genera una clave según el `algo` proporcionado, utilizando la contraseña `password` proporcionada.

Esta función utiliza el algoritmo `Salted S2K`, especificado en OpenPGP ([RFC 2440](https://datatracker.ietf.org/doc/html/rfc2440)).

Es importante tener en cuenta que las contraseñas proporcionadas por los usuarios no son recomendadas para generar claves criptográficas, dado que los usuarios normales recuerdan contraseñas que pueden teclear. Estas contraseñas utilizan solo 6 a 7 de los 8 bits de un carácter (o incluso menos). Se recomienda encarecidamente aplicar una función de transformación (como esta) a una contraseña de usuario.

## Parámetros

`algo`  
El identificador del hash utilizado para crear la clave. Una de las constantes `MHASH_hashname`.

`password`  
Contraseña proporcionada por el usuario.

`salt`  
Debe ser diferente y suficientemente aleatorio para cada clave que se genera, a fin de crear claves diferentes. Dado que el parámetro `salt` debe ser conocido cuando se verifican las claves, es una buena idea añadirlo a la clave. El parámetro salt debe tener una longitud de 8 bytes, y se rellenará con ceros si se proporciona uno de menor tamaño.

`length`  
La longitud de la clave, en bytes.

## Valores devueltos

Devuelve la clave generada, en forma de `string`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Esta función ha sido deprecada. Utilizar las [funciones `hash_*()`](#ref.hash) en su lugar. |
