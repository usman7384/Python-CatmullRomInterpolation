# Catmull-Rom Spline Generation

#### Overview
This project demonstrates the implementation of the **Catmull-Rom spline** curve generation, using the **Pyramidal Formulation** method to interpolate a series of control points. The Catmull-Rom spline is a smooth, parametric curve that passes through a set of given points, which is commonly used in computer graphics, animation, and pathfinding. This implementation uses the centripetal Catmull-Rom spline formulation for smooth interpolation, and visualizes the resulting curve using `matplotlib`.

#### Features:
- **Pyramidal Formulation** for calculating the spline.
- **Centripetal Spline Parameterization** to ensure smooth curve transitions.
- Visualizes the generated spline along with the control points using **matplotlib**.

#### Functions:
1. **`pyramidalFormulation(P0, P1, P2, P3, nPoints=50)`**  
   This function implements the pyramidal formulation for a Catmull-Rom spline between four points. It calculates intermediate points that lie between P1 and P2.
   
2. **`CatmullRomChain(P)`**  
   This function generates the Catmull-Rom spline curve through an entire chain of points and returns the spline curve as a list of points.

