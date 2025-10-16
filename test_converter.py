import converter


class TestToUrlStyle:
    def test_basic_conversion(self):
        assert converter.to_url_style('Hello World') == 'hello-world'

    def test_with_apostrophe(self):
        assert converter.to_url_style("Let's go!") == 'lets-go'

    def test_with_multiple_spaces(self):
        assert converter.to_url_style('Hello    World') == 'hello-world'

    def test_with_special_characters(self):
        assert converter.to_url_style('Hello@World#123') == 'hello-world-123'

    def test_with_dots(self):
        assert converter.to_url_style('file.name.txt') == 'file.name.txt'

    def test_with_leading_trailing_spaces(self):
        assert converter.to_url_style('  Hello World  ') == 'hello-world'

    def test_empty_string(self):
        assert converter.to_url_style('') == ''

    def test_only_special_characters(self):
        assert converter.to_url_style('@#$%') == ''


class TestStrip:
    def test_strip_spaces(self):
        assert converter.strip('  hello  ') == 'hello'

    def test_no_spaces(self):
        assert converter.strip('hello') == 'hello'

    def test_none(self):
        assert converter.strip(None) is None

    def test_empty_string(self):
        assert converter.strip('') == ''


class TestLowercase:
    def test_uppercase_to_lowercase(self):
        assert converter.lowercase('HELLO') == 'hello'

    def test_mixed_case(self):
        assert converter.lowercase('HeLLo WoRLd') == 'hello world'

    def test_already_lowercase(self):
        assert converter.lowercase('hello') == 'hello'

    def test_none(self):
        assert converter.lowercase(None) is None


class TestUppercase:
    def test_lowercase_to_uppercase(self):
        assert converter.uppercase('hello') == 'HELLO'

    def test_mixed_case(self):
        assert converter.uppercase('HeLLo WoRLd') == 'HELLO WORLD'

    def test_already_uppercase(self):
        assert converter.uppercase('HELLO') == 'HELLO'

    def test_none(self):
        assert converter.uppercase(None) is None


class TestExcelFriendly:
    def test_extract_numbers_and_dots(self):
        assert converter.excel_friendly('$123.45') == '123.45'

    def test_remove_all_non_numeric(self):
        assert converter.excel_friendly('Price: $1,234.56!') == '1234.56'

    def test_only_numbers(self):
        assert converter.excel_friendly('12345') == '12345'

    def test_no_valid_characters(self):
        assert converter.excel_friendly('abc!@#') == ''

    def test_none(self):
        assert converter.excel_friendly(None) is None


class TestCapitalizeAll:
    def test_capitalize_multiple_words(self):
        assert converter.capitalize_all('hello world') == 'Hello World'

    def test_already_capitalized(self):
        assert converter.capitalize_all('Hello World') == 'Hello World'

    def test_single_word(self):
        assert converter.capitalize_all('hello') == 'Hello'

    def test_mixed_case(self):
        assert converter.capitalize_all('hELLO wORLD') == 'Hello World'

    def test_none(self):
        assert converter.capitalize_all(None) is None


class TestCapitalizeFirst:
    def test_capitalize_first_letter(self):
        assert converter.capitalize_first('hello world') == 'Hello world'

    def test_already_capitalized(self):
        assert converter.capitalize_first('Hello world') == 'Hello world'

    def test_single_letter(self):
        assert converter.capitalize_first('h') == 'H'

    def test_none(self):
        assert converter.capitalize_first(None) is None


class TestStripQuerystringFromUrl:
    def test_url_with_querystring(self):
        assert converter.strip_querystring_from_url('https://example.com/page?id=123') == 'https://example.com/page'

    def test_url_without_querystring(self):
        assert converter.strip_querystring_from_url('https://example.com/page') == 'https://example.com/page'

    def test_url_with_multiple_question_marks(self):
        assert converter.strip_querystring_from_url('https://example.com?a=1?b=2') == 'https://example.com'

    def test_none(self):
        assert converter.strip_querystring_from_url(None) is None
