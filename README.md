Test Files for Clickjacking
===========================


Run a Python web server in the current directory with the following command line and access `/framing.html` with a web browser.

    python -m http.server --cgi

The file `framing.html` includes an `iframe` element that points to `/cgi-bin/subframe.py`. Comment various lines in this script to test the Content-Security-Policy headers in your browsers. Make sure your force a refresh with Ctrl+F5 or Ctrl-R to reload the full page before each test.

The file `subframe.html` is a static page that can only be used to test the `<meta>` if there are issues with running the CGI script.
