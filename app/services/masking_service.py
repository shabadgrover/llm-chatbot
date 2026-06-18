import re

def mask_phone(text: str) -> str:
    pattern = r"\b\d{10}\b"

    return re.sub(pattern, "[PHONE]", text)


def mask_email(text: str) -> str:
    pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z.]+"

    return re.sub(pattern, "[EMAIL]", text)


def mask_pan(text: str) -> str:
    pattern = r"\b[a-zA-Z]{5}\d{4}[a-zA-Z]\b"
    
    return re.sub(pattern, "[PAN]", text)

def mask_aadhaar(text: str) -> str:
    pattern = r"\b\d{4}\s\d{4}\s\d{4}\b|\b\d{12}\b"

    return re.sub(pattern, "[AADHAAR]", text)

def mask_pii(text: str) -> str:
    text = mask_phone(text)
    text = mask_email(text)
    text = mask_pan(text)
    text = mask_aadhaar(text)

    return text