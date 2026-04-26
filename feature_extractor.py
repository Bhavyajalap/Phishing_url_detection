import re

def extract_features(url):
    features = []

    # URL length
    features.append(len(url))

    # Contains IP
    features.append(1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0)

    # @ symbol
    features.append(1 if "@" in url else 0)

    # Hyphen
    features.append(1 if "-" in url else 0)

    # HTTPS
    features.append(1 if "https" in url else 0)

    # Number of dots
    features.append(url.count("."))

    # Double slash redirection
    features.append(1 if "//" in url[8:] else 0)

    return features
