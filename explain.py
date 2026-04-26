def generate_explanation(url):
    reasons = []

    if "@" in url:
        reasons.append("Contains '@' which can mask malicious links")

    if len(url) > 75:
        reasons.append("URL is unusually long")

    if "http://" in url:
        reasons.append("Uses insecure HTTP")

    if "-" in url:
        reasons.append("Contains '-' often used in fake domains")

    if "//" in url[8:]:
        reasons.append("Contains redirection pattern (//)")

    if url.count(".") > 5:
        reasons.append("Too many subdomains")

    if not reasons:
        reasons.append("No strong phishing indicators detected")

    return reasons
