import pytest
from automation.automation import main, validate_email, validate_phone

def test_exists():
    assert main

# @pytest.mark.skip("TODO")
def test_email_happy():
    actual = validate_email(['hansolo@starwars.com',])
    expected = ['hansolo@starwars.com',]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_email_bad_char_1():
    actual = validate_email(['han(solo@starwars.com',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_email_bad_char_2():
    actual = validate_email(['han)solo@starwars.com',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_email_two_at():
    actual = validate_email(['han)solo@star@wars.com',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_email_length():
    actual = validate_email(['12345678901234@567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890as',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_email_local_length():
    actual = validate_email(['12345678901234567890123456789012345678901234567890123456789012345@starwars.com',])
    expected = []
    assert actual == expected



# @pytest.mark.skip("TODO")
def test_phone_happy():
    actual = validate_phone(['8675308',])
    expected = ['206-867-5308']
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_phone_6_digits():
    actual = validate_phone(['999999',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_phone_7_digits():
    actual = validate_phone(['9999999',])
    expected = ['206-999-9999']
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_phone_8_digits():
    actual = validate_phone(['99999999',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_phone_10_digits():
    actual = validate_phone(['9999999999',])
    expected = ['999-999-9999']
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_phone_area_code():
    actual = validate_phone(['0009999999',])
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_phone_extension():
    actual = validate_phone(['9994567890x12345',])
    expected = ['999-456-7890x12345']
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_phone_garbage():
    actual = validate_phone([')(*$asdf9994567890asdf',])
    expected = ['999-456-7890']
    assert actual == expected