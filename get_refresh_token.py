import json
from google_auth_oauthlib.flow import Flow

SCOPES = ["https://www.googleapis.com/auth/adwords"]
CLIENT_SECRETS_FILE = "credentials.json"

flow = Flow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    scopes=SCOPES,
    redirect_uri='urn:ietf:wg:oauth:2.0:oob'
)

auth_url, _ = flow.authorization_url(
    access_type='offline',
    prompt='consent'
)

print("\n🔥 ABRE ESTE ENLACE EN TU NAVEGADOR Y AUTORIZA EL ACCESO:\n")
print(auth_url)
print("\n🔑 COPIA Y PEGA AQUÍ EL CÓDIGO DE VERIFICACIÓN:\n")
code = input("Código: ").strip()

flow.fetch_token(code=code)
creds = flow.credentials

print("\n🎉 TOKENS OBTENIDOS CON ÉXITO:")
print("🔁 Refresh Token:", creds.refresh_token)
print("🔓 Access Token:", creds.token)
print("⏳ Expira en:", creds.expiry)
