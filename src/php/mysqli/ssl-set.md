---
title: mysqli::ssl_set
description: Utilizada para establecer una conexión segura con SSL
source_url: https://www.php.net/manual/es/mysqli.ssl-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/ssl-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 497c40ac1
order: 55380
---

mysqli::ssl_set

mysqli_ssl_set

Utilizada para establecer una conexión segura con SSL

## Descripción

Estilo orientado a objetos

```php
public mysqli::ssl_set(string $key, string $certificate, string $ca_certificate, string $ca_path, string $cipher_algos): true
```php

Estilo procedimental

```php
mysqli_ssl_set(mysqli $mysql, string $key, string $certificate, string $ca_certificate, string $ca_path, string $cipher_algos): true
```

Utilizada para establecer una conexión segura con SSL. Debe ser llamada antes de `mysqli_real_connect`. Esta función no hace nada si el soporte OpenSSL no está activado.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`key`  
La ruta hacia el fichero que contiene la clave.

`certificate`  
La ruta hacia el fichero que contiene el certificado.

`ca_certificate`  
La ruta hacia el fichero que contiene la autoridad del certificado.

`ca_path`  
La ruta hacia el directorio que contiene los certificados SSL CA en formato PEM.

`cipher_algos`  
La lista de cifrados autorizados para ser utilizados en el cifrado SSL.

## Valores devueltos

Retorna siempre `true`. Si SSL no está correctamente instalado, `mysqli_real_connect` retornará un error cuando se intente una conexión.

## Véase también

`mysqli_options`, `mysqli_real_connect`
