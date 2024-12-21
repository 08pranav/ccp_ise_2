import numpy as np
import matplotlib.pyplot as plt

class WavePlot:
    def __init__(self):
        self.x = np.linspace(0, 2 * np.pi, 100)

    def plot_sine(self):
        plt.plot(self.x, np.sin(self.x), label='Sine', color='blue')
        plt.title('Sine Wave')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    def plot_cosine(self):
        plt.plot(self.x, np.cos(self.x), label='Cosine', color='red')
        plt.title('Cosine Wave')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    def plot_both(self):
        plt.plot(self.x, np.sin(self.x), label='Sine', color='blue')
        plt.plot(self.x, np.cos(self.x), label='Cosine', color='red')
        plt.title('Sine and Cosine Waves')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

# Example usage
wave_plot = WavePlot()
wave_plot.plot_both()
