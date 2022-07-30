let((python codeWorkspacePy projectRoot projectId userName logDir executableWithArgs userWorkspace userCodeWorkspace)
    python = "python"

    _filename = get_filename(piport)
    _softworksDir = substring(_filename 1 strlen(_filename)-strlen("code_workspace.il"))
    codeWorkspacePy = strcat(_softworksDir "../code_workspace.py")

    if(getShellEnvVar("PROJ_ROOT") then
        projectRoot = getShellEnvVar("PROJ_ROOT")
    else
        projectRoot = "/prj"
    )
    projectId = getShellEnvVar("PROJ_ID")
    userName = getShellEnvVar("USER")

    executableWithArgs = sprintf(nil "%s %s %s %s" python codeWorkspacePy projectId userName)

    userWorkspace = strcat(projectRoot "/" projectId "/work_libs/" userName)
    userCodeWorkspace = strcat(userWorkspace "/" projectId "_code")
    if(isDir(userCodeWorkspace) then
        logDir = strcat(userCodeWorkspace "/.logs")
        unless(isDir(logDir)
            createDirHier(logDir)
        )
    else
        logDir = strcat(userWorkspace "/.softworks")
        unless(isDir(logDir)
            createDirHier(logDir)
        )
    )
    ;ipcBeginProcess(executableWithArgs "" nil nil nil strcat(logDir "/softworks.log"))
    system(executableWithArgs)
)
