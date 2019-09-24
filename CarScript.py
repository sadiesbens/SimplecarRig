import maya.cmds as cmds
#Mercedes James
#this script creates a car with 4 wheels and then rigs it so the wheels move and rotate as the car moves



#create shapes,move and scale
body=cmds.polyCube(w=5,h=5,name='body')
cmds.xform(r=True,ro=(90,0,0,))
wheel=cmds.polyCylinder(name='wheel')
cmds.xform(r=True,ro=(90,0,0),t=(-1.6,0,3.026),s=(0.8,0.5,0.8))
wheel2=cmds.polyCylinder(name='wheel2')
cmds.xform(r=True,ro=(90,0,0),t=(1.4,0,3.026),s=(0.8,0.5,0.8))
wheel3=cmds.polyCylinder(name='wheel3')
cmds.xform(r=True,ro=(90,0,0),t=(-1.8,0,-2.99),s=(0.8,0.5,0.8))
wheel4=cmds.polyCylinder(name='wheel4')
cmds.xform(r=True,ro=(90,0,0),t=(1.5,0,-2.95),s=(0.8,0.5,0.8))
#direct connection to translateX of the body to rotateZ
cmds.connectAttr(body[0]+'.translateX', wheel[0]+'.rotateZ')
#create plusMinusAverage node
x=cmds.createNode( 'plusMinusAverage')
#connect translateX of body to translateX of the wheel thru node
cmds.connectAttr(body[0]+'.translateX',x+'.input1D[0]')
cmds.connectAttr(x+'.output1D',wheel[0]+'.translateX')
#place wheel
cmds.setAttr(x+'.input1D[1]', -1.5 )


#direct connection to translateX of the body to rotateZ
cmds.connectAttr(body[0]+'.translateX', wheel2[0]+'.rotateZ')
#create plusMinusAverage node
x=cmds.createNode( 'plusMinusAverage')
#connect translateX of body to translateX of the wheel thru node
cmds.connectAttr(body[0]+'.translateX',x+'.input1D[0]')
cmds.connectAttr(x+'.output1D',wheel2[0]+'.translateX')
#place wheel
cmds.setAttr(x+'.input1D[1]', 1.5 )

#direct connection to translateX of the body to rotateZ
cmds.connectAttr(body[0]+'.translateX', wheel3[0]+'.rotateZ')
#create plusMinusAverage node
x=cmds.createNode( 'plusMinusAverage')
#connect translateX of body to translateX of the wheel thru node
cmds.connectAttr(body[0]+'.translateX',x+'.input1D[0]')
cmds.connectAttr(x+'.output1D',wheel3[0]+'.translateX')
#place wheel
cmds.setAttr(x+'.input1D[1]', 1.5 )


#direct connection to translateX of the body to rotateZ
cmds.connectAttr(body[0]+'.translateX', wheel4[0]+'.rotateZ')
#create plusMinusAverage node
x=cmds.createNode( 'plusMinusAverage')
#connect translateX of body to translateX of the wheel thru node
cmds.connectAttr(body[0]+'.translateX',x+'.input1D[0]')
cmds.connectAttr(x+'.output1D',wheel4[0]+'.translateX')
#place wheel
cmds.setAttr(x+'.input1D[1]', -1.5 )




 