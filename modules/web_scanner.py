import requests
import ssl
import socket
from urllib.parse import urlparse


def ssl_scan(url):

    try:

        hostname = urlparse(url).hostname

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as ssock:

                cert = ssock.getpeercert()

                return {
                    "version": ssock.version(),
                    "expires": cert.get("notAfter"),
                    "issuer": cert.get("issuer")
                }

    except Exception as e:

        return {
            "error": str(e)
        }


def analyze_methods(url):

    methods = []

    try:

        response = requests.options(
            url,
            timeout=5
        )

        allow = response.headers.get("Allow")

        if allow:

            methods = [
                method.strip()
                for method in allow.split(",")
            ]

    except:

        pass

    return methods


def scan_website(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        headers = response.headers

        security_headers = {
            "Strict-Transport-Security":
                "Present" if "Strict-Transport-Security" in headers else "Missing",

            "Content-Security-Policy":
                "Present" if "Content-Security-Policy" in headers else "Missing",

            "X-Frame-Options":
                "Present" if "X-Frame-Options" in headers else "Missing",

            "X-Content-Type-Options":
                "Present" if "X-Content-Type-Options" in headers else "Missing",

            "Referrer-Policy":
                "Present" if "Referrer-Policy" in headers else "Missing",

            "Permissions-Policy":
                "Present" if "Permissions-Policy" in headers else "Missing"
        }

        technologies = []

        if "Server" in headers:
            technologies.append(headers["Server"])

        if "X-Powered-By" in headers:
            technologies.append(headers["X-Powered-By"])

        score = 100

        for status in security_headers.values():

            if status == "Missing":
                score -= 10

        if score < 0:
            score = 0

        ssl_info = ssl_scan(url)

        methods = analyze_methods(url)

        return {
            "headers": security_headers,
            "technologies": technologies,
            "score": score,
            "ssl": ssl_info,
            "methods": methods
        }

    except Exception as e:

        return {
            "error": str(e)
        }