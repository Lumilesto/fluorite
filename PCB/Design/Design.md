### external ADC to monitor voltage of each LED

- ADS7830 x4 - 1 I2C - 32 channels + 4channel (?)

### 3 buck controlled by 3 DACs of 2 MCUs

### V-I Converter

![](/home/lingusilur/9C33-6BBD/develop/projects/HexagramLab/PenguinsLand/fluorite/PCB/Design/V-I-transactor.svg)
$$
V_{var} \geq 3.4V \newline
I: [3, 83]mA, \space 60mA \space typ.\newline
V_{control}: [3.3, 0]V
$$
**TODO:** add capacitors to improve stability