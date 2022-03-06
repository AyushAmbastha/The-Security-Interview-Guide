# HTTP Public Key Pinning (HPKP)

HTTP Public Key Pinning (HPKP) was a security feature that used to tell a web client to associate a specific cryptographic public key with a certain web server to decrease the risk of MITM attacks with forged certificates. It has been removed in modern browsers and is no longer supported.

To ensure the authenticity of a server's public key used in TLS sessions, this public key is wrapped into an X.509 certificate which is usually signed by a certificate authority (CA). Web clients such as browsers trust a lot of these CAs, which can all create certificates for arbitrary domain names. If an attacker is able to compromise a single CA, they can perform MITM attacks on various TLS connections. HPKP can circumvent this threat for the HTTPS protocol by telling the client which public key belongs to a certain web server.

HPKP is a Trust on First Use (TOFU) technique. The first time a web server tells a client via a special HTTP header which public keys belong to it, the client stores this information for a given period of time. When the client visits the server again, it expects at least one certificate in the certificate chain to contain a public key whose fingerprint is already known via HPKP. If the server delivers an unknown public key, the client should present a warning to the user.

Note: Public Key Pinning mechanism was deprecated in favor of Certificate Transparency and Expect-CT header.