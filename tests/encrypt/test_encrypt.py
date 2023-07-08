import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message('string', 13) == 'gnirts'

    assert encrypt_message('string', 1) == 's_gnirt'

    assert encrypt_message('string', 2) == 'gnir_ts'

    assert encrypt_message('', 1) == ''

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('string', '1')

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 1)
