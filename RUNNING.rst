RUNNING
=======

gunicorn mockapi.app:api



SECRETS
-------
To generate keys used for this api

``
$ openssl rsa -in init.pem -outform PEM -out private.pem            # generate initial private key
$ openssl rsa -in init.pem -outform PEM -pubout -out public.pem     # strip the passphrase
$ openssl rsa -in private.pem -outform PEM -pubout -out public.pem  # generate public key
``
