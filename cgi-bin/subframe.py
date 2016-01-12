#!/usr/bin/env python

tmpl = '''<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=Edge"/>
<meta http-equiv="-X-Content-Security-Policy" content="frame-ancestors 'self'"/>
<meta http-equiv="-X-Webkit-CSP" content="frame-ancestors 'self'"/>
<meta http-equiv="-Content-Security-Policy" content="frame-ancestors 'self'"/>
<meta http-equiv="-X-Frame-Options" content="SAMEORIGIN"/>
</head>

<body>
<h1>Content from subframe</h1>
</body>
</html>
'''

output = tmpl.format()
#print('Content-length: {}'.format(len(output)))    # broken in IE11?
print("X-UA-Comptabile: IE=Edge")
print("-X-Webkit-CSP: frame-ancestors 'self'")
print("-X-Content-Security-Policy: frame-ancestors 'self'")
print("-Content-Security-Policy: frame-ancestors 'self'")
print("-X-Frame-Options: SAMEORIGIN")
print('Content-type: text/html\n')
print(output, end='')
