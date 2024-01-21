from jami.encryption import password_decrypt, password_encrypt


def test_encrypt_decrypt():
    cypher = password_encrypt(b"hello world", "mypassword")
    print(cypher)
    assert password_decrypt(cypher, "mypassword") == b"hello world"
