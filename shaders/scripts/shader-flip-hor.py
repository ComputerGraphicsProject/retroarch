import re

horizontalFlip = 'wrap_mode0 = "clamp_to_border"\nmipmap_input0 = "false"\nalias0 = ""\nfloat_framebuffer0 = "false"\nsrgb_framebuffer0 = "false"\nparameters = "MIRROR"\nMIRROR = "1.000000"\n'
shaderPath = 'shaders_glsl/misc/flip-horizontal.glsl\n'

#righe del file
rows = []
separator = ''
#apertura file e successiva lettura
with open("./shaders/retroarch.glslp", 'r') as fp:
   for row in fp:
      #inserimento righe in un array
      rows.append(row)
#ottenimento del numero di shader attivi
nShaders = int(re.search('shaders = "(.*)"', rows[0]).group(1))
#incremento e reinserimento degli shader attivi
rows[0] = 'shaders = "' + str(nShaders + 1) + '"\n'
retroarchGlslp = separator.join(rows) + 'shader' + str(nShaders) + ' = ' + shaderPath + horizontalFlip
print(retroarchGlslp)
fp.close()

file = open("./shaders/retroarch.glslp", 'w')
file.write(retroarchGlslp)
file.close() 