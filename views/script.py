import jsmin
with open("minify.js", "r") as file:
    js = file.read()
minified_js = jsmin.jsmin(js)
with open("minify.js", "w") as file:
    file.write(minified_js) 
