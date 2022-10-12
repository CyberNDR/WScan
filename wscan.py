import whois
import urllib.request
import pyfiglet
import time

logs = open("WScan_logs.txt", "w")

def subdomain_scan():
	print("Running subdomain scan")
	print("Which protocol does the target use?")
	print("[1] http://")
	print("[2] https://")
	protocol = input("Target Protocol: ")
	if protocol == "1":
		webprotocol = "http://"
		print("http:// protocol set.")
	elif protocol == "2":
		webprotocol = "https://"
		print("https:// protocol set.")
	else:
		print("Error, only two available options: 1, 2.")
		return subdomain_scan()
	target = input("Input the website hostname (es: 'example.com'): ")
	print("Running scan")
	with open("subdomain_names1.txt", "r") as subdomainsopen:
		subdomainsread = subdomainsopen.read()
		subdomains = subdomainsread.splitlines()
	query = ""
	exist = ""
	i = 0
	while i < len(subdomains):
		try:
			query = f"{webprotocol}{subdomains[i]}.{target}"
			urllib.request.urlopen(query)
			exist.append(query)
			print("----------------------------------------------------")
			print(f"[TRUE] Subdomain Found: {query}")
			print("----------------------------------------------------")
		except Exception as e:
			print(f"[FALSE] Subdomain not existing: {query}")
		i += 1
	print("\n")
	print("----------------:")
	print("Subdomains Found:")
	print("-----------------")
	print("\n")
	logs.write("-----------------")
	logs.write("\n")
	logs.write("Subdomains Found:")
	logs.write("\n")
	logs.write("-----------------")
	logs.write("\n")
	if exist == "":
		print("No subdomain found.")
		logs.write("No subdomain found.")
	else:
		j = 0
		while j < len(exist):
			print(exist[j]+"\n")
			logs.write(exist[j]+"\n")
			j += 1
	logs.write("\n")
	logs.write("\n")

def domains_scan():
	with open("top-level-domains.txt", "r") as domainsopen:
		domainsread = domainsopen.read()
		domains = domainsread.splitlines()
	target = input("Input the target website hostname (es: 'https://example'): ")
	print("Running scan")
	query = ""
	exist = ""
	i = 0
	while i < len(domains):
		try:
			query = f"{target}.{domains[i].lower()}"
			urllib.request.urlopen(query)
			exist.append(query)
			print("-----------------------------------------------")
			print(f"[TRUE] Domain Found: {query}")
			print("-----------------------------------------------")
		except Exception as e:
			print(f"[FALSE] Domaing not existing: {query}")
		i += 1
	print("\n")
	print("--------------")
	print("Domains Found:")
	print("--------------")
	logs.write("--------------")
	logs.write("\n")
	logs.write("Domains Found:")
	logs.write("\n")
	logs.write("--------------")
	logs.write("\n")
	j = 0
	while j < len(exist):
		print(exist[j]+"\n")
		logs.write(exist[j]+"\n")
		j += 1
	logs.write("\n")
	logs.write("\n")

def registardata():
	maininput = input("Input the website hostname: ")
	target = whois.whois(maininput)

	print(f"Domain Name: {target.domain_name}")
	print(f"Creation Date: {target.creation_date}")
	print(f"Updated Date: {target.updated_date}")
	print(f"Expiration Date: {target.expiration_date}")
	print(f"Status: {target.status}")
	print(f"Name Servers: {target.name_servers}")
	print(f"Registrant Organization: {target.registrant_organization}")
	print(f"Registrant Address: {target.registrant_address}")
	print(f"Admin Address: {target.admin_address}")
	print(f"Admin Organization: {target.admin_organization}")
	print(f"Admin Name: {target.admin_name}")
	print(f"Tech Address: {target.tech_address}")
	print(f"Tech Organization: {target.tech_organization}")
	print(f"Tech Name: {target.tech_name}")
	print(f"Registrar Address: {target.registrar_address}")
	print(f"Registrar: {target.registrar}")
	print(f"Registrar Name: {target.registrar_name}")

	logs.write("-------------")
	logs.write("\n")
	logs.write("Registar Data")
	logs.write("\n")
	logs.write("-------------")
	logs.write("\n")
	logs.write("\n")
	logs.write(f"Domain Name: {target.domain_name}")
	logs.write("\n")
	logs.write(f"Creation Date: {target.creation_date}")
	logs.write("\n")
	logs.write(f"Updated Date: {target.updated_date}")
	logs.write("\n")
	logs.write(f"Expiration Date: {target.expiration_date}")
	logs.write("\n")
	logs.write(f"Status: {target.status}")
	logs.write("\n")
	logs.write(f"Name Servers: {target.name_servers}")
	logs.write("\n")
	logs.write(f"Registrant Organization: {target.registrant_organization}")
	logs.write("\n")
	logs.write(f"Registrant Address: {target.registrant_address}")
	logs.write("\n")
	logs.write(f"Admin Address: {target.admin_address}")
	logs.write("\n")
	logs.write(f"Admin Organization: {target.admin_organization}")
	logs.write("\n")
	logs.write(f"Admin Name: {target.admin_name}")
	logs.write("\n")
	logs.write(f"Tech Address: {target.tech_address}")
	logs.write("\n")
	logs.write(f"Tech Organization: {target.tech_organization}")
	logs.write("\n")
	logs.write(f"Tech Name: {target.tech_name}")
	logs.write("\n")
	logs.write(f"Registrar Address: {target.registrar_address}")
	logs.write("\n")
	logs.write(f"Registrar: {target.registrar}")
	logs.write("\n")
	logs.write(f"Registrar Name: {target.registrar_name}")

Logo = pyfiglet.figlet_format("WScan")
print("\n")
print("\n")
print(Logo)
print("\n")
print("Powered by CyberNDR")
print("\n")
print("Contacts")
print("GitHub: github.com/CyberNDR")
print("Telegram: t.me/NDR4NGHETA")
print("\n")
time.sleep(3)
def main():
	print("Choose an option")
	print("\n")
	print("[1] WHOIS Website")
	print("[2] Subdomains Scan")
	print("[3] Scan All Website's Domains")
	print("[4] All Operations Listed Above")
	print("\n")
	print("[99] Exit")
	operation = input("--->")

	if operation == "1":
		registardata()
		print("\n\n")
		main()
	elif operation == "2":
		subdomain_scan()
		print("\n\n")
		main()
	elif operation == "3":
		domains_scan()
		print("\n\n")
		main()
	elif operation == "4":
		registardata()
		print("\n\n")
		subdomain_scan()
		print("\n\n")
		domain_scan()
		print("\n\n")
		main()
	elif operation == "99":
		print("\n\n")
		print(Logo)
		print("\n\n")
		exit()
	else:
		print("Error, available options: 1, 2, 3, 4, 99.")
		return main()
	print(Logo)

main()

logs.close()
