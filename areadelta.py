from miller import *

def main():
    delta_dat = np.linspace(-1, 1, 10)
    area_dat = []
    for d in delta_dat:
        r, z = flux_surface(delta=d)
        area_dat.append(area(r, z))

    plt.plot(delta_dat, area_dat)
    plt.xlabel("delta ")
    plt.ylabel("area [m]")
    plt.show()
    return


if __name__ == "__main__":
    main()