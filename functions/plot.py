import matplotlib.pyplot as plt

def plot(lim,x_label,y_label,legend,title,font_size,color,linewidth,x,y):
    fig = plt.figure(figsize=(2, 2), dpi=300)
    fig, ax = plt.subplots()
    plt.suptitle("Plot")

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    ax.set_xlim(lim[0])
    ax.set_ylim(lim[1])

    ax.grid(which="major", color="k", linestyle="--", alpha=0.2)
    ax.grid(which="minor", color="k", linestyle="--", alpha=0.1)
    ax.minorticks_on()

    ax.plot(x,y,color,linewidth, label=legend)
    ax.legend(loc='upper right', fontsize=font_size)

    ax.set_title(title)


    plt.tight_layout()
    fig.show()

    input("Press enter to continue...") 

