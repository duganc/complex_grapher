import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def generate_sine_cosine_definition_plot():

    figure, axes = plot_point_on_unit_circle_with_radius_and_arc()

    x = math.cos(math.radians(60))
    y = math.sin(math.radians(60))

    line_to_x = patches.Polygon([(x, y), (x, 0)], fill=False, color="g", linestyle='dashed')
    line_to_y = patches.Polygon([(x, y), (0, y)], fill=False, color="g", linestyle='dashed')

    axes.add_patch(line_to_x)
    axes.add_patch(line_to_y)

    axes.annotate(r"$(\cos{\theta}, \sin{\theta})$", xy=(x * 1.05, y * 1.05))
    axes.annotate(r"$\sin{\theta}$", xy=(1.1 * x, 0.45 * y))
    axes.annotate(r"$\cos{\theta}$", xy=(0.27 * x, 1.025 * y))

    plt.savefig("sine_cosine_definition.png")



def generate_sine_cosine_by_triangle_plot():

    figure, axes = plot_point_on_unit_circle_with_radius_and_arc()

    x = math.cos(math.radians(60))
    y = math.sin(math.radians(60))

    triangle = patches.Polygon([(0, 0), (x, 0), (x, y)], fill=False, color="r")
    axes.add_patch(triangle)

    axes.annotate(r"$(\cos{\theta}, \sin{\theta})$", xy=(x * 1.05, y * 1.05))
    axes.annotate(r"$\sin{\theta}$", xy=(1.1 * x, 0.45 * y))
    axes.annotate(r"$\cos{\theta}$", xy=(0.4 * x, -0.1 * y))

    plt.savefig("sine_cosine_by_triangle.png")

def plot_point_on_unit_circle_with_radius_and_arc():

    figure, axes = plt.subplots()

    AXIS_LENGTH = 1.25

    plt.axis([-AXIS_LENGTH, AXIS_LENGTH, -AXIS_LENGTH, AXIS_LENGTH])

    axes.axhline(y=0, color='k')
    axes.axvline(x=0, color='k')

    x = math.cos(math.radians(60))
    y = math.sin(math.radians(60))

    axes.plot(0.99 * x, 0.99 * y, 'o')

    axes.set_aspect(1./axes.get_data_ratio())

    circle = patches.Circle((0, 0), 1, fill=False, color='g')
    axes.add_patch(circle)

    radius = patches.Polygon([(0, 0), (x, y)], fill=False, color="g")
    axes.add_patch(radius)

    arc = patches.Arc((0, 0), 0.25, 0.25, 0, 0, math.degrees(math.radians(60)))
    axes.add_patch(arc)

    axes.annotate(r"$\theta$", xy=(0.25 * x, 0.25 * y / 3), color="k")
    axes.annotate(r"$1$", xy=(x * 0.45, y * 0.55))

    return figure, axes