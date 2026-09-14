---
title: Errores de Flujos
source_url: https://www.php.net/manual/es/stream.errors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/errors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: 96c9d88ba
order: 87750
---

## Errores de Flujos

Como con cualquier función relacionada con un archivo o con un socket, una operación sobre un flujo puede fallar por varias razones normales (esto es: Incapaz de conectarse al host remoto, archivo no encontrado, etc...). Una llamada relacionada con un flujo puede también fallar porque el flujo no está registrado en el sistema en ejecución. Véase la matriz devuelta por `stream_get_wrappers` para una lista de los flujos soportados por su instalación de PHP. Como con la mayoría de la funciones internas de PHP, si ocurre un error se generará un mensaje `E_WARNING` describiendo la naturaleza del error.
