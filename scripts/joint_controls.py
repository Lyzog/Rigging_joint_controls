import maya.cmds as cmds

def createControls(name="FK_Controller", radius=20, controllerNormal=[1, 0, 0]):
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("No joints selected!")
        return

    previousController = None

    for joint in selection:
        controller = cmds.circle(nr=controllerNormal, r=radius, n=joint + "_" + name)[0]
        controllerGroup = cmds.group(controller, n=joint + "_Group")
        cmds.delete(cmds.parentConstraint(joint, controllerGroup, mo=False))
        cmds.orientConstraint(controller, joint, mo=False)

        if previousController:
            cmds.parent(controllerGroup, previousController)

        previousController = controller

createControls()