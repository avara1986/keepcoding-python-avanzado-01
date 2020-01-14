def test_get_animal_invalid_params(db_connection):
    assert "localhost" == db_connection["host"]
