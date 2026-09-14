---
title: Errores de Socket
source_url: https://www.php.net/manual/es/sockets.errors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/errors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_revision: f453f7036
order: 75500
---

## Errores de Socket

La extensión socket fue escrita para proporcionar una interfaz utilizable para los poderosos sockets de BSD. Se ha tenido cuidado en hacer que las funciones trabajen igualmente bien en implementaciones de Win32 y Unix. Casi todas las funciones de sockets pueden fallar bajo ciertas condiciones y por lo tanto emitir un mensaje `E_WARNING` describiendo el error. Algunas veces esto no ocurre para los deseos del desarrollador. Por ejemplo, la función `socket_read` puede de pronto emitir un mensaje `E_WARNING` porque la conexión se quebró de improvisto. Es común suprimir la advertencia con el operador `@` y capturar el código de error dentro de la aplicación con la función `socket_last_error`. Se puede llamar a la función `socket_strerror` con este código de error para recuperar una cadena describiendo el error. Vea su descripción para más información.

> [!NOTE]
> Los mensajes `E_WARNING` generados por la extensión socket están en inglés aunque el mensaje de error recuperado aparecéra según la configuración regional actual (`LC_MESSAGES`):
>
>     Warning - socket_bind() unable to bind address [98]: Die Adresse wird bereits verwendet
>
>
