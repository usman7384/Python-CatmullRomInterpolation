import numpy
import matplotlib.pyplot as plt


def pyramidalFormulation(P0, P1, P2, P3, nPoints=50):
    # Convert the points to numpy so that we can do array multiplication
    P0, P1, P2, P3 = map(numpy.array, [P0, P1, P2, P3])

    # Parametric constant: 0.5 for the centripetal spline.
    alpha = 0.5

    def knotParameters(ti, Pi, Pj):
        xi, yi = Pi
        xj, yj = Pj
        return ((xj - xi) ** 2 + (yj - yi) ** 2) ** (alpha / 2) + ti

    # calculate t0 to t4
    t0 = 0
    t1 = knotParameters(t0, P0, P1)
    t2 = knotParameters(t1, P1, P2)
    t3 = knotParameters(t2, P2, P3)

    # Only calculate points between P1 and P2
    # numpy.linespace returns num evenly spaced samples, calculated over the interval [start, stop].
    t = numpy.linspace(t1, t2, nPoints)
    # Reshape so that we can multiply by the points P0 to P3
    # and get a point for each value of t.
    t = t.reshape(len(t), 1)
    print(t)
    A1 = (t1 - t) / (t1 - t0) * P0 + (t - t0) / (t1 - t0) * P1
    A2 = (t2 - t) / (t2 - t1) * P1 + (t - t1) / (t2 - t1) * P2
    A3 = (t3 - t) / (t3 - t2) * P2 + (t - t2) / (t3 - t2) * P3
    B1 = (t2 - t) / (t2 - t0) * A1 + (t - t0) / (t2 - t0) * A2
    B2 = (t3 - t) / (t3 - t1) * A2 + (t - t1) / (t3 - t1) * A3
    C = (t2 - t) / (t2 - t1) * B1 + (t - t1) / (t2 - t1) * B2
    return C


def CatmullRomChain(P):
    # length of list or number of items
    length = len(P)
    # The curve contains an array of (x, y) points.
    Curve = []
    for i in range(length - 3):
        c = pyramidalFormulation(P[i], P[i + 1], P[i + 2], P[i + 3])
        Curve.extend(c)
    return Curve


# Define a set of points for curve to go through
Points = [1, 2], [2, 2], [3, 7], [4, 5]
# Calculate the Catmull-Rom splines through the points
c = CatmullRomChain(Points)

x, y = zip(*c)
plt.plot(x, y)
# Plot the control points
px, py = zip(*Points)
plt.plot(px, py, 'or')

plt.show()
