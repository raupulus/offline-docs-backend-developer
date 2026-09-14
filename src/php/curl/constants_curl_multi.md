---
title: curl_multi_* constantes de estado
source_url: https://www.php.net/manual/es/constant.curl-multi.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/constants_curl_multi.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 92e188ab7
order: 9630
---

`CURLM_ADDED_ALREADY` (`int`)  
Un gestor fácil ya añadido a un gestor múltiple ha sido intentado ser añadido una segunda vez. Disponible a partir de cURL 7.32.1.

`CURLM_BAD_EASY_HANDLE` (`int`)  
Un gestor fácil no era bueno/válido. Esto podría significar que no se trata de un gestor fácil en absoluto, o eventualmente que el gestor ya está siendo utilizado por este o por otro gestor múltiple. Disponible a partir de cURL 7.9.6.

`CURLM_BAD_HANDLE` (`int`)  
El gestor pasado no es un gestor múltiple válido. Disponible a partir de cURL 7.9.6.

`CURLM_CALL_MULTI_PERFORM` (`int`)  
Desde cURL 7.20.0, esta constante no se utiliza. Antes de cURL 7.20.0, este estado podía ser devuelto por `curl_multi_exec` cuando `curl_multi_select` o una función similar era llamada antes de que devolviera otra constante. Disponible a partir de cURL 7.9.6.

`CURLM_INTERNAL_ERROR` (`int`)  
Error interno de `libcurl`.

`CURLM_OK` (`int`)  
Ningún error. Disponible a partir de cURL 7.9.6.

`CURLM_OUT_OF_MEMORY` (`int`)  
No hay suficiente memoria al procesar los gestores múltiples. Disponible a partir de cURL 7.9.6.
