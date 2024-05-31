import matplotlib.pyplot as plot
import numpy as np
import LED

wave_lenth=np.arange(380, 830, 1e-1)
strength=np.array(list(map(LED._4000k, wave_lenth)))

plot.plot(wave_lenth, strength)
plot.show()
