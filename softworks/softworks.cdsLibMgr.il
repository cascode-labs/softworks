println("  Adding Softworks Menu")

lmgrCreateMenuItem( "StartVsCode" "simple"
   '(("label" "Start VS Code" )
     ("callback" ("SdmVsCodeStartLmgrCB")) ))

lmgrCreateMenu("SoftworksMenu" '(("label" "Softworks")))
lmgrInsertMenuItems("VirtueHelpMenu" "" '("StartVsCode"))

println("  Done adding softworks menu ")
