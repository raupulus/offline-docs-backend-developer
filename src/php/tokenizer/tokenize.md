---
title: PhpToken::tokenize
description: Separa el código fuente dado en tokens PHP, representado por objetos
  PhpToken.
source_url: https://www.php.net/manual/es/phptoken.tokenize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/phptoken/tokenize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 0e51e26bd
order: 94420
---

PhpToken::tokenize

Separa el código fuente dado en tokens PHP, representado por objetos PhpToken.

## Descripción

```php
public static PhpToken::tokenize(string $code, [int $flags]): array
```php

Devuelve un array de objetos PhpToken que representan el código (`code`) dado.

## Parámetros

`code`  
El código fuente PHP a analizar.

`flags`  
Flags válidos:

- `TOKEN_PARSE` - Reconoce la posibilidad de usar palabras reservadas en contextos específicos.

## Valores devueltos

Un array de tokens PHP representado por instancias de PhpToken o de sus descendientes. Este método devuelve `static[]` para que PhpToken pueda ser extendido de manera transparente.

## Ejemplos

Ejemplo de `PhpToken::tokenize`

```
<?php
$tokens = PhpToken::tokenize('<?php echo; ?>');

foreach ($tokens as $token) {
    echo "Line {$token->line}: {$token->getTokenName()} ('{$token->text}')", PHP_EOL;
}

   
```php

Los ejemplos anteriores mostrarán:

    Line 1: T_OPEN_TAG ('<?php ')
    Line 1: T_ECHO ('echo')
    Line 1: ; (';')
    Line 1: T_WHITESPACE (' ')
    Line 1: T_CLOSE_TAG ('?>')

Extensión de PhpToken

```
<?php

class MyPhpToken extends PhpToken {
    public function getUpperText() {
        return strtoupper($this->text);
    }
}

$tokens = MyPhpToken::tokenize('<?php echo; ?>');
echo "'{$tokens[0]->getUpperText()}'";

   
```php

Los ejemplos anteriores mostrarán:

    '<?PHP '

## Véase también

token_get_all
