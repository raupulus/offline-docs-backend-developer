---
title: Intl.Locale.prototype.script
source_repo: mdn/content
source_ref: main
source_commit: c9a52b432
source_path: reference/global_objects/intl/locale/script/index.md
technology: javascript
version: main
license: CC-BY-SA-2.5
retrieved_at: '2026-08-02'
section: reference
order: 5030
---

The **`script`** accessor property of {{jsxref("Intl.Locale")}} instances returns the script used for writing the particular language used in this locale.

## Description

Script, sometimes called writing system, is one of the core attributes of a locale. It indicates the set of symbols, or glyphs, that are used to write a particular language. For instance, the script associated with English is Latin, whereas the script typically associated with Korean is Hangul. In many cases, denoting a script is not strictly necessary, since the language (which is necessary) is only written in a single script. There are exceptions to this rule, however, and it is important to indicate the script when multiple scripts are applicable.

The `script` property's value is set at construction time, either through the part of the locale identifier after `language` or through the `script` option of the {{jsxref("Intl/Locale/Locale", "Intl.Locale()")}} constructor. The latter takes priority if they are both present; and if neither is present, the property has value `undefined`.

The set accessor of `script` is `undefined`. You cannot change this property directly.

## Examples

Like other locale subtags, the script can be added to the {{jsxref("Intl.Locale")}} object via the locale string, or a configuration object argument to the constructor.

### Adding a script via the locale string

The script, if present, is the second part of a valid Unicode language identifier string, and can be added to the initial locale identifier string that is passed into the {{jsxref("Intl/Locale/Locale", "Intl.Locale()")}} constructor. Note that the script is not a required part of a locale identifier.

```js
const locale = new Intl.Locale("en-Latn-US");
console.log(locale.script); // "Latn"
```

### Adding a script via the configuration object argument

The {{jsxref("Intl/Locale/Locale", "Intl.Locale()")}} constructor has an optional configuration object argument. Set the `script` property of the configuration object to your desired script, and then pass it into the constructor.

```js
const locale = new Intl.Locale("fr-FR", { script: "Latn" });
console.log(locale.script); // "Latn"
```

## Specifications

{{Specifications}}

## Browser compatibility

{{Compat}}

## See also

- {{jsxref("Intl.Locale")}}
- [Unicode script subtag](https://www.unicode.org/reports/tr35/#unicode_script_subtag_validity) in the Unicode locale data markup language spec
