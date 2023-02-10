printf("  Adding Softworks Menu\n")

lmgrCreateMenuItem( "StartVsCode" "simple"
   '(("label" "Start VS Code" )
     ("callback" ("SdmVsCodeStartLmgrCB")) ))

lmgrCreateMenu("SoftworksMenu" '(("label" "Softworks")))
lmgrInsertMenuItems("VirtueHelpMenu" "" '("StartVsCode"))

printf("  Done adding softworks menu\n")
