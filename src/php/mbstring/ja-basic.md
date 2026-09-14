---
title: Casos de caracteres japoneses
source_url: https://www.php.net/manual/es/mbstring.ja-basic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/ja-basic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 8cdc6621f
order: 45630
---

## Casos de caracteres japoneses

Los caracteres japoneses solo pueden ser representados con encodings multiocteto y los estándares de encoding múltiple se utilizan según la plataforma y el texto de referencia. Para facilitar las cosas, estos estándares de encodings difieren ligeramente entre sí. Para desarrollar aplicaciones Web en entorno japonés, el desarrollador deberá tener en cuenta estas complejidades a fin de asegurarse de que se utilice el encoding de caracteres correcto.

- El tamaño necesario para un carácter puede llegar hasta 4 octetos.

- Un carácter japonés multiocteto ocupa generalmente dos octetos, en comparación con los caracteres mono-octeto tradicionalmente utilizados. Estos caracteres se denominan `"zen-kaku"`, lo que significa `"gran anchura"`. Los más pequeños se denominan `"han-kaku"`, lo que significa `"media anchura"`.

- Algunos encodings de caracteres utilizan secuencias `"shift"` (escape) definidas en la referencia ISO-2022 para cambiar a la tabla de encoding del código específico (`00h` a `7fh`).

- ISO-2022-JP debe ser utilizado para los protocolos SMTP/NNTP, y los encabezados así como las entidades deberían ser reencodificados de acuerdo con la RFC correspondiente. Aunque esto no es requerido, sigue siendo una buena idea ya que muchos user-agent (agentes de usuario) populares no pueden reconocer otro método de encoding.

- Las páginas Web creadas para teléfonos móviles como [i-mode](http://www.nttdocomo.com/services/imode/), o [EZweb](http://www.au.kddi.com/english/service/ezweb/index.html) están supuestas a utilizar el encoding Shift_JIS.

- Los emojis utilizados para teléfonos móviles, tales como [i-mode](http://www.nttdocomo.com/services/imode/) o [EZweb](http://www.au.kddi.com/english/service/ezweb/index.html) son soportados.
