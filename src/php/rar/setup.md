---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/rar.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68680
---

## Instalación/Configuración

## Instalación

Rar está actualmente disponible a través de PECL <https://pecl.php.net/package/rar>.

Puede utilizarse el asistente de instalación PECL para instalar la extensión Rar, utilizando el siguiente comando: `pecl -v install rar`.

Asimismo, puede descargarse el paquete `tar.gz` e instalarse Rar manualmente:

Instalación de Rar

```php
gunzip rar-xxx.tgz
tar -xvf rar-xxx.tar
cd rar-xxx
phpize
./configure && make && make install

    
```

Los usuarios de Windows deben activar la biblioteca `php_rar.dll` en el archivo `php.ini` para utilizar estas funciones.

## Tipos de recursos

Esta extensión registra 3 clases internas: La representación del archivo retornada por la función `rar_open` – `RarArchive`, la representación de las entradas retornadas por las funciones `rar_list` y `rar_entry_get` – `RarEntry` y las excepciones de tipo `RarException`.

Esta extensión registra también un flujo de recurso llamado "rar" y un gestor de url llamado "rar wrapper", registrado bajo el prefijo "rar".
