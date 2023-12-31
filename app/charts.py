import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    # Libreria me da dos variables:
    # figura(fig) y coordenadas(ax)
    fig, ax = plt.subplots()
    ax.bar(labels,values)  # ax. usa grafica de barras, toca darle valores/labels
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) # Indicar como son los labels, indicar argumento labels.
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [1001, 1034, 807]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)