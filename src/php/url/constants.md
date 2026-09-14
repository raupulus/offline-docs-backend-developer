---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/url.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_revision: a0ae28d3b
order: 100180
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Las siguientes constantes están pensadas para usarse con `parse_url`.

`PHP_URL_SCHEME` (`int`)  

`PHP_URL_HOST` (`int`)  
Muestra el nombre del host del URL analizado.

`PHP_URL_PORT` (`int`)  
Muestra el puerto del URL analizado.

`PHP_URL_USER` (`int`)  
Muestra el usuario del URL analizado.

`PHP_URL_PASS` (`int`)  
Muestra la contraseña del URL analizado.

`PHP_URL_PATH` (`int`)  
Muestra la ruta del URL analizado.

`PHP_URL_QUERY` (`int`)  
Muestra el string de consulta del URL analizado.

`PHP_URL_FRAGMENT` (`int`)  
Muestra el fragmento (string después del símbolo \#) del URL analizado.

Las siguientes constantes están pensadas para utilizarlas con `http_build_query`.

`PHP_QUERY_RFC1738` (`int`)  
Codificación realizada por [RFC 1738](https://datatracker.ietf.org/doc/html/rfc1738) y el tipo de media `application/x-www-form-urlencoded`, lo que implica que los espacios están codificados como signos "más" (`+`).

`PHP_QUERY_RFC3986` (`int`)  
La codificación se lleva a cabo según el [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986), y los espacios se cofificarán con porcentajes (`%20`).
