from app import app

def test_home():
    client = app.test_client()  # Cliente de pruebas de Flask
    response = client.get("/")  # Hacemos GET al endpoint raíz
    assert response.status_code == 200  # Verificamos que responda OK
    assert b"Hola Mundo" in response.data  # Verificamos el texto
