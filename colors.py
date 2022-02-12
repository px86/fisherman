'''Define terminal escape sequences for color codes.

<ESC>[{attr1};...;{attrn}m

0	Reset all attributes
1	Bright
2	Dim
4	Underscore
5	Blink
7	Reverse
8	Hidden

Foreground Colours
------------------
30	Black
31	Red
32	Green
33	Yellow
34	Blue
35	Magenta
36	Cyan
37	White

Background Colours
------------------
40	Black
41	Red
42	Green
43	Yellow
44	Blue
45	Magenta
46	Cyan
47	White
'''

rt = '\x1b[0m'

bk = '\x1b[30m'
rd = '\x1b[31m'
gr = '\x1b[32m'
yl = '\x1b[33m'
mg = '\x1b[34m'
cy = '\x1b[36m'
wh = '\x1b[37m'
