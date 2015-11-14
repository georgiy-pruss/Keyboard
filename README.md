# Keyboard
All public stuff related to keyboards  

KB-6016-RUA.jpg ........... gembird keyboard  
KB-6016-RUA-mod.jpg ... gembird keyboard after KeyboardRemap.reg  

kb_RU204.klc ................ russian layout, quite normal  
kb_EN214.klc ................ english layout, my own, the most optimal (made with genetic algorithms!)  
kb6016layout.png .......... english layout image  

keyboard-remap.txt ....... definition of remapping  
keyboard-remap.reg ...... reg file, just double-click it  
mkmap.py ..................... keyboard-remap.txt --> keyboard-remap.reg  
scancodes1.html ........... backup of scancodes from www.computer-engineering.org  

The image below is edited to reflect the actual key mapping and layout. Physically no key were harmed :)

![KB-6016-RUA-modified](https://github.com/georgiy-pruss/Keyboard/blob/master/KB-6016-RUA-mod.jpg)

In this keyboard, not all three-key combinations work. For example LShift+CapsLk+F1,2,W,S,X,\\ don't produce any code. That is they must share the same wire inside, I think... Ah, aha... It's keyboard ghosting. So it's good again that I returned RShift (to RWin key).

So, the AltGr and AltGr+Shift layouts will be (RU variant in brackets; and AltGr+Space = nbsp):

<pre>Þ §ßäöü |789* șț  [́  §ýáóé ... ґў  ́  = &#769=U+0301  ]  
  °—!^~ &456- ăâî             [іїє]  
  ←→#() =123+ ,  
  «»©%@ $0_./</pre>  

<pre>♥ µβÄÖÜ ₴√∞ə× ȘȚ  [µβÁÓÉ ... ҐÑ ]  
  π–♀♂≈ £¼½¾– ĂÂÎ           [ІЇЄ]  
  ↑ ≠≤≥ ≡¹²³± •  
  ↓↵™¢¤ €ⁿ…·÷</pre>

The aim is to keep away from the upper row... will see how it works...
