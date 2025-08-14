from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_triage_alta():
    r = client.post('/triage/', json={'febre': 40.2, 'letargia': True, 'vomitos': False})
    assert r.status_code == 200
    assert r.json()['priority'] in {'Alta','Crítica'}
