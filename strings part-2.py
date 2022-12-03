s = "5python programming"
print(s.find("g"))
print(s.find("o"))
print(s.find("r"))
print(s.find("x"))

a = "my name is sowmya"
print(a.count("a"))
print(a.count("m"))
print(a.count("n"))
print(a.count("i"))
print(a.count("t"))

p = "booking counter"
print(p.replace("counter", "section"))

g = "python programming course"
print(g.replace("course", 9))
print(g.replace("course", str(9)))
print(g.replace("p", "h", 3))
print(g.replace("m", "9", 2))
print(g.replace("course", "language"))

s = "    hello world .    "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
