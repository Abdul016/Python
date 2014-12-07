import psutil, datetime


html = open("output.html", "w")

boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

cpu_util = psutil.cpu_percent(interval = 1, percpu=True)

cpuTimes = []
for cpu in cpu_util:
    cpuTimes.append(cpu)

mem = psutil.virtual_memory()
THRESHOLD = 100*1024*1024 #100mb

memavail = str(mem.available)
memused = str(mem.used)
mempercent = str(mem.percent)

str1 = "<td colspan='2' bgcolor = 'LightBlue' >"+boot_time+"</td>"
str2 = "<td bgcolor = 'Plum'>"+str(cpuTimes[0])+"%</td>"
str3 = "<td bgcolor = 'Plum'>"+str(cpuTimes[1])+"%</td>"
str4 = "<td bgcolor = 'Plum'>"+str(cpuTimes[2])+"%</td>"
str5 = "<td bgcolor = 'Plum'>"+str(cpuTimes[3])+"%</td>"
str6 = "<td bgcolor = 'LightBlue' colspan='2'>"+str(memavail)+"</td>"
str7 = "<td colspan='2'>"+str(memused)+"</td>"
str8 = "<td bgcolor = 'LightBlue' colspan='2'>"+str(mempercent)+"</td>"
htmlString = """<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0 Transitional//EN'>
 <HTML>
 <HEAD>
 </HEAD>

 <BODY>
	<table>
	<tr>
		<td width='60%' bgcolor = 'LightBlue'>BOOT TIME</td>"""
htmlString += str1

htmlString += """
	</tr>
	<tr>
		<td rowspan='4'>CPU UTILIZATION</td>
		<td>CPU 1</td>"""
htmlString += str2
htmlString += """
	</tr>
	<tr>
		<td>CPU 2</td>"""
htmlString += str3
htmlString += """
	</tr>
	<tr>
		<td>CPU 3</td>"""
htmlString += str4
htmlString += """
	</tr>
	<tr>
		<td>CPU 4</td>"""
htmlString += str5
htmlString += """
	</tr>
	<tr>
		<td bgcolor = 'LightBlue'>AVAILBLE MEMORY</td>"""
htmlString += str6
htmlString += """
	</tr>
	<tr>
		<td>USED MEMORY</td>"""
htmlString += str7
htmlString += """
	</tr>
	<tr>
		<td bgcolor = 'LightBlue'>USED PERCENTAGE</th>"""
htmlString += str8
htmlString += """
	</tr>
	</table>
 </BODY>
</HTML>
"""
html.write(htmlString)

html.close()
