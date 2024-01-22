import pytest

from jami.encryption import (
    InvalidCypher,
    WrongPassword,
    password_decrypt,
    password_encrypt,
)


def test_encrypt_decrypt():
    cypher = password_encrypt(b"hello world", "mypassword")
    print(cypher)
    assert password_decrypt(cypher, "mypassword") == b"hello world"


def test_decrypt_invalid_cypher():
    with pytest.raises(InvalidCypher):
        password_decrypt(b"1", "mypassword")


def test_decrypt_invalid_password():
    cypher = password_encrypt(b"hello world", "mypassword")
    with pytest.raises(WrongPassword):
        password_decrypt(cypher, "wrongpassword")
