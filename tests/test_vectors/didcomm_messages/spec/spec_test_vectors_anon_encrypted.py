from authlib.common.encoding import json_dumps

from didcomm import AnonCryptAlg, Metadata
from tests.test_vectors.common import TTestVector

TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_XC20P_1 = json_dumps(
    {
        "protected": "eyJ0eXAiOiJhcHBsaWNhdGlvbi9kaWRjb21tLWVuY3J5cHRlZCtqc29uIiwiYWxnIjoiRUNESC1FUytBMjU2S1ciLCJlbmMiOiJYQzIwUCIsImFwdiI6IlkxWXh3b053WU5HNGRKRlBKanZtLTk0aWJhdXFBOUhyV0tZWmhtY29lU2ciLCJlcGsiOnsiY3J2IjoiWDI1NTE5IiwieCI6ImFNZzU4X1JqT2dGcjhZQWtCdmptOXhKYVZ3bnlXRVRmRFpYaGMyWVctamMiLCJrdHkiOiJPS1AifX0",
        "recipients": [
            {
                "header": {"kid": "did:example:bob#key-x25519-1"},
                "encrypted_key": "ThzyeMnViwuOEK3LLAhKXyoTUCOcBhaa4FxMvC1F3nLI9oXeKJjtPQ",
            },
            {
                "header": {"kid": "did:example:bob#key-x25519-2"},
                "encrypted_key": "yglsPC468bnwGL2aPcbGZUdvWFSipmoP9wJoaWqWVc3Ce56jI5v9xQ",
            },
            {
                "header": {"kid": "did:example:bob#key-x25519-3"},
                "encrypted_key": "SpAP0Gzo2lazwfAPyMhaTd1GlO6aRTmXngDu3j9iFwXetow_FkVxsw",
            },
            {
                "header": {"kid": "did:example:bob#key-x25519-4"},
                "encrypted_key": "_bWWYGGUZ2ITqcGDdP7C1_LkYb_2qtOaXQ3sWyoK6g161SGxsWEpoQ",
            },
        ],
        "iv": "9AVo9rQR0ZX7QEhguuRWV-JcCbwkaa3x",
        "ciphertext": "lSto80zaVP0ywIYzF2ecD01SM1xyqqPexRcZ8f-7D1T00AEWdTfJxw3Hp1ktNJFHpj5RHbFomrJy9LXErJWZXQWxmZBhmcIfZwu0b70Nq20m8I4oI-ZN2twVGMApFj-M98aZ11M17SI8jToOPPFJAdfLKBM3Q1nFW4LoqJZQgbRt0T2pHhgeS-xlwzSbC3aNpYPcfm-eceDrZis_GKgvCx5Jqw6BQdSYRxAXIwIM68owSAn9wAPTZlAqgyMXs3aZGvVSGYx6_PnWIqBhubdQ9hod2-XHUzT054MUJPCF16jC1K1qgOYrZguQC6FF0Ly9_Zcr1NQCZSeJLSuSP6BWtDsFaoVC5bLVDAtmqjKgI2uRlo6KaBaXq1f_nzIx_JfBPX8fmSI9k9nfBU0",
        "tag": "NW406iWJxQucfftvd5Cy9Q",
    }
)

TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_XC20P_2 = json_dumps(
    {
        "ciphertext": "912eTUDRKTzhUUqxosPogT1bs9w9wv4s4HmoWkaeU9Uj92V4ENpk-_ZPNSvPyXYLfFj0nc9V2-ux5jq8hqUd17WJpXEM1ReMUjtnTqeUzVa7_xtfkbfhaOZdL8OfgNquPDH1bYcBshN9O9lMT0V52gmGaAB45k4I2PNHcc0A5XWzditCYi8wOkPDm5A7pA39Au5uUNiFQjRYDrz1YvJwV9cdca54vYsBfV1q4c8ncQsv5tNnFYQ1s4rAG7RbyWdAjkC89kE_hIoRRkWZhFyNSfdvRtlUJDlM19uml7lwBWWPnqkmQ3ubiBGmVct3pjrcDvjissOw8Dwkn4E1V1gafec-jDBy4Rndai_RdGjnXjMJs7nRv3Ot",
        "protected": "eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJFczdpUDNFaExDSGxBclAwS2NZRmNxRXlCYXByMks2WU9BOVc4ZU84YXU4IiwieSI6Ik42QWw3RVR3Q2RwQzZOamRlY3IyS1hBZzFVZVp5X3VmSFJRS3A5RzZLR2sifSwiYXB2Ijoiei1McXB2VlhEYl9zR1luM21qUUxwdXUyQ1FMZXdZdVpvVFdPSVhQSDNGTSIsInR5cCI6ImFwcGxpY2F0aW9uL2RpZGNvbW0tZW5jcnlwdGVkK2pzb24iLCJlbmMiOiJYQzIwUCIsImFsZyI6IkVDREgtRVMrQTI1NktXIn0",
        "recipients": [
            {
                "encrypted_key": "G-UFZ1ebuhlWZTrMj214YcEvHl6hyfsFtWv4hj-NPNi9gpi99rRs3Q",
                "header": {"kid": "did:example:bob#key-p256-1"},
            },
            {
                "encrypted_key": "gVdbFdXAxEgrtj9Uw2xiEucQukpiAOA3Jp7Ecmb6L7G5c3IIcAAHgQ",
                "header": {"kid": "did:example:bob#key-p256-2"},
            },
        ],
        "tag": "t8ioLvZhsCp7A93jvdf3wA",
        "iv": "JrIpD5q5ifMq6PT06pYh6QhCQ6LgnGpF",
    }
)

TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_A256CBC = json_dumps(
    {
        "ciphertext": "HPnc9w7jK0T73Spifq_dcVJnONbT9MZ9oorDJFEBJAfmwYRqvs1rKue-udrNLTTH0qjjbeuji01xPRF5JiWyy-gSMX4LHdLhPxHxjjQCTkThY0kapofU85EjLPlI4ytbHiGcrPIezqCun4iDkmb50pwiLvL7XY1Ht6zPUUdhiV6qWoPP4qeY_8pfH74Q5u7K4TQ0uU3KP8CVZQuafrkOBbqbqpJV-lWpWIKxil44f1IT_GeIpkWvmkYxTa1MxpYBgOYa5_AUxYBumcIFP-b6g7GQUbN-1SOoP76EzxZU_louspzQ2HdEH1TzXw2LKclN8GdxD7kB0H6lZbZLT3ScDzSVSbvO1w1fXHXOeOzywuAcismmoEXQGbWZm7wJJJ2r",
        "protected": "eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTM4NCIsIngiOiIxNjFhZ0dlYWhHZW1IZ25qSG1RX0JfU09OeUJWZzhWTGRoVGdWNVc1NFZiYWJ5bGxpc3NuWjZXNzc5SW9VcUtyIiwieSI6ImNDZXFlRmdvYm9fY1ItWTRUc1pCWlg4dTNCa2l5TnMyYi12ZHFPcU9MeUNuVmdPMmpvN25zQV9JQzNhbnQ5T1gifSwiYXB2IjoiTEpBOUVva3M1dGFtVUZWQmFsTXdCaEo2RGtEY0o4SEs0U2xYWldxRHFubyIsInR5cCI6ImFwcGxpY2F0aW9uL2RpZGNvbW0tZW5jcnlwdGVkK2pzb24iLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiRUNESC1FUytBMjU2S1cifQ",
        "recipients": [
            {
                "encrypted_key": "SlyWCiOaHMMH9CqSs2CHpRd2XwbueZ1-MfYgKVepXWpgmTgtsgNOAaYwV5pxK3D67HV51F-vLBFlAHke7RYp_GeGDFYhAf5s",
                "header": {"kid": "did:example:bob#key-p384-1"},
            },
            {
                "encrypted_key": "5e7ChtaRgIlV4yS4NSD7kEo0iJfFmL_BFgRh3clDKBG_QoPd1eOtFlTxFJh-spE0khoaw8vEEYTcQIg4ReeFT3uQ8aayz1oY",
                "header": {"kid": "did:example:bob#key-p384-2"},
            },
        ],
        "tag": "bkodXkuuwRbqksnQNsCM2YLy9f0v0xNgnhSUAoFGtmE",
        "iv": "aE1XaH767m7LY0JTN7RsAA",
    }
)

TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_A256GCM = json_dumps(
    {
        "ciphertext": "mxnFl4s8FRsIJIBVcRLv4gj4ru5R0H3BdvyBWwXV3ILhtl_moqzx9COINGomP4ueuApuY5xdMDvRHm2mLo6N-763wjNSjAibNrqVZC-EG24jjYk7RPZ26fEW4z87LHuLTicYCD4yHqilRbRgbOCT0Db5221Kec0HDZTXLzBqVwC2UMyDF4QT6Uz3fE4f_6BXTwjD-sEgM67wWTiWbDJ3Q6WyaOL3W4ukYANDuAR05-SXVehnd3WR0FOg1hVcNRao5ekyWZw4Z2ekEB1JRof3Lh6uq46K0KXpe9Pc64UzAxEID93SoJ0EaV_Sei8CXw2aJFmZUuCf8YISWKUz6QZxRvFKUfYeflldUm9U2tY96RicWgUhuXgv",
        "protected": "eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTUyMSIsIngiOiJBRWtrc09abW1oZkZYdU90MHMybVdFYlVybVQ3OXc1SFRwUm9TLTZZNXpkYlk5T0I5b2RHb2hDYm1PeGpqY2VhWUU5ZnNaX3RaNmdpTGFBNUFEUnBrWE5VIiwieSI6IkFDaWJnLXZEMmFHVEpHbzlmRUl6Q1dXT2hSVUlObFg3Q1hGSTJqeDlKVDZmTzJfMGZ3SzM2WTctNHNUZTRpRVVSaHlnU1hQOW9TVFczTkdZTXVDMWlPQ3AifSwiYXB2IjoiR09lbzc2eW02TkNnOVdXTUVZZlcwZVZEVDU2Njh6RWhsMnVBSVctRS1IRSIsInR5cCI6ImFwcGxpY2F0aW9uL2RpZGNvbW0tZW5jcnlwdGVkK2pzb24iLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiRUNESC1FUytBMjU2S1cifQ",
        "recipients": [
            {
                "encrypted_key": "W4KOy5W88iPPsDEdhkJN2krZ2QAeDxOIxW-4B21H9q89SHWexocCrw",
                "header": {"kid": "did:example:bob#key-p521-1"},
            },
            {
                "encrypted_key": "uxKPkF6-sIiEkdeJcUPJY4lvsRg_bvtLPIn7eIycxLJML2KM6-Llag",
                "header": {"kid": "did:example:bob#key-p521-2"},
            },
        ],
        "tag": "aPZeYfwht2Nx9mfURv3j3g",
        "iv": "lGKCvg2xrvi8Qa_D",
    }
)

TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON = [
    TTestVector(
        TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_XC20P_1,
        Metadata(
            encrypted=True,
            anonymous_sender=True,
            authenticated=False,
            non_repudiation=False,
            encrypted_to=[
                "did:example:bob#key-x25519-1",
                "did:example:bob#key-x25519-2",
                "did:example:bob#key-x25519-3",
                "did:example:bob#key-x25519-4",
            ],
            enc_alg_anon=AnonCryptAlg.XC20P_ECDH_ES_A256KW,
        ),
    ),
    TTestVector(
        TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_XC20P_2,
        Metadata(
            encrypted=True,
            anonymous_sender=True,
            authenticated=False,
            non_repudiation=False,
            encrypted_to=["did:example:bob#key-p256-1", "did:example:bob#key-p256-2"],
            enc_alg_anon=AnonCryptAlg.XC20P_ECDH_ES_A256KW,
        ),
    ),
    TTestVector(
        TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_A256CBC,
        Metadata(
            encrypted=True,
            anonymous_sender=True,
            authenticated=False,
            non_repudiation=False,
            encrypted_to=["did:example:bob#key-p384-1", "did:example:bob#key-p384-2"],
            enc_alg_anon=AnonCryptAlg.A256CBC_HS512_ECDH_ES_A256KW,
        ),
    ),
    TTestVector(
        TEST_ENCRYPTED_DIDCOMM_MESSAGE_ANON_A256GCM,
        Metadata(
            encrypted=True,
            anonymous_sender=True,
            authenticated=False,
            non_repudiation=False,
            encrypted_to=["did:example:bob#key-p521-1", "did:example:bob#key-p521-2"],
            enc_alg_anon=AnonCryptAlg.A256GCM_ECDH_ES_A256KW,
        ),
    ),
]
