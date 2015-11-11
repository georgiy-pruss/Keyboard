# Read keyboard-remap.txt, parse it, write keyboard-remap.reg

# http://www.computer-engineering.org/ps2keyboard/scancodes1.html
# http://vim.wikia.com/wiki/Map_caps_lock_to_escape_in_Windows

keys = { "CapsLk": "3a 00", "BkSpc":  "0e 00", "Enter":  "1c 00", "Tab":  "0f 00",
         "Left\\|":"56 00", "Insert": "52 e0", "Delete": "53 e0", "Home": "47 e0",
         "RShift": "36 00", "RCtrl":  "1d e0", "RAlt":   "38 e0", "RWin": "5c e0",
         "Menu":   "5d e0", "NumLk":  "45 e0", "Scroll": "46 00",
         "Pause":  "45 00", "Break":  "46 e0" } # (Ctrl+Pause)

m = []
with open("keyboard-remap.txt","rt") as f:
  for line in f:
    tokens = line.strip().split()
    if len(tokens)<3 or tokens[1]!="-->" or tokens[0].startswith("#"):
      continue
    if tokens[0] not in keys or tokens[2] not in keys:
      print( "?", line )
      continue
    m.append( keys[tokens[2]]+" "+keys[tokens[0]]+" " )

if len(m)>0:
  print( "%d mappings"%len(m) ); print( ' '.join(m) )
  with open("keyboard-remap.reg","wt") as o:
    o.write("Windows Registry Editor Version 5.00\n\n")
    o.write("[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]\n")
    o.write("\"Scancode Map\"=hex:00,00,00,00,00,00,00,00,")
    o.write( "%02x,00,00,00," % (len(m)+1) )
    for x in m: o.write( x.replace(' ',',') )
    o.write( "00,00,00,00\n" )
