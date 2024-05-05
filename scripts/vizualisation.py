# from Matrix import Matrix
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import progressbar


def vizualisation(list_of_colonies, resource_matrix, rounds_number, file_name):
    global scats

    bar = progressbar.ProgressBar(maxval=rounds_number,
                                  widgets=[progressbar.Bar('=', '[', ']'),
                                           ' ', progressbar.Percentage()])

    fig, ax = plt.subplots()
    im = ax.imshow(resource_matrix.matrix, alpha=1, 
                   cmap='binary')
    
    ax.axis('off')
    scats = []
 
    bar.start()

    def animate(frame):
        global scats
        bar.update(frame)
        

        for scat in scats:
            scat.remove()
        scats = []

        resource_matrix.resupply()

        for colony in list_of_colonies:

            if colony.cells_number:
                coords_cells = list(zip(*colony.list_of_cells_coordinates))
                scats.append(
                    ax.scatter(coords_cells[1], coords_cells[0],
                               color=colony.color,
                               s=7, marker='o', alpha = 0.9))

                ax.imshow(resource_matrix.matrix, alpha=1,
                        #   norm=norm,
                          cmap='binary', )
            else:
                return

            colony.eat(resource_matrix)

    anim = FuncAnimation(fig, animate,
                         frames=rounds_number,
                         repeat=False, blit=False)
    
    # writer = FFMpegWriter(fps=1,
    #         codec="h264",
    #         extra_args=["-preset", "veryslow","-crf","0"])

    # anim.save(__file__+".mp4", writer=writer)
    anim.save(file_name, writer='pillow')
    # plt.show()
    # plt.close()