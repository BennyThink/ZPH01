# ZPH01

Python extension for ZPH01 sensor

# Usage

```python

from zph01 import ZPH01
zph = ZPH01()
zph.output()
{'VOC status': 'Good', 'PM 2.5 percent': 2.03, 'PM 2.5 count': 1218.0, 'PM 2.5 level': 40.6, 'PM 2.5 status': 'Poor'}
```
You can configure serial port by adding parameter `ZPH01("/dev/serial3")`.


# License
Apache License 2.0