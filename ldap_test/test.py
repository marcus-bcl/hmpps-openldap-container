#! /usr/bin/env python3
import time
import os
import random
from ldap3 import Server, Connection, ALL, SUBTREE, LEVEL


ldap_server = os.getenv("LDAP_SERVER")
ldap_user = "cn=root,dc=moj,dc=com"
ldap_password = os.getenv("BIND_PASSWORD")
server = Server(ldap_server, get_info=ALL)

print("Server: " + ldap_server)
print("User: " + ldap_user)
print("ldap server info: " + str(server.info))

user_list = [
    "Emma",
    "Nicky",
    "Brian",
    "Debbie",
    "George",
    "John",
    "Paul",
    "Stuart",
    "Pete",
]

print("connecting")
for i in range(0, 10000000000):
    print("Run #" + str(i))

    conn = Connection(server, ldap_user, ldap_password,
                      auto_bind=True, authentication="SIMPLE")
    conn.search(
        "ou=Users,dc=moj,dc=com",
        "(&(cn=" + random.choice(user_list) + "*)(objectClass=person))",
        search_scope=LEVEL,
        attributes=["*"],
    )
    print(conn.entries)
    conn.unbind()
