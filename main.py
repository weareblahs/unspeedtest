suffixes = ['bps', 'Kbps', 'Mbps', 'Gbps']
def convert(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])
def convert_nosuffix(nbytes):
    i = 0
    while nbytes >= 1024:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return f

# Importing stuffs
from datetime import date
import os
json_out_fn = "json/speedtest_" + str(date.today()) + ".json"
# Pre-writing existing data clearing
open(json_out_fn, 'w').close()

# Start speedtest process
os.system("speedtest -f json-pretty >>" + str(json_out_fn))
# Importing stuffs
import datetime
import os

json_out_fn = "json/speedtest_" + str(datetime.date.today()) + ".json"
with open(json_out_fn, 'r') as file:
    data = file.read().rstrip()
import json
data2 = json.loads(data)

download = convert(data2["download"]["bytes"])
upload = convert(data2["upload"]["bytes"])
dl_chart = convert_nosuffix(data2["download"]["bytes"])
ul_chart = convert_nosuffix(data2["upload"]["bytes"])
ping_lat = str(data2["ping"]["latency"]) + "ms"
sturl = '<a href="' + str(data2["result"]["url"]) + '" class="btn btn-primary btn-sm btn-block">Result on speedtest.net</a>'
testtime0 = datetime.datetime.now()
testtime = testtime0.strftime("%Y-%m-%d %H:%M:%S")
from tabulate import tabulate
table = [[download,upload,ping_lat,sturl,testtime]]
htmltext = tabulate(table, tablefmt='html')
htmltext = tabulate(table, tablefmt='html') + "\n<!--STDATA-->"
# Code from https://wiki.python.org/moin/EscapingHtml#Unescaping_HTML
def format(s):
   s = s.replace('<table>','')
   s = s.replace('<tbody>','')
   s = s.replace('</tbody>','')
   s = s.replace('</table>','')
   s = s.replace("&lt;", "<")
   s = s.replace("&gt;", ">")
   # this has to be last:
   s = s.replace("&amp;", "&")
   s = s.replace("&quot;", '"')
   return s

# Create chart image for today's speedtest
import matplotlib.pyplot as plt
name = ['','Upload','Download']
data = ['0',ul_chart, dl_chart]
colors = ['red', 'green']
plt.bar(name,data,color=colors)
plt.title('Speedtest result on ' + str(datetime.date.today()))
plt.xlabel('')
plt.ylabel('Speed (in Mbps)')
plt.savefig("apache/latestresult.svg")

print(format(htmltext))
f = open("apache/index.html",'r')
filedata = f.read()
f.close()

newdata = filedata.replace("<!--STDATA-->", format(htmltext))

f = open("apache/index.html",'w')
f.write(newdata)
f.close()

print("Done!")