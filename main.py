import subprocess
import re

# IPアドレスのリスト
ip_list = ["204.13.154.3", "192.210.207.88", "192.3.253.2", "198.23.228.15", "192.3.165.30", "107.173.164.160", "198.23.249.100", "192.3.81.8", "107.173.166.10", "23.94.101.88",]

# pingテストの結果を格納する辞書
ping_result = {}

# pingテストを実行
for ip in ip_list:
    ping = subprocess.Popen(["ping", "-n", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = ping.communicate()
    out = out.decode("shift-jis")
    match = re.search(" = (\d+)ms", out)
    if match:
        ms = int(match.group(1))
        ping_result[ip] = ms
    else:
        ping_result[ip] = float("inf")

# ms値が小さい順に表示
for ip, ms in sorted(ping_result.items(), key=lambda x: x[1]):
    print(ip + " : " + str(ms) + "ms")
