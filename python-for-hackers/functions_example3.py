# I like to name my parameters with an underscore,
# to distinguish them from variables
def attack(_ip, _domain):
    print(f"target ip is {_ip} and {_domain}")

ip = "10.10.10.10"
domain = "domain.com"
attack(ip, domain)

