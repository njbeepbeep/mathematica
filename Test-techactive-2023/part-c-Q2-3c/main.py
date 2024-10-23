import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f1(x):
    return -np.sqrt(3) * np.tan(x / 2) + 1

def f2(x, a):
    return a * np.tan(a * x) + 2

x = np.linspace(0, np.pi, 1000)

a_init = -0.5

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
l1, = ax.plot(x, f1(x), label=r'$-\sqrt{3} \tan\left(\frac{x}{2}\right) + 1$', color='blue')
l2, = ax.plot(x, f2(x, a_init), label=r'$a \tan(ax) + 2$', color='red')
plt.ylim(-10, 10)
plt.xlim(0, np.pi)
plt.legend()
plt.grid(True)

ax_a = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
a_slider = Slider(ax_a, 'a', -1.0, 1.0, valinit=a_init)

# shaded = ax.fill_between(x, f1(x), f2(x, a_init), where=np.abs(f1(x) - f2(x, a_init)) > 1e-6,
                         #color='green', alpha=0.3, label='Regions where f1 != f2')


def update(val):
    a = a_slider.val
    l2.set_ydata(f2(x, a))

    # Update shaded area
    global shaded
    for coll in shaded.collections:
        coll.remove()
    shaded = ax.fill_between(x, f1(x), f2(x, a), where=np.abs(f1(x) - f2(x, a)) > 1e-6,
                             color='green', alpha=0.3)

    fig.canvas.draw_idle()


a_slider.on_changed(update)

plt.show()