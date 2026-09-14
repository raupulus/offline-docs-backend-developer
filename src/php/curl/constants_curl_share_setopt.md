---
title: curl_share_setopt
source_url: https://www.php.net/manual/es/constant.curl-share-setopt.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/constants_curl_share_setopt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 2423fc979
order: 9670
---

`CURL_LOCK_DATA_CONNECT` (`int`)  
Comparte/descomparte la conexión. Disponible a partir de PHP 7.3.0 y cURL 7.10.3.

`CURL_LOCK_DATA_COOKIE` (`int`)  
Comparte/descomparte los datos de cookie. Disponible a partir de cURL 7.10.3.

`CURL_LOCK_DATA_DNS` (`int`)  
Comparte/descomparte la caché DNS. Es de notar que cuando se utilizan múltiples gestores cURL, todos los gestores añadidos al gestor múltiple compartirán la caché DNS por omisión. Disponible a partir de cURL 7.10.3.

`CURL_LOCK_DATA_PSL` (`int`)  
Comparte/descomparte la lista de sufijos públicos. Disponible a partir de PHP 7.3.0 y cURL 7.61.0.

`CURL_LOCK_DATA_SSL_SESSION` (`int`)  
Comparte/descomparte los identificadores de sesión SSL, reduciendo el tiempo pasado en la gestión SSL al reconectar al mismo servidor. Es de notar que los identificadores de sesión SSL son reutilizados en el mismo gestor por omisión. Disponible a partir de cURL 7.10.3.

`CURLSHOPT_NONE` (`int`)  
Disponible a partir de cURL 7.10.3.

`CURLSHOPT_SHARE` (`int`)  
Especifica un tipo de datos a compartir. Disponible a partir de cURL 7.10.3.

`CURLSHOPT_UNSHARE` (`int`)  
Especifica un tipo de datos que ya no será compartido. Disponible a partir de cURL 7.10.3.
