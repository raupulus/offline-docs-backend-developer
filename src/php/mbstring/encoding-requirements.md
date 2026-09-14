---
title: Requerimientos para la codificación de caracteres en PHP
source_url: https://www.php.net/manual/es/mbstring.php4.req.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/encoding-requirements.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 96c9d88ba
order: 44940
---

## Requerimientos para la codificación de caracteres en PHP

Las codificaciones de los siguientes tipos se pueden utilizar con PHP de forma segura.

- Codificaciones de un solo byte,

  - que tienen mapas de referencia compatibles con ASCII (ISO646) para los caracteres en el rango de `00h` a `7fh`.

- Codificación multibyte,

  - que tienen mapas de referencia compatibles con ASCII para los caracteres en el rango de `00h` a `7fh`.

  - que no utilizan secuencias de escape ISO2022.

  - que no utilizan un valor en el rango de `00h` a `7fh` en cualquiera de los bytes compuestos que representan un carácter sencillo.

Estos son ejemplos de codificaciones de caracteres que es poco probable que funcionen con PHP.

    JIS, SJIS, ISO-2022-JP, BIG-5

Aunque algunos scripts de PHP escritos en estas codificaciones podrían no funcionar, especialmente en el caso donde los strings codificados aparecen como identificadores o como literales en el propio script, se puede evitar el uso de estas codificaciones configurando la función de filtro de codificación transparente de `mbstring` para las consultas HTTP entrantes.

> [!NOTE]
> Se desaconseja energicamente el uso de SJIS, BIG5, CP936, CP949 y GB18030 para la codificación interna, a menos que se esté familiarizado con el analizador, el explorador y la codificación de caracteres.

> [!NOTE]
> Si se va a conectar a una base de datos con PHP, se recomienda utilizar la misma codificación de caracteres para la base de datos y la `codificación interna` para un uso más sencillo y un mejor rendimiento.
>
> Si se utiliza PostgreSQL, la codificación utilizada en la base de datos y la utilizada en PHP puede ser distinta debido a que se admite la conversión automática del conjunto de caracteres entre la parte final y la inicial del proceso.
