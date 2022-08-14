/**********************************
 * Softworks Library Manager Menu *
 **********************************/
println("Loading Softworks Menu")

; VS code
lmgrCreateMenuItem( "StartVsCode" "simple"
   '(("label" "Start VS Code" )
     ("callback" ("SdmVsCodeStartLmgrCB")) ))

; Setup lib manager menu
lmgrCreateMenu("SoftworksMenu" '(("label" "Softworks")))
lmgrAddMenuItems("SoftworksMenu" "" '("StartVsCode"))
lmgrAddMenuItems("menuBar" "L" '("SoftworksMenu"))
println("  Done Loading Softworks Menu ")
