default mouse_xpos = 0
default mosue_ypos = 0

default map_list = {"Map1":"Map1"}
default map = map_list["Map1"]
default map_xoffset_list = {"Map1":0}
default map_yoffset_list = {"Map1":0}
default map_ini_xpos_list = {"Map1":0}
default map_ini_ypos_list = {"Map1":0}

define cha = "Tom"
define cha_ini_ypos_list = {"Tom":200,"Susan":100}
default cha_ini_xpos = 0
default cha_xpos = 0
define cha_ypos = cha_ini_ypos_list[cha]

screen MoveMapCamera:
    imagebutton:
        pos (0,540)
        idle "gui/MapScreen/leftarr.png"
        action SetVariable("map_xoffset_list[map]" , map_xoffset_list[map]+50)
    imagebutton:
        pos(1750,540)
        idle "gui/MapScreen/rightarr.png"
        action SetVariable("map_xoffset_list[map]" , map_xoffset_list[map]-50)

screen GetMousePos:
    imagebutton:
        idle "gui/MapScreen/empty.png"
        action SetVariable("mouse_xpos",renpy.get_mouse_pos()[0]+map_xoffset_list[map])

#screen ChaControl:


screen ChaAni:

    on "show" action Show("Map1")

screen Map1():

    add "images/map/Map1.png" pos(map_ini_xpos_list[map],map_ini_ypos_list[map]) offset(map_xoffset_list[map],map_yoffset_list[map])
    
    on "show" action Show("GetMousePos")
    #on "show" action Show("ChaControl")
    on "show" action Show("MoveMapCamera")  