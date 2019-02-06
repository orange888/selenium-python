# Probando Selenium con python

### Arranco Imagen Selenium Webdriver + Gecko driver Standalone
  
```
$ podman run -d --network host --privileged --name server docker.io/selenium/standalone-firefox
```

###  Entorno de runtime para Python 3.x

_Dockerfile_

```
FROM fedora:29
RUN dnf -y install python3
RUN pip3 install selenium
```
_Construcción_
```
$ podman build -t selenium-python .
```

### Script de pruebas 
El script simplemente cargará una URL, chequeará el contenido del titulo de la página y tomará un screenshot.

_browser-test.py_
```
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

server ="http://127.0.0.1:4444/wd/hub"

driver = webdriver.Remote(command_executor=server,
    desired_capabilities=DesiredCapabilities.FIREFOX)

print("Loading page...")
driver.get("https://fedoramagazine.org/")
print("Loaded")
assert "Fedora" in driver.title
driver.save_screenshot("/tmp/screenshot.png")

driver.quit()
print("Done.")
```

### Ejecución 
```
$ podman run -t --rm --network host \
        -v $(pwd)/browser-test.py:/browser-test.py:z -v $(pwd):/tmp/:z \
        selenium-python python3 browser-test.py
Loading page...
Loaded
Done.
```