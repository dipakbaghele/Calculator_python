import sys

from cx_Freeze import *

includefiles = ['Calculator.ico']
base= None
if sys.platform == "win64":
    base = "win64GUI"

shortcut_table=[
    (
        "DesktopShortcut", #shortcut
        "DesktopFolder", #Directory
        "My Calculator",#name
        "TARGETDIR", #Component
        "[TARGETDIR]\SmtCalulator.exe", #Target
        None,  #Argument
        None,  #Description
        None,   #Hotkey
        None,   #Icon
        None,   #IconIndex
        None,      #ShowCmd
        "TARGETDIR", #wkdir


     )
]
msi_data={"Shortcut":shortcut_table}


#change some defoult MSI option and specify the use of above   define tables

bdist_msi_options={"data":msi_data}
setup(
    version="0.1",
    description ="My Calculator",
    author= "Dipak Baghele",
    option={
        'build_exe':{'include_files': includefiles},"bdist_msi":bdist_msi_options},
    executables=[
        Executable(
            script ="SmtCalulator.py",
            base =base,
            icon ='Calculator.ico'
        )
    ]

)
