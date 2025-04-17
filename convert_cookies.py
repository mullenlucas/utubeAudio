import json

def convert_json_to_netscape(json_cookie_file, netscape_cookie_file):
    with open(json_cookie_file, 'r') as f:
        cookies = json.load(f)

    with open(netscape_cookie_file, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        for cookie in cookies:
            domain = cookie.get("domain")
            # Ensure domain starts with a dot for Netscape format, if needed.
            if not domain.startswith('.'):
                domain = '.' + domain
            # The flag indicates if all machines in the domain can access the cookie.
            flag = "FALSE" if cookie.get("hostOnly") else "TRUE"
            path = cookie.get("path", "/")
            secure = "TRUE" if cookie.get("secure") else "FALSE"
            expiration = str(int(cookie.get("expirationDate", 0)))
            name = cookie.get("name", "")
            value = cookie.get("value", "")
            line = "\t".join([domain, flag, path, secure, expiration, name, value])
            f.write(line + "\n")

# Usage:
# Assuming your JSON cookies file is named "cookies.json"
convert_json_to_netscape('cookies.json', 'cookies.txt')
