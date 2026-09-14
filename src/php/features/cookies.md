---
title: Cookies
source_url: https://www.php.net/manual/es/features.cookies.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: features/cookies.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: features
translation_status: ready
translation_reviewed: true
translation_revision: 3e08a8aae
order: 1540
---

## Cookies

PHP soporta las cookies HTTP de manera transparente. Las cookies son un mecanismo de almacenamiento de información en el cliente, y de lectura de dicha información. Este sistema permite identificar y seguir a los visitantes. Se puede enviar una cookie con la función `setcookie` o `setrawcookie`. Las cookies forman parte de los encabezados HTTP, lo que impone que `setcookie` sea llamada antes de cualquier visualización de texto. Estas son las mismas limitaciones que para `header`. Se pueden utilizar las funciones [de bufferización de salida](#ref.outcontrol) para retrasar la visualización de su script hasta que se haya decidido enviar una cookie o encabezados.

Todas las cookies enviadas al servidor por el cliente serán automáticamente incluidas en un array superglobal `$_COOKIE` si [variables_order](#ini.variables-order) contiene "C". Si se desea asignar múltiples valores a una sola cookie, se debe añadir `[]` al nombre de la cookie.

Para más detalles, incluyendo notas sobre errores de los navegadores, ver las funciones `setcookie` y `setrawcookie`.
