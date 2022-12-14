import nuke

strRepeats = nuke.getInput("Please enter the number of copies:", "50")

iRepeats = int(strRepeats)
bFirstLoop = True

nGroup = nuke.nodes.Group()

nGroup.begin()


kX_Trans = nuke.Double_Knob("x_trans", "Translate X:")
kX_Trans.setRange(-50., 50.)
kX_Trans.setValue(20.)
nGroup.addKnob(kX_Trans)

kY_Trans = nuke.Double_Knob("y_trans", "Translate Y:")
kY_Trans.setRange(-50., 50.)
kY_Trans.setValue(20.)
nGroup.addKnob(kY_Trans)

kX_Rot = nuke.Double_Knob("rot", "Rotate:")
kX_Rot.setRange(-20., 20.)
kX_Rot.setValue(0.)
nGroup.addKnob(kX_Rot)

kX_Scale = nuke.Double_Knob("scale", "Scale:")
kX_Scale.setRange(-2., 2.)
kX_Scale.setValue(1.)
nGroup.addKnob(kX_Scale)


nInput = nuke.nodes.Input()
nDot = nuke.nodes.Dot()
nDot.setInput(0, nInput)


for i in range(iRepeats):

    nTrans = nuke.nodes.Transform(name = "t" + str(i), 
                                  translate = "parent.x_trans parent.y_trans",
                                  rotate = "parent.rot",
                                  scale = "parent.scale",
                                  center = "960 540")

    nMerge = nuke.nodes.Merge2(name = "m" + str(i))
    nMerge.setInput(1, nTrans)

    if bFirstLoop:
        bFirstLoop = False
        nTrans.setInput(0, nDot)
        nMerge.setInput(0, nDot)
    else:
        nTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)

    nPrevMerge = nMerge
    

nOutput = nuke.nodes.Output()
nOutput.setInput(0, nMerge)

nGroup.end()