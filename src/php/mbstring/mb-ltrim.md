---
title: mb_ltrim
description: Elimina los espacios (u otros caracteres) del inicio de un string
source_url: https://www.php.net/manual/es/function.mb-ltrim.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-ltrim.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 154d93899
order: 45290
---

mb_ltrim

Elimina los espacios (u otros caracteres) del inicio de un string

## Descripción

```php
mb_ltrim(string $string, [string $characters], [string $encoding]): string
```php

Realiza una operación `ltrim` segura para datos multi-octetos. Elimina los espacios (u otros caracteres) del inicio de un string.

Sin el segundo argumento, `mb_ltrim` eliminará los siguientes caracteres:

- `" "` (Unicode U+0020), un espacio ordinario.

- `"\t"` (Unicode U+0009), una tabulación.

- `"\n"` (Unicode U+000A), un salto de línea.

- `"\r"` (Unicode U+000D), un retorno de carro.

- `"\0"` (Unicode U+0000), el octeto NUL.

- `"\v"` (Unicode U+000B), una tabulación vertical.

- `"\f"` (Unicode U+000C), un avance de página.

- `"\u00A0"` (Unicode U+00A0), un ESPACIO INSÉCABLE.

- `"\u1680"` (Unicode U+1680), una MARCA DE ESPACIO OGHAM.

- `"\u2000"` (Unicode U+2000), un CUADRADO MEDIO.

- `"\u2001"` (Unicode U+2001), un CUADRADO.

- `"\u2002"` (Unicode U+2002), un ESPACIO MEDIO.

- `"\u2003"` (Unicode U+2003), un ESPACIO CUADRADO.

- `"\u2004"` (Unicode U+2004), un ESPACIO DE UN-TERCIO-DE-CUADRADO.

- `"\u2005"` (Unicode U+2005), un ESPACIO DE UN-CUARTO-DE-CUADRADO.

- `"\u2006"` (Unicode U+2006), un ESPACIO DE UN-SEXTO-DE-CUADRADO.

- `"\u2007"` (Unicode U+2007), un ESPACIO PARA DÍGITOS.

- `"\u2008"` (Unicode U+2008), un ESPACIO DE PUNTUACIÓN.

- `"\u2009"` (Unicode U+2009), un ESPACIO FINO.

- `"\u200A"` (Unicode U+200A), un ESPACIO PELUDO.

- `"\u2028"` (Unicode U+2028), un SEPARADOR DE LÍNEA.

- `"\u2029"` (Unicode U+2029), un SEPARADOR DE PÁRRAFO.

- `"\u202F"` (Unicode U+202F), un ESPACIO INSÉCABLE ESTRECHO.

- `"\u205F"` (Unicode U+205F), un ESPACIO MATEMÁTICO MEDIO.

- `"\u3000"` (Unicode U+3000), un ESPACIO IDEOGRÁFICO.

- `"\u0085"` (Unicode U+0085), una LÍNEA SIGUIENTE (NEL).

- `"\u180E"` (Unicode U+180E), un SEPARADOR DE VOCALES MONGOL.

## Parámetros

`string`  
El string de entrada.

`characters`  
Opcionalmente, los caracteres a eliminar también pueden ser especificados utilizando el parámetro `characters`. Basta con listar todos los caracteres a eliminar.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Esta función devuelve un string con los espacios eliminados del inicio de `string`.

## Véase también

mb_trim

mb_rtrim

ltrim
