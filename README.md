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

In this keyboard, not all three-key combinations work. For example LShift+CapsLk+F1,2,W,S,X,\\ don't produce any code. That is they must share the same wire inside, I think... Ah, aha... It's _keyboard ghosting_. So it's good again that I returned RShift (to RWin key). ...Well, 's' still stays mute with CapsLk and any of my shifts. So be it.

So, the AltGr and AltGr+Shift layouts will be (RU variant in brackets; and AltGr+Space = nbsp):

<pre>́  ←→«»… ™©°—· 'π   ['ґ] (́  = &amp;#769;≡U+03) 
  |&?:; /789* []\  [іїє]
  <>()_ =456- "
  ^@#$% 0123+</pre>

<pre>♥ ↑↵‹›§ ♂♀ⁿ–• Þß   [ÞҐ]   (– = ndash, not sure about ↵µ′″β‹›, they are not so important...)
  ↓µ′″β ÷√∞ə× äöü  [ІЇЄ] [áéóý instead of µ′″β]
  ≡ ≤≥≠ ≈¼½¾– ¬          (– = real minus, ¬ = optional hyphen)
  ¥¤£€¢ ₴¹²³±</pre>

<!-- șțў!~ăâî,.♥ÄÖÜȘȚÁÓÉЎĂÂÎ -->

The aim is to keep away from the upper row... will see how it works...
