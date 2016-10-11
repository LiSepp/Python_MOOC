#month.py
#字符串使输入1-12输出月份
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("请输入月份数（1-12）：")
pos = (int(n) - 1) * 3
monthAbbrev=months[pos:pos+3]
print("月份简写是"+monthAbbrev+".")
