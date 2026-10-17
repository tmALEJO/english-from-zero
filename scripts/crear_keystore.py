#!/usr/bin/env python3
"""
Crea la clave de firma del APK (una sola vez) SIN instalar Java ni Android Studio.

Por qué importa: Android solo deja instalar una actualización encima de la app vieja
si las dos están firmadas con la MISMA clave. Sin esta clave, cada APK de GitHub
vendría firmado distinto y tendrías que desinstalar (y perder el progreso) para actualizar.

Uso:
    pip install cryptography
    python scripts/crear_keystore.py

Genera:
    release.p12            -> la clave (NO la subas a GitHub; .gitignore ya la excluye)
    keystore-base64.txt    -> el texto que pegas en el secreto KEYSTORE_BASE64 de GitHub
Y te muestra la contraseña para el secreto KEYSTORE_PASSWORD.

Guarda release.p12 y la contraseña en un lugar seguro (por ejemplo tu gestor de contraseñas).
Si los pierdes, el siguiente APK no se podrá instalar encima del actual.
"""
from __future__ import annotations

import base64
import datetime as dt
import secrets
import sys
from pathlib import Path

try:
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.serialization import pkcs12
    from cryptography.x509.oid import NameOID
except ImportError:
    sys.exit("Falta la librería: ejecuta  pip install cryptography  y vuelve a intentarlo.")

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "release.p12"
B64 = ROOT / "keystore-base64.txt"
ALIAS = "efz"


def main() -> None:
    if OUT.exists():
        sys.exit(f"Ya existe {OUT.name}. No la sobrescribo para que no pierdas tu clave actual.")

    password = secrets.token_urlsafe(18)
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    name = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, "English from Zero"),
        x509.NameAttribute(NameOID.COUNTRY_NAME, "CO"),
    ])
    now = dt.datetime.now(dt.timezone.utc)
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - dt.timedelta(days=1))
        .not_valid_after(now + dt.timedelta(days=365 * 30))
        .sign(key, hashes.SHA256())
    )
    data = pkcs12.serialize_key_and_certificates(
        name=ALIAS.encode(), key=key, cert=cert, cas=None,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode()),
    )
    OUT.write_bytes(data)
    B64.write_text(base64.b64encode(data).decode())

    print("Clave creada.\n")
    print("Ahora en GitHub: tu repositorio > Settings > Secrets and variables > Actions > New repository secret")
    print(f"  1. Nombre: KEYSTORE_BASE64    Valor: todo el contenido de {B64.name}")
    print(f"  2. Nombre: KEYSTORE_PASSWORD  Valor: {password}")
    print(f"\nGuarda {OUT.name} y la contraseña en un lugar seguro. Luego borra {B64.name}.")


if __name__ == "__main__":
    main()
