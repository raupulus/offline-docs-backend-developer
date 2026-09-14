---
title: IntlChar
source_url: https://www.php.net/manual/es/class.intlchar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 63bd68a3f
order: 41270
---

## Introducción

`IntlChar` proporciona acceso a un conjunto de métodos utilitarios que pueden ser utilizados para acceder a información sobre los caracteres Unicode.

Los métodos y las constantes respetan estrictamente los nombres y el comportamiento utilizados por la biblioteca ICU subyacente.

## Sinopsis de la clase

IntlChar

Constantes

public

const

string

IntlChar::UNICODE_VERSION

public

const

int

IntlChar::CODEPOINT_MIN

public

const

int

IntlChar::CODEPOINT_MAX

public

const

float

IntlChar::NO_NUMERIC_VALUE

public

const

int

IntlChar::PROPERTY_ALPHABETIC

public

const

int

IntlChar::PROPERTY_BINARY_START

public

const

int

IntlChar::PROPERTY_ASCII_HEX_DIGIT

public

const

int

IntlChar::PROPERTY_BIDI_CONTROL

public

const

int

IntlChar::PROPERTY_BIDI_MIRRORED

public

const

int

IntlChar::PROPERTY_DASH

public

const

int

IntlChar::PROPERTY_DEFAULT_IGNORABLE_CODE_POINT

public

const

int

IntlChar::PROPERTY_DEPRECATED

public

const

int

IntlChar::PROPERTY_DIACRITIC

public

const

int

IntlChar::PROPERTY_EXTENDER

public

const

int

IntlChar::PROPERTY_FULL_COMPOSITION_EXCLUSION

public

const

int

IntlChar::PROPERTY_GRAPHEME_BASE

public

const

int

IntlChar::PROPERTY_GRAPHEME_EXTEND

public

const

int

IntlChar::PROPERTY_GRAPHEME_LINK

public

const

int

IntlChar::PROPERTY_HEX_DIGIT

public

const

int

IntlChar::PROPERTY_HYPHEN

public

const

int

IntlChar::PROPERTY_ID_CONTINUE

public

const

int

IntlChar::PROPERTY_ID_START

public

const

int

IntlChar::PROPERTY_IDEOGRAPHIC

public

const

int

IntlChar::PROPERTY_IDS_BINARY_OPERATOR

public

const

int

IntlChar::PROPERTY_IDS_TRINARY_OPERATOR

public

const

int

IntlChar::PROPERTY_IDS_UNARY_OPERATOR

public

const

int

IntlChar::PROPERTY_ID_COMPAT_MATH_START

public

const

int

IntlChar::PROPERTY_ID_COMPAT_MATH_CONTINUE

public

const

int

IntlChar::PROPERTY_JOIN_CONTROL

public

const

int

IntlChar::PROPERTY_LOGICAL_ORDER_EXCEPTION

public

const

int

IntlChar::PROPERTY_LOWERCASE

public

const

int

IntlChar::PROPERTY_MATH

public

const

int

IntlChar::PROPERTY_NONCHARACTER_CODE_POINT

public

const

int

IntlChar::PROPERTY_QUOTATION_MARK

public

const

int

IntlChar::PROPERTY_RADICAL

public

const

int

IntlChar::PROPERTY_SOFT_DOTTED

public

const

int

IntlChar::PROPERTY_TERMINAL_PUNCTUATION

public

const

int

IntlChar::PROPERTY_UNIFIED_IDEOGRAPH

public

const

int

IntlChar::PROPERTY_UPPERCASE

public

const

int

IntlChar::PROPERTY_WHITE_SPACE

public

const

int

IntlChar::PROPERTY_XID_CONTINUE

public

const

int

IntlChar::PROPERTY_XID_START

public

const

int

IntlChar::PROPERTY_CASE_SENSITIVE

public

const

int

IntlChar::PROPERTY_S_TERM

public

const

int

IntlChar::PROPERTY_VARIATION_SELECTOR

public

const

int

IntlChar::PROPERTY_NFD_INERT

public

const

int

IntlChar::PROPERTY_NFKD_INERT

public

const

int

IntlChar::PROPERTY_NFC_INERT

public

const

int

IntlChar::PROPERTY_NFKC_INERT

public

const

int

IntlChar::PROPERTY_SEGMENT_STARTER

public

const

int

IntlChar::PROPERTY_PATTERN_SYNTAX

public

const

int

IntlChar::PROPERTY_PATTERN_WHITE_SPACE

public

const

int

IntlChar::PROPERTY_POSIX_ALNUM

public

const

int

IntlChar::PROPERTY_POSIX_BLANK

public

const

int

IntlChar::PROPERTY_POSIX_GRAPH

public

const

int

IntlChar::PROPERTY_POSIX_PRINT

public

const

int

IntlChar::PROPERTY_POSIX_XDIGIT

public

const

int

IntlChar::PROPERTY_CASED

public

const

int

IntlChar::PROPERTY_CASE_IGNORABLE

public

const

int

IntlChar::PROPERTY_CHANGES_WHEN_LOWERCASED

public

const

int

IntlChar::PROPERTY_CHANGES_WHEN_UPPERCASED

public

const

int

IntlChar::PROPERTY_CHANGES_WHEN_TITLECASED

public

const

int

IntlChar::PROPERTY_CHANGES_WHEN_CASEFOLDED

public

const

int

IntlChar::PROPERTY_CHANGES_WHEN_CASEMAPPED

public

const

int

IntlChar::PROPERTY_CHANGES_WHEN_NFKC_CASEFOLDED

public

const

int

IntlChar::PROPERTY_BINARY_LIMIT

public

const

int

IntlChar::PROPERTY_BIDI_CLASS

public

const

int

IntlChar::PROPERTY_INT_START

public

const

int

IntlChar::PROPERTY_BLOCK

public

const

int

IntlChar::PROPERTY_CANONICAL_COMBINING_CLASS

public

const

int

IntlChar::PROPERTY_DECOMPOSITION_TYPE

public

const

int

IntlChar::PROPERTY_EAST_ASIAN_WIDTH

public

const

int

IntlChar::PROPERTY_GENERAL_CATEGORY

public

const

int

IntlChar::PROPERTY_JOINING_GROUP

public

const

int

IntlChar::PROPERTY_JOINING_TYPE

public

const

int

IntlChar::PROPERTY_LINE_BREAK

public

const

int

IntlChar::PROPERTY_NUMERIC_TYPE

public

const

int

IntlChar::PROPERTY_SCRIPT

public

const

int

IntlChar::PROPERTY_HANGUL_SYLLABLE_TYPE

public

const

int

IntlChar::PROPERTY_NFD_QUICK_CHECK

public

const

int

IntlChar::PROPERTY_NFKD_QUICK_CHECK

public

const

int

IntlChar::PROPERTY_NFC_QUICK_CHECK

public

const

int

IntlChar::PROPERTY_NFKC_QUICK_CHECK

public

const

int

IntlChar::PROPERTY_LEAD_CANONICAL_COMBINING_CLASS

public

const

int

IntlChar::PROPERTY_TRAIL_CANONICAL_COMBINING_CLASS

public

const

int

IntlChar::PROPERTY_GRAPHEME_CLUSTER_BREAK

public

const

int

IntlChar::PROPERTY_SENTENCE_BREAK

public

const

int

IntlChar::PROPERTY_WORD_BREAK

public

const

int

IntlChar::PROPERTY_BIDI_PAIRED_BRACKET_TYPE

public

const

int

IntlChar::PROPERTY_INT_LIMIT

public

const

int

IntlChar::PROPERTY_GENERAL_CATEGORY_MASK

public

const

int

IntlChar::PROPERTY_MASK_START

public

const

int

IntlChar::PROPERTY_MASK_LIMIT

public

const

int

IntlChar::PROPERTY_NUMERIC_VALUE

public

const

int

IntlChar::PROPERTY_DOUBLE_START

public

const

int

IntlChar::PROPERTY_DOUBLE_LIMIT

public

const

int

IntlChar::PROPERTY_AGE

public

const

int

IntlChar::PROPERTY_STRING_START

public

const

int

IntlChar::PROPERTY_BIDI_MIRRORING_GLYPH

public

const

int

IntlChar::PROPERTY_CASE_FOLDING

public

const

int

IntlChar::PROPERTY_ISO_COMMENT

public

const

int

IntlChar::PROPERTY_LOWERCASE_MAPPING

public

const

int

IntlChar::PROPERTY_NAME

public

const

int

IntlChar::PROPERTY_SIMPLE_CASE_FOLDING

public

const

int

IntlChar::PROPERTY_SIMPLE_LOWERCASE_MAPPING

public

const

int

IntlChar::PROPERTY_SIMPLE_TITLECASE_MAPPING

public

const

int

IntlChar::PROPERTY_SIMPLE_UPPERCASE_MAPPING

public

const

int

IntlChar::PROPERTY_TITLECASE_MAPPING

public

const

int

IntlChar::PROPERTY_UNICODE_1_NAME

public

const

int

IntlChar::PROPERTY_UPPERCASE_MAPPING

public

const

int

IntlChar::PROPERTY_BIDI_PAIRED_BRACKET

public

const

int

IntlChar::PROPERTY_STRING_LIMIT

public

const

int

IntlChar::PROPERTY_SCRIPT_EXTENSIONS

public

const

int

IntlChar::PROPERTY_OTHER_PROPERTY_START

public

const

int

IntlChar::PROPERTY_OTHER_PROPERTY_LIMIT

public

const

int

IntlChar::PROPERTY_INVALID_CODE

public

const

int

IntlChar::CHAR_CATEGORY_UNASSIGNED

public

const

int

IntlChar::CHAR_CATEGORY_GENERAL_OTHER_TYPES

public

const

int

IntlChar::CHAR_CATEGORY_UPPERCASE_LETTER

public

const

int

IntlChar::CHAR_CATEGORY_LOWERCASE_LETTER

public

const

int

IntlChar::CHAR_CATEGORY_TITLECASE_LETTER

public

const

int

IntlChar::CHAR_CATEGORY_MODIFIER_LETTER

public

const

int

IntlChar::CHAR_CATEGORY_OTHER_LETTER

public

const

int

IntlChar::CHAR_CATEGORY_NON_SPACING_MARK

public

const

int

IntlChar::CHAR_CATEGORY_ENCLOSING_MARK

public

const

int

IntlChar::CHAR_CATEGORY_COMBINING_SPACING_MARK

public

const

int

IntlChar::CHAR_CATEGORY_DECIMAL_DIGIT_NUMBER

public

const

int

IntlChar::CHAR_CATEGORY_LETTER_NUMBER

public

const

int

IntlChar::CHAR_CATEGORY_OTHER_NUMBER

public

const

int

IntlChar::CHAR_CATEGORY_SPACE_SEPARATOR

public

const

int

IntlChar::CHAR_CATEGORY_LINE_SEPARATOR

public

const

int

IntlChar::CHAR_CATEGORY_PARAGRAPH_SEPARATOR

public

const

int

IntlChar::CHAR_CATEGORY_CONTROL_CHAR

public

const

int

IntlChar::CHAR_CATEGORY_FORMAT_CHAR

public

const

int

IntlChar::CHAR_CATEGORY_PRIVATE_USE_CHAR

public

const

int

IntlChar::CHAR_CATEGORY_SURROGATE

public

const

int

IntlChar::CHAR_CATEGORY_DASH_PUNCTUATION

public

const

int

IntlChar::CHAR_CATEGORY_START_PUNCTUATION

public

const

int

IntlChar::CHAR_CATEGORY_END_PUNCTUATION

public

const

int

IntlChar::CHAR_CATEGORY_CONNECTOR_PUNCTUATION

public

const

int

IntlChar::CHAR_CATEGORY_OTHER_PUNCTUATION

public

const

int

IntlChar::CHAR_CATEGORY_MATH_SYMBOL

public

const

int

IntlChar::CHAR_CATEGORY_CURRENCY_SYMBOL

public

const

int

IntlChar::CHAR_CATEGORY_MODIFIER_SYMBOL

public

const

int

IntlChar::CHAR_CATEGORY_OTHER_SYMBOL

public

const

int

IntlChar::CHAR_CATEGORY_INITIAL_PUNCTUATION

public

const

int

IntlChar::CHAR_CATEGORY_FINAL_PUNCTUATION

public

const

int

IntlChar::CHAR_CATEGORY_CHAR_CATEGORY_COUNT

public

const

int

IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT

public

const

int

IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT

public

const

int

IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER

public

const

int

IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER_SEPARATOR

public

const

int

IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER_TERMINATOR

public

const

int

IntlChar::CHAR_DIRECTION_ARABIC_NUMBER

public

const

int

IntlChar::CHAR_DIRECTION_COMMON_NUMBER_SEPARATOR

public

const

int

IntlChar::CHAR_DIRECTION_BLOCK_SEPARATOR

public

const

int

IntlChar::CHAR_DIRECTION_SEGMENT_SEPARATOR

public

const

int

IntlChar::CHAR_DIRECTION_WHITE_SPACE_NEUTRAL

public

const

int

IntlChar::CHAR_DIRECTION_OTHER_NEUTRAL

public

const

int

IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_EMBEDDING

public

const

int

IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_OVERRIDE

public

const

int

IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_ARABIC

public

const

int

IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_EMBEDDING

public

const

int

IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_OVERRIDE

public

const

int

IntlChar::CHAR_DIRECTION_POP_DIRECTIONAL_FORMAT

public

const

int

IntlChar::CHAR_DIRECTION_DIR_NON_SPACING_MARK

public

const

int

IntlChar::CHAR_DIRECTION_BOUNDARY_NEUTRAL

public

const

int

IntlChar::CHAR_DIRECTION_FIRST_STRONG_ISOLATE

public

const

int

IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_ISOLATE

public

const

int

IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_ISOLATE

public

const

int

IntlChar::CHAR_DIRECTION_POP_DIRECTIONAL_ISOLATE

public

const

int

IntlChar::CHAR_DIRECTION_CHAR_DIRECTION_COUNT

public

const

int

IntlChar::BLOCK_CODE_NO_BLOCK

public

const

int

IntlChar::BLOCK_CODE_BASIC_LATIN

public

const

int

IntlChar::BLOCK_CODE_LATIN_1_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_LATIN_EXTENDED_A

public

const

int

IntlChar::BLOCK_CODE_LATIN_EXTENDED_B

public

const

int

IntlChar::BLOCK_CODE_IPA_EXTENSIONS

public

const

int

IntlChar::BLOCK_CODE_SPACING_MODIFIER_LETTERS

public

const

int

IntlChar::BLOCK_CODE_COMBINING_DIACRITICAL_MARKS

public

const

int

IntlChar::BLOCK_CODE_GREEK

public

const

int

IntlChar::BLOCK_CODE_CYRILLIC

public

const

int

IntlChar::BLOCK_CODE_ARMENIAN

public

const

int

IntlChar::BLOCK_CODE_HEBREW

public

const

int

IntlChar::BLOCK_CODE_ARABIC

public

const

int

IntlChar::BLOCK_CODE_SYRIAC

public

const

int

IntlChar::BLOCK_CODE_THAANA

public

const

int

IntlChar::BLOCK_CODE_DEVANAGARI

public

const

int

IntlChar::BLOCK_CODE_BENGALI

public

const

int

IntlChar::BLOCK_CODE_GURMUKHI

public

const

int

IntlChar::BLOCK_CODE_GUJARATI

public

const

int

IntlChar::BLOCK_CODE_ORIYA

public

const

int

IntlChar::BLOCK_CODE_TAMIL

public

const

int

IntlChar::BLOCK_CODE_TELUGU

public

const

int

IntlChar::BLOCK_CODE_KANNADA

public

const

int

IntlChar::BLOCK_CODE_MALAYALAM

public

const

int

IntlChar::BLOCK_CODE_SINHALA

public

const

int

IntlChar::BLOCK_CODE_THAI

public

const

int

IntlChar::BLOCK_CODE_LAO

public

const

int

IntlChar::BLOCK_CODE_TIBETAN

public

const

int

IntlChar::BLOCK_CODE_MYANMAR

public

const

int

IntlChar::BLOCK_CODE_GEORGIAN

public

const

int

IntlChar::BLOCK_CODE_HANGUL_JAMO

public

const

int

IntlChar::BLOCK_CODE_ETHIOPIC

public

const

int

IntlChar::BLOCK_CODE_CHEROKEE

public

const

int

IntlChar::BLOCK_CODE_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS

public

const

int

IntlChar::BLOCK_CODE_OGHAM

public

const

int

IntlChar::BLOCK_CODE_RUNIC

public

const

int

IntlChar::BLOCK_CODE_KHMER

public

const

int

IntlChar::BLOCK_CODE_MONGOLIAN

public

const

int

IntlChar::BLOCK_CODE_LATIN_EXTENDED_ADDITIONAL

public

const

int

IntlChar::BLOCK_CODE_GREEK_EXTENDED

public

const

int

IntlChar::BLOCK_CODE_GENERAL_PUNCTUATION

public

const

int

IntlChar::BLOCK_CODE_SUPERSCRIPTS_AND_SUBSCRIPTS

public

const

int

IntlChar::BLOCK_CODE_CURRENCY_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_COMBINING_MARKS_FOR_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_LETTERLIKE_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_NUMBER_FORMS

public

const

int

IntlChar::BLOCK_CODE_ARROWS

public

const

int

IntlChar::BLOCK_CODE_MATHEMATICAL_OPERATORS

public

const

int

IntlChar::BLOCK_CODE_MISCELLANEOUS_TECHNICAL

public

const

int

IntlChar::BLOCK_CODE_CONTROL_PICTURES

public

const

int

IntlChar::BLOCK_CODE_OPTICAL_CHARACTER_RECOGNITION

public

const

int

IntlChar::BLOCK_CODE_ENCLOSED_ALPHANUMERICS

public

const

int

IntlChar::BLOCK_CODE_BOX_DRAWING

public

const

int

IntlChar::BLOCK_CODE_BLOCK_ELEMENTS

public

const

int

IntlChar::BLOCK_CODE_GEOMETRIC_SHAPES

public

const

int

IntlChar::BLOCK_CODE_MISCELLANEOUS_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_DINGBATS

public

const

int

IntlChar::BLOCK_CODE_BRAILLE_PATTERNS

public

const

int

IntlChar::BLOCK_CODE_CJK_RADICALS_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_KANGXI_RADICALS

public

const

int

IntlChar::BLOCK_CODE_IDEOGRAPHIC_DESCRIPTION_CHARACTERS

public

const

int

IntlChar::BLOCK_CODE_CJK_SYMBOLS_AND_PUNCTUATION

public

const

int

IntlChar::BLOCK_CODE_HIRAGANA

public

const

int

IntlChar::BLOCK_CODE_KATAKANA

public

const

int

IntlChar::BLOCK_CODE_BOPOMOFO

public

const

int

IntlChar::BLOCK_CODE_HANGUL_COMPATIBILITY_JAMO

public

const

int

IntlChar::BLOCK_CODE_KANBUN

public

const

int

IntlChar::BLOCK_CODE_BOPOMOFO_EXTENDED

public

const

int

IntlChar::BLOCK_CODE_ENCLOSED_CJK_LETTERS_AND_MONTHS

public

const

int

IntlChar::BLOCK_CODE_CJK_COMPATIBILITY

public

const

int

IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A

public

const

int

IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS

public

const

int

IntlChar::BLOCK_CODE_YI_SYLLABLES

public

const

int

IntlChar::BLOCK_CODE_YI_RADICALS

public

const

int

IntlChar::BLOCK_CODE_HANGUL_SYLLABLES

public

const

int

IntlChar::BLOCK_CODE_HIGH_SURROGATES

public

const

int

IntlChar::BLOCK_CODE_HIGH_PRIVATE_USE_SURROGATES

public

const

int

IntlChar::BLOCK_CODE_LOW_SURROGATES

public

const

int

IntlChar::BLOCK_CODE_PRIVATE_USE_AREA

public

const

int

IntlChar::BLOCK_CODE_PRIVATE_USE

public

const

int

IntlChar::BLOCK_CODE_CJK_COMPATIBILITY_IDEOGRAPHS

public

const

int

IntlChar::BLOCK_CODE_ALPHABETIC_PRESENTATION_FORMS

public

const

int

IntlChar::BLOCK_CODE_ARABIC_PRESENTATION_FORMS_A

public

const

int

IntlChar::BLOCK_CODE_COMBINING_HALF_MARKS

public

const

int

IntlChar::BLOCK_CODE_CJK_COMPATIBILITY_FORMS

public

const

int

IntlChar::BLOCK_CODE_SMALL_FORM_VARIANTS

public

const

int

IntlChar::BLOCK_CODE_ARABIC_PRESENTATION_FORMS_B

public

const

int

IntlChar::BLOCK_CODE_SPECIALS

public

const

int

IntlChar::BLOCK_CODE_HALFWIDTH_AND_FULLWIDTH_FORMS

public

const

int

IntlChar::BLOCK_CODE_OLD_ITALIC

public

const

int

IntlChar::BLOCK_CODE_GOTHIC

public

const

int

IntlChar::BLOCK_CODE_DESERET

public

const

int

IntlChar::BLOCK_CODE_BYZANTINE_MUSICAL_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_MUSICAL_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_MATHEMATICAL_ALPHANUMERIC_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B

public

const

int

IntlChar::BLOCK_CODE_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_TAGS

public

const

int

IntlChar::BLOCK_CODE_CYRILLIC_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_CYRILLIC_SUPPLEMENTARY

public

const

int

IntlChar::BLOCK_CODE_TAGALOG

public

const

int

IntlChar::BLOCK_CODE_HANUNOO

public

const

int

IntlChar::BLOCK_CODE_BUHID

public

const

int

IntlChar::BLOCK_CODE_TAGBANWA

public

const

int

IntlChar::BLOCK_CODE_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A

public

const

int

IntlChar::BLOCK_CODE_SUPPLEMENTAL_ARROWS_A

public

const

int

IntlChar::BLOCK_CODE_SUPPLEMENTAL_ARROWS_B

public

const

int

IntlChar::BLOCK_CODE_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B

public

const

int

IntlChar::BLOCK_CODE_SUPPLEMENTAL_MATHEMATICAL_OPERATORS

public

const

int

IntlChar::BLOCK_CODE_KATAKANA_PHONETIC_EXTENSIONS

public

const

int

IntlChar::BLOCK_CODE_VARIATION_SELECTORS

public

const

int

IntlChar::BLOCK_CODE_SUPPLEMENTARY_PRIVATE_USE_AREA_A

public

const

int

IntlChar::BLOCK_CODE_SUPPLEMENTARY_PRIVATE_USE_AREA_B

public

const

int

IntlChar::BLOCK_CODE_LIMBU

public

const

int

IntlChar::BLOCK_CODE_TAI_LE

public

const

int

IntlChar::BLOCK_CODE_KHMER_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_PHONETIC_EXTENSIONS

public

const

int

IntlChar::BLOCK_CODE_MISCELLANEOUS_SYMBOLS_AND_ARROWS

public

const

int

IntlChar::BLOCK_CODE_YIJING_HEXAGRAM_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_LINEAR_B_SYLLABARY

public

const

int

IntlChar::BLOCK_CODE_LINEAR_B_IDEOGRAMS

public

const

int

IntlChar::BLOCK_CODE_AEGEAN_NUMBERS

public

const

int

IntlChar::BLOCK_CODE_UGARITIC

public

const

int

IntlChar::BLOCK_CODE_SHAVIAN

public

const

int

IntlChar::BLOCK_CODE_OSMANYA

public

const

int

IntlChar::BLOCK_CODE_CYPRIOT_SYLLABARY

public

const

int

IntlChar::BLOCK_CODE_TAI_XUAN_JING_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_VARIATION_SELECTORS_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_ANCIENT_GREEK_MUSICAL_NOTATION

public

const

int

IntlChar::BLOCK_CODE_ANCIENT_GREEK_NUMBERS

public

const

int

IntlChar::BLOCK_CODE_ARABIC_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_BUGINESE

public

const

int

IntlChar::BLOCK_CODE_CJK_STROKES

public

const

int

IntlChar::BLOCK_CODE_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_COPTIC

public

const

int

IntlChar::BLOCK_CODE_ETHIOPIC_EXTENDED

public

const

int

IntlChar::BLOCK_CODE_ETHIOPIC_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_GEORGIAN_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_GLAGOLITIC

public

const

int

IntlChar::BLOCK_CODE_KHAROSHTHI

public

const

int

IntlChar::BLOCK_CODE_MODIFIER_TONE_LETTERS

public

const

int

IntlChar::BLOCK_CODE_NEW_TAI_LUE

public

const

int

IntlChar::BLOCK_CODE_OLD_PERSIAN

public

const

int

IntlChar::BLOCK_CODE_PHONETIC_EXTENSIONS_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_SUPPLEMENTAL_PUNCTUATION

public

const

int

IntlChar::BLOCK_CODE_SYLOTI_NAGRI

public

const

int

IntlChar::BLOCK_CODE_TIFINAGH

public

const

int

IntlChar::BLOCK_CODE_VERTICAL_FORMS

public

const

int

IntlChar::BLOCK_CODE_NKO

public

const

int

IntlChar::BLOCK_CODE_BALINESE

public

const

int

IntlChar::BLOCK_CODE_LATIN_EXTENDED_C

public

const

int

IntlChar::BLOCK_CODE_LATIN_EXTENDED_D

public

const

int

IntlChar::BLOCK_CODE_PHAGS_PA

public

const

int

IntlChar::BLOCK_CODE_PHOENICIAN

public

const

int

IntlChar::BLOCK_CODE_CUNEIFORM

public

const

int

IntlChar::BLOCK_CODE_CUNEIFORM_NUMBERS_AND_PUNCTUATION

public

const

int

IntlChar::BLOCK_CODE_COUNTING_ROD_NUMERALS

public

const

int

IntlChar::BLOCK_CODE_SUNDANESE

public

const

int

IntlChar::BLOCK_CODE_LEPCHA

public

const

int

IntlChar::BLOCK_CODE_OL_CHIKI

public

const

int

IntlChar::BLOCK_CODE_CYRILLIC_EXTENDED_A

public

const

int

IntlChar::BLOCK_CODE_VAI

public

const

int

IntlChar::BLOCK_CODE_CYRILLIC_EXTENDED_B

public

const

int

IntlChar::BLOCK_CODE_SAURASHTRA

public

const

int

IntlChar::BLOCK_CODE_KAYAH_LI

public

const

int

IntlChar::BLOCK_CODE_REJANG

public

const

int

IntlChar::BLOCK_CODE_CHAM

public

const

int

IntlChar::BLOCK_CODE_ANCIENT_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_PHAISTOS_DISC

public

const

int

IntlChar::BLOCK_CODE_LYCIAN

public

const

int

IntlChar::BLOCK_CODE_CARIAN

public

const

int

IntlChar::BLOCK_CODE_LYDIAN

public

const

int

IntlChar::BLOCK_CODE_MAHJONG_TILES

public

const

int

IntlChar::BLOCK_CODE_DOMINO_TILES

public

const

int

IntlChar::BLOCK_CODE_SAMARITAN

public

const

int

IntlChar::BLOCK_CODE_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED

public

const

int

IntlChar::BLOCK_CODE_TAI_THAM

public

const

int

IntlChar::BLOCK_CODE_VEDIC_EXTENSIONS

public

const

int

IntlChar::BLOCK_CODE_LISU

public

const

int

IntlChar::BLOCK_CODE_BAMUM

public

const

int

IntlChar::BLOCK_CODE_COMMON_INDIC_NUMBER_FORMS

public

const

int

IntlChar::BLOCK_CODE_DEVANAGARI_EXTENDED

public

const

int

IntlChar::BLOCK_CODE_HANGUL_JAMO_EXTENDED_A

public

const

int

IntlChar::BLOCK_CODE_JAVANESE

public

const

int

IntlChar::BLOCK_CODE_MYANMAR_EXTENDED_A

public

const

int

IntlChar::BLOCK_CODE_TAI_VIET

public

const

int

IntlChar::BLOCK_CODE_MEETEI_MAYEK

public

const

int

IntlChar::BLOCK_CODE_HANGUL_JAMO_EXTENDED_B

public

const

int

IntlChar::BLOCK_CODE_IMPERIAL_ARAMAIC

public

const

int

IntlChar::BLOCK_CODE_OLD_SOUTH_ARABIAN

public

const

int

IntlChar::BLOCK_CODE_AVESTAN

public

const

int

IntlChar::BLOCK_CODE_INSCRIPTIONAL_PARTHIAN

public

const

int

IntlChar::BLOCK_CODE_INSCRIPTIONAL_PAHLAVI

public

const

int

IntlChar::BLOCK_CODE_OLD_TURKIC

public

const

int

IntlChar::BLOCK_CODE_RUMI_NUMERAL_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_KAITHI

public

const

int

IntlChar::BLOCK_CODE_EGYPTIAN_HIEROGLYPHS

public

const

int

IntlChar::BLOCK_CODE_ENCLOSED_ALPHANUMERIC_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C

public

const

int

IntlChar::BLOCK_CODE_MANDAIC

public

const

int

IntlChar::BLOCK_CODE_BATAK

public

const

int

IntlChar::BLOCK_CODE_ETHIOPIC_EXTENDED_A

public

const

int

IntlChar::BLOCK_CODE_BRAHMI

public

const

int

IntlChar::BLOCK_CODE_BAMUM_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_KANA_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_PLAYING_CARDS

public

const

int

IntlChar::BLOCK_CODE_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS

public

const

int

IntlChar::BLOCK_CODE_EMOTICONS

public

const

int

IntlChar::BLOCK_CODE_TRANSPORT_AND_MAP_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_ALCHEMICAL_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D

public

const

int

IntlChar::BLOCK_CODE_ARABIC_EXTENDED_A

public

const

int

IntlChar::BLOCK_CODE_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS

public

const

int

IntlChar::BLOCK_CODE_CHAKMA

public

const

int

IntlChar::BLOCK_CODE_MEETEI_MAYEK_EXTENSIONS

public

const

int

IntlChar::BLOCK_CODE_MEROITIC_CURSIVE

public

const

int

IntlChar::BLOCK_CODE_MEROITIC_HIEROGLYPHS

public

const

int

IntlChar::BLOCK_CODE_MIAO

public

const

int

IntlChar::BLOCK_CODE_SHARADA

public

const

int

IntlChar::BLOCK_CODE_SORA_SOMPENG

public

const

int

IntlChar::BLOCK_CODE_SUNDANESE_SUPPLEMENT

public

const

int

IntlChar::BLOCK_CODE_TAKRI

public

const

int

IntlChar::BLOCK_CODE_BASSA_VAH

public

const

int

IntlChar::BLOCK_CODE_CAUCASIAN_ALBANIAN

public

const

int

IntlChar::BLOCK_CODE_COPTIC_EPACT_NUMBERS

public

const

int

IntlChar::BLOCK_CODE_COMBINING_DIACRITICAL_MARKS_EXTENDED

public

const

int

IntlChar::BLOCK_CODE_DUPLOYAN

public

const

int

IntlChar::BLOCK_CODE_ELBASAN

public

const

int

IntlChar::BLOCK_CODE_GEOMETRIC_SHAPES_EXTENDED

public

const

int

IntlChar::BLOCK_CODE_GRANTHA

public

const

int

IntlChar::BLOCK_CODE_KHOJKI

public

const

int

IntlChar::BLOCK_CODE_KHUDAWADI

public

const

int

IntlChar::BLOCK_CODE_LATIN_EXTENDED_E

public

const

int

IntlChar::BLOCK_CODE_LINEAR_A

public

const

int

IntlChar::BLOCK_CODE_MAHAJANI

public

const

int

IntlChar::BLOCK_CODE_MANICHAEAN

public

const

int

IntlChar::BLOCK_CODE_MENDE_KIKAKUI

public

const

int

IntlChar::BLOCK_CODE_MODI

public

const

int

IntlChar::BLOCK_CODE_MRO

public

const

int

IntlChar::BLOCK_CODE_MYANMAR_EXTENDED_B

public

const

int

IntlChar::BLOCK_CODE_NABATAEAN

public

const

int

IntlChar::BLOCK_CODE_OLD_NORTH_ARABIAN

public

const

int

IntlChar::BLOCK_CODE_OLD_PERMIC

public

const

int

IntlChar::BLOCK_CODE_ORNAMENTAL_DINGBATS

public

const

int

IntlChar::BLOCK_CODE_PAHAWH_HMONG

public

const

int

IntlChar::BLOCK_CODE_PALMYRENE

public

const

int

IntlChar::BLOCK_CODE_PAU_CIN_HAU

public

const

int

IntlChar::BLOCK_CODE_PSALTER_PAHLAVI

public

const

int

IntlChar::BLOCK_CODE_SHORTHAND_FORMAT_CONTROLS

public

const

int

IntlChar::BLOCK_CODE_SIDDHAM

public

const

int

IntlChar::BLOCK_CODE_SINHALA_ARCHAIC_NUMBERS

public

const

int

IntlChar::BLOCK_CODE_SUPPLEMENTAL_ARROWS_C

public

const

int

IntlChar::BLOCK_CODE_TIRHUTA

public

const

int

IntlChar::BLOCK_CODE_WARANG_CITI

public

const

int

IntlChar::BLOCK_CODE_COUNT

public

const

int

IntlChar::BLOCK_CODE_INVALID_CODE

public

const

int

IntlChar::BPT_NONE

public

const

int

IntlChar::BPT_OPEN

public

const

int

IntlChar::BPT_CLOSE

public

const

int

IntlChar::BPT_COUNT

public

const

int

IntlChar::EA_NEUTRAL

public

const

int

IntlChar::EA_AMBIGUOUS

public

const

int

IntlChar::EA_HALFWIDTH

public

const

int

IntlChar::EA_FULLWIDTH

public

const

int

IntlChar::EA_NARROW

public

const

int

IntlChar::EA_WIDE

public

const

int

IntlChar::EA_COUNT

public

const

int

IntlChar::UNICODE_CHAR_NAME

public

const

int

IntlChar::UNICODE_10_CHAR_NAME

public

const

int

IntlChar::EXTENDED_CHAR_NAME

public

const

int

IntlChar::CHAR_NAME_ALIAS

public

const

int

IntlChar::CHAR_NAME_CHOICE_COUNT

public

const

int

IntlChar::SHORT_PROPERTY_NAME

public

const

int

IntlChar::LONG_PROPERTY_NAME

public

const

int

IntlChar::PROPERTY_NAME_CHOICE_COUNT

public

const

int

IntlChar::DT_NONE

public

const

int

IntlChar::DT_CANONICAL

public

const

int

IntlChar::DT_COMPAT

public

const

int

IntlChar::DT_CIRCLE

public

const

int

IntlChar::DT_FINAL

public

const

int

IntlChar::DT_FONT

public

const

int

IntlChar::DT_FRACTION

public

const

int

IntlChar::DT_INITIAL

public

const

int

IntlChar::DT_ISOLATED

public

const

int

IntlChar::DT_MEDIAL

public

const

int

IntlChar::DT_NARROW

public

const

int

IntlChar::DT_NOBREAK

public

const

int

IntlChar::DT_SMALL

public

const

int

IntlChar::DT_SQUARE

public

const

int

IntlChar::DT_SUB

public

const

int

IntlChar::DT_SUPER

public

const

int

IntlChar::DT_VERTICAL

public

const

int

IntlChar::DT_WIDE

public

const

int

IntlChar::DT_COUNT

public

const

int

IntlChar::JT_NON_JOINING

public

const

int

IntlChar::JT_JOIN_CAUSING

public

const

int

IntlChar::JT_DUAL_JOINING

public

const

int

IntlChar::JT_LEFT_JOINING

public

const

int

IntlChar::JT_RIGHT_JOINING

public

const

int

IntlChar::JT_TRANSPARENT

public

const

int

IntlChar::JT_COUNT

public

const

int

IntlChar::JG_NO_JOINING_GROUP

public

const

int

IntlChar::JG_AIN

public

const

int

IntlChar::JG_ALAPH

public

const

int

IntlChar::JG_ALEF

public

const

int

IntlChar::JG_BEH

public

const

int

IntlChar::JG_BETH

public

const

int

IntlChar::JG_DAL

public

const

int

IntlChar::JG_DALATH_RISH

public

const

int

IntlChar::JG_E

public

const

int

IntlChar::JG_FEH

public

const

int

IntlChar::JG_FINAL_SEMKATH

public

const

int

IntlChar::JG_GAF

public

const

int

IntlChar::JG_GAMAL

public

const

int

IntlChar::JG_HAH

public

const

int

IntlChar::JG_TEH_MARBUTA_GOAL

public

const

int

IntlChar::JG_HAMZA_ON_HEH_GOAL

public

const

int

IntlChar::JG_HE

public

const

int

IntlChar::JG_HEH

public

const

int

IntlChar::JG_HEH_GOAL

public

const

int

IntlChar::JG_HETH

public

const

int

IntlChar::JG_KAF

public

const

int

IntlChar::JG_KAPH

public

const

int

IntlChar::JG_KNOTTED_HEH

public

const

int

IntlChar::JG_LAM

public

const

int

IntlChar::JG_LAMADH

public

const

int

IntlChar::JG_MEEM

public

const

int

IntlChar::JG_MIM

public

const

int

IntlChar::JG_NOON

public

const

int

IntlChar::JG_NUN

public

const

int

IntlChar::JG_PE

public

const

int

IntlChar::JG_QAF

public

const

int

IntlChar::JG_QAPH

public

const

int

IntlChar::JG_REH

public

const

int

IntlChar::JG_REVERSED_PE

public

const

int

IntlChar::JG_SAD

public

const

int

IntlChar::JG_SADHE

public

const

int

IntlChar::JG_SEEN

public

const

int

IntlChar::JG_SEMKATH

public

const

int

IntlChar::JG_SHIN

public

const

int

IntlChar::JG_SWASH_KAF

public

const

int

IntlChar::JG_SYRIAC_WAW

public

const

int

IntlChar::JG_TAH

public

const

int

IntlChar::JG_TAW

public

const

int

IntlChar::JG_TEH_MARBUTA

public

const

int

IntlChar::JG_TETH

public

const

int

IntlChar::JG_WAW

public

const

int

IntlChar::JG_YEH

public

const

int

IntlChar::JG_YEH_BARREE

public

const

int

IntlChar::JG_YEH_WITH_TAIL

public

const

int

IntlChar::JG_YUDH

public

const

int

IntlChar::JG_YUDH_HE

public

const

int

IntlChar::JG_ZAIN

public

const

int

IntlChar::JG_FE

public

const

int

IntlChar::JG_KHAPH

public

const

int

IntlChar::JG_ZHAIN

public

const

int

IntlChar::JG_BURUSHASKI_YEH_BARREE

public

const

int

IntlChar::JG_FARSI_YEH

public

const

int

IntlChar::JG_NYA

public

const

int

IntlChar::JG_ROHINGYA_YEH

public

const

int

IntlChar::JG_MANICHAEAN_ALEPH

public

const

int

IntlChar::JG_MANICHAEAN_AYIN

public

const

int

IntlChar::JG_MANICHAEAN_BETH

public

const

int

IntlChar::JG_MANICHAEAN_DALETH

public

const

int

IntlChar::JG_MANICHAEAN_DHAMEDH

public

const

int

IntlChar::JG_MANICHAEAN_FIVE

public

const

int

IntlChar::JG_MANICHAEAN_GIMEL

public

const

int

IntlChar::JG_MANICHAEAN_HETH

public

const

int

IntlChar::JG_MANICHAEAN_HUNDRED

public

const

int

IntlChar::JG_MANICHAEAN_KAPH

public

const

int

IntlChar::JG_MANICHAEAN_LAMEDH

public

const

int

IntlChar::JG_MANICHAEAN_MEM

public

const

int

IntlChar::JG_MANICHAEAN_NUN

public

const

int

IntlChar::JG_MANICHAEAN_ONE

public

const

int

IntlChar::JG_MANICHAEAN_PE

public

const

int

IntlChar::JG_MANICHAEAN_QOPH

public

const

int

IntlChar::JG_MANICHAEAN_RESH

public

const

int

IntlChar::JG_MANICHAEAN_SADHE

public

const

int

IntlChar::JG_MANICHAEAN_SAMEKH

public

const

int

IntlChar::JG_MANICHAEAN_TAW

public

const

int

IntlChar::JG_MANICHAEAN_TEN

public

const

int

IntlChar::JG_MANICHAEAN_TETH

public

const

int

IntlChar::JG_MANICHAEAN_THAMEDH

public

const

int

IntlChar::JG_MANICHAEAN_TWENTY

public

const

int

IntlChar::JG_MANICHAEAN_WAW

public

const

int

IntlChar::JG_MANICHAEAN_YODH

public

const

int

IntlChar::JG_MANICHAEAN_ZAYIN

public

const

int

IntlChar::JG_STRAIGHT_WAW

public

const

int

IntlChar::JG_COUNT

public

const

int

IntlChar::GCB_OTHER

public

const

int

IntlChar::GCB_CONTROL

public

const

int

IntlChar::GCB_CR

public

const

int

IntlChar::GCB_EXTEND

public

const

int

IntlChar::GCB_L

public

const

int

IntlChar::GCB_LF

public

const

int

IntlChar::GCB_LV

public

const

int

IntlChar::GCB_LVT

public

const

int

IntlChar::GCB_T

public

const

int

IntlChar::GCB_V

public

const

int

IntlChar::GCB_SPACING_MARK

public

const

int

IntlChar::GCB_PREPEND

public

const

int

IntlChar::GCB_REGIONAL_INDICATOR

public

const

int

IntlChar::GCB_COUNT

public

const

int

IntlChar::WB_OTHER

public

const

int

IntlChar::WB_ALETTER

public

const

int

IntlChar::WB_FORMAT

public

const

int

IntlChar::WB_KATAKANA

public

const

int

IntlChar::WB_MIDLETTER

public

const

int

IntlChar::WB_MIDNUM

public

const

int

IntlChar::WB_NUMERIC

public

const

int

IntlChar::WB_EXTENDNUMLET

public

const

int

IntlChar::WB_CR

public

const

int

IntlChar::WB_EXTEND

public

const

int

IntlChar::WB_LF

public

const

int

IntlChar::WB_MIDNUMLET

public

const

int

IntlChar::WB_NEWLINE

public

const

int

IntlChar::WB_REGIONAL_INDICATOR

public

const

int

IntlChar::WB_HEBREW_LETTER

public

const

int

IntlChar::WB_SINGLE_QUOTE

public

const

int

IntlChar::WB_DOUBLE_QUOTE

public

const

int

IntlChar::WB_COUNT

public

const

int

IntlChar::SB_OTHER

public

const

int

IntlChar::SB_ATERM

public

const

int

IntlChar::SB_CLOSE

public

const

int

IntlChar::SB_FORMAT

public

const

int

IntlChar::SB_LOWER

public

const

int

IntlChar::SB_NUMERIC

public

const

int

IntlChar::SB_OLETTER

public

const

int

IntlChar::SB_SEP

public

const

int

IntlChar::SB_SP

public

const

int

IntlChar::SB_STERM

public

const

int

IntlChar::SB_UPPER

public

const

int

IntlChar::SB_CR

public

const

int

IntlChar::SB_EXTEND

public

const

int

IntlChar::SB_LF

public

const

int

IntlChar::SB_SCONTINUE

public

const

int

IntlChar::SB_COUNT

public

const

int

IntlChar::LB_UNKNOWN

public

const

int

IntlChar::LB_AMBIGUOUS

public

const

int

IntlChar::LB_ALPHABETIC

public

const

int

IntlChar::LB_BREAK_BOTH

public

const

int

IntlChar::LB_BREAK_AFTER

public

const

int

IntlChar::LB_BREAK_BEFORE

public

const

int

IntlChar::LB_MANDATORY_BREAK

public

const

int

IntlChar::LB_CONTINGENT_BREAK

public

const

int

IntlChar::LB_CLOSE_PUNCTUATION

public

const

int

IntlChar::LB_COMBINING_MARK

public

const

int

IntlChar::LB_CARRIAGE_RETURN

public

const

int

IntlChar::LB_EXCLAMATION

public

const

int

IntlChar::LB_GLUE

public

const

int

IntlChar::LB_HYPHEN

public

const

int

IntlChar::LB_IDEOGRAPHIC

public

const

int

IntlChar::LB_INSEPARABLE

public

const

int

IntlChar::LB_INSEPERABLE

public

const

int

IntlChar::LB_INFIX_NUMERIC

public

const

int

IntlChar::LB_LINE_FEED

public

const

int

IntlChar::LB_NONSTARTER

public

const

int

IntlChar::LB_NUMERIC

public

const

int

IntlChar::LB_OPEN_PUNCTUATION

public

const

int

IntlChar::LB_POSTFIX_NUMERIC

public

const

int

IntlChar::LB_PREFIX_NUMERIC

public

const

int

IntlChar::LB_QUOTATION

public

const

int

IntlChar::LB_COMPLEX_CONTEXT

public

const

int

IntlChar::LB_SURROGATE

public

const

int

IntlChar::LB_SPACE

public

const

int

IntlChar::LB_BREAK_SYMBOLS

public

const

int

IntlChar::LB_ZWSPACE

public

const

int

IntlChar::LB_NEXT_LINE

public

const

int

IntlChar::LB_WORD_JOINER

public

const

int

IntlChar::LB_H2

public

const

int

IntlChar::LB_H3

public

const

int

IntlChar::LB_JL

public

const

int

IntlChar::LB_JT

public

const

int

IntlChar::LB_JV

public

const

int

IntlChar::LB_CLOSE_PARENTHESIS

public

const

int

IntlChar::LB_CONDITIONAL_JAPANESE_STARTER

public

const

int

IntlChar::LB_HEBREW_LETTER

public

const

int

IntlChar::LB_REGIONAL_INDICATOR

public

const

int

IntlChar::LB_COUNT

public

const

int

IntlChar::NT_NONE

public

const

int

IntlChar::NT_DECIMAL

public

const

int

IntlChar::NT_DIGIT

public

const

int

IntlChar::NT_NUMERIC

public

const

int

IntlChar::NT_COUNT

public

const

int

IntlChar::HST_NOT_APPLICABLE

public

const

int

IntlChar::HST_LEADING_JAMO

public

const

int

IntlChar::HST_VOWEL_JAMO

public

const

int

IntlChar::HST_TRAILING_JAMO

public

const

int

IntlChar::HST_LV_SYLLABLE

public

const

int

IntlChar::HST_LVT_SYLLABLE

public

const

int

IntlChar::HST_COUNT

public

const

int

IntlChar::FOLD_CASE_DEFAULT

public

const

int

IntlChar::FOLD_CASE_EXCLUDE_SPECIAL_I

Métodos

## Constantes predefinidas

`IntlChar::UNICODE_VERSION` `string`  

`IntlChar::CODEPOINT_MIN` `int`  

`IntlChar::CODEPOINT_MAX` `int`  

`IntlChar::NO_NUMERIC_VALUE` `int`  
Valor especial que es devuelto por IntlChar::getNumericValue cuando no se define un valor numérico para un punto de código.

`IntlChar::PROPERTY_ALPHABETIC` `int`  

`IntlChar::PROPERTY_BINARY_START` `int`  

`IntlChar::PROPERTY_ASCII_HEX_DIGIT` `int`  

`IntlChar::PROPERTY_BIDI_CONTROL` `int`  

`IntlChar::PROPERTY_BIDI_MIRRORED` `int`  

`IntlChar::PROPERTY_DASH` `int`  

`IntlChar::PROPERTY_DEFAULT_IGNORABLE_CODE_POINT` `int`  

`IntlChar::PROPERTY_DEPRECATED` `int`  

`IntlChar::PROPERTY_DIACRITIC` `int`  

`IntlChar::PROPERTY_EXTENDER` `int`  

`IntlChar::PROPERTY_FULL_COMPOSITION_EXCLUSION` `int`  

`IntlChar::PROPERTY_GRAPHEME_BASE` `int`  

`IntlChar::PROPERTY_GRAPHEME_EXTEND` `int`  

`IntlChar::PROPERTY_GRAPHEME_LINK` `int`  

`IntlChar::PROPERTY_HEX_DIGIT` `int`  

`IntlChar::PROPERTY_HYPHEN` `int`  

`IntlChar::PROPERTY_ID_CONTINUE` `int`  

`IntlChar::PROPERTY_ID_START` `int`  

`IntlChar::PROPERTY_IDEOGRAPHIC` `int`  

`IntlChar::PROPERTY_IDS_BINARY_OPERATOR` `int`  

`IntlChar::PROPERTY_IDS_TRINARY_OPERATOR` `int`  

`IntlChar::PROPERTY_IDS_UNARY_OPERATOR` `int`  
Para la determinación programática de secuencias de descripción ideográfica. Disponible a partir de PHP 8.4.0.

`IntlChar::PROPERTY_ID_COMPAT_MATH_START` `int`  
Utilizado en el perfil de identificador matemático en UAX 31. Disponible a partir de PHP 8.4.0.

`IntlChar::PROPERTY_ID_COMPAT_MATH_CONTINUE` `int`  
Utilizado en el perfil de identificador matemático en UAX 31. Disponible a partir de PHP 8.4.0.

`IntlChar::PROPERTY_JOIN_CONTROL` `int`  

`IntlChar::PROPERTY_LOGICAL_ORDER_EXCEPTION` `int`  

`IntlChar::PROPERTY_LOWERCASE` `int`  

`IntlChar::PROPERTY_MATH` `int`  

`IntlChar::PROPERTY_NONCHARACTER_CODE_POINT` `int`  

`IntlChar::PROPERTY_QUOTATION_MARK` `int`  

`IntlChar::PROPERTY_RADICAL` `int`  

`IntlChar::PROPERTY_SOFT_DOTTED` `int`  

`IntlChar::PROPERTY_TERMINAL_PUNCTUATION` `int`  

`IntlChar::PROPERTY_UNIFIED_IDEOGRAPH` `int`  

`IntlChar::PROPERTY_UPPERCASE` `int`  

`IntlChar::PROPERTY_WHITE_SPACE` `int`  

`IntlChar::PROPERTY_XID_CONTINUE` `int`  

`IntlChar::PROPERTY_XID_START` `int`  

`IntlChar::PROPERTY_CASE_SENSITIVE` `int`  

`IntlChar::PROPERTY_S_TERM` `int`  

`IntlChar::PROPERTY_VARIATION_SELECTOR` `int`  

`IntlChar::PROPERTY_NFD_INERT` `int`  

`IntlChar::PROPERTY_NFKD_INERT` `int`  

`IntlChar::PROPERTY_NFC_INERT` `int`  

`IntlChar::PROPERTY_NFKC_INERT` `int`  

`IntlChar::PROPERTY_SEGMENT_STARTER` `int`  

`IntlChar::PROPERTY_PATTERN_SYNTAX` `int`  

`IntlChar::PROPERTY_PATTERN_WHITE_SPACE` `int`  

`IntlChar::PROPERTY_POSIX_ALNUM` `int`  

`IntlChar::PROPERTY_POSIX_BLANK` `int`  

`IntlChar::PROPERTY_POSIX_GRAPH` `int`  

`IntlChar::PROPERTY_POSIX_PRINT` `int`  

`IntlChar::PROPERTY_POSIX_XDIGIT` `int`  

`IntlChar::PROPERTY_CASED` `int`  

`IntlChar::PROPERTY_CASE_IGNORABLE` `int`  

`IntlChar::PROPERTY_CHANGES_WHEN_LOWERCASED` `int`  

`IntlChar::PROPERTY_CHANGES_WHEN_UPPERCASED` `int`  

`IntlChar::PROPERTY_CHANGES_WHEN_TITLECASED` `int`  

`IntlChar::PROPERTY_CHANGES_WHEN_CASEFOLDED` `int`  

`IntlChar::PROPERTY_CHANGES_WHEN_CASEMAPPED` `int`  

`IntlChar::PROPERTY_CHANGES_WHEN_NFKC_CASEFOLDED` `int`  

`IntlChar::PROPERTY_BINARY_LIMIT` `int`  

`IntlChar::PROPERTY_BIDI_CLASS` `int`  

`IntlChar::PROPERTY_INT_START` `int`  

`IntlChar::PROPERTY_BLOCK` `int`  

`IntlChar::PROPERTY_CANONICAL_COMBINING_CLASS` `int`  

`IntlChar::PROPERTY_DECOMPOSITION_TYPE` `int`  

`IntlChar::PROPERTY_EAST_ASIAN_WIDTH` `int`  

`IntlChar::PROPERTY_GENERAL_CATEGORY` `int`  

`IntlChar::PROPERTY_JOINING_GROUP` `int`  

`IntlChar::PROPERTY_JOINING_TYPE` `int`  

`IntlChar::PROPERTY_LINE_BREAK` `int`  

`IntlChar::PROPERTY_NUMERIC_TYPE` `int`  

`IntlChar::PROPERTY_SCRIPT` `int`  

`IntlChar::PROPERTY_HANGUL_SYLLABLE_TYPE` `int`  

`IntlChar::PROPERTY_NFD_QUICK_CHECK` `int`  

`IntlChar::PROPERTY_NFKD_QUICK_CHECK` `int`  

`IntlChar::PROPERTY_NFC_QUICK_CHECK` `int`  

`IntlChar::PROPERTY_NFKC_QUICK_CHECK` `int`  

`IntlChar::PROPERTY_LEAD_CANONICAL_COMBINING_CLASS` `int`  

`IntlChar::PROPERTY_TRAIL_CANONICAL_COMBINING_CLASS` `int`  

`IntlChar::PROPERTY_GRAPHEME_CLUSTER_BREAK` `int`  

`IntlChar::PROPERTY_SENTENCE_BREAK` `int`  

`IntlChar::PROPERTY_WORD_BREAK` `int`  

`IntlChar::PROPERTY_BIDI_PAIRED_BRACKET_TYPE` `int`  

`IntlChar::PROPERTY_INT_LIMIT` `int`  

`IntlChar::PROPERTY_GENERAL_CATEGORY_MASK` `int`  

`IntlChar::PROPERTY_MASK_START` `int`  

`IntlChar::PROPERTY_MASK_LIMIT` `int`  

`IntlChar::PROPERTY_NUMERIC_VALUE` `int`  

`IntlChar::PROPERTY_DOUBLE_START` `int`  

`IntlChar::PROPERTY_DOUBLE_LIMIT` `int`  

`IntlChar::PROPERTY_AGE` `int`  

`IntlChar::PROPERTY_STRING_START` `int`  

`IntlChar::PROPERTY_BIDI_MIRRORING_GLYPH` `int`  

`IntlChar::PROPERTY_CASE_FOLDING` `int`  

`IntlChar::PROPERTY_ISO_COMMENT` `int`  

`IntlChar::PROPERTY_LOWERCASE_MAPPING` `int`  

`IntlChar::PROPERTY_NAME` `int`  

`IntlChar::PROPERTY_SIMPLE_CASE_FOLDING` `int`  

`IntlChar::PROPERTY_SIMPLE_LOWERCASE_MAPPING` `int`  

`IntlChar::PROPERTY_SIMPLE_TITLECASE_MAPPING` `int`  

`IntlChar::PROPERTY_SIMPLE_UPPERCASE_MAPPING` `int`  

`IntlChar::PROPERTY_TITLECASE_MAPPING` `int`  

`IntlChar::PROPERTY_UNICODE_1_NAME` `int`  

`IntlChar::PROPERTY_UPPERCASE_MAPPING` `int`  

`IntlChar::PROPERTY_BIDI_PAIRED_BRACKET` `int`  

`IntlChar::PROPERTY_STRING_LIMIT` `int`  

`IntlChar::PROPERTY_SCRIPT_EXTENSIONS` `int`  

`IntlChar::PROPERTY_OTHER_PROPERTY_START` `int`  

`IntlChar::PROPERTY_OTHER_PROPERTY_LIMIT` `int`  

`IntlChar::PROPERTY_INVALID_CODE` `int`  

`IntlChar::CHAR_CATEGORY_UNASSIGNED` `int`  

`IntlChar::CHAR_CATEGORY_GENERAL_OTHER_TYPES` `int`  

`IntlChar::CHAR_CATEGORY_UPPERCASE_LETTER` `int`  

`IntlChar::CHAR_CATEGORY_LOWERCASE_LETTER` `int`  

`IntlChar::CHAR_CATEGORY_TITLECASE_LETTER` `int`  

`IntlChar::CHAR_CATEGORY_MODIFIER_LETTER` `int`  

`IntlChar::CHAR_CATEGORY_OTHER_LETTER` `int`  

`IntlChar::CHAR_CATEGORY_NON_SPACING_MARK` `int`  

`IntlChar::CHAR_CATEGORY_ENCLOSING_MARK` `int`  

`IntlChar::CHAR_CATEGORY_COMBINING_SPACING_MARK` `int`  

`IntlChar::CHAR_CATEGORY_DECIMAL_DIGIT_NUMBER` `int`  

`IntlChar::CHAR_CATEGORY_LETTER_NUMBER` `int`  

`IntlChar::CHAR_CATEGORY_OTHER_NUMBER` `int`  

`IntlChar::CHAR_CATEGORY_SPACE_SEPARATOR` `int`  

`IntlChar::CHAR_CATEGORY_LINE_SEPARATOR` `int`  

`IntlChar::CHAR_CATEGORY_PARAGRAPH_SEPARATOR` `int`  

`IntlChar::CHAR_CATEGORY_CONTROL_CHAR` `int`  

`IntlChar::CHAR_CATEGORY_FORMAT_CHAR` `int`  

`IntlChar::CHAR_CATEGORY_PRIVATE_USE_CHAR` `int`  

`IntlChar::CHAR_CATEGORY_SURROGATE` `int`  

`IntlChar::CHAR_CATEGORY_DASH_PUNCTUATION` `int`  

`IntlChar::CHAR_CATEGORY_START_PUNCTUATION` `int`  

`IntlChar::CHAR_CATEGORY_END_PUNCTUATION` `int`  

`IntlChar::CHAR_CATEGORY_CONNECTOR_PUNCTUATION` `int`  

`IntlChar::CHAR_CATEGORY_OTHER_PUNCTUATION` `int`  

`IntlChar::CHAR_CATEGORY_MATH_SYMBOL` `int`  

`IntlChar::CHAR_CATEGORY_CURRENCY_SYMBOL` `int`  

`IntlChar::CHAR_CATEGORY_MODIFIER_SYMBOL` `int`  

`IntlChar::CHAR_CATEGORY_OTHER_SYMBOL` `int`  

`IntlChar::CHAR_CATEGORY_INITIAL_PUNCTUATION` `int`  

`IntlChar::CHAR_CATEGORY_FINAL_PUNCTUATION` `int`  

`IntlChar::CHAR_CATEGORY_CHAR_CATEGORY_COUNT` `int`  

`IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT` `int`  

`IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT` `int`  

`IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER` `int`  

`IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER_SEPARATOR` `int`  

`IntlChar::CHAR_DIRECTION_EUROPEAN_NUMBER_TERMINATOR` `int`  

`IntlChar::CHAR_DIRECTION_ARABIC_NUMBER` `int`  

`IntlChar::CHAR_DIRECTION_COMMON_NUMBER_SEPARATOR` `int`  

`IntlChar::CHAR_DIRECTION_BLOCK_SEPARATOR` `int`  

`IntlChar::CHAR_DIRECTION_SEGMENT_SEPARATOR` `int`  

`IntlChar::CHAR_DIRECTION_WHITE_SPACE_NEUTRAL` `int`  

`IntlChar::CHAR_DIRECTION_OTHER_NEUTRAL` `int`  

`IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_EMBEDDING` `int`  

`IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_OVERRIDE` `int`  

`IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_ARABIC` `int`  

`IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_EMBEDDING` `int`  

`IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_OVERRIDE` `int`  

`IntlChar::CHAR_DIRECTION_POP_DIRECTIONAL_FORMAT` `int`  

`IntlChar::CHAR_DIRECTION_DIR_NON_SPACING_MARK` `int`  

`IntlChar::CHAR_DIRECTION_BOUNDARY_NEUTRAL` `int`  

`IntlChar::CHAR_DIRECTION_FIRST_STRONG_ISOLATE` `int`  

`IntlChar::CHAR_DIRECTION_LEFT_TO_RIGHT_ISOLATE` `int`  

`IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT_ISOLATE` `int`  

`IntlChar::CHAR_DIRECTION_POP_DIRECTIONAL_ISOLATE` `int`  

`IntlChar::CHAR_DIRECTION_CHAR_DIRECTION_COUNT` `int`  

`IntlChar::BLOCK_CODE_NO_BLOCK` `int`  

`IntlChar::BLOCK_CODE_BASIC_LATIN` `int`  

`IntlChar::BLOCK_CODE_LATIN_1_SUPPLEMENT` `int`  

`IntlChar::BLOCK_CODE_LATIN_EXTENDED_A` `int`  

`IntlChar::BLOCK_CODE_LATIN_EXTENDED_B` `int`  

`IntlChar::BLOCK_CODE_IPA_EXTENSIONS` `int`  

`IntlChar::BLOCK_CODE_SPACING_MODIFIER_LETTERS` `int`  

`IntlChar::BLOCK_CODE_COMBINING_DIACRITICAL_MARKS` `int`  

`IntlChar::BLOCK_CODE_GREEK` `int`  

`IntlChar::BLOCK_CODE_CYRILLIC` `int`  

`IntlChar::BLOCK_CODE_ARMENIAN` `int`  

`IntlChar::BLOCK_CODE_HEBREW` `int`  

`IntlChar::BLOCK_CODE_ARABIC` `int`  

`IntlChar::BLOCK_CODE_SYRIAC` `int`  

`IntlChar::BLOCK_CODE_THAANA` `int`  

`IntlChar::BLOCK_CODE_DEVANAGARI` `int`  

`IntlChar::BLOCK_CODE_BENGALI` `int`  

`IntlChar::BLOCK_CODE_GURMUKHI` `int`  

`IntlChar::BLOCK_CODE_GUJARATI` `int`  

`IntlChar::BLOCK_CODE_ORIYA` `int`  

`IntlChar::BLOCK_CODE_TAMIL` `int`  

`IntlChar::BLOCK_CODE_TELUGU` `int`  

`IntlChar::BLOCK_CODE_KANNADA` `int`  

`IntlChar::BLOCK_CODE_MALAYALAM` `int`  

`IntlChar::BLOCK_CODE_SINHALA` `int`  

`IntlChar::BLOCK_CODE_THAI` `int`  

`IntlChar::BLOCK_CODE_LAO` `int`  

`IntlChar::BLOCK_CODE_TIBETAN` `int`  

`IntlChar::BLOCK_CODE_MYANMAR` `int`  

`IntlChar::BLOCK_CODE_GEORGIAN` `int`  

`IntlChar::BLOCK_CODE_HANGUL_JAMO` `int`  

`IntlChar::BLOCK_CODE_ETHIOPIC` `int`  

`IntlChar::BLOCK_CODE_CHEROKEE` `int`  

`IntlChar::BLOCK_CODE_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS` `int`  

`IntlChar::BLOCK_CODE_OGHAM` `int`  

`IntlChar::BLOCK_CODE_RUNIC` `int`  

`IntlChar::BLOCK_CODE_KHMER` `int`  

`IntlChar::BLOCK_CODE_MONGOLIAN` `int`  

`IntlChar::BLOCK_CODE_LATIN_EXTENDED_ADDITIONAL` `int`  

`IntlChar::BLOCK_CODE_GREEK_EXTENDED` `int`  

`IntlChar::BLOCK_CODE_GENERAL_PUNCTUATION` `int`  

`IntlChar::BLOCK_CODE_SUPERSCRIPTS_AND_SUBSCRIPTS` `int`  

`IntlChar::BLOCK_CODE_CURRENCY_SYMBOLS` `int`  

`IntlChar::BLOCK_CODE_COMBINING_MARKS_FOR_SYMBOLS` `int`  

`IntlChar::BLOCK_CODE_LETTERLIKE_SYMBOLS` `int`  

`IntlChar::BLOCK_CODE_NUMBER_FORMS` `int`  

`IntlChar::BLOCK_CODE_ARROWS` `int`  

`IntlChar::BLOCK_CODE_MATHEMATICAL_OPERATORS` `int`  

`IntlChar::BLOCK_CODE_MISCELLANEOUS_TECHNICAL` `int`  

`IntlChar::BLOCK_CODE_CONTROL_PICTURES` `int`  

`IntlChar::BLOCK_CODE_OPTICAL_CHARACTER_RECOGNITION` `int`  

`IntlChar::BLOCK_CODE_ENCLOSED_ALPHANUMERICS` `int`  

`IntlChar::BLOCK_CODE_BOX_DRAWING` `int`  

`IntlChar::BLOCK_CODE_BLOCK_ELEMENTS` `int`  

`IntlChar::BLOCK_CODE_GEOMETRIC_SHAPES` `int`  

`IntlChar::BLOCK_CODE_MISCELLANEOUS_SYMBOLS` `int`  

`IntlChar::BLOCK_CODE_DINGBATS` `int`  

`IntlChar::BLOCK_CODE_BRAILLE_PATTERNS` `int`  

`IntlChar::BLOCK_CODE_CJK_RADICALS_SUPPLEMENT` `int`  

`IntlChar::BLOCK_CODE_KANGXI_RADICALS` `int`  

`IntlChar::BLOCK_CODE_IDEOGRAPHIC_DESCRIPTION_CHARACTERS` `int`  

`IntlChar::BLOCK_CODE_CJK_SYMBOLS_AND_PUNCTUATION` `int`  

`IntlChar::BLOCK_CODE_HIRAGANA` `int`  

`IntlChar::BLOCK_CODE_KATAKANA` `int`  

`IntlChar::BLOCK_CODE_BOPOMOFO` `int`  

`IntlChar::BLOCK_CODE_HANGUL_COMPATIBILITY_JAMO` `int`  

`IntlChar::BLOCK_CODE_KANBUN` `int`  

`IntlChar::BLOCK_CODE_BOPOMOFO_EXTENDED` `int`  

`IntlChar::BLOCK_CODE_ENCLOSED_CJK_LETTERS_AND_MONTHS` `int`  

`IntlChar::BLOCK_CODE_CJK_COMPATIBILITY` `int`  

`IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A` `int`  

`IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS` `int`  

`IntlChar::BLOCK_CODE_YI_SYLLABLES` `int`  

`IntlChar::BLOCK_CODE_YI_RADICALS` `int`  

`IntlChar::BLOCK_CODE_HANGUL_SYLLABLES` `int`  

`IntlChar::BLOCK_CODE_HIGH_SURROGATES` `int`  

`IntlChar::BLOCK_CODE_HIGH_PRIVATE_USE_SURROGATES` `int`  

`IntlChar::BLOCK_CODE_LOW_SURROGATES` `int`  

`IntlChar::BLOCK_CODE_PRIVATE_USE_AREA` `int`  

`IntlChar::BLOCK_CODE_PRIVATE_USE` `int`  

`IntlChar::BLOCK_CODE_CJK_COMPATIBILITY_IDEOGRAPHS` `int`  

`IntlChar::BLOCK_CODE_ALPHABETIC_PRESENTATION_FORMS` `int`  

`IntlChar::BLOCK_CODE_ARABIC_PRESENTATION_FORMS_A` `int`  

`IntlChar::BLOCK_CODE_COMBINING_HALF_MARKS` `int`  

`IntlChar::BLOCK_CODE_CJK_COMPATIBILITY_FORMS` `int`  

`IntlChar::BLOCK_CODE_SMALL_FORM_VARIANTS` `int`  

`IntlChar::BLOCK_CODE_ARABIC_PRESENTATION_FORMS_B` `int`  
Bloque de las formas de presentación árabes B, incluyendo ligaduras adicionales y formas contextuales.

`IntlChar::BLOCK_CODE_SPECIALS` `int`  
Bloque reservado para caracteres especiales y no estandarizados.

`IntlChar::BLOCK_CODE_HALFWIDTH_AND_FULLWIDTH_FORMS` `int`  
Bloque de las formas de media anchura y anchura completa utilizadas principalmente en escrituras asiáticas.

`IntlChar::BLOCK_CODE_OLD_ITALIC` `int`  
Bloque de caracteres del antiguo alfabeto italiano utilizado en inscripciones italianas antiguas.

`IntlChar::BLOCK_CODE_GOTHIC` `int`  
Bloque de caracteres góticos utilizados en ciertas escrituras históricas.

`IntlChar::BLOCK_CODE_DESERET` `int`  
Bloque de caracteres Deseret utilizados en el alfabeto Deseret creado por la Iglesia de Jesucristo de los Santos de los Últimos Días.

`IntlChar::BLOCK_CODE_BYZANTINE_MUSICAL_SYMBOLS` `int`  
Bloque de símbolos musicales bizantinos utilizados en la notación musical histórica.

`IntlChar::BLOCK_CODE_MUSICAL_SYMBOLS` `int`  
Bloque de símbolos musicales utilizados en la notación musical moderna.

`IntlChar::BLOCK_CODE_MATHEMATICAL_ALPHANUMERIC_SYMBOLS` `int`  
Bloque de símbolos alfanuméricos matemáticos utilizados en expresiones y notaciones matemáticas.

`IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B` `int`  
Bloque de ideogramas unificados CJK, extensión B, añadiendo un gran número de caracteres adicionales.

`IntlChar::BLOCK_CODE_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT` `int`  
Bloque de ideogramas de compatibilidad CJK suplementario para caracteres adicionales.

`IntlChar::BLOCK_CODE_TAGS` `int`  
Bloque de caracteres de etiquetado utilizados para anotaciones textuales.

`IntlChar::BLOCK_CODE_CYRILLIC_SUPPLEMENT` `int`  
Bloque de caracteres cirílicos suplementarios añadiendo letras utilizadas en otras lenguas eslavas.

`IntlChar::BLOCK_CODE_CYRILLIC_SUPPLEMENTARY` `int`  
Bloque de caracteres cirílicos suplementarios utilizados para necesidades lingüísticas específicas.

`IntlChar::BLOCK_CODE_TAGALOG` `int`  
Bloque de caracteres Tagalog utilizados en la escritura Tagalog.

`IntlChar::BLOCK_CODE_HANUNOO` `int`  
Bloque de caracteres Hanunoo utilizados en la escritura Hanunoo.

`IntlChar::BLOCK_CODE_BUHID` `int`  
Bloque de caracteres Buhid utilizados en la escritura Buhid.

`IntlChar::BLOCK_CODE_TAGBANWA` `int`  
Bloque de caracteres Tagbanwa utilizados en la escritura Tagbanwa.

`IntlChar::BLOCK_CODE_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A` `int`  
Bloque de símbolos matemáticos diversos A utilizados en diversos contextos matemáticos.

`IntlChar::BLOCK_CODE_SUPPLEMENTAL_ARROWS_A` `int`  
Bloque de flechas suplementarias A ofreciendo variantes adicionales de flechas.

`IntlChar::BLOCK_CODE_SUPPLEMENTAL_ARROWS_B` `int`  
Bloque de flechas suplementarias B proporcionando aún más variantes de flechas.

`IntlChar::BLOCK_CODE_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B` `int`  
Bloque de símbolos matemáticos diversos B utilizados en dominios especializados de las matemáticas.

`IntlChar::BLOCK_CODE_SUPPLEMENTAL_MATHEMATICAL_OPERATORS` `int`  
Bloque de operadores matemáticos suplementarios para operaciones avanzadas.

`IntlChar::BLOCK_CODE_KATAKANA_PHONETIC_EXTENSIONS` `int`  
Bloque de extensiones fonéticas Katakana para representar sonidos adicionales.

`IntlChar::BLOCK_CODE_VARIATION_SELECTORS` `int`  
Bloque de selectores de variación utilizados para especificar variantes de presentación de caracteres.

`IntlChar::BLOCK_CODE_SUPPLEMENTARY_PRIVATE_USE_AREA_A` `int`  
Bloque suplementario de uso privado A para caracteres definidos por el usuario.

`IntlChar::BLOCK_CODE_SUPPLEMENTARY_PRIVATE_USE_AREA_B` `int`  
Bloque suplementario de uso privado B para caracteres definidos por el usuario.

`IntlChar::BLOCK_CODE_LIMBU` `int`  
Bloque de caracteres Limbu utilizados en la escritura Limbu.

`IntlChar::BLOCK_CODE_TAI_LE` `int`  
Bloque de caracteres Tai Le utilizados en la escritura Tai Le.

`IntlChar::BLOCK_CODE_KHMER_SYMBOLS` `int`  
Bloque de símbolos Khmers utilizados en la escritura khmer.

`IntlChar::BLOCK_CODE_PHONETIC_EXTENSIONS` `int`  
Bloque de extensiones fonéticas que añaden caracteres para representar sonidos específicos.

`IntlChar::BLOCK_CODE_MISCELLANEOUS_SYMBOLS_AND_ARROWS` `int`  
Bloque de símbolos diversos y flechas utilizadas en diversos contextos.

`IntlChar::BLOCK_CODE_YIJING_HEXAGRAM_SYMBOLS` `int`  
Bloque de símbolos de hexagramas del Yi Jing utilizados en textos tradicionales chinos.

`IntlChar::BLOCK_CODE_LINEAR_B_SYLLABARY` `int`  
Bloque de silabarios Linear B utilizados en la escritura minoica.

`IntlChar::BLOCK_CODE_LINEAR_B_IDEOGRAMS` `int`  
Bloque de ideogramas Linear B utilizados en la escritura minoica.

`IntlChar::BLOCK_CODE_AEGEAN_NUMBERS` `int`  

`IntlChar::BLOCK_CODE_UGARITIC` `int`  

`IntlChar::BLOCK_CODE_SHAVIAN` `int`  

`IntlChar::BLOCK_CODE_OSMANYA` `int`  

`IntlChar::BLOCK_CODE_CYPRIOT_SYLLABARY` `int`  
Bloque de silabarios cypriotas utilizados en la escritura chipriota antigua.

`IntlChar::BLOCK_CODE_TAI_XUAN_JING_SYMBOLS` `int`  
Bloque de símbolos Tai Xuan Jing utilizados en el manuscrito clásico chino Tai Xuan Jing.

`IntlChar::BLOCK_CODE_VARIATION_SELECTORS_SUPPLEMENT` `int`  
Bloque de selectores de variación adicionales utilizados para especificar variantes de presentación de caracteres.

`IntlChar::BLOCK_CODE_ANCIENT_GREEK_MUSICAL_NOTATION` `int`  
Bloque de notaciones musicales griegas antiguas utilizadas en las notaciones musicales de la antigua Grecia.

`IntlChar::BLOCK_CODE_ANCIENT_GREEK_NUMBERS` `int`  
Bloque de números griegos antiguos utilizados en inscripciones y documentos históricos griegos.

`IntlChar::BLOCK_CODE_ARABIC_SUPPLEMENT` `int`  
Bloque de suplementos árabes que añaden caracteres adicionales para escrituras árabes extendidas.

`IntlChar::BLOCK_CODE_BUGINESE` `int`  
Bloque de caracteres Buginese utilizados en la escritura Buginese de la isla de Sulawesi en Indonesia.

`IntlChar::BLOCK_CODE_CJK_STROKES` `int`  
Bloque de trazos CJK utilizados para la composición y descomposición de ideogramas chinos, japoneses y coreanos.

`IntlChar::BLOCK_CODE_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT` `int`  
Bloque de marcas diacríticas combinantes adicionales utilizadas para modificar caracteres base.

`IntlChar::BLOCK_CODE_COPTIC` `int`  
Bloque de caracteres coptos utilizados en la escritura copta de Egipto.

`IntlChar::BLOCK_CODE_ETHIOPIC_EXTENDED` `int`  
Bloque extendido de caracteres etíopes que añade letras adicionales para lenguas etíopes específicas.

`IntlChar::BLOCK_CODE_ETHIOPIC_SUPPLEMENT` `int`  
Bloque de suplementos etíopes que añaden caracteres adicionales para necesidades lingüísticas específicas.

`IntlChar::BLOCK_CODE_GEORGIAN_SUPPLEMENT` `int`  
Bloque de suplementos georgianos que añaden caracteres adicionales para la escritura georgiana.

`IntlChar::BLOCK_CODE_GLAGOLITIC` `int`  
Bloque de caracteres glagolíticos utilizados en el alfabeto glagolítico, uno de los primeros alfabetos eslavos.

`IntlChar::BLOCK_CODE_KHAROSHTHI` `int`  
Bloque de caracteres Kharoshthi utilizados en la escritura antigua del noroeste de la India.

`IntlChar::BLOCK_CODE_MODIFIER_TONE_LETTERS` `int`  
Bloque de letras modificadoras de tono utilizadas en ciertos idiomas para indicar variaciones tonales.

`IntlChar::BLOCK_CODE_NEW_TAI_LUE` `int`  
Bloque de caracteres New Tai Lue utilizados en la escritura Tai Lue para ciertos idiomas del sudeste asiático.

`IntlChar::BLOCK_CODE_OLD_PERSIAN` `int`  
Bloque de caracteres persas antiguos utilizados en la escritura del Imperio persa antiguo.

`IntlChar::BLOCK_CODE_PHONETIC_EXTENSIONS_SUPPLEMENT` `int`  
Bloque de extensiones fonéticas adicionales que añaden caracteres para representar sonidos específicos.

`IntlChar::BLOCK_CODE_SUPPLEMENTAL_PUNCTUATION` `int`  
Bloque de puntuaciones adicionales utilizadas para diversos requisitos tipográficos.

`IntlChar::BLOCK_CODE_SYLOTI_NAGRI` `int`  
Bloque de caracteres Syloti Nagri utilizados en la escritura Syloti Nagri para ciertos idiomas de la India.

`IntlChar::BLOCK_CODE_TIFINAGH` `int`  
Bloque de caracteres Tifinagh utilizados en la escritura de las lenguas bereberes.

`IntlChar::BLOCK_CODE_VERTICAL_FORMS` `int`  
Bloque de formas verticales utilizadas en ciertas escrituras para la presentación vertical de caracteres.

`IntlChar::BLOCK_CODE_NKO` `int`  
Bloque de caracteres Nko utilizados en la escritura Nko para ciertos idiomas de África Occidental.

`IntlChar::BLOCK_CODE_BALINESE` `int`  
Bloque de caracteres balineses utilizados en la escritura balinesa de Indonesia.

`IntlChar::BLOCK_CODE_LATIN_EXTENDED_C` `int`  
Bloque de extensiones latinas adicionales C que añaden caracteres adicionales para la escritura de idiomas que utilizan el alfabeto latino.

`IntlChar::BLOCK_CODE_LATIN_EXTENDED_D` `int`  
Bloque de extensiones latinas adicionales D que añaden caracteres adicionales para la escritura de idiomas que utilizan el alfabeto latino.

`IntlChar::BLOCK_CODE_PHAGS_PA` `int`  
Bloque de caracteres Phags-pa utilizados en la escritura Phags-pa, un script histórico del Imperio mongol.

`IntlChar::BLOCK_CODE_PHOENICIAN` `int`  
Bloque de caracteres fenicios utilizados en la escritura fenicia de la antigüedad.

`IntlChar::BLOCK_CODE_CUNEIFORM` `int`  
Bloque de caracteres cuneiformes utilizados en la escritura cuneiforme de la antigua Mesopotamia.

`IntlChar::BLOCK_CODE_CUNEIFORM_NUMBERS_AND_PUNCTUATION` `int`  
Bloque de números y puntuaciones cuneiformes utilizados en la escritura cuneiforme.

`IntlChar::BLOCK_CODE_COUNTING_ROD_NUMERALS` `int`  
Bloque de cifras en varilla utilizadas en sistemas de numeración antiguos.

`IntlChar::BLOCK_CODE_SUNDANESE` `int`  
Bloque de caracteres sundaneses utilizados en la escritura sundanesa de Indonesia.

`IntlChar::BLOCK_CODE_LEPCHA` `int`  
Bloque de caracteres Lepcha utilizados en la escritura Lepcha del Himalaya.

`IntlChar::BLOCK_CODE_OL_CHIKI` `int`  
Bloque de caracteres Ol Chiki utilizados en la escritura Ol Chiki para el idioma Santali.

`IntlChar::BLOCK_CODE_CYRILLIC_EXTENDED_A` `int`  
Bloque de extensiones cirílicas A añadiendo caracteres adicionales para la escritura de lenguas eslavas y no eslavas.

`IntlChar::BLOCK_CODE_VAI` `int`  
Bloque de caracteres Vai utilizados en la escritura Vai de Sierra Leona.

`IntlChar::BLOCK_CODE_CYRILLIC_EXTENDED_B` `int`  
Bloque de extensiones cirílicas B añadiendo caracteres adicionales para la escritura de lenguas eslavas y no eslavas.

`IntlChar::BLOCK_CODE_SAURASHTRA` `int`  
Bloque de caracteres Saurashtra utilizados en la escritura Saurashtra de la India.

`IntlChar::BLOCK_CODE_KAYAH_LI` `int`  
Bloque de caracteres Kayah Li utilizados en la escritura Kayah Li para los idiomas Kayah en Birmania.

`IntlChar::BLOCK_CODE_REJANG` `int`  
Bloque de caracteres Rejang utilizados en la escritura Rejang de Indonesia.

`IntlChar::BLOCK_CODE_CHAM` `int`  
Bloque de caracteres Cham utilizados en la escritura Cham del Sudeste Asiático.

`IntlChar::BLOCK_CODE_ANCIENT_SYMBOLS` `int`  
Bloque de símbolos antiguos utilizados en diversos contextos históricos y culturales.

`IntlChar::BLOCK_CODE_PHAISTOS_DISC` `int`  
Bloque de caracteres del disco de Phaistos utilizados en la inscripción del disco de Phaistos, un artefacto minoico.

`IntlChar::BLOCK_CODE_LYCIAN` `int`  
Bloque de caracteres licios utilizados en la escritura licia de la antigua Licia.

`IntlChar::BLOCK_CODE_CARIAN` `int`  
Bloque de caracteres carios utilizados en la escritura caria de la antigua Caria.

`IntlChar::BLOCK_CODE_LYDIAN` `int`  
Bloque de caracteres lidios utilizados en la escritura lidia de la antigua Lidia.

`IntlChar::BLOCK_CODE_MAHJONG_TILES` `int`  
Bloque de fichas de Mahjong utilizadas en los juegos de Mahjong.

`IntlChar::BLOCK_CODE_DOMINO_TILES` `int`  
Bloque de fichas de dominó utilizadas en los juegos de dominó.

`IntlChar::BLOCK_CODE_SAMARITAN` `int`  
Bloque de caracteres samaritanos utilizados en la escritura samaritana.

`IntlChar::BLOCK_CODE_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED` `int`  
Bloque extendido de silabarios aborígenes canadienses unificados añadiendo caracteres adicionales para ciertos idiomas indígenas.

`IntlChar::BLOCK_CODE_TAI_THAM` `int`  
Bloque de caracteres Tai Tham utilizados en la escritura Tai Tham para ciertos idiomas del sudeste asiático.

`IntlChar::BLOCK_CODE_VEDIC_EXTENSIONS` `int`  
Bloque de extensiones védicas que añaden caracteres adicionales para textos védicos.

`IntlChar::BLOCK_CODE_LISU` `int`  
Bloque de caracteres Lisu utilizados en la escritura Lisu de ciertas regiones de Asia.

`IntlChar::BLOCK_CODE_BAMUM` `int`  
Bloque de caracteres Bamum utilizados en la escritura Bamum de Camerún.

`IntlChar::BLOCK_CODE_COMMON_INDIC_NUMBER_FORMS` `int`  
Bloque de formas numéricas indic comunes utilizadas en sistemas de numeración de idiomas indoarios.

`IntlChar::BLOCK_CODE_DEVANAGARI_EXTENDED` `int`  
Bloque extendido de caracteres Devanagari que añade caracteres adicionales para la escritura de idiomas que utilizan Devanagari.

`IntlChar::BLOCK_CODE_HANGUL_JAMO_EXTENDED_A` `int`  
Bloque extendido A de Jamo Hangul que añade caracteres adicionales para la escritura coreana.

`IntlChar::BLOCK_CODE_JAVANESE` `int`  
Bloque de caracteres javaneses utilizados en la escritura javanesa de Indonesia.

`IntlChar::BLOCK_CODE_MYANMAR_EXTENDED_A` `int`  
Bloque extendido A de caracteres Myanmar que añade caracteres adicionales para la escritura Myanmar.

`IntlChar::BLOCK_CODE_TAI_VIET` `int`  
Bloque de caracteres Tai Viet utilizados en la escritura Tai Viet para ciertos idiomas del sudeste asiático.

`IntlChar::BLOCK_CODE_MEETEI_MAYEK` `int`  
Bloque de caracteres Meetei Mayek utilizados en la escritura Meetei Mayek para el idioma Meitei.

`IntlChar::BLOCK_CODE_HANGUL_JAMO_EXTENDED_B` `int`  
Bloque extendido B de Jamo Hangul que añade caracteres adicionales para la escritura coreana.

`IntlChar::BLOCK_CODE_IMPERIAL_ARAMAIC` `int`  
Bloque de caracteres arameos imperiales utilizados en la escritura aramea antigua.

`IntlChar::BLOCK_CODE_OLD_SOUTH_ARABIAN` `int`  
Bloque de caracteres árabes del sur antiguos utilizados en la escritura árabe del sur antigua.

`IntlChar::BLOCK_CODE_AVESTAN` `int`  
Bloque de caracteres avestánicos utilizados en la escritura avestánica de textos zoroastrianos.

`IntlChar::BLOCK_CODE_INSCRIPTIONAL_PARTHIAN` `int`  
Bloque de caracteres partos inscriptionales utilizados en la escritura parta antigua.

`IntlChar::BLOCK_CODE_INSCRIPTIONAL_PAHLAVI` `int`  
Bloque de caracteres pahlavi inscriptionales utilizados en la escritura pahlavi de la antigua Persia.

`IntlChar::BLOCK_CODE_OLD_TURKIC` `int`  
Bloque de caracteres turcos antiguos utilizados en la escritura turca antigua.

`IntlChar::BLOCK_CODE_RUMI_NUMERAL_SYMBOLS` `int`  
Bloque de símbolos numéricos Rumi utilizados en el sistema de numeración Rumi.

`IntlChar::BLOCK_CODE_KAITHI` `int`  
Bloque de caracteres Kaithi utilizados en la escritura Kaithi de la India del Norte.

`IntlChar::BLOCK_CODE_EGYPTIAN_HIEROGLYPHS` `int`  
Bloque de jeroglíficos egipcios utilizados en la escritura egipcia antigua.

`IntlChar::BLOCK_CODE_ENCLOSED_ALPHANUMERIC_SUPPLEMENT` `int`  
Bloque de suplementos alfanuméricos encerrados añadiendo caracteres alfanuméricos en círculos u otras formas.

`IntlChar::BLOCK_CODE_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT` `int`  
Bloque de suplementos ideográficos encerrados añadiendo ideogramas en círculos u otras formas.

`IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C` `int`  
Bloque de ideogramas unificados CJK, extensión C, añadiendo aún más caracteres.

`IntlChar::BLOCK_CODE_MANDAIC` `int`  
Bloque de caracteres mandeos utilizados en la escritura mandea.

`IntlChar::BLOCK_CODE_BATAK` `int`  
Bloque de caracteres Batak utilizados en la escritura Batak de Indonesia.

`IntlChar::BLOCK_CODE_ETHIOPIC_EXTENDED_A` `int`  
Bloque extendido A de caracteres etíopes añadiendo caracteres adicionales para la escritura etíope.

`IntlChar::BLOCK_CODE_BRAHMI` `int`  
Bloque de caracteres Brahmi utilizados en la escritura Brahmi antigua de la India.

`IntlChar::BLOCK_CODE_BAMUM_SUPPLEMENT` `int`  
Bloque de suplementos Bamum añadiendo caracteres adicionales para la escritura Bamum.

`IntlChar::BLOCK_CODE_KANA_SUPPLEMENT` `int`  
Bloque de suplementos Kana añadiendo caracteres adicionales para la escritura japonesa Kana.

`IntlChar::BLOCK_CODE_PLAYING_CARDS` `int`  
Bloque de caracteres de cartas de juego utilizados en los símbolos de juegos de cartas.

`IntlChar::BLOCK_CODE_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS` `int`  
Bloque de símbolos y pictogramas diversos utilizados en diversos contextos visuales.

`IntlChar::BLOCK_CODE_EMOTICONS` `int`  
Bloque de emoticones utilizados para representar expresiones faciales y emociones en el texto.

`IntlChar::BLOCK_CODE_TRANSPORT_AND_MAP_SYMBOLS` `int`  
Bloque de símbolos de transporte y mapas utilizados en las representaciones gráficas de sistemas de transporte y mapas.

`IntlChar::BLOCK_CODE_ALCHEMICAL_SYMBOLS` `int`  
Bloque de los símbolos alquímicos utilizados en la representación de los conceptos alquímicos históricos.

`IntlChar::BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D` `int`  
Bloque de los ideogramas unificados CJK, extensión D, añadiendo aún más caracteres.

`IntlChar::BLOCK_CODE_ARABIC_EXTENDED_A` `int`  
Bloque extendido A de caracteres árabes añadiendo caracteres adicionales para la escritura árabe.

`IntlChar::BLOCK_CODE_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS` `int`  
Bloque de los símbolos alfabéticos matemáticos árabes utilizados en las expresiones matemáticas.

`IntlChar::BLOCK_CODE_CHAKMA` `int`  
Bloque de los caracteres Chakma utilizados en la escritura Chakma de la India y Bangladesh.

`IntlChar::BLOCK_CODE_MEETEI_MAYEK_EXTENSIONS` `int`  
Bloque de las extensiones Meetei Mayek añadiendo caracteres adicionales para la escritura Meetei Mayek.

`IntlChar::BLOCK_CODE_MEROITIC_CURSIVE` `int`  
Bloque de los caracteres cursivos meroíticos utilizados en la escritura meroítica antigua.

`IntlChar::BLOCK_CODE_MEROITIC_HIEROGLYPHS` `int`  
Bloque de los jeroglíficos meroíticos utilizados en la escritura meroítica antigua.

`IntlChar::BLOCK_CODE_MIAO` `int`  
Bloque de los caracteres Miao utilizados en la escritura Miao de ciertas regiones de Asia.

`IntlChar::BLOCK_CODE_SHARADA` `int`  
Bloque de los caracteres Sharada utilizados en la escritura Sharada de la India.

`IntlChar::BLOCK_CODE_SORA_SOMPENG` `int`  
Bloque de los caracteres Sora Sompeng utilizados en la escritura Sora Sompeng de la India.

`IntlChar::BLOCK_CODE_SUNDANESE_SUPPLEMENT` `int`  
Bloque de los suplementos Sundaneses añadiendo caracteres adicionales para la escritura sundanesa.

`IntlChar::BLOCK_CODE_TAKRI` `int`  
Bloque de los caracteres Takri utilizados en la escritura Takri de la India.

`IntlChar::BLOCK_CODE_BASSA_VAH` `int`  
Bloque de los caracteres Bassa Vah utilizados en la escritura Bassa Vah de Guinea.

`IntlChar::BLOCK_CODE_CAUCASIAN_ALBANIAN` `int`  
Bloque de los caracteres albaneses caucásicos utilizados en la escritura albana caucásica antigua.

`IntlChar::BLOCK_CODE_COPTIC_EPACT_NUMBERS` `int`  
Bloque de los números epactales coptos utilizados en el cálculo de los epacts para el calendario copto.

`IntlChar::BLOCK_CODE_COMBINING_DIACRITICAL_MARKS_EXTENDED` `int`  
Bloque de las marcas diacríticas combinantes extendidas añadiendo caracteres adicionales para modificar los caracteres de base.

`IntlChar::BLOCK_CODE_DUPLOYAN` `int`  
Bloque de caracteres Duployan utilizados en la escritura fonética de la estenografía Duployan.

`IntlChar::BLOCK_CODE_ELBASAN` `int`  
Bloque de caracteres Elbasan utilizados en la escritura Elbasan de la antigua Albania.

`IntlChar::BLOCK_CODE_GEOMETRIC_SHAPES_EXTENDED` `int`  
Bloque extendido de formas geométricas que añade formas adicionales para una variedad de símbolos gráficos.

`IntlChar::BLOCK_CODE_GRANTHA` `int`  
Bloque de caracteres Grantha utilizados en la escritura Grantha de la India.

`IntlChar::BLOCK_CODE_KHOJKI` `int`  
Bloque de caracteres Khojki utilizados en la escritura Khojki de la India.

`IntlChar::BLOCK_CODE_KHUDAWADI` `int`  
Bloque de caracteres Khudawadi utilizados en la escritura Khudawadi de la India.

`IntlChar::BLOCK_CODE_LATIN_EXTENDED_E` `int`  
Bloque de extensiones Latinas adicionales E que añaden caracteres adicionales para la escritura de lenguas que utilizan el alfabeto latino.

`IntlChar::BLOCK_CODE_LINEAR_A` `int`  
Bloque de caracteres Linear A utilizados en la escritura Linear A de la antigua Creta.

`IntlChar::BLOCK_CODE_MAHAJANI` `int`  
Bloque de caracteres Mahajani utilizados en la escritura Mahajani de la India.

`IntlChar::BLOCK_CODE_MANICHAEAN` `int`  
Bloque de caracteres maniqueos utilizados en la antigua escritura maniquea.

`IntlChar::BLOCK_CODE_MENDE_KIKAKUI` `int`  
Bloque de caracteres Mende Kikakui utilizados en la escritura Mende Kikakui de Sierra Leona.

`IntlChar::BLOCK_CODE_MODI` `int`  
Bloque de caracteres Modi utilizados en la escritura Modi de la India.

`IntlChar::BLOCK_CODE_MRO` `int`  
Bloque de caracteres Mro utilizados en la escritura Mro de ciertos pueblos del Sudeste Asiático.

`IntlChar::BLOCK_CODE_MYANMAR_EXTENDED_B` `int`  
Bloque extendido B de caracteres Myanmar que añade caracteres adicionales para la escritura Myanmar.

`IntlChar::BLOCK_CODE_NABATAEAN` `int`  
Bloque de caracteres Nabateos utilizados en la antigua escritura Nabatea.

`IntlChar::BLOCK_CODE_OLD_NORTH_ARABIAN` `int`  
Bloque de caracteres árabes del Norte antiguos utilizados en la antigua escritura norteárabe.

`IntlChar::BLOCK_CODE_OLD_PERMIC` `int`  
Bloque de caracteres permic antiguos utilizados en la escritura permic de la antigua Persia.

`IntlChar::BLOCK_CODE_ORNAMENTAL_DINGBATS` `int`  
Bloque de dingbats ornamentales utilizados para añadir elementos decorativos en el texto.

`IntlChar::BLOCK_CODE_PAHAWH_HMONG` `int`  
Bloque de caracteres Pahawh Hmong utilizados en la escritura Pahawh Hmong para el idioma Hmong.

`IntlChar::BLOCK_CODE_PALMYRENE` `int`  
Bloque de caracteres palmirenos utilizados en la escritura palmirena de la antigüedad.

`IntlChar::BLOCK_CODE_PAU_CIN_HAU` `int`  
Bloque de caracteres Pau Cin Hau utilizados en la escritura Pau Cin Hau de ciertas comunidades en Asia.

`IntlChar::BLOCK_CODE_PSALTER_PAHLAVI` `int`  
Bloque de caracteres pahlavi de los salmos utilizados en la escritura pahlavi para textos religiosos.

`IntlChar::BLOCK_CODE_SHORTHAND_FORMAT_CONTROLS` `int`  
Bloque de controles de formato taquigráfico utilizados para la taquigrafía y la transcripción rápida.

`IntlChar::BLOCK_CODE_SIDDHAM` `int`  
Bloque de caracteres Siddham utilizados en la escritura Siddham de la antigua India.

`IntlChar::BLOCK_CODE_SINHALA_ARCHAIC_NUMBERS` `int`  
Bloque de números arcaicos Sinhala utilizados en la escritura Sinhala antigua.

`IntlChar::BLOCK_CODE_SUPPLEMENTAL_ARROWS_C` `int`  
Bloque de flechas suplementarias C que añaden aún más variantes de flechas para diversas representaciones gráficas.

`IntlChar::BLOCK_CODE_TIRHUTA` `int`  
Bloque de caracteres Tirhuta utilizados en la escritura Tirhuta del noreste de la India.

`IntlChar::BLOCK_CODE_WARANG_CITI` `int`  
Bloque de caracteres Warang Citi utilizados en la escritura Warang Citi para el idioma Ho.

`IntlChar::BLOCK_CODE_COUNT` `int`  
Bloque code-count que define el número total de bloques disponibles.

`IntlChar::BLOCK_CODE_INVALID_CODE` `int`  
Bloque code-invalid-code que representa un código de bloque inválido o no definido.

`IntlChar::BPT_NONE` `int`  
Tipo de puntuación bidireccional: Ninguno.

`IntlChar::BPT_OPEN` `int`  
Tipo de puntuación bidireccional: Apertura.

`IntlChar::BPT_CLOSE` `int`  
Tipo de puntuación bidireccional: Cierre.

`IntlChar::BPT_COUNT` `int`  
Número total de tipos de puntuaciones bidireccionales.

`IntlChar::EA_NEUTRAL` `int`  
Ancho este-asiático: Neutro.

`IntlChar::EA_AMBIGUOUS` `int`  
Ancho este-asiático: Ambiguo.

`IntlChar::EA_HALFWIDTH` `int`  
Ancho este-asiático: Semi-ancho.

`IntlChar::EA_FULLWIDTH` `int`  
Ancho este-asiático: Ancho completo.

`IntlChar::EA_NARROW` `int`  
Ancho este-asiático: Estrecho.

`IntlChar::EA_WIDE` `int`  
Ancho este-asiático: Ancho.

`IntlChar::EA_COUNT` `int`  
Número total de categorías de ancho este-asiático.

`IntlChar::UNICODE_CHAR_NAME` `int`  
Nombre de carácter Unicode estándar.

`IntlChar::UNICODE_10_CHAR_NAME` `int`  
Nombre de carácter Unicode versión 10.

`IntlChar::EXTENDED_CHAR_NAME` `int`  
Nombre de carácter extendido Unicode.

`IntlChar::CHAR_NAME_ALIAS` `int`  
Alias de nombre de carácter Unicode.

`IntlChar::CHAR_NAME_CHOICE_COUNT` `int`  
Número de opciones para los alias de nombres de caracteres Unicode.

`IntlChar::SHORT_PROPERTY_NAME` `int`  
Nombre de propiedad corto.

`IntlChar::LONG_PROPERTY_NAME` `int`  
Nombre de propiedad largo.

`IntlChar::PROPERTY_NAME_CHOICE_COUNT` `int`  
Número de opciones para los nombres de propiedades.

`IntlChar::DT_NONE` `int`  
Tipo de descomposición: Ninguno.

`IntlChar::DT_CANONICAL` `int`  
Tipo de descomposición: Canónico.

`IntlChar::DT_COMPAT` `int`  
Tipo de descomposición: Compatibilidad.

`IntlChar::DT_CIRCLE` `int`  
Tipo de descomposición: Círculo.

`IntlChar::DT_FINAL` `int`  
Tipo de descomposición: Final.

`IntlChar::DT_FONT` `int`  
Tipo de descomposición: Fuente.

`IntlChar::DT_FRACTION` `int`  
Tipo de descomposición: Fracción.

`IntlChar::DT_INITIAL` `int`  
Tipo de descomposición: Inicial.

`IntlChar::DT_ISOLATED` `int`  
Tipo de descomposición: Aislado.

`IntlChar::DT_MEDIAL` `int`  
Tipo de descomposición: Medial.

`IntlChar::DT_NARROW` `int`  
Tipo de descomposición: Estrecho.

`IntlChar::DT_NOBREAK` `int`  
Tipo de descomposición: Sin ruptura.

`IntlChar::DT_SMALL` `int`  
Tipo de descomposición: Pequeño.

`IntlChar::DT_SQUARE` `int`  
Tipo de descomposición: Cuadrado.

`IntlChar::DT_SUB` `int`  
Tipo de descomposición: Sustitutivo.

`IntlChar::DT_SUPER` `int`  
Tipo de descomposición: Superíndice.

`IntlChar::DT_VERTICAL` `int`  
Tipo de descomposición: Vertical.

`IntlChar::DT_WIDE` `int`  
Tipo de descomposición: Ancho.

`IntlChar::DT_COUNT` `int`  
Número total de tipos de descomposición.

`IntlChar::JT_NON_JOINING` `int`  
Tipo de unión: No unido.

`IntlChar::JT_JOIN_CAUSING` `int`  
Tipo de unión: Causante de unión.

`IntlChar::JT_DUAL_JOINING` `int`  
Tipo de unión: Unión doble.

`IntlChar::JT_LEFT_JOINING` `int`  
Tipo de unión: Unión izquierda.

`IntlChar::JT_RIGHT_JOINING` `int`  
Tipo de unión: Unión derecha.

`IntlChar::JT_TRANSPARENT` `int`  
Tipo de unión: Transparente.

`IntlChar::JT_COUNT` `int`  
Número total de tipos de unión.

`IntlChar::JG_NO_JOINING_GROUP` `int`  
Grupo de unión: Sin grupo de unión.

`IntlChar::JG_AIN` `int`  
Grupo de unión: Ain.

`IntlChar::JG_ALAPH` `int`  
Grupo de unión: Alaph.

`IntlChar::JG_ALEF` `int`  
Grupo de unión: Alef.

`IntlChar::JG_BEH` `int`  
Grupo de unión: Beh.

`IntlChar::JG_BETH` `int`  
Grupo de unión: Beth.

`IntlChar::JG_DAL` `int`  
Grupo de unión: Dal.

`IntlChar::JG_DALATH_RISH` `int`  
Grupo de unión: Dalath Rish.

`IntlChar::JG_E` `int`  
Grupo de unión: E.

`IntlChar::JG_FEH` `int`  
Grupo de unión: Feh.

`IntlChar::JG_FINAL_SEMKATH` `int`  
Grupo de unión: Final Semkath.

`IntlChar::JG_GAF` `int`  
Grupo de unión: Gaf.

`IntlChar::JG_GAMAL` `int`  
Grupo de unión: Gamal.

`IntlChar::JG_HAH` `int`  
Grupo de unión: Hah.

`IntlChar::JG_TEH_MARBUTA_GOAL` `int`  
Grupo de unión: Teh Marbuta Goal.

`IntlChar::JG_HAMZA_ON_HEH_GOAL` `int`  
Grupo de unión: Hamza sobre Heh Goal.

`IntlChar::JG_HE` `int`  
Grupo de unión: He.

`IntlChar::JG_HEH` `int`  
Grupo de unión: Heh.

`IntlChar::JG_HEH_GOAL` `int`  
Grupo de unión: Heh Goal.

`IntlChar::JG_HETH` `int`  
Grupo de unión: Heth.

`IntlChar::JG_KAF` `int`  
Grupo de unión: Kaf.

`IntlChar::JG_KAPH` `int`  
Grupo de unión: Kaph.

`IntlChar::JG_KNOTTED_HEH` `int`  
Grupo de unión: Heh anudado.

`IntlChar::JG_LAM` `int`  
Grupo de unión: Lam.

`IntlChar::JG_LAMADH` `int`  
Grupo de unión: Lamadh.

`IntlChar::JG_MEEM` `int`  
Grupo de unión: Meem.

`IntlChar::JG_MIM` `int`  
Grupo de unión: Mim.

`IntlChar::JG_NOON` `int`  
Grupo de unión: Noon.

`IntlChar::JG_NUN` `int`  
Grupo de unión: Nun.

`IntlChar::JG_PE` `int`  
Grupo de unión: Pe.

`IntlChar::JG_QAF` `int`  
Grupo de unión: Qaf.

`IntlChar::JG_QAPH` `int`  
Grupo de unión: Qaph.

`IntlChar::JG_REH` `int`  
Grupo de unión: Reh.

`IntlChar::JG_REVERSED_PE` `int`  
Grupo de unión: Pe invertido.

`IntlChar::JG_SAD` `int`  
Grupo de unión: Sad.

`IntlChar::JG_SADHE` `int`  
Grupo de unión: Sadhe.

`IntlChar::JG_SEEN` `int`  
Grupo de unión: Seen.

`IntlChar::JG_SEMKATH` `int`  
Grupo de unión: Semkath.

`IntlChar::JG_SHIN` `int`  
Grupo de unión: Shin.

`IntlChar::JG_SWASH_KAF` `int`  
Grupo de unión: Swash Kaf.

`IntlChar::JG_SYRIAC_WAW` `int`  
Grupo de unión: Waw Syriac.

`IntlChar::JG_TAH` `int`  
Grupo de unión: Tah.

`IntlChar::JG_TAW` `int`  
Grupo de unión: Taw.

`IntlChar::JG_TEH_MARBUTA` `int`  
Grupo de unión: Teh Marbuta.

`IntlChar::JG_TETH` `int`  
Grupo de unión: Teth.

`IntlChar::JG_WAW` `int`  
Grupo de unión: Waw.

`IntlChar::JG_YEH` `int`  
Grupo de unión: Yeh.

`IntlChar::JG_YEH_BARREE` `int`  
Grupo de unión: Yeh Barree.

`IntlChar::JG_YEH_WITH_TAIL` `int`  
Grupo de unión: Yeh con cola.

`IntlChar::JG_YUDH` `int`  
Grupo de unión: Yudh.

`IntlChar::JG_YUDH_HE` `int`  
Grupo de unión: Yudh-He.

`IntlChar::JG_ZAIN` `int`  
Grupo de unión: Zain.

`IntlChar::JG_FE` `int`  
Grupo de unión: Fe.

`IntlChar::JG_KHAPH` `int`  
Grupo de unión: Khaph.

`IntlChar::JG_ZHAIN` `int`  
Grupo de unión: Zhain.

`IntlChar::JG_BURUSHASKI_YEH_BARREE` `int`  
Grupo de unión: Yeh Barree Burushaski.

`IntlChar::JG_FARSI_YEH` `int`  
Grupo de unión: Yeh Farsi.

`IntlChar::JG_NYA` `int`  
Grupo de unión: Nya.

`IntlChar::JG_ROHINGYA_YEH` `int`  
Grupo de unión: Yeh Rohingya.

`IntlChar::JG_MANICHAEAN_ALEPH` `int`  
Grupo de unión: Aleph Maniqueo.

`IntlChar::JG_MANICHAEAN_AYIN` `int`  
Grupo de unión: Ayin Maniqueo.

`IntlChar::JG_MANICHAEAN_BETH` `int`  
Grupo de unión: Beth Maniqueo.

`IntlChar::JG_MANICHAEAN_DALETH` `int`  
Grupo de unión: Daleth Maniqueo.

`IntlChar::JG_MANICHAEAN_DHAMEDH` `int`  
Grupo de unión: Dhamedh Maniqueo.

`IntlChar::JG_MANICHAEAN_FIVE` `int`  
Grupo de unión: Cinco Maniqueo.

`IntlChar::JG_MANICHAEAN_GIMEL` `int`  
Grupo de unión: Gimel Maniqueo.

`IntlChar::JG_MANICHAEAN_HETH` `int`  
Grupo de unión: Heth Maniqueo.

`IntlChar::JG_MANICHAEAN_HUNDRED` `int`  
Grupo de unión: Cien Maniqueo.

`IntlChar::JG_MANICHAEAN_KAPH` `int`  
Grupo de unión: Kaph Maniqueo.

`IntlChar::JG_MANICHAEAN_LAMEDH` `int`  
Grupo de unión: Lamedh Maniqueo.

`IntlChar::JG_MANICHAEAN_MEM` `int`  
Grupo de unión: Mem Maniqueo.

`IntlChar::JG_MANICHAEAN_NUN` `int`  
Grupo de unión: Nun Maniqueo.

`IntlChar::JG_MANICHAEAN_ONE` `int`  
Grupo de unión: Uno Maniqueo.

`IntlChar::JG_MANICHAEAN_PE` `int`  
Grupo de unión: Pe Maniqueo.

`IntlChar::JG_MANICHAEAN_QOPH` `int`  
Grupo de unión: Qoph Maniqueo.

`IntlChar::JG_MANICHAEAN_RESH` `int`  
Grupo de unión: Resh Maniqueo.

`IntlChar::JG_MANICHAEAN_SADHE` `int`  
Grupo de unión: Sadhe Maniqueo.

`IntlChar::JG_MANICHAEAN_SAMEKH` `int`  
Grupo de unión: Samekh Maniqueo.

`IntlChar::JG_MANICHAEAN_TAW` `int`  
Grupo de unión: Taw Maniqueo.

`IntlChar::JG_MANICHAEAN_TEN` `int`  
Grupo de unión: Diez Maniqueo.

`IntlChar::JG_MANICHAEAN_TETH` `int`  
Grupo de unión: Teth Maniqueo.

`IntlChar::JG_MANICHAEAN_THAMEDH` `int`  
Grupo de unión: Thamedh Maniqueo.

`IntlChar::JG_MANICHAEAN_TWENTY` `int`  
Grupo de unión: Veinte Maniqueo.

`IntlChar::JG_MANICHAEAN_WAW` `int`  
Grupo de unión: Waw Maniqueo.

`IntlChar::JG_MANICHAEAN_YODH` `int`  
Grupo de unión: Yodh Maniqueo.

`IntlChar::JG_MANICHAEAN_ZAYIN` `int`  
Grupo de unión: Zayin Maniqueo.

`IntlChar::JG_STRAIGHT_WAW` `int`  
Grupo de unión: Waw recto.

`IntlChar::JG_COUNT` `int`  
Número total de grupos de unión.

`IntlChar::GCB_OTHER` `int`  
Categoría de cluster de grafemas: Otro.

`IntlChar::GCB_CONTROL` `int`  
Categoría de cluster de grafemas: Control.

`IntlChar::GCB_CR` `int`  
Categoría de cluster de grafemas: Retorno de carro.

`IntlChar::GCB_EXTEND` `int`  
Categoría de cluster de grafemas: Extensión.

`IntlChar::GCB_L` `int`  
Categoría de cluster de grafemas: Letra L.

`IntlChar::GCB_LF` `int`  
Categoría de cluster de grafemas: Salto de línea.

`IntlChar::GCB_LV` `int`  
Categoría de cluster de grafemas: LV.

`IntlChar::GCB_LVT` `int`  
Categoría de cluster de grafemas: LVT.

`IntlChar::GCB_T` `int`  
Categoría de cluster de grafemas: T.

`IntlChar::GCB_V` `int`  
Categoría de cluster de grafemas: V.

`IntlChar::GCB_SPACING_MARK` `int`  
Categoría de cluster de graphemes: Marca de espaciado.

`IntlChar::GCB_PREPEND` `int`  
Categoría de cluster de graphemes: Prefijo.

`IntlChar::GCB_REGIONAL_INDICATOR` `int`  
Categoría de cluster de graphemes: Indicador regional.

`IntlChar::GCB_COUNT` `int`  
Número total de categorías de cluster de graphemes.

`IntlChar::WB_OTHER` `int`  
Categoría de separación de palabras: Otro.

`IntlChar::WB_ALETTER` `int`  
Categoría de separación de palabras: Letra A.

`IntlChar::WB_FORMAT` `int`  
Categoría de separación de palabras: Formato.

`IntlChar::WB_KATAKANA` `int`  
Categoría de separación de palabras: Katakana.

`IntlChar::WB_MIDLETTER` `int`  
Categoría de separación de palabras: Letra media.

`IntlChar::WB_MIDNUM` `int`  
Categoría de separación de palabras: Número medio.

`IntlChar::WB_NUMERIC` `int`  
Categoría de separación de palabras: Numérico.

`IntlChar::WB_EXTENDNUMLET` `int`  
Categoría de separación de palabras: Extensión numérica y letra.

`IntlChar::WB_CR` `int`  
Categoría de separación de palabras: Retorno de carro.

`IntlChar::WB_EXTEND` `int`  
Categoría de separación de palabras: Extensión.

`IntlChar::WB_LF` `int`  
Categoría de separación de palabras: Salto de línea.

`IntlChar::WB_MIDNUMLET` `int`  
Categoría de separación de palabras: Número y letra media.

`IntlChar::WB_NEWLINE` `int`  
Categoría de separación de palabras: Nueva línea.

`IntlChar::WB_REGIONAL_INDICATOR` `int`  
Categoría de separación de palabras: Indicador regional.

`IntlChar::WB_HEBREW_LETTER` `int`  
Categoría de separación de palabras: Letra hebrea.

`IntlChar::WB_SINGLE_QUOTE` `int`  
Categoría de separación de palabras: Comillas simples.

`IntlChar::WB_DOUBLE_QUOTE` `int`  
Categoría de separación de palabras: Comillas dobles.

`IntlChar::WB_COUNT` `int`  
Número total de categorías de separación de palabras.

`IntlChar::SB_OTHER` `int`  
Categoría de separación de frases: Otro.

`IntlChar::SB_ATERM` `int`  
Categoría de separación de frases: Aterm.

`IntlChar::SB_CLOSE` `int`  
Categoría de separación de frases: Cierre.

`IntlChar::SB_FORMAT` `int`  
Categoría de separación de frases: Formato.

`IntlChar::SB_LOWER` `int`  
Categoría de separación de frases: Minúsculas.

`IntlChar::SB_NUMERIC` `int`  
Categoría de separación de frases: Numérico.

`IntlChar::SB_OLETTER` `int`  
Categoría de separación de frases: Letra O.

`IntlChar::SB_SEP` `int`  
Categoría de separación de frases: Separador.

`IntlChar::SB_SP` `int`  
Categoría de separación de frases: Espaciado.

`IntlChar::SB_STERM` `int`  
Categoría de separación de frases: Sterm.

`IntlChar::SB_UPPER` `int`  
Categoría de separación de frases: Mayúsculas.

`IntlChar::SB_CR` `int`  
Categoría de separación de frases: Retorno de carro.

`IntlChar::SB_EXTEND` `int`  
Categoría de separación de frases: Extensión.

`IntlChar::SB_LF` `int`  
Categoría de separación de frases: Salto de línea.

`IntlChar::SB_SCONTINUE` `int`  
Categoría de separación de frases: Continuación.

`IntlChar::SB_COUNT` `int`  
Número total de categorías de separación de frases.

`IntlChar::LB_UNKNOWN` `int`  
Categoría de separación de líneas: Desconocida.

`IntlChar::LB_AMBIGUOUS` `int`  
Categoría de separación de líneas: Ambigua.

`IntlChar::LB_ALPHABETIC` `int`  
Categoría de separación de líneas: Alfabética.

`IntlChar::LB_BREAK_BOTH` `int`  
Categoría de separación de líneas: Separación en ambos lados.

`IntlChar::LB_BREAK_AFTER` `int`  
Categoría de separación de líneas: Separación después.

`IntlChar::LB_BREAK_BEFORE` `int`  
Categoría de separación de líneas: Separación antes.

`IntlChar::LB_MANDATORY_BREAK` `int`  
Categoría de separación de líneas: Separación obligatoria.

`IntlChar::LB_CONTINGENT_BREAK` `int`  
Categoría de separación de líneas: Separación contingente.

`IntlChar::LB_CLOSE_PUNCTUATION` `int`  
Categoría de separación de líneas: Puntuación cerrada.

`IntlChar::LB_COMBINING_MARK` `int`  
Categoría de separación de líneas: Marca combinante.

`IntlChar::LB_CARRIAGE_RETURN` `int`  
Categoría de separación de líneas: Retorno de carro.

`IntlChar::LB_EXCLAMATION` `int`  
Categoría de separación de líneas: Signo de exclamación.

`IntlChar::LB_GLUE` `int`  
Categoría de separación de líneas: Pegamento.

`IntlChar::LB_HYPHEN` `int`  
Categoría de separación de líneas: Guión.

`IntlChar::LB_IDEOGRAPHIC` `int`  
Categoría de separación de líneas: Ideográfico.

`IntlChar::LB_INSEPARABLE` `int`  
Categoría de separación de líneas: Inseparable.

`IntlChar::LB_INSEPERABLE` `int`  
Categoría de separación de líneas: Inseparable.

`IntlChar::LB_INFIX_NUMERIC` `int`  
Categoría de separación de líneas: Numérico intermedio.

`IntlChar::LB_LINE_FEED` `int`  
Categoría de separación de líneas: Salto de línea.

`IntlChar::LB_NONSTARTER` `int`  
Categoría de separación de líneas: No iniciador.

`IntlChar::LB_NUMERIC` `int`  
Categoría de separación de líneas: Numérico.

`IntlChar::LB_OPEN_PUNCTUATION` `int`  
Categoría de separación de líneas: Puntuación abierta.

`IntlChar::LB_POSTFIX_NUMERIC` `int`  
Categoría de separación de líneas: Numérico postfijo.

`IntlChar::LB_PREFIX_NUMERIC` `int`  
Categoría de separación de líneas: Numérico prefijo.

`IntlChar::LB_QUOTATION` `int`  
Categoría de separación de líneas: Cita.

`IntlChar::LB_COMPLEX_CONTEXT` `int`  
Categoría de separación de líneas: Contexto complejo.

`IntlChar::LB_SURROGATE` `int`  
Categoría de separación de líneas: Surrogate.

`IntlChar::LB_SPACE` `int`  
Categoría de separación de líneas: Espacio.

`IntlChar::LB_BREAK_SYMBOLS` `int`  
Categoría de separación de líneas: Símbolos de ruptura.

`IntlChar::LB_ZWSPACE` `int`  
Categoría de separación de líneas: Espacio cero ancho.

`IntlChar::LB_NEXT_LINE` `int`  
Categoría de separación de líneas: Línea siguiente.

`IntlChar::LB_WORD_JOINER` `int`  
Categoría de separación de líneas: Unificador de palabras.

`IntlChar::LB_H2` `int`  
Categoría de separación de líneas: H2.

`IntlChar::LB_H3` `int`  
Categoría de separación de líneas: H3.

`IntlChar::LB_JL` `int`  
Categoría de separación de líneas: JL.

`IntlChar::LB_JT` `int`  
Categoría de separación de líneas: JT.

`IntlChar::LB_JV` `int`  
Categoría de separación de líneas: JV.

`IntlChar::LB_CLOSE_PARENTHESIS` `int`  
Categoría de separación de líneas: Paréntesis cerrado.

`IntlChar::LB_CONDITIONAL_JAPANESE_STARTER` `int`  
Categoría de separación de líneas: Inicio condicional japonés.

`IntlChar::LB_HEBREW_LETTER` `int`  
Categoría de separación de líneas: Letra hebrea.

`IntlChar::LB_REGIONAL_INDICATOR` `int`  
Categoría de separación de líneas: Indicador regional.

`IntlChar::LB_COUNT` `int`  
Número total de categorías de separación de líneas.

`IntlChar::NT_NONE` `int`  
Tipo de número: Ninguno.

`IntlChar::NT_DECIMAL` `int`  
Tipo de número: Decimal.

`IntlChar::NT_DIGIT` `int`  
Tipo de número: Dígito.

`IntlChar::NT_NUMERIC` `int`  
Tipo de número: Numérico.

`IntlChar::NT_COUNT` `int`  
Número total de tipos de números.

`IntlChar::HST_NOT_APPLICABLE` `int`  
Tipo de sílaba Hangul: No aplicable.

`IntlChar::HST_LEADING_JAMO` `int`  
Tipo de sílaba Hangul: Jamo inicial.

`IntlChar::HST_VOWEL_JAMO` `int`  
Tipo de sílaba Hangul: Jamo vocal.

`IntlChar::HST_TRAILING_JAMO` `int`  
Tipo de sílaba Hangul: Jamo final.

`IntlChar::HST_LV_SYLLABLE` `int`  
Tipo de sílaba Hangul: Sílabas LV.

`IntlChar::HST_LVT_SYLLABLE` `int`  
Tipo de sílaba Hangul: Sílabas LVT.

`IntlChar::HST_COUNT` `int`  
Número total de tipos de sílabas Hangul.

`IntlChar::FOLD_CASE_DEFAULT` `int`  
Opción de plegado de mayúsculas: Por defecto.

`IntlChar::FOLD_CASE_EXCLUDE_SPECIAL_I` `int`  
Opción de plegado de mayúsculas: Excluir la I especial.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se añadieron `IntlChar::PROPERTY_IDS_UNARY_OPERATOR`, `IntlChar::PROPERTY_ID_COMPAT_MATH_START`, `IntlChar::PROPERTY_ID_COMPAT_MATH_CONTINUE`. |
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 7.0.6 | La constante `IntlChar::NO_NUMERIC_VALUE` ha sido añadida. |
