# Keyboard
All public stuff related to keyboards

KB-6016-RUA.jpg ........... gembird keyboard  
KB-6016-RUA-mod.jpg ... gembird keyboard after KeyboardRemap.reg

K_LAT2015B.klc .............. latin (english) layout, my own, the most optimal (made with genetic algorithms)  
K_CYR2015B.klc ............ cyrillic (russian) layout, quite normal  
K_LAT2015B.png ............ english layout image  
K_CYR2015B.png ........... cyrillic layout image  

keyboard-remap.txt ........ definition of remapping  
keyboard-remap.reg ....... reg file, just double-click it    
mkmap.py ....................... keyboard-remap.txt --> keyboard-remap.reg  
scancodes1.html ............ backup of scancodes from www.computer-engineering.org

The image below is edited to reflect the actual key mapping and layout. Physically no key were harmed :)

![KB-6016-RUA-modified](https://github.com/georgiy-pruss/Keyboard/blob/master/KB-6016-RUA-mod.jpg)

In this keyboard, not all three-key combinations work. For example LShift+CapsLk+F1,2,W,S,X,\\ don't produce any code. That is they must share the same wire inside, I think... Ah, aha... It's _keyboard ghosting_. So it's good again that I returned RShift (to RWin key). ...Well, 's' still stays mute with CapsLk and any of my shifts. So be it. ...But Alt+Ctrl+Shift does work. Also is works in Skype! Not the easiest combination :)

So, the AltGr and AltGr+Shift layouts will be (RU variant in brackets; and AltGr+Space = nbsp):

<pre>´ ←→«»… ·—°™© 'π   ['ґ] (´ = &amp;#769;≡U+0301)
  |&?:; /789* []\  [іїє]
  <>()_ =456- "
  ^@#$% 0123+</pre>

<pre>♥ ↑↵‹›§ •–ⁿ♂♀ Þß   [ÞҐ]  (– = ndash, not sure about ↵µ′″β‹›, not so important...)
  ↓µ′″β ÷√∞ə× äöü  [ІЇЄ] [áéóý instead of µ′″β]
  ≡☺≤≥≠ ≈¼½¾– ☎         (– = real minus)
  ¥¤£€¢ ₴¹²³±</pre>

<!-- !,. good as is, ~`{}\[] no need in RU, șțăâîȘȚĂÂÎ ÄÖÜ ÁÓÉ ўЎ -->

The aim of having the AltGr layout is to keep away from the upper row... will see how it works...

![Latin layout](https://github.com/georgiy-pruss/Keyboard/blob/master/K_LAT2015B.png)

![Cyrillic layout](https://github.com/georgiy-pruss/Keyboard/blob/master/K_CYR2015B.png)

#Keyboard for Samsung Galaxy Note 5 (Android - Multiling O Keyboard)

Eng1.txt, Rus1.txt ...... source text for keyboards (English/Latin, Russian/Ukrainian/Cyrillic)  
eng1.png, eng1sym.png, rus1.png, rus1sym.png, altgr1.png ...... how the layouts look

![Latin layout](https://github.com/georgiy-pruss/Keyboard/blob/master/eng1.png)

![Cyrillic layout](https://github.com/georgiy-pruss/Keyboard/blob/master/rus1.png)
