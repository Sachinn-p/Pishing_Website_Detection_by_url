import whois
import datetime
def who_info(value):
    lst = ['domain_name', 'registrar', 'whois_server', 'referral_url', 'updated_date', 'creation_date', 'expiration_date', 'dnssec', 'name', 'org', 'address', 'city', 'state', 'registrant_postal_code', 'country']
    res = whois.whois(value)
    #for key, val in zip(res.keys(), res.values()):
    #    print(f"Keys: {key} \t\t\tand Values: {val}")
    res = {key:res[key] for key in res if key in lst}
    return res
res = whois.whois("https://www.google.com/")
    #for key, val in zip(res.keys(), res.values()):
    #    print(f"Keys: {key} \t\t\tand Values: {val}")
print(res)