
def test_simple_case(mock_google_maps):
    from main import convert_street_address
    assert convert_street_address("5 Av. Anatole, Paris, Champ de Mars") == "Avenue Anatole France,75007,Paris,France"