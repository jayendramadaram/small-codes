proxyList = []
with open("ngl.txt", "r") as f:
    for i in f.readlines():
        proxy = i.strip()

        try:
            resp = requests.get("https://httpbin.org/ip",
                                proxies={"https": proxy, "http": proxy}, timeout=4)
            proxyList.append(proxy)
        except Exception as e:
            print("e")

print(proxyList)
