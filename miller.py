import numpy as np
from numpy import cos, sin, linspace, pi, arcsin
import matplotlib.pyplot as plt

def flux_surface(A=2.2, R0=2.5, kappa=1.5, delta=0.3):
    """Calculate the flux surface. Returns R_s, Z_s, 1D arrays
    Arguments
    A - float
    R0 - float
    kappa - float
    delta - float
    ---------
    """
    theta=linspace(0,2*pi)
    r=R0/A
    R_s=R0+r*cos(theta+(arcsin(delta)*sin(theta)))
    Z_s=kappa*r*sin(theta)
    return R_s, Z_s

def plot_surface(radius, height, savefig=True):
    """Plot the flux surface.
    Arguments
    radius - 1D array
    height - 1D array
    savefig - boolean
    ---------
    """
    plt.plot(radius, height)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    if savefig:
        plt.savefig("./miller.png")
    return

def area(r, z):
    # abs because (r, z) start on the out-board midplace and r decreases
    return np.abs(np.trapezoid(z, r))

def main():
    """Main function to plot the flux surface
    """
    R_s, Z_s = flux_surface()
    plot_surface(R_s, Z_s)
    return 


if __name__ == "__main__":
    main()