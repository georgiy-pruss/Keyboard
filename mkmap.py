# Read keyboard-remap.txt, parse it, write keyboard-remap.reg

# http://www.computer-engineering.org/ps2keyboard/scancodes1.html
# http://vim.wikia.com/wiki/Map_caps_lock_to_escape_in_Windows

keys = { "CapsLk": "3a 00", "BkSpc":  "0e 00", "Enter":  "1c 00",
         "Left\\|":"56 00", "Insert": "52 e0", "Delete": "53 e0", "Home":  "47 e0",
         "RShift": "36 00", "RCtrl":  "1d e0", "RAlt":   "38 e0", "RWin":  "5c e0",
         "Menu":   "5d e0", "NumLk":  "45 e0",
         "Pause":  "45 00", "Break": "46 e0" } # (Ctrl+Pause)

m = []
f = open("keyboard-remap.txt","rt")
for line in f:
  line = line.strip()
  tokens = line.split()
  if len(tokens)!=3 or tokens[1]!="-->":
    continue
  if tokens[0] not in keys or tokens[2] not in keys:
    print( "?", line )
    continue
  m.append( keys[tokens[2]]+" "+keys[tokens[0]]+" " )
f.close()

if len(m)>0:
  print( "%d mappings"%len(m) )
  print( ' '.join(m) )

  o = open("keyboard-remap.reg","wt")
  o.write("Windows Registry Editor Version 5.00\n\n")
  o.write("[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]\n")
  o.write("\"Scancode Map\"=hex:00,00,00,00,00,00,00,00,")
  o.write( "%02x,00,00,00," % (len(m)+1) )
  for x in m:
    o.write( x.replace(' ',',') )
  o.write( "00,00,00,00\n" )
  o.close()
