#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Sphere'
sphere1 = Sphere()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [938, 592]

# show data in view
sphere1Display = Show(sphere1, renderView1)
# trace defaults for the display properties.
sphere1Display.Representation = 'Surface'
sphere1Display.ColorArrayName = [None, '']
sphere1Display.EdgeColor = [0.0, 0.0, 0.0]
sphere1Display.OSPRayScaleArray = 'Normals'
sphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
sphere1Display.SelectOrientationVectors = 'None'
sphere1Display.ScaleFactor = 0.1
sphere1Display.SelectScaleArray = 'None'
sphere1Display.GlyphType = 'Arrow'
sphere1Display.PolarAxes = 'PolarAxesRepresentation'
sphere1Display.GaussianRadius = 0.05
sphere1Display.SetScaleArray = [None, '']
sphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
sphere1Display.OpacityArray = [None, '']
sphere1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
sphere1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
sphere1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
sphere1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
sphere1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(sphere1Display, ('POINTS', 'Normals', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
sphere1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
sphere1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Normals'
normalsLUT = GetColorTransferFunction('Normals')

# current camera placement for renderView1
renderView1.CameraPosition = [-1.284556531192704, -2.2490613039024985, 2.0293350710729694]
renderView1.CameraViewUp = [-0.05177568566262315, 0.6851493239001553, 0.7265601711718896]
renderView1.CameraParallelScale = 0.8516115354228021

# save screenshot
import os 
dir2save = os.getcwd()

pngFileName = dir2save + '/test.png'
if not os.path.exists(os.path.dirname(pngFileName)):
    os.makedirs(os.path.dirname(pngFileName))

SaveScreenshot(pngFileName, magnification=1, quality=100, view=renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-1.284556531192704, -2.2490613039024985, 2.0293350710729694]
renderView1.CameraViewUp = [-0.05177568566262315, 0.6851493239001553, 0.7265601711718896]
renderView1.CameraParallelScale = 0.8516115354228021

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
