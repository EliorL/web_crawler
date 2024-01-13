from urllib.parse import urlparse


def get_domain_name(url):
    """Get main domain name (example.com)."""
    try:
        results = get_sub_domain_name(url).split('.')
        return str(results[-2]) + '.' + str(results[-1])
    except Exception as e:
        print(f'Error getting domain name. ({e})')
        return ''


def get_sub_domain_name(url):
    """Get sub domain name (name.example.com)."""
    try:
        # Return network location.
        return urlparse(url).netloc
    except Exception as e:
        print(f'Error getting sub domain name. ({e})')
        return ''
