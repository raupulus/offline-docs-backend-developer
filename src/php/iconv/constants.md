---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/iconv.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/iconv/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: iconv
translation_status: ready
translation_reviewed: true
translation_revision: 5208882ce
order: 31160
---

## Constantes predefinidas

Es posible identificar durante la ejecución, la versión de la biblioteca iconv que se utiliza.

| Constante                  | Tipo     | Descripción                 |
|----------------------------|----------|-----------------------------|
| `ICONV_IMPL` (`string`)    | `string` | El nombre de la biblioteca  |
| `ICONV_VERSION` (`string`) | `string` | La versión de la biblioteca |

Constantes de implementación `iconv`

> [!NOTE]
> La programación de scripts dependientes de versiones específicas, con estas constantes, está fuertemente desaconsejada.

Las constantes siguientes también están disponibles :

| Constante | Tipo | Descripción |
|----|----|----|
| `ICONV_MIME_DECODE_STRICT` (`int`) | `int` | Una máscara utilizada por `iconv_mime_decode` |
| `ICONV_MIME_DECODE_CONTINUE_ON_ERROR` (`int`) | `int` | Una máscara utilizada para `iconv_mime_decode` |

Otras constantes `iconv`
