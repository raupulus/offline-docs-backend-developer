---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/xattr.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xattr/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xattr
translation_status: ready
translation_revision: 86e6094e8
order: 102000
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`XATTR_ROOT` (`int`)  
Establece atributos en la raíz (segura) de espacio de nombres. Requiere privilegios de administrador.

`XATTR_DONTFOLLOW` (`int`)  
No sigue el enlace simbólico pero se puede operar en este.

`XATTR_CREATE` (`int`)  
La función falla si el atributo extendido ya existe.

`XATTR_REPLACE` (`int`)  
La función falla si el atributo extendido no existe.
