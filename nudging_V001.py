import bpy
#add some comment 
curframe = bpy.context.scene.frame_current

###################################################
#  if you are making addon for the clip editor,   #
#  you can use top and comment out bottom         #
###################################################
#clip = bpy.context.space_data.clip              # will not work in text editor
clip = bpy.data.movieclips['seq.0001.png']       # use your clip name here
###################################################
tiny = 0.1
norm = 1
size = clip.size
marker =clip.tracking.tracks.active.markers
for m in marker:
    if (m.frame == curframe):
        break
posx = m.co[0] * size[0]
posy = m.co[1] * size[1]

print ("frame %d  selected marker location x: %6.3f (pixel %6.3f)" % (curframe, m.co[0], m.co[0] * size[0]))
print ("frame %d  selected marker location y: %6.3f (pixel %6.3f)" % (curframe, m.co[1], m.co[1] * size[1]))

moveto_x = posx - norm # new x location in pixels
moveto_y = posy + norm  # new y location in pixels

m.co.__setitem__(0, moveto_x / size[0])
m.co.__setitem__(1, moveto_y / size[1])

print ("frame %d  selected marker new location x: %6.3f (pixel %6.3f)" % (curframe, m.co[0], m.co[0] * size[0]))
print ("frame %d  selected marker new location y: %6.3f (pixel %6.3f)" % (curframe, m.co[1], m.co[1] * size[1]))
