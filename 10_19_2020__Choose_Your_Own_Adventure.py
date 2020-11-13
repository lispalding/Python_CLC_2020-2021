# PROGRAM NAME: 10_19_2020__Choose_Your_Own_Adventure.py
# PROGRAM PURPOSE: [PYTHON CLASS PROJECT]: Choose your own adventure game
# MADE BY: Connor Paxman, Daniel Lehman, Lisette Spalding, Ty Smart
# CLASS HOUR: 4/5th
# BOOK USED: Underground Kingdom
# DATE LAST MODIFIED: 10-27-2020
# PYTHON VER. USED: 3.8
# PROGRAM USED FOR GROUP WORK: Repl.it


# imports
import time

# variables
# screen animation
def title_page():
  title_page1 = ("""             _   ___    ___   __     ___     __     ___               _   ___""")
  title_page2 = (""" |    | |   / | |   \  |     |  \   /   \   |  \   /   \  |    | |   / | |   \ """)
  title_page3 = (""" |    | |  /  | |    | |---  |  /  |  ____  |  /  |     | |    | |  /  | |    | """)
  title_page4 = (""" \____/ |_/   | |___/  |___  |  \   \___/|  |  \   \___/  \____/ |_/   | |___/""")
  title_page5 = ("""      _ _      _    ___    ___     ___    _    _""")
  title_page6 = (""" |  /  |  |   / |  /   \  |   \   /   \  | \  / | """)
  title_page7 = (""" | |   |  |  /  | |  ____ |    | |     | |  \/  | """)
  title_page8 = (""" |  \ _|_ |_/   |  \___/| |___/   \___/  |      | """)
  title_pages = (title_page1, title_page2, title_page3, title_page4,"_"*80, title_page5, title_page6, title_page7, title_page8, '_'*50)
  for page in title_pages:
    time.sleep(0.15)
    print(page)
  title_art()

def the_end():
    the_end1 = """___________.__             ___________ _______       .___"""
    the_end2 = """\__    ___/|  |__   ____   \_   _____/ \      \    __| _/"""
    the_end3 = """  |    |   |  |  \_/ __ \   |    __)_  /   |   \  / __ | """
    the_end4 = """  |    |   |   Y  \  ___/   |        \/    |    \/ /_/ | """
    the_end5 = """  |____|   |___|  /\___  > /_______  /\____|__  /\____ | """
    the_end6 = """                 \/     \/          \/         \/      \/"""
    the_end_list = (the_end1, the_end2, the_end3, the_end4, the_end5, the_end6)
    for page in the_end_list:
        print(page)
        time.sleep(0.2)

def title_art():
    print("""                                                                                   
                .^^:~:::' ` `       `',.                                 '`            
                -^kIMYYy>}xv}|=._<?}VkVGIu|)vmcv;        -r<>        `)~.             
                        :**c]yi)}YYvu}oozq6KiyhOdjV_`-l**hQ$mvzwxykayP5:`'``           
                            *y?}v)TsbV3HIq88r=~\EBQQQ#0M3XzcMzM$3ywmM#gdzx~           
                                `=V0#DdO0ziv'   ``._;ZwTwc}\r\^:`    ,``              
                            <^~vZBQ3r*HL!                                              
        _~` :xPHYirLxIhV^LdO3ZQmx|Vx`       "?lVVL~`                                 
        :P$QZKOm3MVTIwMkMhhYkZXVadGr``!";*)<v8@@@@@@@BTr<!":`          ',!;(V}TzmTeL'  
        _^|W$dGddzcT*:^YOZUuKhXHz-*k$jy3OE@@@@@@@@@@@@@@Ba*-         _xyKOQ$WKsdMGx`  
        `)y}:)Hx:      `**v8m3GMdOMM93dMGQ@@@@@@@@@@@@@@#Er,_`::-. `''''!9gga:-!:`    
    .!>ru$l` ``            :vrwukEMMwZ0y. y@@@@@@@@@@#6WRBQ6gOWdggdhMEdW$#B#Q##QPy3x.  
    _Kozyc3dqR0dov(|YVuY_-xr``*uI##d$M    `6@@@@@@@@@@@Z^VQ00$KbQgemP50Hz\,``!38$IwwI- 
    !LXulowMXW$5s3TyVy}c$##BZPUXzTxx:,`=.!__cg@@@@@@@#c!]Iu)zbTX8Oy}hsQZUzkzMKcUdUTTx' 
    .:VUVuyV^^^`    `|yyc#Q#Q$QHoeMM8EO0OQOPY_:\y00}xYoTr\IEOy86u*=~zgQckMzGzVuIawcY:  
                `<uuTuVIsywQ8qg$9g$Zzk.      `)zQQODEORPggdRE0UW5VmP6BKUOm3syVTyewUr  
    :~=(r^i?!,:y0VYcUIwT:`xoYL"|E#MlTkY*`.}PMZ$eZdq0POkzGdH3zdGhqeI3bB6e0GgQzcVVkksm~ 
    ~xLKm8Ze55Kb8QqII3zx)rv}oZgQ#B9QK680mzTyuO8g6P0WM5IjXoahPam6GU3Vm6BQM0D}9QGyyqzLi" 
    `;xuumekk}Phdd6Z3sMIdB50$g#3r::*`|  ->xGsTLITiVh3B5Pe3ZhTkwR$53MeOQBKIYed5Iv>*_`   
    `:!<^\^=~)^,=~i}x}r``v'~}v^-,:``   :``=TVMGL~rzGMdowuKXIswuwMGTTxVz$E8866cvrymWGkx""")

    input("Press Enter to Continue: ")

def warning_page(): 
    print("\tSPECIAL WARNING")
    print("""The Underground Kingdom is not easy to reac, Many players never get there. Others never return...Before starting out on your journey, you may
    want to read Professor Bruckner's theory, which
    is set forth on the pages that follow.
    Professor Bruckner is a rather boring writer,
    and I wouldn't suggest that you bother to read his
    theory, except that, if you ever get to the Underground Kingdom, it might save your life.
    Good luck!""")
    input("Press Enter to Continue: ")
# Connor Paxman pages 1 - 26
def page1():
    print("<--STORY STARTS HERE-->")
    print("""\nYou are standing on the Toan Glacier in northern Greenland, staring down into the black void
of the crevasse. You shiver as you wonder
whether you were lucky or unlucky to be invited
on this expedition.
Standing next to you are Gunnar Larsen of the
National Research Institute and Dr. James Sneed,
a geologist. A small black box containing a signal
transmitter is suspended over the crevasse by two
long poles. The transmitter is wired to a console a
few yards away in the ice. Dr. Sneed turns a dial
as he monitors the display screen.
"Well?" Larsen's voice is impatient.
Sneed looks up, a broad smile on his face.
"This is it, friends—the Bottomless Crevasse."
"Any radar return?" Larsen asks.
Sneed shakes his head. "None."
For a minute no one speaks. Like you, the
others must feel excited to have reached their
goal but also a little sad. It was just a year ago that
your old friend, Dr. Nera Vivaldi, radioed from
this spot that she had reached the Bottomless
Crevasse. A few moments later, her radio went
dead. She was never seen again.""")
    input("Press Enter to Continue: ")
    page2()

def page2():
    print("""\nNow you stand at the edge, lost in thought
How could the crevasse have no bottom? Could it
really lead to an underground kingdom? What
happened to Dr. Vivaldi?
But your thoughts are shattered. You didn't
seem to slip, yet suddenly you are falling into the
crevasse! A ledge is coming up fast beneath you.
You could land on it, but you're falling so fast
you're sure to be badly injured. You might only
be saving yourself for a slow, agonizing death.
These thoughts race through your head in a
split second.
""")
    choice = input("Do you want to land on the ledge?")
    page4()
    if choice == "yes" or choice == "Yes":
        page5()
    else:
        page3()

def page3():
    print("""\nYour consciousness slips away as you fall faster
down, down, down.
The next thing you know, you're floating in air.
In the soft, reddish light you can see that you are
in a cavern, drifting toward the ceiling—or is it the
floor? In a flash you realize what has happened—
you've fallen to a point where gravity above you
is almost equal to gravity beneath you!
You brush against a firm surface—a wall that
feels like clay. You cling to it for a moment. Then
you're floating again, drifting slowly down. You
begin to lose your fear as you realize that gravity
here is so weak that you can fall mile after mile
without being hurt After a while you begin to
relax and enjoy drifting through a fantastic twilight world. You only wish it weren't so hot! Closing your eyes, you try to pretend that you are
safely home in bed""")
    input("Press Enter to Continue: ")
    page6()

def page4():
    print("""\n..............................................................................
..............................................................................
..............................................................................
.............::.:::...:::.:*:...:::::::.......................................
...........::::**:::::***V**:...:...::::......................................
...........:::::*:::****:*:...................................................
..................................................................:.::........
......................::..:****:::::::*:...........:::*******::..::::::::::::.
.......:*V***************V**FMMIVV**V*VV*******::::*::::::::..................
.........:*:::*:*******::...VMNNIIVV*:::::..:::::**:::***::...................
..................:****:...:.*N$$V*F*::****:.........*V*:::***:...............
................:**::*::.::**IIV**:FMFMMINMMMVVVV*:::VV*:::..::*:::::::::.....
................:**:.::*******V*VMMMFMNNNMV*M$$$$$IV*****:VV*****::::::::.....
.....................****....:**N$$NNN$$$I*VNFVFVI$MV*:::*******:..:.:**V:....
.......::.:*::V***::........::FNN$$$$$$$NV*VV.:VVVMNI*::***...::*:............
....:*VVVVMI**V**VV*........*:V$$$$N$$$$$IV*VVF*VMMV*:::::...*:**:............
...*::****:*::**:*::::..:****::*VMNNNNN$$$$V*FVVVMV:::::::::.:::......:**.....
.:****:.:...:::**********VVV**:**I$$$N$NNNNMM$$$$NV*****VV*V**.::.......::....
.:.:*:.....:*:*:****:**:********$$$NIVIN$NMFM$$$MIMIVV*::*****::*****:::......
...::........*:......:::::**VVFNN$$NFVMMMMMMMMM$NNNNF*IV***:****VVV:*V*.......
............*:.....****V*VV*VM$$$NMMNNIMNMFNI::*MMMV**F$NIVVVV**:*VV*::.......
..........::..::*:*:::*:.::*FMN$NNMN$NFN$$$NV:**:*VVVFNV***:::................
.........:*:::****:.::.::*M$MNMNIMIM$MMNN$$NI***....::*::....*................
.....::***:*******:*:....V$$MMNMMMNNNMINMIMNNNV:****:.:::....:................
.....:**V:*****:V***.....:*M$$$$NNMIIIFN$$N$NMN*::::..:**:...:................
.....::.......:.FIF:....::..*VM$$$$$$$N$$$N$$N$V***:.:*:....:::VV*:...........
..............::VV*:..::::...:*NNIIMMMMM$$$$$$M:.::.::*:*VVV*:::*:V::::.......
.......:::::::**V*V::...::..**F$MMMV:.:V$$$$$M:.....*V******::**V*::::........
.......::*******VVM*....::.:**$NMMM*..*$$$$$$*....*V*****:.:::::..............
............:::::*V**.::::.**V$$MMM**VN$$N$$M:***VV*:**:****:::::::...........
.............:**.V***.*::.:**M$$NMI::V$$$N$N*..*VV******:::...................
..............::.:VV:.::****VN$$$NMVVN$$$$NFV*V*V****:........................
...................:**:::***:F$$$$IV*IM$$NNV*...:.............................
.....::*********:*:::.....::*N$NN$$NV:*VNN$NV**::::::::.......................
.........:::::....::::::::*.:VMMMNN$$N*.*VIMIV***VVVV**::::...................
.......:::::..:::******::****::*VIMMMIV:**:*FV*::.*VV*****:...................
....:::*::****V****:::::.****V***::::::.....*V*.....::**::....................
.....:*****::...:*****VV**::.::::..........:*FV:::::***:**....................
...................*:...............:.....::*VM********FV.....................
.............................................*I:::::****:::::.................
..............................................:...............................""")

def page5():
    print("""\nYour whole body is racked with pain as you
crash onto the ledge. You're shaken and bruised
but still alive! A snowbank cushioned your fall.
"HELP!" you cry.
"Hold on!" Larsen yells. "It's going to be tricky,
but we're rigging our ropes. We'll get you up."
You feel a flash of joy; then you remember
something that chills you to the bone. You were
very careful not to fall in. You're quite sure you
didn't slip; you were pulled as if by an unknown
force within the Bottomless Crevasse.
Should you warn your friends about the
strange force? If you do, they may be afraid to get
close enough to rescue you.""")
    choice = input("\nAre you going to warn your friends?: ")
    page7()
    if choice == "yes" or choice == "Yes":
        page13()
    else:
        page9()

def page6():
    print("""\nOnce again you brush against a firm surface.
This time it's the floor of the cavern. In fact, you
have touched down on the mossy bank of an
underground stream. You drink from the cool,
clear water, then step out of the cavern into this
strange world.
The only illumination is a dim red-orange glow
that seems to come from the ground. The air is so
clear that you can see shadowy, curving hills and
valleys stretching out in all directions, even above
you.
Why do you feel so good? It must be because
you are so light—you could hardly weigh more
than ten or fifteen pounds. You spring to your
feet Every movement is easy. You jump—twenty
or thirty feet high—and float gently to the
ground.
Then you realize that you are not alone. Only a
few yards away is an odd creature. As big as you
are, it seems to be some kind of bird yet much
more than a bird. Under a crown of soft golden
feathers are enormous blue-green eyes, so vivid
and intense that they seem to be not only a
means of vision, but also a means of power.
There is something terrifying about that face,
but also something angelic, something that draws
you to it In fact, you feel as if you are being
hypnotized by those eyes—eyes of an angel bird!""")
    choice = input("\nAre you going to run from the strange creature?: ")
    if choice == "yes" or choice == "Yes":
        page15()
    else:
        page10()

def page7():
    print("""\n:.**V::FF***V*VV****::::.......................................::*.*V:.:**:...:**:::
**:**V*:VNV*VV*VV*VIFV***VV*::...............................:VFV:***::****.:****:*V
*V*:*VV*:VNNV*V**VV*VMFF*:*VVV*...........................::*MF*:**V*:****:****::*V*
V:**:*VVV:*V$I****VV**IMVVVVVMI*:......................:V*VVV**:****:***:.****:.*VV*
VV******VV*.VNMFV****V**MNNIV*VFV*:...................VIVV*:*V*:VV***V*:****::.****:
**VI**V**VIV*FNNV*****VV*VN$MV::*VFV:...............:VFVV*:*VV*:V*:VV*::*V***.*VVV*:
VVIIV*:****VIV*NNNV*VV**VV*VM$MV*FVIF**:..........:*FVV*:*VVV*:*V**F*:VFFMMIIMMMMMVI
IMIMIVFV:*V*****VNNMMIFV*VVV*VM$V*VV*VVV*:......:VIIVV*:*VVVV:*VFVVIFNNN$$MIVVV*VVVV
N$NNMINMVVV***VV**VMMNMMFV**V**VNMVIV*VMMIV*:.*FNNMMF**VIMMMIINNNMFINMVVVV*VV*FVVVMM
*V**VIMMMMMV*****VV*VI$NMNV**VV**M$$$$$N$$$$NM$N$NNNFMNNMMMNMMIVIIVIV**FVV*VVVIN$NMM
**VVV*VIMMMMV****:*VVVVVNNMMVV*VVVI$NMNMMMMMMIFIMMMMMN$N$NMNMMVVMIMV*VFVVMVVNNN$NIVV
*:**V***VFMMNNIV******V**FNNMMV**V*V$MIIIVVFVVIIVVFVVF*VVVFVVVFIIMNNNNNM$$MM$MIIVVV*
**:***VV:*VVFNNMMMFVV***VV*VMN$MIIVVVVNNMNMFMMIFMN$NMIFMFVF*::**VVVVFMMM$$MVV*VFV*V*
**:****V***VVVVVNNNNMVVV**VV*VVNNNIIFVVI$$$NMIVFV***:*:*VIMNVFV*:***VVINNIVVVVV*V**V
***:***VVV*:**V**VFNN$NMIFV*VFVVFMNNNIFVVIN$NMI*VV******::*VIM$$NMMMNMNMIFVVV**VV*V*
***::V***VVV***VVV**VM$N$NMVVV*VIVFMNNMMMMVFINIMMMVVF**V****FFINN$$$MMNNF**FMIIIIMNM
****:***:*VVV*:**VV**VVF$$$$IIVFFFVMMIVINNN$NMMMIM$$$NVVFIVVM$$$$$NNNNNM*FN$N$NMM$N$
****:**V*:V*V**::VVV***V*VM$MFVVMFNN$$IVVVFIFM$$NIMMNNNMN$$$NNNNMNMN$$NMNN$$NNNNN$$$
VVVV:*VV*********:*VVV*:VVVVVM$$$MFVV*IV*******VVINN$$$$$$$NMMIFIIIMFVVVVVFMNNMMFVMI
*VVV:****V**V***V*:*V**V**VVV*VFMNNV*VV***VVVVFMNNMNNMVVVFIV*VVVFVIIVVMN$NNNFVVINNVV
***::***VVVVV***VV*:*V*VV***V***VVIIMN$MNMNMIN$NIIVVVVFMVVFFV*VVV*FIMNNNNFVVVIMNNV*F
*VVV***::***:*VVVVIV:*V*VVVV*VV*:*VIVVFMN$NNMV****VVFF***VFIVVMMIFMNNIFFVVFVVMNV****
***VMMMF*FVV*******V*.:*VVVV*VVVV**VIMNNMFV**VFV:VVV*****VIMMMNNMFIVVVVV*VVMMVVVFV*V
****V***:*VVV*VV**::****::**:*VVVMMNNMFV**VVFV******VV*VMNNNNMVVVVFVVVVIMNMVVV*VF***
VINMMNIIMFFV*VVVV******:***VFVFMN$MV***VIV*VV**VVVVVVIMNNMFIVIMIVVVVIMM$I*:V*VV*:VVV
$$N$$$$NN$NNMMNIFIIV*I$NN$NNNNMV****VVVVV:***FVVFFVMN$NIMFVVIVVVVVIN$NFVV***VVFVIMMM
*VVVV*******VVFMMN$$N$NMNMFV***VVVF*VFV*:*V*IMNMIINNMFVVVVIFV*VIMNFV*VMFFFMMNNIM$$NN
MNMVMMVVV*VVVVV***********V*V*VVVVF*FIIVFMMMNNNNIFFVVVVVVVVVVMNMF*VV*IN$NNN$$$NMIVVF
FIIINNNMF*FVV**V***VMIMV*VVVV*V**VMM$NN$$NMNNIVVVVVIV***VFM$MIFVFINNM$$MMMM*VFFIV***
VVVVVVFMMMN$NMMIIIFV*VII**FV*VFINNN$NVVVVFN$NNNINMMVVIMNNMVVVIN$NNMVVVVVV**VVVV****V
V*IVVVFFVVFIIMNMMNNNNIMMFVIIM$N$NNNMFVIVVVVVVMN$$NNNNNNIMIIMN$NIFIVVVVVV**VVVVV**V**
VMMIV*VIV*VIVVVVV*VVFFM$$$$N$$$$NVMIMVIV*VVIIVVVMMN$$NNN$$$NIFFMIVVIMMMMFN$NM$NNMNFV
FFMN$NMMMIFIMIF**V*VVFFIIMMMNN$$$NNVVVFV*VV**VVMMNN$$NMMIMMMFNNNMIIIIVMVVVVVVVMMMMNN
MIVVVVFFVVVVMN$NMIMFVVMNNIVV***VVVVFMMMNNNNNNNNMN$MFVVFMMN$MVV*VV**VV***V*VFVVMNNIVV
VFNNVVVFFV**VVVIMMNMN$$NIVVVVV*VVVVVVVMNN$$$$$$NVVVMMNNIVV**FF*VV**VVV*F**VVF*VIFFV*
VVVVVMMI**IVVV*VVVVVVFN$NMMFVV*FFFIM$$$$$$NIVVVFNNNIV*:*VVV**:*II*FIF*VV*VVVVVVVVVVV
**FIV*VINV*V*VV**VVII*VFM$$$$NMN$$$$NMFVV**VMM$NMF**V**VV***V*VIFVV**VVV**:*VVFFVMIV
VV**VVIII$$NFVVFMIM$NIMNMIMNN$NFVVFVV**IIVMN$FV**VV***V*.:VV*VVVV*V*VVVV**VIMNMNN$$N
*VFVVVMN$$$$$$$MNMIFVVV*VIM$NMVVFMIMMFINNMIV***VV***VV****VV*FVVV**VVIMMIN$NMIFVFV*V
MFM$$$$$$$NMMFMVVF*V**IV**VFFIIMN$$$N$$$$I*VFV***VVVV*VVV*V**V*V*VFN$$$MVVVVVVVVVVII
$$IN$NMFFIVI**V*VF*V****VV*VFIV**VVVIN$$$$$NNMVVFFMFV*IV*VVVMNMMNNNIVVV*VVV**VVFIVN$
MFV***VVVVIVVIVVVV**VV****VV*VVVVVVVIVVIIIMIM$$$$$$$$$$$$$$$$NIVVV**VVV***VIINMNNNNN
***FN$$$NN$M$NM$NMF*VVV:*V**V***VVFV**VIMMIIVVIIIIIN$$$$$$$$NVVMMMV***VIMMMNN$MIVIM$
NMMIIIFFFVVVVFMN$$$NNNNMFNF*VVV**V***V**VVVVVVFVININN$$$$$$$$$$$$MMMIMNN$NN$NVMVIVF$
VVV*VV*VV*VVV*VVVVVVVVMN$$$$NNNMMFIIVVVVMFVV**VFVMM$$NN$$$$$$$$$$$$$$NM$MVVMNVINMMN$
$$$N$$N$$MN$MNNNMM$NNMIIIIMIMMMN$N$$NMNMVVVFIFFIM$NN$$$$$M$$$$$$$NNN$MI$$NNNIVFINVIM
IFIM$N$N$NM$NM$MMN$$$$N$$$$NNMMIMIFMN$N$$NM$NNN$$$N$NM*M$$N$$$$MMVFN$$MMMIVIMIVIVVVI
VFVV**VVFIMNNNMN$$$$NVVMNMNN$NIMN$$$NMMMN$N$$NFF$NM$V.:*NN$NNMVIIMMMIFMIFMNFNMMMIMMM
$MNMMVVVVFVVVVIFNN$$IMIMNNN$FNNMIMN$NMIFMMVVVM*V$NN$N*:VNNMMIMMVVMIMIVIF$$MIMMMIVVVV
VFI$INNMNNNNN$$NMMM$$$MMMMN$NMMIII$M$$NMN$$MNNVM$$N$N**IM$NFMMFVVMVIFMMNM$MVVVMMIIV:
VVMNNMM$$$$NIMMMIMIN$NNMIIMNMFM$$MMINMMMM$$$$NM$N$$NNVMM$MNFMMVMNNMVVFMNIMNIIMMM*VI:
IIMNMMNIVVVVVFVV*VVVVVVVVMMN$NIM$NM$NMMM$N$$$$$$$$$$NN$$$NFINNNFMVFMNIVMVIMINMFFIVV:
FMMMNMII**V*::*::..:**VVV*******VVIVVVIFMMNMMMMMMNMN$$$$$MVVFVFIIIIMIMMINIMVM$MVVV*.
IMMIMFIFV*::...:.:.::::.:..::.:::**:*VVVV**:*V*VVVV*INNMMMIIMNFMNNNVMINMMMNNIMMMVV*:
IMNNIVMMV****::.:*::::::FMMII*:..::..:::**::::**::*VN$$$$VVVNNM$NM$IINMMVFMI*M*IV*:.
VVVVVV***VVV***V*VVFIINM$$$$$$V::::**VV**:::*:******VFIFVV*VFIMNN$$NM$$MVMIVINMVMVV.
***VV*:::***FVM$MMN$$$IV*I$$$$NNF*IFVVVIFIVVVIMNMIIIMMMMMIINNNNN$$$IMMFMVVVVVVVVFMF*
NN$$NMMMIMNN$$$$$$$NN$*..FIMM$$$NN$$$$$NNNNNNNMMMIIIMMMMMMMNNNNN$$$$$$MVVII*VMIFVV*:
M*VNMN$N$N$NNMMVVFI$$NF:VI*MN$$$$$NNN$MMN$$NMMFMIVVFIFFIMIMMNNMMMNNNNMVVIV****VF*...
F*IMVMIIN$$$NN$N$$N$$$F*$NMN$$$$$$$$$$MMMMN$NMMMMMMMMMMMMMMMNNNNNNM$MVMMV**.*VMM*...
::VVVFIIIN$$N$$$$$$$$$IN$$NN$$$$$$$$$$$$VVIMMMMMNMIMMIMMNMNNNNNNN$$NMVMVV***VVVV*...
:*.**VFMIM$$NNN$$$$$$$$$$$$$$$$$$$$$$$$NMNMNMMMNMMMNNNNNNN$NNN$$$MMNNVVV*.**V*::::..
:**FVVMVVVFMMNN$N$$$$$$$$$$$$$$$$NNMMNNMNMMMMMIIIVMMIMNMMNNNNNNFFMNMV****VIV*V****..
.*VVVV**VVMMMM$$N$$$$$$$$$$$$$$$$$$NMNNMNNN$$NF******:::VVFMNNINMFIVV*:**VVFVIMF*...
.:****::*VMINM$$$$$$$$$$$$$$$$$$NNNN$NIMN$NMNIIIFFFVV*::VVFIVIIMVFM*V*V*FVFVVV***...
.......*V*VVMFVI$$$$$$$$$$$$$NNIVVFIFV****VIMMIIMMMVV*:.*VVIFIIVIVIVVV****:*VV......
.......:***VVIVM$$$$$$$$NN$$$NMIV****VVV**VV******VV****VVVFVVV***V*V*:.**VIV*......
......::.:*VVVVVMVN$$$$$MN$$NV****::**********::*VVVFFMF*VFVV****V*VV...*VVVFV::....
*V**.**VVIFFVVVFFMIIMIN$N$$$NNNMV**V:::***:*:.*VNIFIIMVVVVFIIVFVV*VV*****VVFFF***:..
*VV**..::**V*:***VIVVVMNVVMVVIV*****::::..:*::::*****FINMVVVIVII*VVF*VVVIVVVVFV*:...
:****....::::.***VVVFFVVVVVVVFMFFFV*::........::::.:*:*::*::**VVVVVVVVVV**:*::*:....
...::..........:::::*V:*VIVVVV*:::.......................:....*:***:****............
......................**VFV***:.....................................................
.......................:*:**........................................................""")
    
def page8():
    print("""\nYou run as fast as you can, hoping that once
the mother sees her baby is safe, she will not
pursue you.
You dart into a cavern. It's darker and hotter
than the pleasant spot where you found the fledgling. Is it the same passageway you came
through?
Still running, you look back over your shoulder
to see if the mother bird is following. At that
moment you find yourself falling, or rather rising,
toward the earth's surface—drawn up into what
must be the same shaft that forms the Bottomless
Crevasse!
Soon you stop rising and start falling. Then you
rise a shorter distance, stop, and begin to fall
again. You feel like a yo-yo, bouncing up and
down, up and down, until you finally come to rest
at the center of gravity, the point where you will
neither rise nor fall. Like a cork thrown in the
ocean, you seem doomed to drift forever.""")
    the_end()

def page9():
    print("""\n"Hurry!" you yell.
A moment later you see Dr. Sneed's reassuring
face on one side of the opening above you.
Larsen peers over the other side. "Don't worry,"
he calls.
"Hey, what's..." Dr. Sneed's voice is cut off as
he slides over the icy lip of the crevasse. You
watch with horror as his body hurtles by, down
into the abyss!
You yell at Larsen to get back from the edge.
But a blur whirls by, and you feel the rush of air as
his body plummets after Sneed's.
They're both gone, and now you are alone,
trapped on a narrow icy ledge. If only you had
warned them, you would have saved them and
probably yourself too.
Now your chances look slim. A search helicopter might fly over. But will it land? Will anyone
ever find you down here? Will you even survive
the arctic night?""")
    input("Press Enter to Continue: ")
    page12()

def page10():
    print("""\nYou stand there and watch as the strange creature walks slowly toward you. Then you see the
large, blue-white pieces of broken shell. This angel bird is only a fledgling, just hatched!
Losing your fear, you walk up and stroke the
creature gently. It cocks its head to the side and
touches you with one of its wings. At that moment
it seems almost human.
But suddenly you hear a loud whirring sound.
Hovering above you is another angel bird, a
much larger one. It must be the mother of the
fledgling. She swoops toward you.
""")
    choice = input("\nDo you run(1), grab the fledgling and try to use it to shield yourself(2), dive to the ground and shield your face with your arms(3): ")
    if choice == "1":
        page8()
    elif choice == "2":
        page14()
    else:
        page11()

def page11():
    print("""\nYou dive to the ground and shield your face
with your arms, hoping the angel bird will leave
you unharmed.
Nothing happens; the angel bird must have
taken her young one away. What's more, you
begin to have the feeling that you are completely
safe. Slowly you get to your feet. Standing
nearby are three more of the large creatures. One
of them effortlessly leaves the ground, glides
through the air, and lands beside you. You have a
strong urge to climb on its back.
Why is it you feel so safe? The angel birds
begin to make musical sounds, more beautiful
than anything you've ever heard. Is it this music
that causes your good feelings, or something
more? These creatures seem to communicate not
in words, or even ideas, but in feelings.
Without thinking more about it, you leap up,
and because there's very little gravity, you almost
float onto the creature's feathery back. You nestle
in. It feels like a bed of goose down, soft and silky""")
    input("Press Enter to Continue: ")
    page16()

def page12():
    print("""\n..........................::......................................................
.........:................**......................................................
.........*:...............**....:............:*..::...*V*..:......:...............
.........:.........:......:*....*::..........*...::.......:*.....*.....:..........
........:*:........::.....:V:...*::.....::..:*....:.:..::*VV*.:*:*V:...:**V:......
........:*:........::.:...:*:...:::..:..**...V:...V**IFV****V::**:*::..:V**.::....
........*::........::.....:**....:*..*:.**...*V:..*:VN$M*:..:**:.:*:*:::*:..::....
.......:*:*...:..*::*:....:*:....***.**.**...V*..:*:*FMV......*:::****:**::.::....
.......:***......*.:V:.....*:.:..:**.****:::***:..**:*:::::*VVMIV*:**::**::.......
..........:......VVVFV****:*:.::**::*IIV*IMMIIMF::V*:*******VIMNNNVVVIF**:::::....
.:......::*...:*I$NNNNNIINNMV*::VI*::*::.*VVF$NV:.VVIV*:VV*V*VV**VIFVV**VVV*:::...
.*:......:*.*I$$$$$MMN$MMMNNNMNNNI**.:*.:MIVV***:.*MNIMV*MMIVM*VMVV*:***:****:**:.
.**......::*N$$$N$NMIMNNMIMMNNM$$$N*..:.:::*V*:****VFMMM*MNNI*VMMFNV*:**:.:.:*::..
:**......:*MN$$$$N$$NNNM$MINNM$$$$NV*:**VVVVM*:**::VMM$$MN$$$NNMFFVV***::......:..
:*:::**..:VN$$$$NNN$NNNN$$NIMN$$$$MVV*FV*:..*:..*:*VN$$$MMN$$N$N$M**:**V..........
.**:::*:.*MMNMN$N$$N$$N$$$$$$$$F:VMF:**:*...:.:.V***$NMMMNNNMNNN$M:**:*:..........
.*:...:*.*MIMMM$$$$$$$$N$M$NIMN*:VIV***::::*:*V*FVVN$NMFMNMMMNMN$I.:*.::..........
.*:...::.VNNN$$$$$NNIVIVVIF*:IVV:*VV****VVFVVM$$$$MMFFVVMNMMMMMN$V**:.*V:.........
.*:......:M$N$$$$MVVVV**V*:*.*::*VNMFMNNN$NNNMMFVV**VVVVIIVMIMN$M*.:..**:.........
.*:.....:*M$$$III**VV**::**::VVIIN$NNNIINMIIIFVVV**VIIIMMMIFMM$N**.::.............
::*:::.:**FNMMI*::.**:...*VV*I$$$IIMIVVVMIIMV***VVFIFVVFVVIMMNN*.:.::.............
:V*:...*:.:*VMV*::*::*:*VIMNN$IVF*VMFV*VFVIVVVIMFIIVVVVMMNN$NV*::*:FVV............
.V:....***VVMI**:***IV*M$NNNNNF*:**NNIFV*VFIIIMFVVVVIIMNNNNF***:V:.**:............
:*:...:VM$MMMV:*:*IVVVV$MIMMMMMV::**FMMIIIVVIIMMNNNNNNNNMV*:**:.V*.::.............
.:*:.:FM$NN$NNFVVNIIIVMMIIFFIMMMI::**VIMMMIVVMNNNNMNNV**:**:*:..VV................
.:*:.VNNV*VINNFMNMIMMMMIFVVVVVVVII*::.:VMMMFFMNN$$VV*:***:..:*::*V******:.........
.:*:.F$I:.*MMMMMIIIIIIVVV*****VVVFIIV*::*FNN$$$$$N.**.::***..*:::*****:*..........
:*:..:I*.:MMIMMIVVFIVVVVV*****IVVVVIIIMIV**VMN$$$M.**:..:**..*.**.:*:.............
::V*..**.VMMIIIFIIVVVVVFIV***VVIF*VVFVVIMNMFMMN$$$:V:*:..**....::..::.:V*.........
::V*.:***MIIVVVVVV**FFFVFV:**VVVV*VVVVVVFIMNNN$$$NVV.*:..**..:.:::.....:..........
*.*:..V*VMIFVFVVVVV*FVVVF****VV****VVVVVVFVFIMNNMM$M*V::.::..:.::.................
:.*:..*:VMIFFVVVVV*VVVVVVF**:**:**VVVVV*V*VVVVIIMMNNNN*..:*.....:.................
..*...::*NMFFVVVFV*VVVVVVVV::::*VVVVV***VVV**VVVVFMMMNN*.::.....:.................
.........VNIFFVVV****VVVVVV*:::*V**VVVVV**VVVVVVV*IMNNNNV:........................
.........:FMIIV*::..**VVVVV*::::V*VVVVV*VVVVFVVVV**VVMN$NI*.......................
..........:V*:......::::*:......**:******::::::......:****:.......................
..................................................................................
..................................................................................
..................................................................................""")
    print("""\nYou look along the ledge. It curves up toward
the surface, but it also becomes narrower. You try
to gauge how close to the surface you could get
without losing your footing. By cutting a couple of
handholds in the ice with your pocket knife, you
could make it to the top, if you don't lose your
grip.""")
    choice = input("\nDo you decide to wait?: ")
    if choice == "yes" or choice == "Yes":
        page18()
    else:
        page20()

def page13():
    print("""\n"Get back from the edge!" you yell. "I didn't
fall, I was pulled in!"
For a few moments you hear nothing; then
Sneed yells, "Thanks for warning us. There may
be some force here we don't understand. But
don't worry, we're rigging a brace so we can pull
you up without getting too close."
A few minutes later you see a nylon climbing
rope dangling in front of you. You pull in enough
to tie around your waist and under your arms.
Taking a firm grip, you call up to the top, "I'm
ready—pull away!"
Your heart skips a beat as you're yanked off the
ledge. You dangle for a moment; then, slowly,
foot by foot, your friends pull you up over the
edge. You scramble across the ice into their arms.
"Thank goodness we got you!" says Larsen.
"The Bottomless Crevasse is a killer. I think we'd
better quit now."
"I agree. I've had enough," Sneed says.
After what you've been through, you're not
about to argue with them. The three of you pack
up and begin the long trek back across the glacier.
You're happy to be alive, but you know that
you'll always regret that you never reached the
Underground Kingdom.
""")
    the_end()

def page14():
    print("""\nYou lunge for the baby bird, hoping that you
can use it as a shield.
Even as you move, you feel a rush of wind as
the mother dives to protect her baby. You realize
that you've just made the stupidest decision of
your life.
Strangely, the mother bird did not harm you.
Instead, you feel that you have been put into a
trance. Stranger still, you sense that something
has set time back—that you are being given another chance!
""")
    input("Press Enter to Continue: ")
    page10()

def page15():
    print("""\nYou run from the angel bird—up a hill that gets
steeper and steeper. In the light gravity of the
underworld you can run faster than a deer, even
up this mountain. Twenty, thirty, forty feet at a
bound! You feel even lighter than you did before.
You try to leap only a few feet in the air, but you
find yourself floating. There is no way you can get
down. You are entombed between the ground
above and the ground below.
You close your eyes. Then, instead of feeling
warm, you feel cold; instead of feeling light, you
feel heavy. Instead of floating, you're lying on a
hard, cold surface. Opening your eyes, you see
ice walls rising above you.
Now you understand. When you fell into the
crevasse, you landed on this ledge, about thirty
feet below the surface. You must have hit your
head on the ice. What a strange dream you've
had! It seemed so real—as if the angel bird put
the dream in your head! But there are other
things to think of right now.
"HELP!" you shout
No one answers. Larsen and Sneed have probably given you up for lost
""")
    input("Press Enter to Continue: ")
    page12()

def page16():
    print("""\nThe angel bird glides through the canyons and
corridors beneath the earth. It increases its speed,
and you hold tight as it swoops through long,
curving passageways. It's the most exciting ride of
your life, and would certainly be the scariest if
you didn't feel that you've never been safer.
Then, ahead of you, is a tunnel that flares out
into a broad new world. An endless landscape
stretches before you. It is bathed in soft, reddish
light, as if the sun had just set everywhere around
you!
A great river forms a curving line that divides
the land. Trees line its banks. Farther back from
the river are mountains, some of them lavender
or blue and others that flicker like glowing embers. Strangely there is no horizon; instead the
landscape fades into dusky reds and browns that
curve over your head, forming a sky that is almost
the same color as the ground. Directly above you
is something that looks like the sun, but it is
absolutely black!
So this is the Underground Kingdom—strange,
vast, and very beautiful. What people or creatures
live here? What mysteries does it hold? But you
are swept from your daydreaming by the realization that your life here could be in danger.""")
    choice = input("\nDo you set out to explore the Underground Kingdom?: ")
    page17()
    if choice == "yes" or choice == "Yes":
        page19()
    else:
        page22()

def page17():
    print("""\n......:::::..........::::::::::::::::..:....**...:::::::...:::::...............
..::***:.......::::::::..:........:::::::::**V:......:::::::...:::.::..........
:***V*:::::::::**:............................:::.........:*:::...::::::.......
*:..:**.:*:***..:...::::::**::*:::::*::::::...........:::..:::**::..::::::*:...
....:**:******:.:**V*VVV*::*:...::::::...::::::::*:.....::::...::**:..::..:*VV*
.::***:.::**:.:::V**:...:::*::::::::::::::****::..::..::...::::...:V**.::::.***
***::........:::::::::::::...................:*****::.:**.....:::...:V*...:::..
::............:::::........:::::::::..............::**:..:::.....**:..::....:::
......:.....:::.......::::******:********:...........::*:...:::...***..:*:.....
....:::...::.....::**:................:......::::.......:**::.::*..::*:..:*....
..**.....:*...::::...........:::::::::V*:.......:::::.....::***::*:..**:..:*:..
:*:...:*:.::::.......:::::::::::......:***:VV........::*...::**::**:..*V:..:*::
:...:*:..:::........:*......::::::::.:.....:V:.::::::..:***:.:*::::*:.*MV...*::
...::..:::.......::::.:*********VV:***:::*::V***:..::::::::**:.**:::*V:***::.*:
..*:..::......:::.::::::.:::*::***:*........:**V::::....::::.:::*::*:**:.:**:::
::.........::::::::..::****:..:::**::::::::::::::::::*::....:::::...*:.:*:.::*V
:.:..:::::::::::..:*:::::..::....::.....::..::**::::::***:::..::**:..**::**..:V
:*******:::*:...:*:...::..:.:VIV********VVV*VVVV**:::....:*:::::**:::*V*****:**
*:***::..*...:**:....:*:*V*VVFMFIMIIMNMMIFFVIIMIMMV***::.:*:...:::**:::.**::VV*
.:F*:..:*...:::.....:*VFVVVVVVVIIMNMIFVVFMMMMNMIMN$$M*:*:.:*:..*:*::**::.***V*V
.**...::..*::.....:*VVVVVVVVMMNMIIFVVMNMMNN$$$$$$$MNMMMN$IVI*::::*..:**:..:VVVV
**...*::*:*.....:*VFFFFIMMNMIMMIIMMNNNNMMMVFIN$MFVMNINNNINIMI::**:::..:**:***V*
*..:*::*......:*VM$NNNN$NMMMNNMMNNNNMVVVMVVMMMMFMMMNM$NMNNIVVVVV:V***:.:*V*****
:*V*::**....:VFNVIMM$$$$$$N**M$$$$NNMNFVMNN$$N$NNN$$$IVIIMI*VV*VFV****..**:*VF*
***.::::..::VFIFVVV*VFFIMMV.*I$$NIFVMIFNMIMIM$$$$$$NIIFVIMFVVV*VMMM****V*:**V*:
V*.*:::.:*.*MV*VVVVVVVMNMV..:*N$$NIFIMMN$$$NVV**IN$NMFVVVIVINFVMVVM*:*V**VV***.
*.*:**::***VIIIIMMNNM$$F***:::*M$$$$$$$$NMN$$NMV*FMN$NMIIMNMM$$NMFIV:VV*VMVVVV*
:.***:.*:M$$$$$IVFVVMMMI**:*IVMIMVVVFMMFV*VMMN$$NMIN$$$NN$NIIFVVVIIFV:****VV*:.
.:**:..*VFINMV*::VMV::V*::*::*:***VMFV**VVFV*VVMIIFIIIMM$MIIFVVVVF$M*********:.
.*::..**MNMMMV..:*******:....***:VMF***V:*MFVIV*FI**VVFMIMV:VIVVIMM*:*******V:.
.*....*:VMMM***V**VV*.:::..VVVIMIMNI*:*V*VMI$$F*FV*VIIMNFNM***VMMVV**V***V**V:.
**...:V:IIIMNNMIMVVV**VV*:*FVVVIVI$M**V*MM$N$$$NNV*VNNIV*$$VVVMV*V**VV****VV**:
F:...:V*IIV*VVIVMIIVFVVVVV***FIVVN$MVFMI$$$$$$$$$MVVFMVV*MMIVFVMI***VVVVVVF**:.
V*....VVVVNNIFMIVFMV*F*VVIF****VIN$NVMMM$MNMMMMMMMMVMIVFINIVVVFNV:**FMV*VF***..
*...::****F*V****VNV*IV:VVVVFVVIVINMVMIMMVF***V*VVMMMIVII$$V*:**:*V***VFV*V*:..
*..::*:::VV**:VVV**FNNFVIIFIVVV*FMNIFMNMNNFNFMFMFMINMNMMM$MVVV*:**VVV**VV*:*:..
:.:*:....*NI****:..:*VI*:::***MMMNMMFM$M$$N$$$$$$$$NN$NNN$$$M*:**VMV:*V**VV**..
..........VMMMMV:*::..:...**VVVVMN$MMN$V$$$$$$$$$$$FM$$$$$$$$V**VF****V**VV:::.
:...::...:*VIVMF*VVV:::::::VVVV*:*MMN$$$$$$$$$NN$$$MN$$$$NIMI**VVV***VV******:.
.....::...::*VFFIIV*:*:IFV:.****:*M$$$$$$$$$NNNN$$$$$$$NN$$NM***V**V*:*VV**VV:.
*:....::..:::*V***VIIVVVVV****V*VF*M$$$$$NNNNNNN$$$$$$$$NNN$V****V**IF**VVVFV*:
:*:.....**:..::VVVVVVV**VVMMMINMNVM$$$$$NNNMN$NN$$$$$N$$$$NM*VVVVVV******VV*:V*
..:*:....:**..:VMV*I**V*V**VVIVMVVM$$$$$NNNNNNN$NN$$$MVVVV***VV*VVVVVV*VV******
....::::...**::::::*VVVVV*VVV*VMVVVI$$$$$$NMMIMNNN$$$$NV***VIV**VV**VFV**VV***V
:....:***::.:*VV*:..:*:VMFIVV*VVVI*I$$N$$$MMMMMMN$$$$$$NI*V:VV*VFV*VVV::**VV*VV
*::...VV*:**.:**:**:..::**VFIV*MVVI$$$$$NNN$NMMN$$$$$$$$$V*F*V**VV*::*V**VV**VV
**:::..**:..**:****V*****:V:*MVIIIM$$$$$$N$$$NN$$N$$$$$$$I*V*:*VVV:*V****VV*VI*
:*******V*:***V*.:*.:V:**:V:****MMN$$$$$$$$NNN$$$$$$$MI$$M**V***V*:*VV**V****VV
:****:***.:*.:V::**.******VIV.VMMM$$$$$$$$$$NFVMFIII**M$$$V*V**V**VVV*V**V*:*V*
***V*:*FVVVIV****.V*:V:*V*.MI:VMNN$$$$MFVV**V*V:**VV**I$$$N**V*****V***VVVV***F
V:*V***V*****:*:*:VV.***.**VMVI$NI$$$$V*****V**VV**VVVV$NN$V:VV****V****V**VVV*
:**VMF*V**:VFV:***:*:VF:.V*VIVVV$MM$$$NF*V*F*VVV**I***VF$$$M*VV*VV**V*VVVI**IF*
V*:VV**VMV*V.***I**F*:V:**.**V**VNN$$$$$***FVV:*FVMV*VVV$$$I*******VVV*V**V*VV*
V*:*:*:*V:**:***V.*V.**VV*.**N*:VM$$$$$$$I*****VVV***I*VVVVV***VVV**V*:*VV*VV*:
V*FVV**F*V*V***:****VV*I***.VV*:**M$$NMN$**V*VV**FIV****V*V***VV*****V**VV:*V*.
VI*:VV:FVV*V:*V*F*IIV****VV*F*:V*VVFNIM$V*V:**:**VV:***V**V**VVV*******VV**VV:.
IF*:****:V:VV*V*.:V*:VV*I*V*:*:VV***$N$M****VV***I*:**:V*V*V:*V*VV*V*:**:**VV::
*V::**VVVV*.VV*V.*:*:V***.*.*VV**V.V$NN*VV****V*:V:VV*VV**:*V*VV*VIMFV**VV**:*V
****:*****.*:***:V.**V.*V.*.***:****INM***:VI**V*V*I***V**V:*::*:VIVVV***V*****
M*V*V:*V****:I**VV*IIV:**:F:V.V****I*VV***M****V*V::*V:***V:*V:*VVI*VIVFVF***:*
*:VIFV**V*V::F:VMFIVVVV******:*VVV:**I**VIV**M*F**V::M*VV*VV:***VV*VFV**VV*::**
:*V**V.*F:*:VF**V:*:****V***VF:VV***V*V:MV:VVM***V***V:V******V*I*V:*V*:*F*****
::F*VF*F*:F***V***F**VV*V**:VV:*:*:FV*VFFVFV:V*.*F*:IVVV:*I*V*V**:*V*VVV**VV*::
**VV*VV**V*.*:V.V*FF:V*:VV***:V*.***V:***V:V.*:VVFI****I:.VVV*VV:*:*VIV:***VF*.
*::*:**V:*.*F:***:F*.***V*****V*:****VV**V:V:*:*VV**V**:*:*V*::**V**VV*:.:V**IV
:**.*VV.:*:V**VM****:**FV:V:V*:FV.*V*V.VV*VV*VV***:*V.V::VVF*:*:****::*****V:*F
**:**V:.V*VV*.MFV**FV:***FV*V**:*:V::*:*V.*VV**V*:**V*VF*V*V:**:**V***:***VV*::
***:*V.*VV**.:VV*VMVVV:**VI**VM:FIV*:V*VF:.**:.*V**M**V*IF**V::V*FIV**V*F**VFV*
V*:***V:*:*:.***.:V**I:*:*V::FFFV*:*V*II****:*.*:*.V**::***:***VVI**V**.:******
***:***.*:*.*:**:*:*VVVV***:**VFVV:FVV**.*II:***.**:**V::*.V*V::V*:.:**::*V*V*:
*::V::V*V**V*:*:VV:IV*MMI*:VVVFV::V*.:.*:****:IV::V***V***::*:*:.**:.:V*.:VV:V*
::V*:*V*VIV*V***IV*F*VVIVMVVV:::**V***::*V:.***:*:VF*VIV:*V.**.:*:*:**:V**:*V**
::V*:*F*VV*:I*V:**IV**VV*IF*:....::V****VV*.*MV:*V**:F:**:**:V*::**V**VV**V::::""")

def page18():
    print("""\nYou inch your way along the edge, keeping
your body flat against the wall of the crevasse.
You should be able to make it, as long as you
don't panic. You try not to look down.
After almost an hour of slow progress, you're
able to raise a hand over the rim. But you still
can't pull yourself up.
You hack away at the ice, gouging out another
handhold, then another foothold. It seems like
hours before you can take even one step higher.
Then, with one great effort, you heave yourself
over the edge, then twist and roll away from the
deadly opening.
Stiff and shaky, you manage to stand and stare
at the bleak world around you. The sun has set
behind the western mountains, and you begin to
shiver in the chill wind. You're thankful that in this
part of Greenland it never grows dark in July. But
it does grow cold—well below freezing—and
you're too exhausted to run and jump to warm
yourself.""")
    input("Press Enter to Continue: ")
    page21()

def page19():
    print("""\nYou know how you feel: the risks don't matter.
You want to explore the Underground Kingdom!
The angel bird seems to understand. Steeply
banking, it swoops down along the great river and
glides gently onto a mossy plain. Nearby is a
grove of tall trees. Short stumpy branches with
clusters of multicolored leaves thrust out from
their trunks. They look almost like hands holding
bunches of flowers.
You slide to the ground, and at once the angel
bird rises in the air. As it glides up into the dark
red sky, you feel a wave of happiness. You follow
its path with your eyes long after it has disappeared. Then, turning to survey the strange landscape, you wonder where you will go. What
dangers await you?
""")
    input("Press Enter to Continue: ")
    page40()

def page20():
    print("""\nYou decide not to risk the treacherous climb to
the surface. Surely help is on the way. You huddle
on the icy ledge, stamping your feet and clapping
your hands, trying to keep warm. You feel your
body temperature dropping. You've got to stay
awake until a search party arrives.
The hours pass slowly. The sun dips below the
horizon, but there is still light in the sky. Straining,
you think you hear something. . . .Pocka pocka
pocka pocka pocka . . . overhead. A chopper is
Hovering over the crevasse! For a moment you're
blinded by a searchlight. The chopper drops to
just a few yards above you. The crew lowers a
harness. Eagerly you grab it and buckle it around
you.
"HOLD ON. WE'RE PULLING YOU UP."
Beautiful words over the bullhorn. You're suddenly yanked into the air. Moments later a pair of
hands pulls you through the hatch. The pilot
pours you a cup of hot chocolate from his Thermos.
"Thanks for staying alive till we got here," he
says with a grin.
You soon feel life seeping back into your body.
"Thanks for pulling me out!"
"This is the one place in the world everyone
should stay away from," the pilot says.
"Nothing could get me back here," you say""")
    the_end()

def page21():
    print("""\nThere is no shelter from the relentless wind and
no sign of Larsen or Sneed. It's getting hard to
breathe. You soon begin to feel the dull aches,
stiffness, and sick feeling you've read about—the
dread symptoms of hypothermia; you are freezing to death. Maybe a search helicopter will arrive
any moment. Maybe in a few hours. Maybe
never.
You are very tired. You desperately need rest.""")
    choice = input("\nDo you huddle in your parka and try to conserve your strength?: ")
    if choice == "yes" or choice == "Yes":
        page32()
    else:
        page25()

def page22():
    print("""\nYour strongest desire now is to be home again.
You cling tightly to the angel bird. As if it knows
what you're thinking, it rises in the air, banks
steeply, and then, accelerating, hurtles into a corridor within the ground. You nestle into its thick
downy coat as it streaks through the darkness. All
the while you feel completely safe, and in time
you sleep.
When you awake, it is much colder. A chill
wind bites against your body. The brightness of
the world around you is not the warm red light of
the Underground Kingdom, but the cold white
light of the Arctic. The barren landscape,
pocketed with ice and snow, is a familiar scene, as
is the rude village of shacks and tin-roofed buildings nearby. You're in Greenland! The village is
the coastal settlement from which your party began its trek across the ice fields to the Bottomless
Crevasse.""")
    input("Press Enter to Continue: ")
    page23()

def page23():
    print("""\n............................:............................::::::...................
.......................::::*V............:...........::****:.:***:................
............::....:*****:***V*:.....::*VV*****::...:***:*:*..*:*****:.............
.....::*****FV*******V*..:*VV****VV*****.::***VVV****:.**V:*::**::*VV*:...........
*******VV***:***V::*V*V**VVIV:********::.:***********:*::V***:*:*::**:***::.......
:*VVV**::*V*VV**::**:*:*VV*IV::**V*****VV*****::*VV***V*:VV:*:V*:***V:.***V***::..
.::**VVV*VV:::.*:*:*:V*:*IIMI*VVVVVFVVMMVIIVV**IV**V*VV*:V**M*:IV:**VV***VIVVV*VV:
...:*V***.....:**::*V**:VFVIMMNINMNN$$NNMFMMNIMMVVVMNMV*VVVVN**VIV:VFMV***V***:::.
**V*:.::.::.**VV*VVFMMFVF$N$MN$MVM*VMMIMNV*VN$NMFVIVVVVV**VV**V******VVVFFVVVVVFF*
*****::FVMVVMMNN$MMMMMMFFMMNIIIVVVMN$NIN$M*VMNM*:.VII$$$$NNMMMIIFMIFVIIFIMIFIIFV:.
:***:VVV*********:****V*V***::::::::::**:::**VFV*:*VVFVVV*********VV*VFMMIIFFV*:..
................::*INMNMM:.................:VNMM*::::..****:::::*V***::::**VVV*::.
..............:*FNMFFVVVV*:...............:I$$$$M:....::::::::.......:***:........
........::*:..*VV*:.::*VMMFF*::...........:VM$$$F:................................
.....:*INNMV:::..:***V*::::...::....:::....*V$$$F:..:::::.........................
..:*IIV*:..............................:::**V$$$N*................................
:*:*******:::..................:::::::****::FIVVV:................................
:****::....................:**:::::::::::..*F**:::................................
.....................::...:.:.............:*V::*:.................................
................::::**::................:::**::**.................................
...............::....................:::*:*V*.**V:::*****:*****:::..:.............
......::::::.:......................:.....::::**:....:::..::::..:::::::*::........
..:::::.:::::..........................:VV*:::**::................................
........::::............................::::......................................
.........:::::.:::...................*V**:..::*:::................................
...........:::...::.................:**::..*V*::::................................
..................................*::::.:.:.:::...................................
................................:::::*...VVVVM*...................................
................................::V***..**V**:....................................
.............................::::::....::.::...:::::..............................
...........................::**:::....:****:........::.::.........................
........................*V*:.::.:....:V*:...................:.....................
........................:.............:...........................................""")
    print("""\nAs you trudge across the frozen slope to the
village, you think about the angel bird and the
Underground Kingdom, and you think how
much more there must be in the universe, and
even on our own planet, than we can ever imagine.""")
    the_end()

def page24():
    print("""\n"There's no chance of that," Professor
Bruckner's assistant tells you. "An aerial photograph taken a few weeks ago showed that the
glacier has moved, sealing the crevasse with
6,000 feet of solid ice."
You hang up the phone and stand by the window, thinking about the world that lies beneath
the earth's surface. What is it like? What creatures
might live there? What happened to Professor
Bruckner? Did he find Larsen and Sneed? Is Dr.
Vivaldi still alive? Now, of course, you'll never
know.
""")
    the_end()

def page25():
    print("""\nYou force yourself to keep walking. If you
wander too far from the crevasse, a search team
might miss you, so you walk in a large square:
fifty paces north . . . fifty east. . . fifty south . . .
fifty west . . . fifty north . . . again . . . again.
Your legs feel like lead. Your eyes are half shut.
You hardly notice when the weak arctic sun reappears ... the sun . . . you can't think . . . dizzy
. . . you can't stand. . . .
It seems like another world when you wake up
in a room with pale green walls and gleaming tile
floors. Your head is swimming. What happened
to Larsen and Sneed? You feel as if you've lived
through a nightmare.
"You're lucky, we were able to save your leg."
A tall, bearded doctor is speaking. "You'll be
OK." Then his voice trails off as he tells you that
your friends, Gunnar Larsen and Dr. Sneed, have
joined Dr. Vivaldi, all lost forever.
"Larsen . . . Sneed." You keep mumbling their
names until finally sleep comes.
By morning your head has cleared. It was a
terrible ordeal, but at least you survived. In a few
weeks you'll be home—home for good, because
nothing could ever persuade you to go near the
Bottomless Crevasse again!""")
    input("Press Enter to Continue: ")
    page26()

def page26():
    print("""\n....................:***:**:.............................
................:**VVVMV****V:...........................
...............:VF:..........VV:.........................
..............*MMM:..::***:..*MV:........................
..............VVMV:..:::*::..:MIV:.......................
..............VMV...::*::::::*NMV*.......................
.............:IVV..:*VVV**VVV:*NM*.......................
..............*VF::**VF*:IVV**:VM:.......................
..............*VV*:...:*:VV..:VM*........................
...............*MNM*VMN$$$$MFFF:.........................
................:*M$NVF$$$F*M$*..........................
.................:VMF*:*VV:*NNV::........................
...........::**VIN$NN$NMMNMNNMN$NMF**:...................
.........*M$NNN$$NNIF*V$N$$V:*I$$MMMMMI*.................
.......:F$$NMM$$NNNM*:*$$$$V:*M$$NNNMMMMV:...............
......:MNMNMMM$$MMNM**MN$MV**:IMMN$MNNNMIV:..............
......VNMMINNN$NMMNM:..I$M:..:IMMM$NN$$NMIV..............
.....*MMNMN$NN$$NNNI...I$N*..:FNMMM$N$$$NMI*.............
.....FNNMMMNN$$$NNNN:..I$NV..:FMMMM$$N$$NMMM:............
....*MMIIMMN$NM$$NNN*.:M$NF:.:MMIIN$$$$$NMMII*...........
...:MNMMMMMM$MM$NMIM*.:NNNI:.*MIIFM$NNN$NNMMIF:..........
...*NMMMMMMM$MNNMMMN*.*MNNF*.*MFVIMNN$N$$$NMNMM:.........
...VNMMMMMN$$NNNMMNNV.:NNNFV.VMIFFMNNN$$$$$NNNN*.........
...VMMMMMMM$$MMNMMNNF.:MMNFF:IMIFFM$$$$$$$$NNNNI:........
...VMMMIINN$$MMNNNNMI::NNNFM*MMIIN$$$$$$$$NMNNNIV........
...FNMMMMN$$$$MMNNMMM::MNMVM*MMMMN$$$$$$$$$$$N**M:.......
..:MMMMMFI$$$$MMN$NNN*.M$MVNINNNN$NNN$$$NN$$M::M$*.......
..*NMMMNMN$N$$$NNN$$N*.MMNFNM$NN$NNMNN$$$$$N*.*VV*:......
..*NMMIMMN$$$N$NN$$$$*:MNMVNMNN$$NMN$NN$$$N*...:::::::...
..*MMMMMMM$$$$$$NN$$$I*MNMFNNN$$NMNN$NN$$$M::..*:::*:*::.
..*NMIMNMMN$$$$NNMMN$MVI$NIN$$$$$NNN$$$$$$$V::::****:***.
..*NMMMMIMMN$$$$$NNN$NIM$$M$$$$NNMNN$$$$$$$$M*:**:::::**.
..*NMMMMFIMN$$$N$N$$$$$$$$$$$$$$$$$$N$$$$$$$V:*:*::**....
..:NMMIMMMMN$$$$NMN$$$$$$$$$$$$$$$$$$$$$NN$$*..***.::....
...VMNNNNMNN$$$NMIN$N$$$$$$$$$NNN$$$$$$N$$$N*............
....:*M$NNN$$$$NMIN$$$$$$$$$$$$$$$$$$$$$$$$N:............
.......*FVVM$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N:............
.......:***V*VVVVVVVVVV******VVVVVVVVVVVVVVV:............""")
    print("""Three months have passed. You return home
late one afternoon to find a man waiting at your
front door.
"I'm Professor Bruckner. From the National
Research Institute in Washington." He shakes
your hand warmly.
"Please come in. Are you still studying the
Bottomless Crevasse?"
Bruckner nods. "We've identified the force that
may have pulled Larsen and Sneed into the crevasse. Would you be willing to go back? Precautions would be taken so there would be no
chance of its happening again.\"""")
    input("Press Enter to Continue: ")
    page27()

#Ty Smart 
def buckners_theory():
    print("\tPROFESSOR")
    print("\tBRUCKNER'S")
    print("\tTHEORY")
    print("""\nThe discovery of the Bottomless Crevasse in
    Greenland by Dr. Nera Vivaldi supports my
    theory that the earth is not solid, as has been
    thought, but that it is hollow. The Bottomless
    Crevasse is probably the sole route from the
    earth's surface to a vast "Underground Kingdom." The only other possible link would be an
    underground river, flowing in alternating directions in response to the tides, but this seems
    unlikely.
    How, you may ask, was the earth hollowed
    out? My studies show that more than a billion
    years ago a tiny black hole collided with our
    planet and lodged in its center, pulling the
    whole molten core into an incredibly massive
    sphere only a few hundred meters across.
    If you were to stand on the inner surface of
    the earth, like a fly on the inner shell of an
    enormous pumpkin, you would see the black
    hole directly overhead, like a black sun.
    The gravity of the earth's thick shell would
    hold you to the inner shell of the earth, though
    you would weigh much less than you would on
    the outer surface because the mass of the
    Black Sun would tend to pull you toward it. If there were a very tall mountain in the Underground Kingdom and you were to climb to the
    top of it, you might be pulled up into the Black
    Sun because gravity gets stronger as you approach a massive object.
    In all other respects the Black Sun would
    not be dangerous to any creatures in the Underground Kingdom. On the contrary, the
    Black Sun would be necessary to life in the
    underworld, but in the opposite way that the
    sun is necessary to life on the earth's surface.
    Our sun gives us heat and keeps us from freezing. The Black Sun absorbs heat. If there is an
    underground kingdom, it is the Black Sun that
    keeps its inhabitants from being baked to
    death by the heat within the earth!""")

#Ty Smart 27-49
def page27():
    print("""\nYou shake your head. "I'm afraid not, Professor. I don't think I could go back to the place
where my friends died."
Smiling, the professor leans toward you.
"Would it change your mind if I told you that your
friends may still be alive?"
"What?"
"It's true. We received faint radio signals from a
point far beneath the earth's surface. I believe that
one or more of the others must be alive somewhere in the Underground Kingdom, and we
have the means to reach them. Now will you
come?"
""")
    choice = input("Do you want to go on the expedition? ")
    if choice == "yes" or choice == "Yes" or choice == "Y" or choice == "y":
         page28()
    else:
        page30()

def page28():
    print("""\nProfessor Bruckner, count me in!"
"Good," he says. "This time we'll be far better
equipped. NASA has put two helicopters at my
disposal. One of them will transport our party of
scientists and technicians. The other will carry the
Vertacraft, a rocket-propelled capsule specifically
designed for this mission."
""")
    input("Press enter to go to the next page ")
    page29()

def page29():
    print("""\nThree weeks later you find yourself staring
once again at the Bottomless Crevasse.
"It looks narrower than when I was here before," you remark.
"Yes," Bruckner says, "the glacier has been
advancing about three feet a year. It won't be
long before the crevasse is completely sealed."
While you and the other members of the party
stand at a safe distance, the professor cautiously
walks to the rim of the crevasse. In one hand he
holds an oblong instrument that emits an increasingly rapid clicking.
"Don't get too close!" you cry.
"Indeed." Bruckner takes a few steps back. "I
think I know what happened to Larsen, Sneed,
and Vivaldi."
"What?"
"Gravity waves coming from the center of the
earth have disrupted space-time enough to pull
them in." The professor looks down into your
puzzled face. "And you, as well," he adds. "I've
always suspected that the laws of physics may be
different in the vicinity of a black hole. Now we
have proof!"
"What does this mean?"
The professor smiles. "It means that the interior
of the earth—beginning about 800 miles deep—
is hollow.\"""")
    input("Press enter to go to page 75")
    page75()
 
def page30():
    print("""\n"No, thank you, Professor," you say. "I've seen
enough. I never want to get near the Bottomless
Crevasse again."
Bruckner shrugs. "I understand," he says as he
holds out his hand.
From then on, you follow the news eagerly,
hoping to hear some report on Professor Bruckner's expedition. One day, passing a newsstand,
you see a headline that makes your heart sink:
PROFESSOR AND PARTY MISSING IN
WORLD'S MOST DANGEROUS ICE FIELDS!
In the months that follow you hear nothing
further about the Bottomless Crevasse, until one
night, watching the news, you hear an interview
with two scientists who claim to have picked up
radio signals coming from inside the earth. "We
can't explain their seemingly impossible origin,"
one of them reports, "nor can we decipher the
message, except for two words, All Safe."
The next morning you call Professor
Bruckner's office at the National Research Institute. "I was wondering whether there were any
plans for another expedition to the Bottomless
Crevasse," you say.""")
    input("Press enter to turn to page 24")
    page24()

def page31Art():
    print("""\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX00K0KNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX000kkkkOOddxo;:dKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKd;..':dkkxc,...   .cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo..   ...,;.       .,;ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;.        .     'oKXd..xWMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOc           .cx0KNWK; 'oOXWMMMMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK0k;,ll'     .dK0kkKWK,    .,lONMMMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKOlxKXd,.    ':cdOXNx.        ;OWMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKXWKolxXNKo.     .':co,          ,0MMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKkKNNWWXKNMMO'  ..    ..           .xMMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOxO0NMMMMMMNx,',;,         .   ...,kWMMMMMMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKKXWMWWMMMMMN0d:'        .:c::loodkKWMMMMMMMMMMMMMMMMN
MMMMMMWNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0XXXMMMMMM0:. .   .';:coxxdxkkxxk0WMMMMMMMMMMMMMMMN
MMMMMMXxdk0NWMMMMMMMMMMMMMMMMMMMMMMMMWXKNNNMMMMMWx...',:cdO00koxK0K0OOxdd0WMMMMMMMMMMMMMMN
MMMMMMNkl:;lx0NMMMMMMMMMMMMMMMMMMMMWKk0NMMMNXK0OkoclxOKKkxXWXOdoocoO0OkxodKWMMMMMMMMMMMMMN
MMMMMMNXKxoc,':d0NWMMMMMMMMMMMMMMMMMXxxOkxdolloxOKkld0WMXdkWN0OkxdodO0kkocdXMMMMMMMMMMMMMN
MMMMMMNNKOOOkdc,':d0NWMMMMMMMMMWNX0kdlcccoxdllodOW0c:ldKWKOKXXXKXXNWWN0xoc;o0NWMMMMMMMMMMN
MMMMMMWNXKOk0O0Ool:;;oONWWNNK0OxdooooddlclK0lclcoXKdOXO0XXXK0OKXKNMMMMWKx:,'o0kxkKWMMMMMMN
MMMMMMNKKNNX0kOOO0Oo..'cdxxdolccdOxdcxXKxl0Wk:dkx0X0KXXKK00Odx0KKNMMWNNKx;..;OX0OKNMMMMMMN
MMMMMMWXKNKkkO000xc:;;:cloxOOl,oXWXl'cKWNOOXK00KXXK0XWNOxdk00XNKOdOWMWNXx;.'c0WWMMMMMMMMMN
MMMMMMNKO0K0KOxollldxO0KXNWMMKloOKNOdk0XXXKXNNXK0kxdkNMNNWXO0WKcclcxXMMXkdokNNKXWMMMMMMMMN
MMMMMMWXKKOKWOdO0XXNWWNKKWMMMMKxdx0XXXXK0kx0WW0kOO000KXkdkOo:kKlcd:;OMMMNKO0KKKKXWMMMMMMMN
MMMMMMNO0NXKNXKXWMMWKOkxONWWXXXXK0XK0OkkkkkKNMWKxcdX0lkk;:dl;;OXOxxkXMMMMWKxxkOOKNWMMMMMMN
MMMMMMN00KKOOKNXXNMMN00000KXKKK00OOKOO0KKxokNMWO;'ckKdckdckXOkKWXNWMMK0NMMW0l:odlxNMMMMMMN
MMMMMMWXXXXKKNNWXOKWMWXK0OOkkkxx0XXN00WMO,'l0NWWOol;o0dxXXKK0O000XNKXXxkNMMWX0X0;cXMMMMMMN
MMMMMMNKXNXKXNWMWko0WMMMKxkOOKKNNO0Xd:kWNkoc;,xN0kkx0NKOO00000XXNXxcdKXkOWMMMWWNkxNMMMMMMN
MMMMMMNNXK0O0XNNk'.oKNMMWNWWXkkOd''xKo:0MNxlloOWWX0KXKO0KNXXWKolodOd:dNXOKNNXXNWK0NMMMMMMN
MMMMMMWWK0KKXXXk, .xXKWMMMMMK;.;,co;d0ldNWXKNWX0OOKXWWN0dxklkXo;:lkOk0NNKKXXKXXWWNWMMMMMMN
MMMMMMWX00KKKXKl. ,kKO0WMMMMWk:oKNNxdKXkO0O0NMWNNKOOkx0d,c0x:lxxk0XXXKNNKKXXXKKNWMMMMMMMMN
MMMMMMWNK0OO0NK:..cKWNKXWMMMMNkdKWWWN0kkOXNNWMMMXl,dKoo0l,dKOkKK00OOO0XWNXXKXK0KNMMMMMMMMN
MMMMMMMMMWNK0KO:.,lKMMWKKWMMMMWWNK0NWNNWNkdxXMMMM0;lNKxXX0KK0KX00K00O0KNWXXXXX0O0XMMMMMMMN
MMMMMMMMMMMMWN0d::kWMMMWKXMMMMMMMWWWWKoo0x:oOKXWMW00NNKKXKOOOkOXXXXKKKKXWNXXX0OkkKWMMMMMMN
MMMMMMMMMMMMMMMWXXWMMMMMNKNMMMMMMMKdkl'lkko:odkNWNKKXKKKXXOOKOxKNXKXXX0OK0occd0XNWMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMXKNMMMMMMWdcollo0XK000KKK0KX0xdxKNMMWOkXK0OOxo;,'. .oNMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMXKWMMMMMMXxOWWWNWWkcxXN0dx00c'oKWMMMKdkOdlo;.......cKMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMWKXWMMMMMMWNX0OO0NXkxk0OkKWWx.'xXXX0Oolc,'........ '0MMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMNKNMWNXK0OkkOKXXNWW0xXMXxdOx,.:olc,,'........      cXMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMKKWN0xxOK00XNXXXNWNOxKK:':;.....             ..   .kMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNKXWX0KXXXXNNXXKOxkd;''.....         .. .....;;... :XMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXXXNNXXXK0xo;...  ......         .......':c;,,. .lNMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNXXK0000x;.        ..       ......:c;'..;cloxo;. .kMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNW0c''.      ..  ..,'.:ol;;cxko:,,::lkxc:;,,xWMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOxdl;.     .....'cl:oOxlld0Kd:;:;:ddlcclc:OMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKXkoc'..   .''',;dkokKOocxXXxc:;;oOdcc::;:OMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKNW0ddl:'.  .,;,;ckKOk0Ood0KKOdl:d0klc:::::OMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNKNMWXXKOc....,:;clkK0O00O0K00KKKO0XOl::::;:OMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWMMMMWNO:';loxkOKNWWWWNXNNNWMMMMWMNOdxkkOKWMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN00NWWMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMN
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
""")

def page32():
    print("""\nYou huddle in your parka, but the cruel wind
penetrates your body. You feel yourself growing
numb. You try to stand up, but your legs won't
move. You feel as if you are drifting through time
and space. Then you feel nothing at all.
The search and rescue team almost reached
you in time. They were never able to locate
Larsen and Sneed. A few days later a memorial
service was held for the brave people who lost
their lives exploring the Bottomless Crevasse. Everyone spoke very highly of you.
""")
    the_end()

def page33():
    print("""\n"All right," says Bruckner, "if no one will volunteer, I'll go alone." The rest of you help position
the Vertacraft over the crevasse and wish him well
as he snaps the hatch shut and releases the craft
into free-fall.
Hank Crouter, Bruckner's assistant, glances at
his watch. "If he survives, we'll get a signal back
within ten minutes," he says.
You all wait anxiously, watching the clock,
watching the crevasse. Ten minutes go by, fifteen,
twenty, twenty-five. A chilling wind bites through
your parka. You kick the icy ground.
"Thirty minutes," says Crouter. "There's no
way . . ."
Weary and sad, your party trudges back across
the ice fields. The moving glacier is rapidly closing
the crevasse. There won't be another chance.""")
    the_end()

def page34():
    print("""\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMWNNMMMWXXWMMMWNNMMMMMWNXNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0xkOkxxOKO0NNNWMWX0KNWNKKKXWWNNXXWMMWNXXXNWMWWMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kd:''''..';;cocoOkOKNWNXKKNX00KNWWNXKXNNNNNNXXXNMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKOoc:;;,,''.';,...'.:xxdOXNK00KNNNXKKKNNXK00KXXNWMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNKOxollcc::;;;'.  ..'',lclkKXK0O0XXXK000KKXXNNWMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXOd:........,oOxl;'...',;'':::oO00000KKXXXKKNWNNXXNWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWXXXXKKKK00d'..      ,OX0O0Oxoc;'''',..';:dO0000KXXX0000KXXXXNMM
MMMMMMMMMMMMWWNXXKKK0K00K0xxxodooxxxkxollc:;::o0KOOOkkkkkkdlc:;,'..',;oO0OO00000KKK0000XWM
MMMMMWXK0O0O00xOOdOxdOddKxoxdoxoxOoxKkldOdodoloxkkOOkOOOO000Okdc;...',;;:okO0000OOOOO00XWM
MMMMW0k0dokdkkoxdcdooxlcc;;:,;:;cc;:l::lclooxxxolxkddk0KKK00KKOOx:,'.,;'..;lxkOO0000KXXNWM
MMMWKxokxdkxkOO0000kdlllodO0XXXNXXXKKK0kxdl::ccoxxddddldk0K0Oxc;...';;,'....,dkO0KXXKKKXWM
MMWX0OKNNNWMMMMN0xoldOXWMMMMMMMMMMMWWWWMMMWN0kxoccdkdlclodxxl. ..,;;'';,... 'dOOO0KKXXXNWM
MMMMMMMMMMMMMXkoox0NMMMMMMMMMMWNXK0XXK0KXKXNWMMW0xddkOkxdoooolldkc.,;;ldc,.;kKXXXNNWMMMMWW
MMMMMMMMMMMXxoxKWMMMMMMMMMMMNKOO0dlool:lddkKKKXWMMNOdoOX0kOKK0kxxo,:ddxdxxoOWWNXK0Okdol::l
MMMMMMMMMNkcdXWMMMMMMMMMMMWKKKx;:clol;..:lcoxxk0XWMMW0llxOKXKXK0Okdoooool:cllcc:,;c::cldk0
MMMMMMMWOllOWMMMMMMMMMMMMNKOkc,,lO0Oxl::xOx;';oOOONMWXO0KXKK0Okxdc;;;,;:;,:olokkoo0kooxXMM
MMMMMWKocxNMMMMMMMMMMMMMWKX0;.,c:lkOkkxxOO0OxOocxO0WN0XNxc;;;;:lcccoo:dxc:lOxxxlclOxlcoKMM
MMMMNxcdKWMMMMMMMMMMMMMMXOkc.'':ccokKOodOxkO0Kk;lkxXW0K0,.d0xlkOlccoxclxlcok0OkkOO0KXXXNWM
MMW0c:OWMMMMMMMMMMMMMMMMKOO;::'lxc.l0KOxkkllxkO::OOKMX00l.xWKodOk0NKX0k0XNWNNWXXWWXXOxOxOW
MNx:oKMMMMNNMMMMMMMMMMMMK0Kl,:,:l,.lkdkOkk;;ddxcckkKMM00O';KWNKXNWWWWXKK0x0OxkodX0OXOdOOKW
0c:kNMMWXKkkXWMMMMMMMMMMN0kd'..,,'.lc.;lc:.;dl;;xO0WMMX0Ko'dWMKxdoodoocdxoO0kO00NWWMWWWWWW
:c0MMMW0o:dOOO000XWWWMMMMN0Kk,  ',';,.';;;;:c::dOOXMMMWK00;'OMKoloxOk0KKNNNNNXNXXNXNNXNKXW
dXMMNkc. ;0NXKOocd0Kkd0WMMNKOxo;. .,,...';::cdxxONMMMMMNO0x.cNWX0KKXNXXXNNXNXXNXXNXXNXNWMM
WMMKc    ;0NWWKdlo0Kc 'kNWWWXKK0xccl:,':lcokkx0NMMMMMMMMKO0c.kWWK000KKKKK0KKXXXXXKKK00KNWM
MMWd.     ..,:oO0KWNx'..,::l0WWXK0KKKOk0K00XWWMMMMMMMMMMW00O,;KMWKOOO0OOOOO0KK00K0KKK00XWM
MM0'          ,odx00o,.  .. .o0KXNWNNNNWWMMMMMMMMMMMMMMMMN0Kk,:0NXKXNNXXKXKXNXKKKKKKKKXXNW
MWo          .lOl,:xd;.  ..   ..;cxOKWMMMMMMMMMMMMMMMMMMMMX0X0oclllodddddddxkkOOOkkkO0000X
MNc           'dOxd0NNk;;'        .:d0WMMMMMMMMMMMMMMMMMMMMNKKK0kxdddxdooooooodddooollllok
MXc            .xWMMMMWNXl          .'lONMMMMMMMMMMMMMMWWWMMWXKXXOldOO0Oo::oollllxxlllllox
Wx.             ;OXWMMMNk;.            .;xXMMMMMMMMWNKOOOOkxc;:ll:.,lkXKl. '...  ';.     '
Xc              .':d00x:..                ,xNMMMNK0Oxl:;'..          :KNk' .'';:;,;;'.   '
Nl..               ;kxol:::'.               ,codc,'.                  ,O0, .;d00x;;;;'   ;
MKc.                ......'ckkdo;.       .                             .c' .;d00x:::;'   :
MMXo'.  ..                 .codk0Kkc.          .                        .. .,o00x::;..   ;
MMMNk;. ....  .    ...  .. ...';lxKNO;        ...  ..            ..        ';oOOd;:,.    '
MMMMWXx;.  ..  ..   .. .,,''....;clkNXd,.    ...   .o:        .'','.       ,ccoo:;:'.    .
MMMMMMMN0d;..   ..      ...'c:'..';ldxKX0o.    .;:. .       .'.....        .:ccccxl,.     
MMMMMMMMMMXkdl;..''':cc;.  ,c::'...:c;cxOOxc:;'.cOo.       ..'.. ..'.      .,::c:lc'.    ,
MMMMMMMMMMK0K0K0dokXWXxlxx:'...':,.'::::,,lxkOx' ..       .. ...;oO0l.     .,:lo:''.    .l
MMMMMMMMMMN0K0KWMNKKNNxo0MW0l. .'',..';:;.'cc;:'          .  .:xKX0x:       ';oo'...   .cO
MMMMMMMMMMMX0KKKWMWNKXNWMMMMW0c..';. ..,,:dOkdxdo:.         ;ONNXkokd.     .;cd;...    ;kX
MMMMMMMMMMMMNKKKKWMMWNKXWMMWKO0Oc..  ....;oxxxxx0N0o.    .,:oxxxkkxOx.    .;:ol....   ,dKW
MMMMMMMMMMMMMNKKKKNMMMWKKNMNo,xWWO:.   .''....;lco0NKo,:k0kodolxXWXX0'   .;coo. ..   'd0NM
MMMMMMMMMMMMMMNKKX0XWMMMNKKNNXNMMMWOc...,.....,,. .:dOKXX0l:odkNMMWMNc    'cl,      'd0NMM
MMMMMMMMMMMMMMMWKKX0KWMMMWXKXWMMMMMMWKo;.            ;OKkoclOKXNMMMMWk.    ..      ,d0NMMM
MMMMMMMMMMMMMMMMWX0XKKNMMMMWXKNMMMKxxXWN0dl::;:cl,...,lddkOKWMMMMMMMWKo.         .;d0WMMMM
MMMMMMMMMMMMMMMMMMX0KK0XWMMMMNKKNMNkkXWMMWXKXWWMWo..;loONMMMMMMMMMMMMN0l.       'lkXWMMMMM
MMMMMMMMMMMMMMMMMMMNKKXKKNMMMMWX0XWMMMMMMWx:xNWMWx';xKWMMMMMMMMMMMMMMMWXkc..  .lOKNMMMMMMM
MMMMMMMMMMMMMMMMMMMMWXKXXK0OOOOOkdxKWMMMMMNXNWN0kk0NMMMMMMMMMMMMMMMMMMMMNX0kxkKNWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWXKKOkxxxxxxxxxkKNWWN0kkkOKWMMMMMMMMMMMMMMMMMMMMMMMMNNWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWNXXXXKXXXXX0kkkkkkk0XNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
""")

def page35():
    print("""\nYou know that your chances of surviving the
expedition are slim. Even if you safely descend
into the Bottomless Crevasse, there's no assurance
that the Vertacraft will be able to get you out
again. Still, it's your only chance to find your lost
friends and to explore a new world.
You grit your teeth and climb aboard. The
professor climbs in beside you.
"Ready?" he says. "I'm going to activate us as
soon as we're centered."
"Ready." You strap yourself in and say a
prayer. You feel like a larva inside a cocoon.
Looking through the port, you watch the others position the Vertacraft over the crevasse. You
wave at them, and they wave back. Suddenly you
are falling—faster and faster, plummeting toward
the center of the earth. Has the Vertacraft gone
out of control?
"Professor Bruckner!" you yell. "Won't the
rockets work? Can't you slow us?"
"We're saving our fuel," he shouts. "Gravity
will slow us—you'll see."
Has he gone mad? You notice a red button on
the control panel. Next to it is a sign that reads:
EMERGENCY
REVERSE/RETURN TO INITIAL POSITION.""")
    input("Press enter to turn to page 37")
    page37()

def page36():
    print("""\nYou and Dr. Vivaldi cross the Great River and
start your trek to the Shining Mountains. Along
the way your guide, Mopur, brings back mountain game, breadbush, and tanga.
The air seems lighter and brighter than in the
valley of the Great River. Never have you felt so
happy as you do right now—hiking through the
Shining Mountains.
But your Archpod guide grumbles and frets.
He blinks and rubs his eyes.
""")
    input("Press enter to turn to page 92")
       
def page37():
    print("""\nThanks to the dual control system, it looks as if
you have a chance to escape this madness. Still,
you can't be sure it will save you. . . .""")
    choice = input("Do you want to push the Emergency-Reverse button?")
    if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y":
        page89()
    else:
        page38()

def page38():
    print("""\n"We're going too fast! Can't we slow down?"
you call.
"No. We have hundreds of miles to go. We've
got to get through the earth's mantle fast, or we'll
be baked to death." Bruckner's voice is cool and
reassuring. Maybe he knows what he's doing.
But every minute, the temperature rises. You
begin to sweat. Whatever made you think you
could survive such a trip? Sipping cold lemonade
from a plastic bottle, you try to close your eyes
and relax. Then it seems as if the Vertacraft is
slowing, but you can't be sure.
Suddenly everything is still. The Vertacraft has
come to rest. Looking through a porthole, you
see that you have landed inside a large crater.
Slowly you climb out of the Vertacraft and open
the other compartment. Professor Bruckner's face
is ashen gray. You feel for his pulse. Nothing. The
strain of the descent must have been too much
for his heart.
""")
    input("Press enter to turn to page 43")
    page43()

def page39():
    print("""\nYou could probably climb a nearby tree and
hide among the clusters of giant leaves. But is it
wise to run like a frightened animal? Maybe
things will go better for you if you bravely face the
inhabitants of this world.""")
    choice = input("Do you want to face the creatures?")
    if choice == "yes" or choice == "y" or choice == "Yes" or choice == "Y":
        page42()
    else:
        page46()

def page40():
    print("""\nThe scene around you reminds you of a photographic negative. All the shades and colors seem
reversed. The ground is grayish pink clay with
white outcroppings. In the distance you can see
areas that glow like beds of hot coals. Nearby is a
forest of trees with green trunks and white leaves.
The trees are short; yet their branches, taking
advantage of the light gravity, spread out for hundreds of feet in all directions.
You climb a small hill to get a better view.
Wherever you look, the land curves upward, as if
you were standing in the bottom of an enormous
bowl. The sky is covered with what looks like
reddish yellow clouds.
Most amazing of all is the sight directly overhead—a disc almost the size of the sun; but,
instead of shining brightly, it is absolutely black.
You can feel its coolness, as if it were drawing
heat from your skin. It's the black hole at the
center of the earth!
You turn sharply at the sound of chattering.
Coming up the ravine are more than a dozen
creatures, smaller than you, yet walking upright
on two legs. Half human, half ape, they look like
creatures that might have once lived on the
earth's surface. They are carrying ropes and nets.""")
    input("Press enter to turn to page 39")
    page39()
    
def page41():
    print("""\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMNXKKKKKXNNWMWMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWN0xl::::lloxddxkO0NWNK0Okddddk0KKKKK00XNWMMMMMMMMMMWWWWMMMMMMMMMMMWNNWMMMMMMMMM
MMMMMMMMMMMMMMXkdox0x;;,';:cllddolc:;;,'.,;cllc;;lxXMMMMMMMMW0xxkXWMMMWWMMWXkkKNWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWXK0xdc;c:;;clccc;;,''';cc:;'';cxXNKxxOkc,',ldlodooooollxXWWWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMOoddodxl;,::;,''..;lxkxo, .,,'....',;,','..',;'..':cldx0WMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWMWWN0o'..','.,ccdOXMMWKkkxdc..,,,;:cccclok00OOdlldOKNWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWNXNXOo;'':l:',cd0WMMMMMMMMMMMMNKXXK0KKXNWWWMMMMMMMMMMMMMMMMMMMMMM
MMMMWNNMWNOdodk0K00kdx0Xx:;:;...:dxooxKWMMMMMMMMMWWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MWKdc,cdo:,'';:;;,,,.';:;'',,.':lldONMMMMMMMNKOo:,',;cd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MWO:'.....,'',:;,;;,'.,;c;',;;';dKN0kkxddool,.         .:odkOO0XWMMMMMMMMMMWNXK0Oxdxdolool
MMMNKk;.,,.',clodO0Od;.';;,';,,d0k:',;;''.                 .':o0WMMMMMMMMMNOl;'.. ....',,'
MMW0dlok0ocxKWWMMMMMWOdx:.'.''.,,,''',;,'.                 .,dXMMMMMMMMMMMMWNKOl'..cdoccld
oo:'c0WWNNWMMMMMMMMMMMMNxc:,;;..',,'..ck0c              .....:ooodoclodkxdxxxdl'...,okkkOK
'''';:lc;:oOKKK00OO0NWNNWMWKOl...'';okXMWx.             .''...,'','...''....'. ..';. .,:,,
;;,,'.''....',,'...;cc,,oOxlc;..';:xXMMMMNo.             ;xd,....''. .''''..,:oO0KKd'..;:;
',''.':;;cxxkOOOkxl,.   ..';:cloodkOOxxkxkkl,'.       .,oxdoooo;,c:'.,::;,..,:lool::;'.,cc
odkkdOXNNWMMMMWKdlccc,.. ...','.',',,,,'',cd0XKko:'':lllclddoc',:;';ok0x:...;,',,;;cc;,;::
MMMMMMMMMMMWKxlcccll:;::.........,;;:kXXXNWMMMWXxc.';,..'cc'......''.,:,'...;,',;;:ccc;;;:
Okxkkxk0KKkc,:cll::clx0kc,:ldl'..;cllxOXWNOxdol,.'..'''',,;,.'','.,,.,:;,...;,.,,';ccc:;:;
;'..''',;,. .::;:ccoO00kdlcc:,'. .....;d0xc;.....'..'',;,,;;,,,;;,',,,;;'...,,.'..'cccc;;;
:;,,,;;;;,..',..';,'.'.... ..':;'cc,:::,co:;;,,'......';;,,,;;;;;;.';,;;,....;;;l;.';:;,co
c:;;;;,;;;,....',';o:':;.. .oxOK0XK0NWXkdc',cccclol::,..',,,,,;;:;..,;,,,....;ldo:,';ooo0W
c;,,,';;,,,,;:dkloKWX0XKlck0Xxokk0X0oc;''''.  .,ldo:;...''''',,;;;,..,;::,..   ..';cxkolc:
xxxdolkKOOkKKONMNNMMWWWMkl0Kk:'..':,. ..',;.........'...;:c;:dxdl;,...:odo:'.... .''''.''.
oxK0kkKNXNKKWNWMMMWXXWMXo'''..  .',....''','........'..'cxkkkxOXN0d;.  .....'... .,'',....
..;:d0NXdOXXNWWMMMNOdOWXkoc;.    .,'. .',,,........,,..;::,'',;lolooc'......'.....':cll,.'
.','.'co,.co::coKMKdccok0KOdc:,. ..,'...;ll:llloc;;oxcoXNKk:;lllc;clc:;;:;........':lddc,.
'';;'..'. ';....:oc;''. ..,l0NXOd:,:,',. ......',',;,.'::,...;ooc:clodxkX0dc;,;,..::,''...
'',,...'. ....  ...''..   .'';oKWNXN0kKKkxollldxOKXNk:oOOd'.....,;ckXN0kKOONK0NXllXNk::::;
c;,'..'....cdcc;';loo:';:;coc;dKWMMMMXXWMMWWWMKoxXXOl,:lc;........,:;;;,;;xKkkxc,lOOkx0XNN
WKoddd0dlxlc0K0KOKNXNXkdkdd0KKXK0NMMMXkKWWXOxdl'';,.'..,c;..';:;,,':;......,'.. .;:c:,:x0N
XXk0kkNXXKdcxXK0XKK0OX0doollkKNNOONMNN0oll;.  ...,;:,..,:,.'clc;'.,;;'...,c::kOoxXKNNOONWM
XOx0oldool,.,oxlldoxkdk0Odxxx00kocdXXOKOokx;:ol''kN0ocdOx:,dx:lx:;lxolxOkONNNXKKNXOXWNWMMM
k:;:..,;:ldo:'''....',,:dkO0OkO0d;':c,;dococokd'.lOOk0KOxxOOdkK0dOWWKXMWNWWNN0ONMKkXMMMMMM
'.';;:d0OxKWXOxxxxkd::;..';:c;'cdd:.    .';:clolcdooOXNKxol;:llcdNMX0NWK0WNKKkOWWKKNXNMMMM
:coddxOxocxX00K0kOKK00xo;''... .... .';;;:cdkx0KOxllkKKXXOdl;...;kOlldocxXKKOoONO0WKkXMMMM
xxdodOklcxOxookOdxkdo0Kxlc;.    ..',;cclddollckNNK0K0xxdOKOd;..  ...''..;ccl:lK0d0NkxXMMMM
kkkddolokOxdkdd0c....''..  .    ;lllodkkkdllx0XN00Oxkx00oc'.';colcokkl,,;,...,c;c0KodNMMMM
KOdlcoxdllddko;:'   ';;;,'..   ..,cox00OOkookK0xxKxcddodc..,llcxOdok00Oddoc:::,.':;.;kXWMM
xddxOOocoo:'....,;cdOXKOkxO0dc;'..  .;ccodxOxlcoK0c';:. ..,cccoxkkllxxk00Okdddolllc;'';dKW
xkOkd:;:,.  .:dolclookxlkOkOOOOxl:;,'.....;;...;:'.  ...,:ldookxOXkclxkOOxOKKOdllldkOdc:ox
cc,..... ..';loc:cldokOoxOxc;cxKkl:::,.        .',,:cokOOOkxocx0XN0o:dOkkxoOX0000OxdOOkdll
..  ...,:clodxdlcoxdd0XkddkOl:;cl;..    ..,;ldoooolcoxxdk0kocdkOX0OxcdK0ddOO0OkkO0kxkxxxkk
,,;,:llcllllldlcddolokkxl:lc,..  ....,:cccokkxdlclddlcok0xccdkddkOdoxOkkOxk0OO000kkxkkkxOX
;,,;cc:;::;:clcol,.....'.    .':llllloxddxxdlcldkOkooxxdxocokxkkdxc,ld:;oxlck0kdllloddodO0
......... .......           .;oocoxdokkololodxxddc;:c:,cl::ol;:,..   ....'...:l'   ..,;:oo
',,;::;''... ....            .   .'..,,'''.....       ......    ..,:;';do;'..'.';:,.    .'
ddoodddddl,''';cc:::,'.',:cc:,,,.','............,,;:;lkocc,..;codxxxkxxxdolx0xoOXOdodc;;;:
KOxooxxollodxxxdolcc;',:lxO0klllokkc,,,,cldkoc;;c:ldlodO0kdccxOkkkOxdoddk00K0xk0Oxx0kx0O0X
occ:codxkO0KK0d:;::;,;clxOOOxdoxxl,  .,ckK0XkollkKkdkkdodd;..;:;:;;coocldkkOkdx0klckkk0OXM
0Okxl:lc,,dxdxd:;:;,;:lkXNX0KNOl,..''l00xOXNKOkkkOKK0Oc..'.     ...,odllxl',,...'..',;,,dN
OOOkodOxdkKXxoOOdol:;;okxc,'oOl::ld0XK0kdlokdloollolcc;.  .....'cdddo:,,:ldxdl::dxc::;:o0W
kXKOkkO0koddlldkxkkxkxdxxl:.';,,cc,;llodc.......''...  .,cc;;cdooOd:o0OxOKkl,'';:ccldl:ckN
Okxkkxodxdo;;:lddoodx000xoxc. .''..........''...,.  ..:ddO0Okxl'.....;;;o0x;.,c;;ccoOklo0N
..':;'...''...',,.',,clllccc,..ldodxoc;,...';,'.   ;dxKX0OkOx:,::,,:looox00OkkddOOocokkOKW
;;:clooxolc;;,''..''.;coxxdddolxKOdlododxxc',::' .cdk00K0OKN0ooOXKOKNNKkxO0Oxxxdl;....':kN
X0kkKNNWKKOO0xoc',:cldkkkl;','.':looxkkxxkocdOkd,.',;::dllOOd:lKNX0KK00kkOkdoc;,''''..:kNM
OXXXWWXX0kkKN0Oxo::dkKXOkd::c:::;colo00xd:'...''... ....  .''';dxdcoxc:;:;,..;;..''''.,o0N
O000KKkk0kOKKkdc'..l00k0K00K00xl:c::oxd:,..........,lc;;;;',:. .''.':l:;coooc:'..,:cc:okOK
,.'cxdlxOxxkxl:lolcllc:llcccc:'... .,.'. ...,,,,:lkK0OkK0xodxolokkoxKK0kldXWKdlcc:'',cx0XW
 .;oddddkkkOxxxdOOOKOocc:,....,. ',........'lxdddx0kxdoO0xdxodOOxlcdxkXN0OKWNOkKXxclodxddK
xOKKOk0K0O0NKOc':cccoxkdoo;....,cc,.;::cc,'lOKK0Oxl'....:x0Oxdo;......,dxd0X0dlxK0xook0ooO
KXOk0XNWXOO0k;     ,xkkkoc;','..;:'..,;,,';x0OOOOko:c:,;:lOKOdo:.',,;loxdlk0kcdKOxxo::::ld
XNKx0OkOOkOx:.     .oxl:'.  .......;c'..  .:ooooldkkdxxooook0kkxdddO00KKxoOX0llkko;,....,:
OOxdxo:ll:,.   ...                ....      ...'',oo'.,''clodookdlx0Occc'.;:,'..,,',:odokX
,......        .'.                                   ......''.... .c;...........'..',::lON
,...                      .   ..     ..      ...   ...'.  .lc..':ccc;,,....,;,''';,,,,:oOX
olc,.    ...         ..             ..,,;:clc:oxxddkxkkd:..,cc::;cox000kkkkkxdoodxdoloxdox
llc,.       .             ..       .,ok0XNWNKO000O0KKKKXX0kdlokOdllokKNWWWWWNXXXXNNXKK000K
oclo,      .,'.'..',,'';;;;:codxkkdlc:::coo:,':dO0XWWMMMMWNNKO0KK00Oxdk0XXXXXNMMMMMWWWWWWM
c,;;,,;cllolclddodxdookXNKXNNNWWWWK00kkkkO0xc,,:ldxdxKWWWWMMWWMMMMMMWXKKXNWWWWWWWWNXNNNXXN
kkO000KKXXK0kkkddkKKNWMMMMMMMMMMMMMMWKKXKKOdolclxxoc;;odkKNWWMMMMMMMMMMMMMMMMMWWWWWWWWWWWM
xdx0KKKXNXXWMWWNWWMMMMMMMMMMMMMMMMMMWWNNNKOOKXNWWWWNK0kxxxxxO0XNNWWMMMMMMMMMMMMMMMMMMMMMMM
dlcodxxkxk0XMMMMMMMMMMMMMMMMMMMMMMMWWMWWWMWWMMWNWWWWNNNNXXXXNXKK000KKXNWMMMMMMMMMMMMMMMMMM
WNXNNNWNXXKKKXXXXK000XXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWMMMMMMMMMMMMMMMMMM
MMMWMMMMWWWWNNXKK0kkOKKKKKKKKKKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWWMMWWNXK0OkkkO0KXXXXXNNWWNNWWMWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWWMWWWWNNNNNNXKOOkOkdoxKNWNNWWMMMWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKXNNNXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")
    
def page42():
    print("""\nYou step forward to meet the strange procession. The underworld creatures form a circle
around you, cackling and gesturing to each other.
You smile and hold out your arms. "Hello,"
you begin, but the creatures raise their nets and
close in on you. One of them barks an order.
They motion for you to follow them. You don't
have much choice. Despite their small size, they
move rapidly through the thick woods. Occasionally they freeze, and you hear them whispering,
"Kota, ib saben Kota."
You march a mile or so through groves of trees.
It's as hot as you've ever known it, and you feel as
if you're going to faint, but finally you reach open
land. Instantly you feel cooler. The Black Sun is
drawing heat from your body.
Soon you reach a village of igloo-shaped structures that look as if they're made of green clay.
One of your captors leads you to the nearest one.
"Ib agon," he says as he takes you inside.""")
    input("Press enter to turn to page 44")
    page44()

def page43():
    print("""\nYou bury the professor's body near the Vertacraft, and say a prayer. You feel sad and afraid
of setting forth alone in a strange world. But there
is no choice. You must search for food and shelter.
First, you've got to get out of this crater. There
is a tunnel nearby. Peering inside, you see that it
leads straight down. Suddenly you realize that it
was through this tunnel that the Vertacraft traveled; you're looking through the other end of the
Bottomless Crevasse. The tunnel doesn't lead
straight down, but straight up—to the surface of
the earth!
So Professor Bruckner was right. The earth is
like a hollowed-out pumpkin, and you're standing on its inner shell. Your feet must be held to
the ground by the gravity of the shell itself.
You look around at the walls of the crater. They
are too steep to climb. But you feel so light—as if
you were walking on the moon—you might be
able to jump out.
You stand there a minute, wondering why the
pull of gravity here isn't as strong as it is on the
earth's surface. Then you remember the rest of
Bruckner's theory: There is a black hole at the
center of the earth, pulling you toward it. You
leap as high as you can—twenty feet in the air!
Then, with one great bound, you're out, standing
on the surface of the Underground Kingdom.""")
    input("Press enter to turn to page 40")
    page40

def page44():
    print("""\nThe interior of the agon, as it seems to be
called, is lit by glowing stones circling the inner
wall. In the center is a small fountain. Clear water
bubbles forth and flows along a silver trough
before disappearing underground. The floor is
soft and spongy, like a thick bed of moss.
The leader steps forward. "Ket," he says,
pointing to himself. "Ket Raka." Pointing to the
others, he says, "Akim Raka, Tor Raka ..."
You repeat each name, then pointing to yourself, tell them your name. The Rakas laugh as
they try to pronounce the strange sound.
Tor, who seems younger than the others, brings
you something that looks like cheese but tastes
like honey. Ket gives you a small pink fruit. "Ib
tanga," he says, smiling.
Tanga is delicious, and you are eating a second
one when a large blue-furred Raka rushes into
the agon. Pointing at you, he speaks excitedly in
his own tongue. Tor begins to argue with him.
The others join in.
"Nar mg calla!" the blue-furred Raka says
loudly. It's clear he wants you to come with him; it
seems likely that he represents the chief, or
leader.
Ket and Akim gesture as if you should obey.
But Tor shakes his head, warning you not to go.""")
    choice = input("Do you want to follow the blue furred Raka?")
    if choice == "yes" or choice == "y" or choice == "Yes" or choice == "Y":
        page48()
    else:
        page50()

def page45():
    print("""\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK00KNWNNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNWNNXXXXXXNWMMMMMMMWK0XXKK0Oxc::okk0XXKKXNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWNNNNXXK0Okd:::::;'..':l0MMMMNKOx;.,odoldOOOxok0KXNNKOOXNWNXXKXWM
MMMMMMMMMMMMMWNNNNNNNNNXNXKXXK0Okxdc,.. .,loooldxOWNXXX0l:,...,:cc::ododOKKKXXNNNNXK0xldOO
MMMMMMMMMWNKKXXNNNXXNKK0OOkkxl::;::,,..  .:odoloococcc:l:'..',..;oo;.';:lk00OOOO0NMWNX00Ok
MMMMMMMWNK00XWNXX0OOxlol;,',,,;cllccc;.........,c:'  . ..,;'',::',okxd:';ok0XWN0kk0NMMWWNN
MMMMMWXK0O0NWWWNNXXXK00Odolcclk0koc;;:ll::;'',;cll;.....',,'cddodoldxKKxdxkxxOXWNK0KNNWMMM
MMWKOOO000NMMMWMMNKKWMMNKkdddx00xllxkdx00kl:ccoooc,'','.';ccoO00KK000KNWNXKOxldKWNK0OkxKWM
KXXKKXWWWMMMMWNNX00XNKOxddollx00kO00xkKX0kxdllodoc;:cdOxllodk0xxKNKkOOkKMWXK0xdx0XXKK0kkXM
XXWMMMMMMWWNNXXKXWMXxoxkdddk000XXX0OKXXKKKKdlodxkdxxldXNNNX0KWKxx0NX0kdkNWX0KK0OO0XNNWWNNM
MMMMMMWN0ookKXNWMMWKOOxodO0KXXNWWNWWNXXO0N0xolxKXKXOoxXMMNXKKWKkxdONWKkk0WMKkOXXKNWWNXXNWM
MMMMMNXX0olkNWMWNWMMN0kk000NWMMMMWNNNNK0K0OOkkONMMW0dd0WMNKKX00XKxdkXN0kkKMWOdOWMWXK0XWNX0
MMMWWWWNXKXWMMWNNWMNKO0XKKNMMMMMWNNWMWNX00XXXWKXMMW0ooOWMWKKKxkXN0xxxKWKO0XWNOk0WNOdkXWW0x
MMMMWNXXWMMWNXWWNX0OXWWMWWMMMMMWKXWMMMWXOKWWX0OKMWX0xlxXMMNNNXNWNX0xdOWN0OXWMXkxOXXkxOXWXk
MMMNK0XWWNXXXNNOxk0XWMMMMMMMMWNXNMMMMMNX0XMN0kkKWMKOO0OXMMWNWWWMWWN0xkKNOdxXMN0xxOXXkO00NX
MMXKXWMWKOKNW0xkXWWMMMMMMMMNKKXWMMMMMWX0KWWXKNXOKWNOOXXXWMWWN0KWWWNX0kKWXOkKWNKOxk0NNXKxkN
MNKNWKO0KNMWKOKWMMMMMMMMMMXOOXWMMMWWMNkxXNKKWMNOOWMKONXO0KNWWxdXKxk0NXXWWXKNMWXOxx0KNWNkx0
MWWNXko0WMMWNNWMWWWMMMMWX0kkXMMMMWXXWKkKWKOKWNXO0WMX0NX0KNNXOooKX0KKNNKKKO0XWMWNKO00OKXKdd
MMWN0OXWMMNK0OXWXNWMWNKKOxkKWMMMMXKXKO0WWNNW0xx0XWMX0XWKKWMNKdoKWNWXXWNXxclxKMMNKOO00XNNko
MNKO0WMMWNKOOKNXNMMMWXNN0OXWMMMMWX0OO0XWNWMWOlo0WMMXOKWXOXMMMKkXXx0WWMMMKxddONWX00OXXXWW0d
NOkXWMMNK0OKKOkKWMMNNMMXOXMMWMMW00X00KNNKNMWOooONWMWNNWNXNMMMWNWN0XWNWWMW0xdk0KXXKKNXKNMXk
KXWMMMW0xxkXK0XWMWWK0NWNWMWXNMXkox000KNWNNWNklld0NNNWWMWXNMMMWWMMWXKkxKWM0ddxOOk0NWWKkXMNO
WMMMWNWKkkXWXNMMMXKNKOKNMMNXWW0l:xKKOKNWNWNXOdloKW00NWMWKKWMMWWWWNKKOdOWMXxdOKK0OXNXKOKNWX
MMW0kKXOkKWNKNMMW0KNOONWMX0NWXOc;kXKKXNNXX0K0dclXN00XWMW0xKXXNK0OKXXKkKWMNkdO00OkXX0KOkKNW
MWOoOKkoONNK0XMN0KNOkNWNN0ONNKOldXNXOk00XNxdkdcoNN0KWWMWkoKK0NOO0XNKKXNMMN0dokOkkKKkOkx0KN
W0xOXkokNX0kONW0lk0okWNX0x0WXOOxxxdold000WkclooxXKxONNXXOONKOKKKXXNXK0KNX0kdcdOkOKKxkOdkKN
Xk0N0dkXXkxdOWXl,c:l0Xxc:cdkOkkd::lol:dxxx:;:;:;lxokkoodc:xkx0O00kxodxONXxkOld0O0KOd0Kxo0M
OkKXkxK0o;';kXx,',,:xOo;:ol.'::'...,'.'oOd....',llcdc,;...;::olol:,:c:dK0ddl;;lxOK0xKKdlxX
K000KXOlc,..ox:...;cdx;..          ...'oOkd:,,cO0c:l:;;.      .....'ccdOd,.....'o00oodc,lO
Odod0Xd'..,cOkc;;;::xd'.     ....    ..'clkk;.,c:..;'cl.          ...:0WO:.....cO0x;..',';
,;c;:od:',lOO00doc;','      .':c'     .;'...       ....   .''.    'c;cXMKko,;'cXNXO:. .. '
,..,lcoOkd;,;;cc:;'..      ......     ..           ..    ....'..  ,xkkKWWNxcxddNNXKxc:;,;:
xo,ok;';:;::c;:d0Ko,.      .,,'''.          .......      .:,.,'   .lkkxkKXOx0xkXXOxxodxxxo
XO:;:,;oOkk0K0O0XNOl,       ';,'.  ..       .......       .;'   .. 'd0xdKWNX0dONNkcodxKXXO
k,'lxdllkO0XWNKKNXOl' ..                  .,'.  .,'             .. .cxx0NXWNOd0WWx:okkKNKO
O;.;oxOxxocd0Xxcloc'.  .                   .. ..;;.              .  cxoOXOKXddKNXocdk0KXk0
WO;.;lddxxl;:ll;,::..  .    ...              ..  .              ..  ...:dxKOcoONXOOxd0Kxo0
NOx;';,;oxOxlxKXXXKk:. ..   .;,.     ..                   ...    .    .  .:;'cx0Oxd::xx:o0
KxOO;. ..,:oOKXKK0kxc. .'.  .,,.     ...     ...             . .,'  .';,.  ...;c:'. .,;,ok
OoOXk, .ll:::cl::lol,. ...  ..        ..    ..,,.            .  ,;. ..,::clcloccc::;'. .'c
Odk0x' 'oxOKOkkddKK0d,.    .'.             .....   ..       ..  .'',::cddc:oOKXNNKOkc'''',
0kxk0o. .';codookKOxc.     ..'.                    ..  .    .   .';codokK0kkO0KXK0Odoooool
OOkxxo;.    ..  ...            ..                              .,clxOOkkOO00KKOxdoolccldxd
:.'.. ..   .''..               ...                             .,:lONXOOKXXNNXX00K0KXX0Okk
  .'.,cc;''.....       ..   .. ..        ..    ..      .   ..':oddkKXNNNWWXKKK0OOOO0K0OkkO
:;:dxkOxo::;'...      .,.   .            ..   .;,..       ...:dkOO0KXNNXK0OKXKOO00KXNNNWMM
OO00OOOOxl:,.    .''..,,.   .                 .:,   .    ';;lO0kxkKNWWNXNNXNWWWWNWMMMMMMMM
WWWNNXOdclc;.   .',..''.    .       .         .,..      .,kKXNNX00XNNNNNNNNNXXNKOKWWNWMMMM
WWWWWO;''',;;,'''..  ...,,.                '::llooc. ..',l0XK0KXXNNXOkOOkkkOOOOO0XNWNNNNNW
MMWWKc.....''',:looodxxkkkd.              .;ldxOkxdocclooddddddxONMMWXXK0000kxxk00OkO0000X
NKKX0OkxddddxxxkKNNK00O0OOk:             .;cdk0XX0kO0OddxllONWNX00NWWWMMMMWWNXK00XKO0XNNXX
K0kxkO0OxkO0XKkodddooodxdddl'...,,......,lkOkxxOXX0O0000000KNWMWWWWNNWMMMMMMMMMWWWNNNNNWMM
WWWWWNXKKXNNNXKK0000Okxdodoc,...''...'..'cxxlccxNNXXXKOkO0KXXX00OkOKXXXKKKXXNNNXNWMMMMMMMM
MMMMMMMMMWNNWWWWWNNKOxl:;;,'.....    ..  ...';lk00O00OO0OO0KKKOxxxOXXkddddxkOkxx0NWWMMMMMM
NXKKXNNWWWNXNX0OOkOOkdc:c;,''';:'.. ..'.......,:ooo0OxOK0O0NMWWNNNNNNKOOkkOOO0KNXXNWWWMMMM
WXXXNWWNK0XNXK0OkxkK0xccc,'.',,cl;. .',;::::;,;;'.,d0Oxocclk00KNXNNNXKKXNXXKOKWMMMMMMMMMMM
WWNNWNWWX0000Ok00od0Oxlcllc;,;:ll:'..,:::lcc:,,;.'cxOKNNOookO0NWMMMMMMMMWWNX0KWMMMMMMMMMMM
Okxxkxool:;,,';O0ldklolcoolc:cc;','.';clcccccc;...dKKKXMXO0NWWMMMMMWWMMMMMMMMMMMMMMMMMMMMM
XXXNXK0OkdooclOXO:,:,;,'cc::cc:,,;'';,:c:cloxxc. 'xkkKKWKxxxk0XNNWWWMMMMMMMMMMMMMMMMMMMMMM
MMMWNXNNKOxolkNXk,  ..';:::ccc;;;:,,:;clllldkxc..,dllKKXXo;:cdxxxxxkkOKXNWNNNNXXNNNWMMMMMM
MMMWNNWWNX0OOKXOo.   .'cllcccccccl;,:;odl:;loc,. ,c:l000NKdldxxxkOkkkOOOOOOOkxxddxddOKXNMM
WNWMMMMWWWNKKNXkc..   .;clc:clllol;;:coo:;;lc;,...'':k0l:xkkKKKXNWX0O0KXKK00OkxxxdllxOKXWM
MMMMMWNWMWK0NN0xc,.   .,:ll:ccccll:;:clc:::lc;,.. .';dK0l:cododOXWWNXWWWMMWWWWNNX00XNNMMMM
MMMWWXKXNXKXNK0Oc''. .',;llloolc::,,:ccc:;:l:'.. ..';ckKKdcl:,dXNNNNNWWWMMMMMMMMMMMMMMMMMM
MMMWWXXNNKXWNK0Oo;'. .,;:oooool:cc;,clcc::cd:..   .',;loxOx:,,:dkOkOOO0XNWMMMMMMMMMMMMMMMM
WWX0koloxkKMNK00dc;. .',;codlcloxd:;;:::::lo:'.    .,;;;cdd:.,oO00KXXK0KXNWMMMMMMMMMMMMMMM
WWX0kdlllckKkxOOd:..  .',;od::dkd:;;;;::;:c;,'...  .',,,,'.'cOXNNWMMWWNNWWMMMMMMMMMMMMMMMM
MMMWNNK0koxOl;coc'.    ',;ll;;lkdc;:::;;,;:'.'.,:'. .....;oxkOkOKKNMWNMMMMMMMMMMMMMMMMMMMM
MMWNWMMMMNOc..','.     .'.;;,,cxxc:::;,'';;....;dxkdooodOXXKK0KK0kKXXNWMMMMWWMMMMMMMMMMMMM
MMWNWMMMWW0,    . ..  ..'.,;,.;dd:;;,'''';,.  .;xkOKXNWWMMMMMMWK0XWKOKOkKWWNWMMMMMMMMMMMMM
MWNNNNXXKK0d;,,,....;;'',''::''cl,','.',',.   .;ododkOXWWWMMMMWNWMWWNX00XWMMMMMMMMMMMMMMMM
WXXXXXK00Oxooloc''cldo' ..',,...;'... ....   .;0NNNWWWMMMMMMMMMMMMWMMMMWWWMWWWWNXXNWMMMMMM
KK0xxxxdooololllccc:;,.   ....  ...         ..oNNNWWX0KNNNNWMWXKKXXXNK0000Okxxkxdddk0XWMMM
KXX00OOkxxxxxxkkkxdol;,.                      ,dxk00OxxkkOO00kxxxkkO0OOO00KK0kxxoollcokOKW
XWMMMMMMWNNXXXNNXK0dc;.                       .lxkOkxdx0KXNNXK0OOO0KXXNWWWMNXXXXK0OkxOXNWW
WMMMMMMMMMMMMMWNWMWXOo.     ..         ...     oXNWWNXK0OOOOOkdddxkOKKKXNXXNWWMMMWNNWMMMMM
MMMMMMMMMMMMMMWNNNXKN0,   .''.      .  ..''.   cKXNNNWWWNXXXXKXXNWWWWWWWWNWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNK00KWk. . ....  ..... ...;'   .dNXXWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
0000000000000000OOO0Ol.........':;,,....,,.   'x000000000000000000000000000000000000000000
""")

def page46():
    print("""\nYou hide in the cluster-leaf tree. The strange
creatures pass by except for one straggler, who
stops to stretch. For a moment he looks right at
you. "Kota zaark!" he cries, then turns and runs
after the others.
Perhaps you needn't have been so cautious.
The creature looked more like a frightened animal than a fierce hunter.
As you climb down from the tree, you hear a
low moaning coming from the brush. A pair of
bright blue lights is shining from within the darkness.
""")
    input("Press enter to go to the next page ")
    page47()
    
def page47():
    print("""\nNow the moaning comes from behind you.
Turning, you see another pair of blue lights. Beneath them are long, glistening fangs. Slowly the
creatures close in on you; their moans rise into
high-pitched shrieks. What are they?
You have only a few seconds to live, so it
hardly matters.
""")
    the_end()

def page48():
    print("""\nHoping for the best, you follow the blue-furred
Raka to the center of the village. As you walk
along the narrow footpaths, other Rakas emerge
from their agons and stare at you curiously.
When you reach the central agon the bluefurred Raka lets out a long, low hooting noise,
which is answered from within. Inside an old
white-headed Raka sits near the central fountain.
A large black disc hangs from his neck. For a long """)
    input("Press enter to turn to page 49: ")
    page49()

def page49():
    print("""\ntime he stares at you. Finally he rises and steps
closer. "So, you are what my hunters found. My
name is Arton. I am the High Raka of the village
of Rakmara."
You are so startled by the familiar words that it
takes you a minute to answer. "How is it you
speak my language?" you finally ask.
Arton smiles. "A visitor from the Nether World.
She called herself Nera."
"Dr. Vivaldi? She's alive? Where?"
The old Raka shakes his head. "She tried to
swim across the Great River. The river spirits have
swallowed her."
"She might have made it across!" you say.
"Even if she did, the Archpods would have fed
her to the Kota beasts."
"What are Archpods?"
"The Archpods live beyond the Great River.
For a long time the Rakas and Archpods have
each had one hunting boat; that is the law. Now
the Archpods build many boats. They are not
hunting boats; they are war boats. The Archpods
plan to conquer Rakmara."
You hold your head in your hands. Poor Dr.
Vivaldi! And now the threat of war.""")
    input("Press enter to turn to page 51")
    page51()
   
# Lisette Spalding did pages 50 - 73 !! Work starts here
def page50():
    # Printing out the story
    print('''\nYou shake your head and stand your ground.
The blue-furred Raka glares at you and strides
from the agon. He returns a few moments later
with two other Rakas, each holding ropes and a
net.
"I won't be taken captive like some animal!"
you shout.
A Raka tries to rope you, but you duck out of
reach. They draw closer. Like a football quarterback, you spin and dart past them.
"Kela! Zaark!" the Rakas yell, but you're already out of the agon, running across the dimly lit
land.
Helped by the light gravity, you quickly reach a
grove of cluster-leaf trees, and you keep running,
on and on. At last you reach the open countryside. In the soft reddish gray twilight you see
the Great River just ahead. You stop to rest beside
its waters.''')
    # Telling next page to go to
    page53() 

def page51():
    # Printing Story
    print('''"\nYes, bad times are upon us," Arton continues.
"But we shall protect ourselves. We have learned
to mix powders and call up the fire of the earth in
a great blast of noise and heat"
"You mean bombs?"
"We call them brakpa. With brakpa and with
your help, we shall destroy the Archpods before
they destroy us."
"What do you mean, 'with my help'?" you ask.
"You come from the Nether World, where war
is the way of life. If you ride with us, our warriors
will have courage."
"What are the Kota beasts?"
"You ask too many questions!" the High Raka
snaps back. "Now you must answer mine: Will
you go with our warriors to attack the Archpods?"
You shrink back from the choice. The High
Raka's voice grows stern and cold "If you are not
with us, then you are against us, and we shall deal
with you as our enemy."
''')
    # Makeing a choice...
    choice = input("Do you tell the hgih Raka that you will go with his warriors?")
    if (choice == "Yes") or (choice == "yes"):
        page52()
    else:
        page56()

def page52():
    print('''"\nI'll go with your warriors," you answer.
"Very well," says Alton. "You will stay with
Tomo. Vivaldi taught him English, and he will tell
you what you need to know."
Immediately one of the Rakas steps forward
and takes your arm. "I am Tomo," he says. Then
he leads you to the outskirts of the village and
into his agon. He brings you woven mats. "You
must rest now," he says.
You peer outside at the red-streaked sky.
"Doesn't it ever get dark here?"
"We have no night or day," says Tomo. "We
measure time by the tides of the Great River. Dr.
Vivaldi said two of our tides equal one of your
days. It is sleeping tide now."
You realize that you have not slept since you
arrived in the Underground Kingdom. How long
have you been here? How many tides? Too tired
to think about it, you lie down and quickly fall
asleep.''')
    input("Press Enter to Continue: ")
    page54()

def page53Art():
    print("""\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNolXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc.oNMMWNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0d, .cKWXOXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:. .   'ccdNMMMMMMMMMMMMMMMMMMMMMMWKXMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx.  ';.   .;kWMMMMMMMMMMMMMMMMMMMMMXdOMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWWWNXXKKo';,.'.  ...'ldk0NMMMWWX0kxk0NMMMMM0xXMMMMMMMMMMM
MMMMMMMMMMMMMWWWWWNXNWWNXK0Oxol:''c:....;.  .'',oO0Oko'.   .,oO0KKOkXMMMMMMMMMMM
MMWNXXNNNXKK0000OkddkOKXNXOxc,ll. 'oc'...     .';:llc,.   .  'dkkoco0WMMMMMMMMMM
WWXK0OO0Okxddx0OxxO0OO0Okxdo'.od.             ..'','.. .'co:.':ol'  ,d0NMMMMMMMM
kkOKKNNNNXXX0OOxxkkdlll:;;::' .lc,..   ...       ...'';okXKo:,.':. .:kKWMMMMMMMM
00OOkxkkkkkOkxxxxxdolccccc:,.   .':,.....'......''cdl:xNWWO,........okKWMMMMMMMM
XKK0ko;......'.....',;;::;,'...   .;,.';lc'.;,....':';OWMWO,  .;c,.;dOXMMMMMMMMM
xxxoc:'.. ...,;,'';cooodollc;'.   .:;...'.            cKWXk,   ,c..;lx0NWMMMMMMM
o:,'..  ... .',...,;:c:::clc:,..   ...  ...         .,xXX0x;  ...'coxOKNWMMMMMMM
,.         ...';;,.'cl:;;::;;;;:;;;;,;;. .'..   .  .lkOdolol'    ,lodkKNMMMMMMMM
c.    ..      .;;'...,'.',;:lookXX0kdoc.   ..... .,xkc,'....,;. .':oxOKKXNWMMMMM
:.    ....      ..''..cxkOkkxdlcclc:::;,',''.;c;'.lx;.       .'....',;:lx0XWMMMM
'.      .,,.     ''''',;ccc:cldxxxkO00kxxxdo;.'...c:     .    ...cl;..,coONMMMMM
:.       .:c.      .;:;,,codkk000kxxxxxdooolc,.'''c:.   ....  ..':,..',.':dXMMMM
:.  ...   ':,.......;llc,',coddxxkkkxk000KKkoc'. .';..c:'     .. .  ....';l0WMMM
:. .....    ...,:c:...':cc:;:lkOOxddxkkkkkkdc:;'...,..',.      ...... ...:OXWMMM
o. .....      .,:cl,. .,;cc:'.;lodxkOKXXKK0Odolc:;,,...,,.     .:occ;... .lXMMMM
d;',cc::,.     ,ooc:;..',ll::;,:dxxxkkkkkxxxkOO00Odc;,',;'..,'....';:'...ckXWMMM
xlc;;,,:c;..   .:ddc'.,ok00d:;;'.;oxO00KK00Okxocc:::cclddc,;lc;,'.    .';ld0WMMM
o::;cl::cll:'.  .,::'.';oddc,,,'.';cclllcclllloddodO0Okxdo:,;:;;:,''.  .,oKWMMMM
d:c:;;::lool'.    ..;,. .','.',',:;'.';cloxO000Oxddxdoodxo;;:,;cc;col;..';xNMMMM
0xdd:.;dxxdoc,.    .:o;. .,,'..,coddccdkkxddxkkkkkxdoodddocloollcc::c:::;',kWMMM
NKOdc::coololc;..   'lc'...;:..,:cldo::oooodddoooooodkOKXX0kdolc:::ldxxkxlcdXMMM
0kxdxo:,cddocc:,.    ..''..;d;  ..;oxdc::clclooxO0KXXK0000xllldxxdool:cllcdKWMMM
Odxkkdc:cc;:lddc....  .';' .l:.  .';lodddl:oxkOkdooxOOOOkkOO0OOkdlc:;:oxOKWMMMMM
WNXXXKkl;,';oddl;...  .,oo' ...    .:ldddc,;clooodO000O00KK0kxxdddxkO00KXNMMMMMM
X0KXXX0Oo;,;cl:;;,.    'll,..,:;''...';cllolccxOOOOkxoxOOkkkk0XNNNWWNWMMMMMMMMMM
X0KXNNNX0xo:,;;,,,'. .  ......,,;:,...'codxkkdokxdddx0KXNWWMMMMWWMMMMMMMMMMMMMMM
XOOxdxOOOxdl,.',,::'..   .''',;:ccl:'..;lcccllclookKNMMMMMMMMMMMMMMMMMMMMMMMMMMM
NKKOkOKK0Okdl:;;;;cll:;;,:dolk0Okxkxl:';c:cokKXNNKXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMNXNNNNNWNK0O0kxk0XXKK0XWX0XWMWWNXK0kxx0KKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")

def page53():
    print('''\nOnce you've caught your breath, you walk
along the river bank and soon reach a crude
wooden dock. Two Rakas are guarding their
hunting boat, a long flat-bottomed shell fashioned
from duster-leaf wood. Nearby is a smaller boat,
one you could paddle yourself. You just might be
able to untie it, push off, and get across the river
before the guards catch you.
''')
    page53Art()

    choice = input("Do you want to try to take the small boat and make a break for the other side?  ")
    if choice == "Yes":
        page57()
    else:
        page58()

def page57():
    print('''\nYou quickly reach the boat, but you can't untie
the rope! Instantly the Rakas are upon you. Uttering angry cries, they fling their nets over you. One
of them blindfolds you. Then they march you
along a winding, bumpy path.
"Where are you taking me?" you ask. But the
Rakas ignore you, muttering angrily in their own
tongue.
Death seems certain. How will they execute
you? They seem to like ropes; maybe they will
hang you.
As you march on, hour after hour, the air turns
colder. You feel your strength ebbing.
Finally the Rakas stop. Exhausted, you crumple to the ground. All is silent, and you fall into a
deep sleep.
''')
    input("Press Enter to Continue: ")
    page60()


def page54():
    print('''\nWhen you wake, Tomo gives you a bright pink
tanga. You hadn't realized how little you've
eaten, and you wolf it down. Smiling, Tomo replaces it with another.
"Someday we will go hunting," says Tomo.
"Are you a hunter?"
"Almost. I must first go on the Hunt of the
Black Sun. I must kill a Kota beast."
"A Kota beast? What are they?"
Tomo frowns. "Great toothed animals, with
eyes like blue flames and teeth like iron fangs.
They live in the darkest, hottest parts of the
woods. They tear anything apart, even themselves."
You start to ask about the Hunt of the Black
Sun, but Tomo raises a hand. "Now we must talk
of war. The Archpods will not expect an attack
when the river is low. That is when we shall cross
and destroy their boats."
The next morning as the Great River begins to
fall, the Rakas load their hunting boat, now called
the war boat, with brakpa—crude bombs packed
in hollowed logs. You shudder to think that you
are about to witness the beginning of a war. But
there seems to be no way to avoid it Before the
sleeping tide has ended, Tomo, you, and five
hunters set off in the war boat.''')
    input("Press Enter to Continue: ")
    page55()

def page55Art():
    print("""\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkko;;lkO0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNXKc.  ..  .'xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWXkc. .cdxo,  lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOKWM
MMMMMMMMMMMMMNOocldkKWMMMMMMWXx..xkdxoc..lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;.;0M
MMMMMMMMMWXkl,      .cKMMMWN00Kdcolxkc;;dXMMMMMMMMMMMMMMWWXXNWMMMMMMMMMMWNXKKKKXWMWk,. .dW
MMMMMMMMNx,.          cXWNKxoxXNx,'l00KNMMMMMMMMMMWWN0kdl:;;;ckNMMMMWXkdd:...''';lc.   'OM
MMMMN0xdc.            ;KXKkcclOWk. :XMMMMMMMMMMMXkl:'.  ..... 'OMMWKd,.             .c';KN
MWXx;. .     .,..   .;xO0Kl':o0NKl.,kXWMMMMMMMMKl.  .         .kMMKc.              .xKlcKk
Ko'      .''...    'xKdoxd,.:OXOdx;.ldxXMMMMMMMNk:.           .lOxc'.        .. .;o0WXcckc
:.       .,,.      .;;..'.. .;xxcc:..:oONWMMMMMMNx,    . ...   ...       .......oXWNKd,.'.
.        ',....             ..:odd:;:oO0KKKK0O0Ol'     ...,''....         ,;.  .;clc,.    
    ..  ... ......    .     ...:dxxOkoc::c:::;;.          ...             .;'... ......   
,.....   ..         .          ..'oXNk:'..                                   ..    .. .. .
l;;,'..   ..  .................'...;dkkkOOl.....  ...........'''''....            ........
o:;'...    .  .......,;,'...,,,,'......':oo:....'''',;:;,,,;;;''................,;;;;,....
:;;,....      .....,::;,;:;:cc;'''''..    ..  .,,,,..';;,;cll;;c:::,'',,;;;,,'..,,'..... .
...'cc;'.       ...';,'...','...;c;'..           .';;'.....''.'::,'.......'''.   .','.',..
olcllcoo,. .',:c:::ldxoc,...   .'cooc,..    ......,ldd:;;'..',:ldOxolcclllldxdooooxkd'.,..
xxd:'':c. 'dOkkkddO0Okxoolccc::c:cxkkxdl:,,:odxxddddc:cooc:lkOxxxxdlodddddddolodollc,. ,,.
doxl,''.;oxO00OkdodkOOOxkkxk0KK0K0klcclol:cccloxxkkdldkOxlloddxkkdlcldxxkOOO0XK0kol:;.'d:.
occll;..;okkxokXNXKOkk0000OO0XNNXKOkkOKK0xdoodxkOKKK0XN000OOOOkOXNNK00K00KKOO00Oxoloc.;Oo'
dkkd;.'coxdooodO000OkxxxxdddolokOkk000kkOkxxxxxkkkkO0KX00OkxddxxxxkkxxdddxxdooxkOxol;.;xxo
Oxl'.;lddolllc:;;:oloddoollllccl::lk00KKKOOkO00KXXNK00KOkkxxdxkOO0000kxxddxO0Okxddoc;:cc;;
:,.',..,colc:c:'':dxkOkkkkkkkxxdlcodddkxxk0KNWWWMMMX0KXKNWWWWWWWWWXNWNXKOxxkOOkkkxxkOOxolo
kkOKK0kxk00kk00O0K0KKXXKOOkkkkkkxkO0Oxod0NNWMMMMMMMWNWWWWMMMMMMMMMWWMMWWNNN0OOkOXNXKOOOkO0
MMMMMMMMMMNNWWMMMMMMMNNXXXNNNWNNNWMMNKOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWMMMMWKXNXWM""")

def page55():
    print('''\nThe Raka hunters are clumsy at rowing, and
the boat is so heavy that a few small waves would
easily swamp it. You realize you might be able to
swim to shore before the Rakas could turn
around and catch you. It's risky, but it's your only
chance to avoid the war!''')

    page55Art()

    choice = input("Do you dive overboard and swim for shore?")
    if (choice == "Yes") or (choice == "yes"):
        page61()
    else:
        page62()

def page61():
    print('''\nIn a flash you're over the side and swimming
for shore. The Rakas yell at you. One of them
tries to hit you with an oar while the others stroke
furiously, trying to turn their unwilling craft
around.
Swimming hard, you hear screams behind
you. The war boat has overturned! The brakpa
have gone to the bottom, and the Rakas are
struggling to save their lives and right the boat.
Using all your strength, you swim in to shore and
start running for the groves of duster-leaf trees.
Almost at once you hear a loud, trilling song.
Above you is an enormous flying creature with
wings stretching twenty feet across! You stare into
its great blue-green eyes and at once feel completely safe. You know you've seen it, or at least
dreamed of seeing it, before. It's like some kind of
angel bird sent to protect you. Without thinking,
you leap right onto the creature's back.
''')
    input("Press Enter to Continue: ")
    page22()

def page62():
    print('''\nSwimming to shore looks too risky. You sit
quietly in the boat, hoping for the best. As the war
boat nears the middle of the river, the current gets
stronger. The Raka warriors can hardly row
against it As the Rakas struggle with their oars,
the boat is swept farther and farther downstream.
You wonder where the current will take you,
until you hear a sound up ahead that quickly
grows into a roar.
"Ig riba!" the Rakas shout. "Ig zaark!" They
begin to unload the heavy brakpa. Frantically you
help, but at the sight of the boiling white rapids
ahead, you lose heart. Moments later the boat
smashes into the rocks, and you and the Raka
warriors are swept away by the raging torrent.''')
    the_end()

def page56():
    print('''\n"I won't have anything to do with your
brakpa," you say. "I am not an enemy of you or
of the Archpods."
"Ig krig zaark!" the High Raka says angrily.
Two Raka guards seize you and march you out
of the agon. But the moment you get outside,
you make a break. You've always been able to
run fast when you needed to. In the light gravity,
you're even faster. As you dart through the
groves of duster-leaf trees, you can hear the cries
of the Rakas from both sides and behind you. But
the Great River lies just ahead, and for once
you're in luck—there's a crude raft tied up along
the shore. You quickly untie it, and push off as
you jump aboard. The current soon takes you
around a bend in the river and safely out of sight.
You lie low on the raft, afraid of landing until
you are well past Rakmara. Now you have time to
think. Where will the river take you? What will be
your fate?''')
    input("Press Enter to Continue: ")
    page63()

def page63():
    print('''\nYour raft floats on past marshy banks and
yellow clay islands. The river grows narrow as it
flows through a deep canyon. Rock cliffs rise up
on both sides. You hold on, hoping to reach a
place where you can land.
Never have you experienced as dark a night as
this. It's as if the river were flowing through a
tunnel somewhere in the depths of the earth.
Finally you sleep, and it seems as if a very long
time has passed when you awake and find your
raft pitching up and down. Why has the river
grown so rough? It's still too dark to see much,
but at least the stars are out.
Stars? There aren't any stars in the Underground Kingdom. You're not on the river—you're
on an ocean!
''')
    input("Press Enter to Continue: ")
    page64()

def page58():
    print('''\nYou think fast. Luckily, you remember the
command that the blue-furred Raka gave. You
walk up to the guards, smiling. You point in the
direction you came from, then to yourself, and
then to one of the boats.
"Nar mg calla," you say with authority.
The guards mutter. Then, to your surprise, they
smile. One of them unties a boat and motions for
you to board it. They must think you're a privileged guest of the High Raka. You quickly get
aboard and push off.
As the current takes you around a bend, you
notice Archpod settlements on the opposite
shore. Soon you spot a good landing place. As
you get closer, you notice a band of Archpods
standing on the shore. Like the first Rakas you
met, they are armed with ropes and nets. They
don't look very friendly. You could be in for more
trouble than you had with the Rakas.''')
    choice = input("Do you continue to shore?")
    if (choice == "Yes") or (choice == "yes"):
        page66()
    else:
        page65()

def page64Art():
    print("""\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMMMXXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNKNMMMMMMMMMMMMMMMMMMMXKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNKNMMMMMMMMMMMMMMMMMMXKMMMMMMMMMMWXNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNKNMMMMMMMMMMMMMMMMWKKMMMMMMMMMWKOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWXXWMMMMMMMMWXWMMWNkOMMMMMMMMWK00kXMMMMMMMWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWKKWMWNNMMMNO0WMWNkOMMMMMMMWK0K0XWMMMMWXXWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKWMX0XW0KKONMWXkOWKO0KWWKKK0XWMMMMNKKNNXWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWWXNMMMMWWMMMMMMMMWXKWWKOXXOOxOWWW0OWKOk0NK0NX0OXMMN00KXK0KXWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWXKO0XNWMNXKXWMWKXWMWK0XWKOXKdcldKMXOxxKKOOkOKXO0WWK0kxkKXK0KWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNXXKKXKXWNKKXWX00XWKxxOK0kXKkkdx0KKkkX0xkOO0OKWNKKNNXNK0KNWWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWWWN00XNNK0KXOkOxddcxOoxkxdl;,;coddooc:dxOWMWWX0XX0KNNKKXWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMNKO0KXXK0OkOkxo,,:cox0KKKK000OOxl;':dxOKX0OO0KXXK0KNMMWWMMMMMMMMMMMMMM
MMMMMMMWXNWMMMMMMMMMMWNX0kk0Ok00Od;;o0NWWWMMWWX00K00KX0kd;,kXOxONNOxOXWNXKKNMMMMMMMMMMMMMM
MMMMMMMWXXXNXXNNWMMMMMMMWK0kdood::kNWWWMMMMMWWWNNXKOddOXNk;:dlo0KOkkOKKKXNWMMMMMMMMMMMMMMM
MMMMMMMMMMMMWNNXNXXKXXNWWK0kkkl;oKMMMMMMMMMMMMMMMMMWXOllOWXl';oooxk0XNWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWNXKKKK0Oxxc'lXMMMMMMMMMMMMMMMMMMMMMXdckWXl.,ododk000KWWWWWNXXNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWNX0xc:;':KMMMMMMMMMMMMMMMMMMMMMMMNdcOW0,.:odxkOOKKKK0KXXXKNMMMMMMMMM
MMMMMMMMMMMMMMMMWWNNXKd:cooc;.dNOOWMMMMMMMMMMMMMMMMMMMMMKldNNo.,x0kxOKNWWWMMMMMMMWWWMMMMMM
MWNNNNNWMMMWWWNWNXK0OkxcckOl.'kNooNMMMMMMMMMMMMMMMMMMMMMXloXNo..cxkkKWWNXK0000K0KKKNMMMMMM
MWNNXXNWMWMWNNXNNNXXKkxocokx;'xWNNMMMMMMMMMMMMMMMMMMMMMMKodKXl.,oddkKWWKkxxkk0KKNWWMMMMMMM
MMMMMMMMMMMMMMMMMMMMNKK0dllo:'lNMNNMMMMMMMMMMMMMMMMMMMMNxld00;.cxdoxKWKkkxxkkO00KKKK000NMM
MMMMMMMMMMMMMMMMMWWNK0Oxddxodl;kWXOXMMMMMMMMMMMMMMMMMMNklokKo';ddld0K0o:dO0KKNWMMMMWNXNWMM
MMMMMMMMMMMWNNWWXKOOOO0K00Oxxkc;kWX0KNWWWMMMMMMMMMMWNKxodk0o,:cxKNNNNNKKKKKKKKKXWWMMMMMMMM
MMMMMMMMWWNK0KXXXXNNWNXKXKkxxxl::dXNK00OO00XXXNNXKOkxxkOOkl,lx:;d0XNWWXXXNWWNXKK0KNMMMMMMM
MMMMWNXXKXXXNWMMMWNXXXNNXK0OOxdOxc:dKNXK0kxkxdxxxdxOKNXOl,;cx0kdx0XXKXXXKKKXXXNMMWMMMMMMMM
MMMMWNNWMMMMMWNNNWWWNXXKXWXkxxxxocl:;cx0XNNNXKXXNNNKOdlc:ldxk000KNMWNNXXKXNNXKKK0KXWMMMMMM
MMMMMMMMMMMMMWWWWNNNNNWWNXKK0kkxcl0Kko:;:cclooddll:;,,:xXXkkK0kk0KXNWMMWNXXXKXWWNKKNMMMMMM
MMMMMMMMMMMMMMMMWNWMMWXKXNWWXOdx0NX0KXxdxl;,,,cddd:cxOOxkK0xkOolOKKKXNWMMMMWXKKXWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWXXXNMMWKkkKNMN0OOkxkkollc:clol,;ddo:oKN0k0KXWNXK0KKXNWMMMMMWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWNNWMMMWX0KWMWNK00KXO00kkxl::cl:co0Nkox0NNKOxOXMMWNNWWNWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWNKKNMMWKKX0XWMNN0OXOxxkxOKK00NMWWX0XMWXKKKNMMMMMMMMWNNWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWXXWMMMN0KNKXWMMMMNNMKO00kKMMWKXMMMMNKXWMMWX0KWMMMMMMMWNXXNWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWWMMMMNKNWNNMMMMMMMMMXKNK0NMMMNNMMMMMWKXWMMMWXKXWMMMMMMMMWXNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXWMMMMMMMMMMXKNK0NMMMMWWMMMMMWKKWMMMMNNWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWK0NMMMMMMMMMMMXXWX0NMMMMNKNMMMMMWXXNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWXXWMMMMMMMMMMMMXNMXKNMMMMWKKWMMMMMMNXNWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWXXWMMMMMMMMMMMMMMMMNKWMMMMMN0XMMMMMMMWXNMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNKXWMMMMMMMMMMMMMMMMMNXWMMMMMMX0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWXXWMMMMMMMMMMMMMMMMMMN0XMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")

def page64():
    print('''\nSo, the Great River must be an underground
link between the earth's seas. The tides were with
you and carried you through the earth's mantle
and crust to the surface. There's land nearby. And
you notice a faint glow on the horizon. Soon the
sun will be rising, not the cold Black Sun of the
Underground Kingdom, but your own warm,
bright, life-giving sun!''')
    the_end()
    page64Art()

def page66():
    print('''\nTrying to act unafraid, you row straight in to
shore, hop out of the boat, and step forward to
meet the Archpods. "Hello. I come as a friend!"
you call out. But their only response is to take you
prisoner and march you back to their village.
You soon find that the Archpods live in agons
similar to those of the Rakas. Your captors lead
you into the largest one, where you expect to be
presented to their chief. Instead, a woman calls
your name. It's Dr. Vivaldi!''')
    input("Press Enter to Continue: ")
    page67()

def page67():
    print('''\nShe hugs you warmly. "I thought I'd never see
another human face!" she cries, tears streaming
down her cheeks.
One of the guards says something you cannot
understand. Then the Archpods march out of the
agon, leaving you alone with your friend.
Dr. Vivaldi tells you how she barely survived
her fall through the Bottomless Crevasse, how
she lived for almost a year with the Rakas and
finally swam across the Great River to the land of
the Archpods. You tell her of your descent to the
Underground Kingdom and your adventures in
Rakmara.
"We must set upon a plan," she says. "The
Archpods have learned that the Rakas are making
bombs. They think we may be Raka spies. That is
why you were treated so rudely. They have told
me that their chief, the Grand Akpar, will soon
decide whether to execute us."''')
    input("Press Enter to Continue: ")
    page68()

def page68():
    print('''\n"What can we do?" you ask.
Dr. Vivaldi looks at you thoughtfully, then says,
"If there is a war, we cannot expect to survive. I
am going to talk to the Grand Akpar. But here,
take my gold bracelet. If you give it to the guard,
he will let you escape."
"But what will happen to you? I don't want to
leave you here. I'll go to the Grand Akpar with
you!"
Dr. Vivaldi replies, "Think carefully before you
make such a decision."''')
    choice = input("Do you decide to face the Grand Akpar with Dr. Vivaldi?")
    if (choice == "Yes") or (choice == "yes"):
        page70()
    else:
        page100()

def page65():
    print('''\nYou try to row back to the Rakmara shore, but
the current is now so swift that you find yourself
being carried downstream. Desperately you try to
paddle against it It's no use. And there's bad
trouble up ahead—foaming, white rapids! You
hang on for your life, but your raft smashes into a
rock with a terrific thunk. One end tilts straight up,
dumping you into the wild, swirling waters. You
try to grab the raft, but you can't reach it. You
start swimming toward shore, but you can't make
any headway.
You're not a quitter. You'll go down trying.''')
    the_end()

def page60():
    print('''\nHours later you awake, stiff and shaking from
the cold. Cautiously you pull off your blindfold.
Your captors are gone. All around you is dark
brown clay. There are no trees, no water, and no
shelter from the cold wind that blows across the
vast, empty plain. So this is your intended fate—
you will be left to die of exposure under the Black
Sun.
It's a long trek across the desert of the Underground Kingdom, but if you can only reach some
trees, you may be able to find a warm place to
rest. Somehow you know that you'll make it, if
you have the will.
Do you?
''')
    the_end()

def page69():
    print('''\nYou're glad that your friends are still alive, and
you hurry to meet them. A few minutes later you
are exchanging stories of your adventures in the
Underground Kingdom. But Larsen and Sneed
do not seem happy.
"Is anything wrong?" Dr. Vivaldi finally asks
them.
"I'm afraid so," Larsen replies. "We've just
inspected the Bottomless Crevasse. The glacier
has sealed it tight. We are trapped here forever!"
"We'll never get home now," you say.
"That's the way it looks," says Larsen. "Like it
or not, we're pioneers. The only thing for us to do
is to make the best of our lives in this new world."
"That's not good enough for me," says Dr.
Vivaldi. "We're going to find a way out of here!"
She looks at you with a broad smile. "Right?"
"Right," you answer.
''')
    the_end()

def page70():
    print('''\n"I'll face the Grand Akpar with you."
"That's a brave choice," says Dr. Vivaldi, "but it
also would have taken courage to escape." She
smiles. "Sometimes there's nothing to do but to
be brave!" As she speaks three Archpod guards
walk into the agon. They motion for you to follow
them, but when Dr. Vivaldi tries to join you, they
block her way.
"Good luck. ... " Dr. Vivaldi's voice fades as
the guards march you out of the agon.
A few minutes later you are standing in the
central agon. Facing you is the Grand Akpar. His
long, silky fur is combed like an oval frame
around his stern, gray face. A pendant made of
smooth black stone hangs from his neck.
He studies you a moment and says, "We have
learned from Dr. Vivaldi that you come from the
Nether World—the world of warfare. You know
much more about such things than we do. You
can prove that you are not a Raka spy by telling
us how we can defeat them!"
You stand silently, trying to think of what to say.
"I'm waiting," the Grand Akpar says.
What will you do?
''')
    choice = input("Do you try to play along with him?  ")
    if (choice == "Yes") or (choice == "yes"):
        page73()
    else:
        page104()

def page72Art():
    print("""\nNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
NMMMMMMMMMMMMMMMMMMMMMMMWWMMWXWMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
NMMMMMMMMMMMMMWNNMMMMMMWX0000OOKKOXWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
NMMMMMMMMMMMMWXkxKWWMMWXOxolcdoccokxdOKKKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
NMMMMMMMMMMMMWXd;cdkK0o,..,,,ldoc,:l::okKNMMMMMNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
NMMMMMMMMMMMMNKx,'odl.   . .;dxdoloxo:;:cdKXXK0OXWMMMMMMMMMMMMMMMMMWNWMMMMMMMMMMWWMMMMMMMN
NMMMMMMMMMMMMMWKxclxdc,.    ;ooodkkoc'..  ,dkk0WWNXXWMMMMMMMMMMMMMNOKWMMMMMMXXNKKNMMMMMMMN
NMMMMMMMMMMMMMMMO,..:od;::.  .cxx0Oc,....',cdkO0OO0XWMMMMMWXKNNXKKkkNWNWMMMKk00KWMMMMMMMMN
NMMMMMMMMMMMMMM0;..:OKOoldc.  .,''..,lolldocoxOXWMMMMMMWXXXOdlll:::odc:dOKKdoxkKWMMMMMMMMN
NMMMMMMMMWNXXXO;.  :KMWkcc;;;     ,ldxxkO0xlldxOOOO0KKNXxc,';coololc,..',lOkdokXNXKKKXWMMN
NMMMMMMMMNkc:,..   .dNWk,;oo;    ;oxkxool:;;:lodddxkO00Ox; .,lxkoodc'',,;kNXdcoxkO0XNWMMMN
NMMMMMWXkol:,..     .cOd':OO;   ;o,.cXWO;. 'OWNN0xoloxOd;......;cl;..,':kkxkdcokXMMMMMMMMN
NMMMNOdoodlc:'',;cccccclool:.   c0d:xKk;.  .loccdkxl:cdoc:lko.   ....;:dx;....xWMMMMMMMMMN
NWX0xloolo::l'.,:oxdxKX0c.       ,okxc.    .....'dKXk;...;l00o' .'. ,dlxX0;  .lNMMMMMMMMMN
Kkdolcclxolkk:;cclxxlxXNd'....    'odo:..':c::;..:kO;.    :00do:'.  ;l..lx,   ;XWNNNNWMMMN
kdo:;lok0ookd:,:oloddkKK00KXOxxkkk0Kkxkdc:,,oOx:,lo,...  .kKc.,d:   lx;','    'xkc;:lkKNMN
KXkdoxKNXOkoc:;:lllc,';:;cx0KKXWWNKOxxdooc;':ddocdOc.... .:o,.:0o   'cc,.      ';'..,;:lod
NNOkx0WXOxlccccc,.   'ol. ..''':lcoO0dodol;':lodlcdc.      .':od,        .',;,',,',,:ll:,:
K0xd0KOOOxdddxo:.   .oKd...    .'.:xOOkdooc;:c:;,'ld;   ..',:c;.      .cdkkxxo::;,,.',::':
OdooxOKX0O0Okxdllc'.'kKc ..      .oxoxX0olccc;,,,'cOx' .cdokKK0o'.;cco0WNXKOdlclc;,'..,;,c
0OxkKWN0KXOkOdoooo;.,00;...      .xO;'x0dc:loc;'..,cc;:cokOkdokKKXWMMMWWWN0xololl:;',:llco
NWXNMMWWNKkOxcol:l:.:Kd':o:.  .'.'kk:,:odl:odc'.'':ol;::ll:c:..okxk00KKOOdlc;lxdl:'.';oxlc
NMMMMMMNOxl:;;xd;,,;oOc.;lc. .,' cOxoolcx0kdc:,'.',',;:clc..;'.ox,':;''.. .,'.o0l,'.;cdkxl
NMMMMWXkc,:;,;kKl':dOk,.,:,. .. .dkxxlldxdkx,'...,c;,:coxc.    ;kc...     ... .xk;,;,:o0Xx
NMMMW0dl,:k0o:xXkcoxOx;'........locldoclclkkc:,..;c:,;::lo;.   .lx'..    .:;.  'ko.;:;dOko
NWNXOollo0WW0dxXW0ooxo;::;;::::oxl:odl,;::dOxxxl;;:cc;,;::oo;.  'dl'',.  .;c;. .ok;;dOKKkO
X00Odlx0XWMMWXXWMWOoxlcxxddllodddxO0dccc;',,:cloc;;';:,lxllooc. .:xc,;,.  ':,.':cxdkWMMWX0
0doocoKMMMMMMMMMMMKoc:ckxdl:cccclOX0dcc::';:...cl:;,::;oxo;;od,. .:d:;:'   ..;oocodkNMMMMN
0xxOoxNMMMMMMMMMMMXd::codd:;::oolONKOkdc;..,' .,;:c:loclooc',lool'.;l,''. .,::lc:lokNMMMMN
KXWWKXWMMMMMMMMMMMNdloodlcdkdkKKKXNkccool,.   .'''';c;;ldoc:;;lk0x:;l:.',:dkkdoldxdkNMMMMN
NMMMMMMMMMMMMMMMMMWNN0kkxoONXNMMWXkc',ccc:,...''''.;c;::colodl;:ldolc::;;cdoood0NWXx0MMMMN
NMMMMMMMMMMMMMMMMMMMMWWNWWWMMMMXOkd,..cl:,,;''...:;,:coo;;odxl;',clcodl,:odc,:xNMMWkkWMMMN
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXKNNk:;ldo:,,::;,'....''..',;:cdl:lc;:olloodo;oKMMMMNNMMMMN
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXOdddoolllc;..........:OXKO0klc:clolodONWMMMMMMMMMMN
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXk0XKK0000Oxoooll::ld0WMMWNXxdKkdOkkNMMMMMMMMMMMMN
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMWNNNWMMMMMWKKMNKNNNWMMMMMMMMMMMMN
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN""")

def page72():
    print('''\nSuddenly, you feel a presence. Looking around,
you see pairs of bright blue lights staring at you.
Then you see brown bristly faces, iron fangs, and
long curled claws. Kota beasts! The last sounds
you hear are their unearthly shrieks of triumph.''')
    the_end()
    page72Art()

def page73():
    print('''\nYou try to think fast. You don't want to be
responsible for killing the Rakas, but you have to
sound helpful. "Land your fleet during the sleeping tide," you say. "That way you will surprise
them."
"Thank you." The Grand Akpar smiles. "But, if
your advice fails, you will be taken to the Mouth
of Fire."
The Grand Akpar motions to his guards. They
lead you back to Dr. Vivaldi.
You and Dr. Vivaldi wait anxiously, wishing that
you could do something to prevent the war. You
know that the Archpods are building boats as fast
as they can. Dr. Vivaldi pleads with the guards to
let her see the Grand Akpar, but they refuse to
listen.
One day the Grand Akpar comes to your agon.
"Our boats are ready," he says. "We invade Rakmara now."
That sleeping tide, you lie on your bed, dreaming of home. An explosion startles you. The war
has begun! The Rakas must have had their
bombs ready. You wait anxiously for news of
what's happened. Finally it comes—in the form of
Archpod guards carrying ropes and nets.
''')
    input("Press Enter to Continue: ")
    page84()

# Lisette's work ends here

def page74():
    print("""\nYour head aches. You feel as if you've been
run over by a steamroller .. . but a cool hand is
pressed against your forehead.
"Don't worry, you're going to be OK," Dr.
Vivaldi says. "The radio worked. Help is on the
way."
Your face is bruised. It's painful just opening
your eyes, but well worth it. For in the bright
sunlight you can see ice fields all around you.
You're back in Greenland, and right now the
whole surface of the earth feels like home!
You look up at Dr. Vivaldi. Her face shows she,
too, is in pain. "A broken arm," she explains.
"Otherwise, I'm OK."
"We were lucky," you say.
"Yes." She smiles. "The Vertacraft Just
squeaked through. The crevasse has narrowed
two more feet. In another few weeks it will be
impossible to get through. You and I will probably
be the last ones ever to visit the Underground
Kingdom."
"I'm glad we had the chance," you say. "I
wouldn't have missed it for the world."
""")
    the_end()
# Daniel's work starts here and goes to the end
def page75():
    print("""\n"But what does that have to do with the black
hole?" you ask Bruckner.
The professor pauses to fill his pipe. "As I explained in my published theory, a tiny black hole
lodged in the center of the earth more than a
billion years ago. It pulled the interior of the
earth—everything except for the crust and mantle—into itself, leaving the earth hollowed out like
a Halloween pumpkin. That is what the gravity
readings tell us."
"Then where is the Underground Kingdom?"
"It is the whole interior surface of the earth.
And if you stood there and looked straight up,
you would see the black hole. It would look
exactly like our sun except that it would be jet
black."
Professor Bruckner lights his pipe, then says, "I
did not expect to undertake this mission for some
months. I only planned to inspect the crevasse
and test the Vertacraft, but the crevasse is closing
rapidly. I must make the descent today. Otherwise, my return path might be blocked. Who will
volunteer to come with me?\"""")
    the_end()

def page76():
    print("""\nWhen you tell Dr. Vivaldi of the advice you gave the Grand Akpar, she shakes your hand. "I would have said the same thing. If our destiny is to die at the hands of the Archpods it will not be your fault."
Now three tides have passed. You and Dr. Vivaldi are still waiting for the news that will seal your fate. It must be midway through the second sleeping tide when the guards awaken you. A moment later, the Grand Akpar walks into your agon. With him is the High Raka. "The Archpods and the Rakas have made peace," says Akpar. "From now on we shall build boats for both tribes, and there shall be no bombs!"
""")
    input("Press Enter to Continue: ")
    page78()

def page77():
    print("""\nOne after another, the team members shake their heads. Finally Bruckner turns to you. "Well?" You hesitate. You don't want to risk your life. But this could be the only chance of finding your lost friends.""")
   
    choice = input("Do you decide to go with him?: ")
    if choice == "yes" or choice == "Yes":
        page35()
    else:
        page33()

def page78():
    print("""\nFrom then on you and Dr. Vivaldi are treated like honored guests. The Archpods bring you baskets heaped with tanga, and cakes made from golden grain. They show you their mineral pools where you swim in the swirling, bubbly water. Later you lie in the warmth of the glowing rocks, then cool off under the Black Sun. A few tides later the Grand Akpar pays you a visit. "Would you like to stay longer and explore the Underground Kingdom?" he asks. "We shall lend you three hunters to guide you. Or, if you wish, you may return to the Nether World." "Which do you prefer?" Dr. Vivaldi asks you. "There may still be a chance to return home, though the risks are great.\"""")
    
    choice = input("Do you want to stay longer and explore the Underground Kingdom?: ")
    if choice == "yes" or choice == "Yes":
        page81()
    else:
        page82()

def page79():
    pass

def page80():
    print("""\n......................................................................................
.................*:::::::::...........................................................
................*:.......:::::::::::..................................................
...............*:.......:*:........:::::::::::........................................
..............*:........::..................:::::::::.................................
.............::........*:...........................:****::::::.......................
............::.**.:***VV.....................:::*****V*V*::::::::::::::::.............
...........*:.......*V***:::*......::**VVVFV*****:***VVV*VVVIVVV**:......:::::::::....
..........::.......:*:........:**VVVV**::.**:*.**.*:**V*.**V*..:**VVV*...........:::::
.........::.......:*......:*VVV****:*V**:...:*.:::*.**:::**:........:*VV:.............
........::.........:...:*VVV*::V::*:::::.******::.::*V*:*:.............*VV*...........
.......::............:VFVV**:::*:*:**.:V:.:*::*V*.:::***:...........:*V*.:VV:.........
......:*...........:VV*...********.*:..:**:*.:*:.:*****......:*:*V*****:...*M*........
.....:*..........:V*:...:**V****:***:*V:::**.:V**F**.....:*VVV::...::**VFIMMIIV:......
....:*.........:VV:.:***:*::V*:*VVV***:...:*V**:**.....::V*:..::***VVVVV**:...*V:.....
....*........:VV:::****V::::*****VVV**********VVV*:...*V:..::******VFF*........*V:....
...*:.......*V*:*V::.:.:*V*V******:**V:..:*V*:*VV*:.:**:..:******VFMV...........*V....
..::......*V*.::::.:*V****:*V**:*V*****.****::VVV*:.....:VV****VFMF*.............VV...
.::.....:VV:......:**:**::**:::V:********:***VV***:....:VV***VIMF*...............:M*..
:*.....*V*........:....:V****:.::..*****V*V**IV**V*V**:V**VVMIV*..................VI..
*....*I*....:****:.....:*::::*....:*VIFVVFVVNFMIVVMVVVVVVVV*:.**V***:.............:M*.
....*I*......::***VV***:.:...*:.:*VVFMINMIIMMFVVIFMMNIVV:....:*******V****::.......VF.
...*I:........:**:::::**V****:.:*IVFVMIV*IMMMNMVMMFMMV:.*VV**::*V*..:*******V*.....*N:
..*M:.........::**IV**:.::***:.VVVV*VVFVIMFMIMIVVMMM*..V*VI**V:::..:***VF**:*:.....:M*
.*M*.:.:..........::**........*VMIIFFFV****V***VMMV:...VV****V:*VVV*:...::***V*:....F*
*II**V*V*V*:**:::..............:***:***:***VVIMI*:..::..*****V********V**.::.::.....V*
NV:*********V*:****.*V*::............:*VIIV***:.::*VVF*:.:..******VV**:::.:VV*:.....V*
I:..:**V:::::::::..:***V*V**::::...:*IMV*:::::**IIFV**VV*IVVV*V*V*****V*V*V**::.....F*
:......****:***V......::****VIVIVV*IMNVIVVIFFMV*VMMV**MFV:*IV***::***V*VVV*:*......:M*
.**::::**:.....:....:*****::**VFMIMMNIIIIFV**IFMNI*:IIMF***MIIFV:.....::***********VM*
:***VV*******::..****V********:**VVVVFVVVVFIMVMMIMVVNF*VV:*NFVVFV*::..**V***:*:.*:.VV*
.....:::::***VV**:..:::****VV:*VVVN*V*......:*V*:VVVFV*VMVVVMVFIVVIVVV***.:*.::::**M**
:*****IV**:*:**::V****V:...*VVV**FIV*.........::::**:::***V***:***VV**:**V.**.V:::VV*:
**VFVVVVVIFIF*.**:***:V::***VV**VIV*:.....:****...**VVVVV***:::**VMV****:****:.:*:M**.
:*VVMM*VVVIV*..:::*V:::*VVV****VIV*:...********.......:::**VVV:..*FFVVV***::****:VV:*.
:*VFFIIV**V*......:***********VII**..:********V**:...........:..*V::.******V****VMVVV.
:***:**V*V*.:::**V****V*****VFMF:V:..::*VV*V*****:............:V*::.*:***..:*::V*$VV*.
.:::****VVVVFVV*VV********VVFF*:*::*F*..*F*::***V**:.......:****V.:****V***:**::VM**..
VFMMIIMIMIVVVVVVFFVVVV**VVVV*..*V**V*V***V*...::.:::.:*******:.::..V*::.:*:.::V*N**...
*************************:....*V:::.:***V**::VI*.::***:**...*:..**...*:.**.**:*MV:*...
......::::...................:V*VMV:VF*VVF**F***VIVF**.*::*.:V.::::*....:*:*::VV.*:...
......**VVV****::...........:F*::**:**:******::*V*V*::*:.**.:**V..:*.**.*V::VIV.:*....
......:**::******..........:V*...::*VV*:::VI*:*:*IM:*.*:.:*:.:::::...**..:V:VI:.*:....
......:**::*V**:...::......VV....:.*V:*::*V*:*FI*VVV*..*::V.*V:.*V...:*..***I:..*.....
....:VV***:::**....*:.....*V:........:::*F***:**V**V*..V*::.::..:::*:**.:.*M*..**.....
.......:*****V***:*:::...*M*::::::::::::***V*:.**:.:***:.**..*::V:.*:..**VM*...*......
*..............*V*:::::::*:::.............::::::::....:***..:V::*::.:*.*MM*...:*......
M*..........::::...........::::....::::.:::::...:*:.....:****:...**.***MM:....*:......
*M*.......:::.................:***:::::::::::::::..........::***:::..*MF:.....*.......
.*MV:..::::......................:::...........**:****:........:*****NV:.....:*.......
..:VI**:........................**.::::.::....:V**:****...........:VM*.......**.......
...:*:..........................:*:::.*****:*****:::*V*.........:*FV:........*:.......
:::..............................::::::*......:::**.*:**V*V*:.*VV*:..........*........
:..................................::..:*:.............:::*VVVV:............:*........
................................::...:::**.............:*VVV*...............*:........
...............................:*::...:**:......::**VVVV*:..................*.........
...........................:::****::...VFVVVVVVVV***::.....................:*.........
..........:::::::::::::*******:..::*::**::.................................*:.........
.......::**::::::::*::**.......::::::......................................*..........
....:::..............:::::::::**:::::::::::::::::.........................**..........
.::::......................................:::::::::::::::::::::::::......*:..........
::..............................................................:::::::::**...........
......................................................................................
......................................................................................""")
    page81()

def page81():
    print("""\n\"This may be the only chance earth people have to explore the Underground Kingdom," you say, "and I don't want to pass it up." "I'm glad to hear you say that" Dr. Vivaldi unfolds a map of the Underground Kingdom. "I made this map from what the Rakas and Archpods have told me. Although the Underground Kingdom has an area sixty percent as large as the surface of the earth, only a very small portion is cool enough to be habitable. Most of the land is too hot to set foot on. It is the molten red rock, you know, that provides the reddish glow that lights this dim world. If it were not for the tremendous cooling effect of the Black Sun, life could not exist here." Sometimes Dr. Vivaldi gets too scientific for you. "Where do you think we should explore?" you ask.""")
    input("Press Enter to Continue: ")
    page83()

def page82():
    print("""\n\"If there's a chance of making it," you say, I'd like to try to get home." "Then we must hurry," says Dr. Vivaldi. "Akpar, there is not much you can do but lead us to the crater where we arrived." The Grand Akpar speaks in his own tongue to a guard, who quickly leaves the chamber. Turning to you he says, "I shall have a boat readied to take you across the Great River. Come then, we will guide you back to the secret canyon." After a three-tides' journey you and Dr. Vivaldi, guided by a party of Archpods, reach the Bottomless Crevasse. Dr. Vivaldi runs toward a small metal craft on the crater floor. "A Vertacraft!" she says. "With luck this will get us back to the earth's surface." Dr. Vivaldi gives instructions to the Archpods, who then use their ropes to suspend the craft directly over the shaft of the crevasse. You and Dr. Vivaldi thank your hosts and bid them farewell. The canopy cover closes. You watch anxiously as Dr. Vivaldi checks out the instruments. "Are you ready?" she asks. "Ready." You grit your teeth as the Vertacraft accelerates into the crevasse and begins the 800mile descent to the surface of the earth. You're pressed flat against your seat. The g force is terrific! It's getting worse. What's happening? Can't Dr. Vivaldi stop it? You're blacking out.""")
    input("Press Enter to Continue: ")
    page74()

def page83():
    print("""\n\"There are three areas that fascinate me equally," she answers, "so I'll let you choose among them. To the west are the Weightless Peaks, where you become lighter and lighter, the higher you climb. To the south are the Hills of Diamonds. The Archpods are afraid to go there. They say it is too close to what they call the Lair of the Ghost Wolf." "What lies across the Great River?" you ask. "Beyond Rakmara." "The Shining Mountains. There we may find creatures whom the Archpods call the Flying Clera. They are great birds, who may be the true rulers of the Underground Kingdom—higher even than humans on the evolutionary scale. What would you prefer?\"""")

    choice = input("Do you want to explore the Weightless Peaks(1), Do you want to go to the Hills of Diamonds(2), Do you want to explore the Shining Mountains(3)")

    if choice == "1":
        page85()
    elif choice == "2":
        page88()
    else:
        page36()

def page84():
    print("""\n...........................::**::.:*VINMV:.......:**:...................
..............::*****:...*VMNN$N$NN$$$$$$N*...:VMN$$NF*:................
.........:::VIMMM$NNNNV.*MNNN$$$$$$NNF**VMNV*V$NMMMMNNNM:...............
........:*I$NMMMMIFMN$N:V$N$NMMN$$NMV*:*FVNNN$$$NNM*:::VV...............
........:VFNNNNN$$NMNIM*MNN$MIIFMN$N*F*:V:*M$$$$N$V:*:*M*...............
....:***INN$$$$$NNFIMM$N$$$$$MMMN$$$*:.:VVV$$$NMI*.:***VV*..............
....:*VN$$$$N$$$NMFV:*N$$$$MVVM$$$NN$MV***F$$MFNV****V**I*..............
..:**VVIN$$NVVFNNIMM*FFI$$$$F*VVMNVIIN$FINMMM:.:MMFFMMFVFM*:............
......*NNNN$NVIN$N$MNMMNNNN$NIVVMF**::VMNNNFV..:*MNV:VN*VM*::...........
.....*IMN$$$NV*VM$NMNIN$$$$$NNMN$V*V:..***FMM*****V**VVMV****...........
.....VI$NN$$NMF*VINMN$NNM$$$N$$$$M*V:..*F*.*MIFV:.**...*:*VN*...........
....*FN$$N$N$NNV**IMN$$$$$$$$$$NN$F*:...**..:IMV:.VF:..:**VM:...........
...:*INNNN$$N$$NMVVVFFINMN$$$$$NN$$F....:V:..*F*.*MV*...**FV............
...VMNN$NMMM$$$$NNNNMNNNMM$$$$NMN$$$:....VV..IVV:NMV::::*VNV............
..:IM$MMMFIFIN$I*VMIMN$NIM$$$N$$$$$$M*::*VV*VNNMNNMF:*IMIMM*............
..VM$NMMVVMMFNV..:..:V$NM$N$NN$$$$$$MI*:VMNIM$$$N$$NVMMN$$V:............
.*MN$MMFVMMMNV.......:I$N$$$$$NNNN$$N$NMN$$$$NMMMMMIFMMMMI*.............
.:M$$NI*IIMNNI:.......:VIN$$$N$$NN$$NV*IIMNNNIVMNNNMMNN$$V..............
.:M$$NVVVVIIMNM*........MNN$$NN$$$$IV.:**:FVFV.V$$$$N$$$N*..............
.:M$NNMMIV*VVMNM:......*$NNNNN$$NII*V.:::.*****M$$$N$$$$$V..............
..*NNNMMMMIV*VINI:.....V$NMNNMNN***:V.:*:.:**:V$$$MFIM$$NV..............
...:I$$N$N$M*VIMNI:...:NNIMIIFNI.V*:*.***..*:*:N$NNIVI$$FV:.............
....:VNN$$NNMVVVMNV...*NNVVIIMM*.V*:*:VV**V*.*.FNMMIFM$NVV..............
......*M$NNNMFFVVMM:..*NMIIVF$M.:VV*VFF*:*V::*:*NMMMVMNNFV..............
.......*VMNNNNMMVVM*..*$MMVFNNI:*V***F*..*:.:***MIVVVM$IV*..............
........:FIN$$NMV*VV..:F$NFIMN$V*V*:*I*VVV..****MMFV*MNIF:..............
.........:M$$NMM$NMM*..:N$NNIIN$F**:V*****..:VF:MIV*VM$IV...............
........*M$$$N$$N$$V....*M$$NM$$V**:...:*::..VN*NMMMMNNIV...............
.......:V$$$N$NNN$F:.....*MN$$$M***:....*:*..V$VNNNN$MMVV...............
.......*M$$N$N$NNI:.......*FN$$F***:....:**..I$INNN$$MIFV...............
......:INN$NMM$NN*..........*VF****.....:*:.:N$INM$$MIM$*...............
.....:M$$$$$$MN$V.........:::*V***:....:***.*$$I$N$NVINN*...............
....*I$$$$NN$NNV:...:*****VVVNF**:.....**V:.V$$$$$NVFNNM:...............
..*IN$$$$$$N$N*....::::**VVFN$$MIV*****VV*::MN$NM$$NN$NMV***:.:.........
.V$$$$$$$$$$$V.........:::**VVINNMN$$$$$$$$$$NVVM$$N$$F*::..............
.VN$$$$$$$$$NV:.:.......::****FVVM$$$$$$$$$$F::.*$$$$$V:................
**VM$$$$$$$$$MVVVVV************VVM$$$$$$$$NNV:**I$$$$NNI**::............
*VVFMMNN$$$$$$$N$$$NMFV*****VVFIIM$N$$$$$NIMNMMFMMM$$$NN$$NV:::...:.....
***VV*VIIIMN$$$$$$$NMV*:*:**VVVVVM$N$$$$$$MIMMF***VV**VVFVV*............
*V********VVIMMN$NMMV**:..::.:*::M$$NI$$NV*::*...::.....................
..::::**::::*****:*::::......::.*$$$VI$$$*..............................
.............:..........:::::***N$$$*M$$$$I:............................
.........:..........:::**VV*VVIN$$N$N$$$$$$NV*..........................
.........................:*V**VIMN$$$$$NM$$$$N*.........................
.....................::..::****VVVIM$$$$NM*V*:..........................
......................:..:::::*****VFIIIIV:.............................
....................................:*:.................................""")
    print("""\n\"You betrayed us," says the head guard. "The Rakas threw bombs into our boats. Nearly all of them were lost Many of our hunters were killed." He turns to the others behind him. "Bind them and take them to the Mouth of Fire." You cry out for mercy, but you know there will be none.""")
    the_end()

def page85():
    print("""\nA few tides later you and Dr. Vivaldi set out for the Weightless Peaks. With you is a young Archpod named Katu, chosen because she speaks your language. On the trek from the Archpod village to the Weightless Peaks, Katu tells you the legend of the Archpods who traveled through a shaft that led to a new universe. Few Archpods believed there could be such a place. Most of them thought that the earth was infinitely thick, that nothing could lie beyond it. "Now that human beings have arrived, we know that there is a whole new world right under our feet. We call your world the Nether World," she says. "We are curious about it. But we are also afraid of it, and of its creatures who could destroy us." "Sometimes we human beings are afraid of ourselves," you reply. After hiking for fourteen tides, you begin to climb—first gentle hills, then steep mountains. You tire under the weight of your pack, but Dr. Vivaldi urges you on. "It will soon be easier," she says. And she is proven correct, for as you struggle up the next steep hill, you feel your pack growing lighter, and you feel lighter too. Ahead of you, Katu is bounding up the higher peaks like a mountain gazelle.""")
    input("Press Enter to Continue: ")
    page87()

def page86():
    print("""\n....................................:*:......::...............::..................
................................::..:*******..***:.**:::****::*:............::....
.....................::::::::.:*IVVFFV::*VV:.:********:.:*VIV*.***V*.:*::::*V..::*
.....................:*VVVV**::.::*:..:::*V*.***:**..:::**V**:::**V********VFVVVVV
..:::...::..:*V*::***:.:***::............**VV:*:::....................::*****::***
..:****:***:***::**VFV*:::...............**:V*...........................::*:*V**V
....:*:*VFF*:............................:*:*V.............................:::****
********:................................*:::*F:..................................
VVVV**:..................................:*.:.*...................................
:::..................................:::***.:*V*..................................
....................................:IVVNI*:*FIV:.................................
....................................*IVIMFV*FN$$V.................................
....................................*F*VVVV***IIV*................................
....................................****:V********................................
...................................:*:*V:V****:***:...............................
...................................*V*V*:V*.:*:*:*:...............................
..................................:V**I*.***::***V:...............................
..................................*V**V*..**..*::*:...............................
................................*VIV:*I*:::...::*V*:..............................
...............................*MMV**VF*V........*V*..............................
...............................VFF***F*:*........****:............................
..............................:VVV**VF***......:*:****............................
..............................VVV***VF*V:.......:..**:............................
.............................:V*****V*V*.........:.:**............................
.............................*F******:**:.::::..**::V*:...........................
............................:VI*******.**:***:..**:*:V*...........................
............................:MMVVVV*V*.:*****...:*.*.V*...........................
............................*VFV***:*:..V**V*...**:*:*V...........................
..........................:VVV*:::::.:.:VV*V:...:V**VV*:..........................
..........................*FV****.*::*.:*IVV:....*:*IVV:..........................
..........................*VV:****V:.*.:**IV*....***VV*V:.........................
.........................*V******VV:*:.::*F*V....**V**VV*.........................
.........................**V*****V*VVV**:**VV.....:*****:*........................
........................:VV********:.::**V:*V*....::*:***I:.......................
........................*VV::****:*:...**V*.*V:....:::***VV:......................
.......................:V*:****:.:*:...**V***MV....****:**VV*:....................
.......................*V****V*:.***...**V*VF*V:....**::*V*VNV....................
......................:F****I*..***V:.::**FVV*VV...:*****V*:V*:...................
.....................VVFV**VV:.:****..::**VV:*V**:..:******.:**...................
....................VVVII*VV*..*V***...:*VVV.:V*:V:.:V***VVV*:**..................
...................:I*VVVVMV:..*V*VV:..***V*.:*****.:VV***V*FVV*........::*:......
...................*IVIVFM$**:.VVVVV...*V**:.:*V*:**.:V**VVVIIMM*...:***::*::*:...
..................:IVVF.VNMV*::FFVV*..:*V**.:****VFF**VV*VVVVMMNV..:VV:.*.:VFNNV::
.................*VMVIFVI$FVV**IVVF*.:VVVV:.:*V*:VMMF:*FVIVFVFN$N*:IIFV:**MMFV****
...............:FMVVVV:VIM$MI**MM**:*VF*V:..*VVF*MNNMV*IIIFMNM*::VVIFMMV****:.....
..............:VFVVFI:.*:*VIMIVNV**.*VMV*..:*VFNIV**VVINMNNNI::.*VVMMMNN*.........
..............VV***V*..:*:.*MMM$FV*:*VIV*..*VMVV*:...*M$NF****...*:NNFMNF*......::
............:VV****V*....**.:VN$NVVV*VVFV.:VV**:::**V:*F*::::...:*:*IVMNFV*:......
...........:**V*VVV*:.....:*:.V$NMMMVIIV*:*I*VV*.:*VNM*:.:*.....::*:VM$$MVI**.....
..........**VV*VV*.*:.......**:VIMMMV$F***FV*V*.*IIFV*...:......*..::*VMNNVM*:....
........:*VVF*V*:............::.*V$IMNVV*INV**:*FMV*:...*.....**.....:::MNVVI.....
......:*VVV*......**.........:*:.:VMNMMVVMMVVIVIF*V:..:**.....V::.::::..*NFVM*::..
.....*VVVV*...:..:*...........:*..**VNNMMMIVVMNF*VVV:*V*.....:**:.:.:...**IINM::..
...:*VVV**...::..*:............:*..:*F$$NFVVFMV*VVVV*V**.....*::....:..*:.VINMF:..
:***VFF:....:*..:V............:**:::*.*M$IMMMVVVVFV***V:....**::....:..:..:VNMM*:.
::***:......*:..VV............*:***:*:.:INNNFVFVVVV***:....:*::.....:.....::INF**.
..........*II:.*NV...........::.:**::VV***:*IMIV****VV:....::.........*:....*NNNI.
.......:::VVVFINN*...........*.:VVVVVV***::.*VMFVVVVV*....:*:........:*....:**NNM:
.....::**V*VVNNM*...:.......****IMI*.....:*::::**VVVV:....:*...:.....**.....:.*NV*
......:VMVVVF$F:...**......:***MIV:......:::::.:::*VV:........::.....**.......:V*.
...:*VIMMVMMFV...:**......:**VMV:...........::.....:****::....*:....:**...:::..*:.
.:*VVV*FFMMMVMIVVV*.......**FI*.............**:.....:::*:*V*:.*:..::***:::::*VF*::
**VFIVFNVNNNM$M*:........VFIV:..............:::...:VV:.:*:**VVVVV****:...:******:*
.:**VMMNN$$$MV:.........*IV*:..::................*V*:.:::**:VVV*:....::**VVV*:...:
..*:*MV**VVV*:.......*:*IV**..:*:............:VIV*....:.**:.:::*****V*VVV*:*VMV*::
..***:...*:........:*:VVV:**..::............VNMV:........:::::*:**:**..:*:...:****
::*:................:VV::.*:.:::...........:N$V:..................:***VVFVV**V*VVV
...................**:..:::..:*............*M*:............:*VVVVV**:::::........:
...............:::**:..**:..::...........:*MV........:**VVFVV*:::.................
.............::::**..:**....:...........:*I*::...:*VFNVV**:.......................
............::.:*::.*:...................**::.**INMV*****.........................
..........::.:::::.**..................::VVVVMIVV*::::.::.........................
.......::::*::.:..:*:...............::..VNIFV**:::::..............................
.........::...:..::..........*:..:::**VII*::..::::................................""")
    page87()

def page87():
    print("""\n\"Now you can see," says Dr. Vivaldi, "how on the Weightless Peaks the higher you go, the lighter you'll get Look!" She points to the highest peak of all. Its top is a spire jutting into the sky. A thin plume of smoke rises from the top. "It must be a volcano," you say. "No," says Dr. Vivaldi. "Something else is going on. The mountain's gravity at its peak is so weak that dust is being pulled off by the tremendous gravity of the Black Sun." "I bet I only weigh five or six pounds," you say. "I could easily climb to the top of that spire." "Better not," says Dr. Vivaldi. You realize that if you're so light, the huge boulders around you can't weigh very much either. You decide to test your theory. You nudge a boulder twice your size. It rolls into another boulder. Then above you, Katu screams, "Avalanche!\"""")
    input("Press Enter to Continue: ")
    page106()

def page88():
    print("""\nCertainly the Hills of Diamonds must be an amazing sight And, if you ever do make it back to the surface, it wouldn't hurt to have a few dozen diamonds in your pockets—you could be rich for life! The Archpods provide you and Dr. Vivaldi with their largest boat for the trip down the Great River to the diamond hills. After a journey of six tides, you hear a roaring up ahead. The Archpods quickly beach the boat. "We can go no farther," the leader tells you. "There are deep canyons and fierce rapids ahead. We must go on foot across the field of white clay." You soon find that the white clay is extremely hot. Your feet would burn up were it not for the light gravity of the underworld that permits you to race across the field in great leaps. Finally you reach cooler ground. Ahead of you is a dazzling vision: dozens of little hills of brilliant diamonds!""")
    input("Press Enter to Continue: ")
    page91()

def page89():
    print("""\nYou push the Emergency-Reverse button. Instantly you are pressed to your seat, almost crushed by the forces as the retro-rockets fire. The artificial weight squeezes the air out of your lungs. Then, slowly, the pressure eases. For a moment you're completely weightless. Your heart is pounding as you check the depth meter. The Vertacraft is rising! "You fool. What have you done?" Bruckner sounds wilder than ever. "I'm returning us to the surface, Professor." Your voice is cool. You feel confident now that the Vertacraft has responded to your command. "Why didn't you ask?" Bruckner's voice is bitter. "The auto-return isn't programmed to adjust for this gravitation." Bruckner sounds more sane now. It's you who's beginning to feel crazy. "What will happen then?" you ask. Suddenly the darkness is replaced by blinding sunlight. The Vertacraft has reached the surface, yet it's still accelerating, shooting up into the stratosphere! "Can't we bring it back down?" "I'm afraid not, my foolish young friend," Bruckner replies in a cold, dead tone. "It's a command procedure. There's no override. We're headed into outer space. Within a few hours we'll be frozen solid.\"""")
    the_end()

def page90():
    print("""\n...........................................................................
...........................................................................
......................:::**:.....................::*:::.......:*:::*:......
...................::*V**IM:...................:::.**::**..::*****V**V*:...
:................:*VFFMVV*:::...............:::****IF.*V**VVVVV*VVFV*MI**..
MV*:............:*IV*VMV$M*V*:.......:*::.::**FM:VMIV*VMI**VNNFV:**I**MMV*:
IVIFIF*:.......*IIVVMVF*FVVVF**:....:VIIFV*VFMI*VVVMV:VVMM*:*NNMVV*VM*IVMM*
NFFMNMVVV*:..:VMVVVVF*M*VMV**VV*:***IMVNV*V*VF*IM**NI:VVVVIMVIIMM$*V$VFNVVN
IMMFIMIVMMMV*VNNV**NV*IVVM****MMVVVNMNF*VMMMI:VVV*VFI***V*VVIIIM$NMMNM*MNVV
FMIMF*MNNVVVM*VV*VIMVMM**NF**VIMIVINMIMMMFMMI*F****VMVVVV**VIFVVNMFM$MVIMNM
NMVINNMMVIIMV*VMNNNMNMIV*NI:*V$NNN$NV*VN$***VINF****VI*VMV***VV*VVFFMVVIMNM
VN$$NNMVMMV*INNMIVVM$MNVNMVVVFM$N$NMV***V***V*IV**V*VFVIMMF*:*:VVINNMMNNIV*
MM$NNFF$NMMMV:*.:V*VMNNNN$MNMMNNFVMIVN**V:***:FFVVV*VVVFMIV::VV**INNNMVVVVI
$NFVV*VNVVFV*F**IMVFMMIM$$$NMN$NIFIVFIV****VVVFMMMV*V:*VVINIVVVIIMIIIVMIMMN
MMMFFMVVFMIFMM:*MIIIVV$M*VIN$$NIFV*IIMMIIF*VMFVVVVIMF*:VVFMMMMIVFIIMFMIVV**
FMNNMNNMVINMMV*VNVVNN*VII****VFM$MFFNMMMIF*VMMMVVMIIV**VVNFVNVVM$V*FVVMNF**
MIMMMNNVVNNNMVVVMMIINNFV*VMMMIV:*VVINNIMMMFVIM*V*VMMMV*MN$NMMNMV*VV**VFVVNI
IFNFFNNIMMNMFMV*VNNVVNIV*VVVFFFIMNMFVVVIMNNMIN*VI:VIVVN$N$MMMV*VV*VV*VMIMMV
MVVFINMV*INVNNMIVVVIVMIVVVVFMVVIVFMMIMIV*VVIMNMMFFVNMMMNNIV:VVNM*VVVVFVIMV*
MMFMMM**MMVVFIVV*VFNF*VMFI:*INMVFMIVVVVMNMF*VIMNNMMV**VV*V**FINI*VVFV*VVMV*
**MMMVVMNIVIVFI*V*FMV**::VFV**MNFV**NIVVVFVFN$NNI***F$F**MIV**V*VNMFVMMFMMI
*FNV*VFVVNMV:***VF**V**VVIM*FVV*VVFMFFVVVVFMNFV**F$NVMV:VV**VVV**VNVIMMFFVM
NNNVIM:VMNNV*FVVVIM*VVIVMMNMVMIV**VMMNMM$$IVVVVFMVFV**V**VI***:*FVVVMM**IIV
VIVIM:*FFMFVVIIV**MF*IFVM$NMNIMNVV*VNN$NMMVVFNIM$V**VVV*:***V*VMIVFNF*:*FM*
NVVI**FFFIII*VVIMMV***FVIIIIMMVIFV:VMNMMIV*VMNNMMI:*V*:*V*V*:VFFN***:*FMMV*
V:***VIVVVFV*VVMI**::**VVMNMMNMV*IVNMFNNFMI**V*VII***VFIV******FF***VIFIV:V
*VFV*VFVIIMMVVII**VFMVMMMV**FMMMN$NMNNIVVM*::*V*V**VVFV**V*VIIMVV*:VVVV**VM
IIVMIFV*VIIIMMMMFVV**VV*MFIINM$NNMMMMMIIVF***V*FVMM*:*VF**IVVVV***VV*VV**VF
VVFVMV*::VVMINMMIM*.******VMMVMFMMMMVVNNV*FIIIMNI**:VMV*VFVVVV:*VFVVMMFVVVV
*VV*IVIV*VFIVMNMMM*VMNMV$$$$NNFVVIVV*IF*:*IIMMMIVII*VVVVMI*VMFVNVINVVIMVVIM
VFV*F*VVVVIMIVIMNFVVMM$NMIMNNNN$NNMV***VFMIIIFFN$NMNMMI*MMVVMNMMVNNVMN$I*VM
NIVMMFIVN$$NNN$$$$M$$NMI*VVFIINMVVNMI*VIFNMV**IFMV*IMV*MIIN$NNNN$$MMMMNVVVF
NMFVVVMMFVVVIIMMVVFMNFMMVIINMNNMIVMIMVVMMIVVIIN$NIIN$$MIVIMMIFVVVIIMNNNMNMI
*VFIIVV*******V*VVMIMNNN$$MFMN$NFIFVNMNMM$NNNNNM**FFMNMV*:**VVIMV****VIFMNN
VV*V***::**VV*VVVV*VMNIIMI**VV*VVVIN$MMMIFIVIIMFF****FIVV..::::.:*:.:::*VII
:*********VI*:::.*VVIMIFV**.*V.*V*VII*I**:VV**:*VIV*:*V**I*:*:.::::******VF
***VFVVFV***VVV***::::V:***::.::.*IV**FFIV:*.:::***::::*:VIV::*:******:VFNI
::*******::***V***:::*::**:..::::*V**:..:V::.*:*V$I:.*:...:FMMV*VVV:**:****
.:**:**:*:::VV::****::::.:*:..:::****VI**V*:.:..:V*:.:.:*:**VNNV:*:::*****:
.:***VV*:..:::.::**V**::**:*..**...**VV:.:*:.*.:***..:*:.:*:.*NI**..::...:.
:::..:*:..::..::::*::**:*:..:.::....:**....::*::::**:**:::::*:I*.::.:::.:::
:***V**..****VV::.::***:::.::.*::*::**:....::**:::::**:::::****::.::::.**::
:::::*:.:.:::****...:::*****:**.:*::**:VV*.:.:...:::..:::..:::*:...........
:*::::****VVV***:::*V*****FV*V**VF****:V*:*VI**::***:..:..:.:...:.:**:::..:
.***:***VV**IIVF**VF****::::***V*VVVIN$F*VFIVV:.:*******::*:::....::*..:..:
.::::**:.:.:***:..**::*:V:.::******:*VVV**V*:*..........:::::::.::*****VV**
:::.::...::***:..******V::*:.:.:**:::.:V*:*:**..::****:.:::*::..*:..:::*V**
..:::*::*:...:..:*:**VF:.*:...:::**:*..:*:..:::.:..:::::.::**::**:******::.
..:***:.::**::*::.:*VM*::*::::*::*:::.::*:....:........:..::*:.::.:*.......
*::::***:::..**:.:*IMM:***::::..::..:...:*..:.:........::.::*F:.....:......
*******VV*V*V***.*M*V*:::::****:::..:.:**V*************:*..::V*.....:*:..::
..*:*:***::*V*:::F:*:....::::.:::......:::..*.*......:....::.:*::.:*******V
:::....::.*V*...V**::........:::...::..:....::*...::.::::::.....:::::...:..
.:*.....*VV*...******:..:.:*::....:*:..:......*......::.:........::.::****:
*::.:*:*IV*....:.:.......:::***::::*....::::::*....:**V:.:....::.:...::*:..
:....:VNM*:...::.::..:::*:.:*::::::*...****:..:..........::...:..::::.::::.
***::VN$F*:***:..:....::***V*:*:::*V:..::::*.:*:..........:::.::.:**:..:::.
*V*VMN$F:..:::..:::*::**VVFNIF*VVVVIV*******::**.....:::::****:*:::::*..:::
VFMIIIMNMF****VVV**VFIFMMMIIIMMIFVVVV***VVVVVVVV*V**********:*:...::.:::..:
*..:::*FM*V::*::***.:::*****:::*:.:**:..:....::::*:*.:****VV**V:..****:::..
V*::::VM***:**:*:......:..:*.:**:.::..............::....:.:*VVVMF**F*....::
:..::*M*.:....::..........:...:*.**...............:*:......:**:*VVMNM*:***:""")
    page91()

def page91():
    print("""\n\"Look at all those diamonds," you say. "I'm surprised the Archpods haven't already taken them." "Villa tarem, zaark!" One of the Archpods is screaming. Several of them point to the north. "Tarem Agax!" You can't see anything unusual, but the Archpods are deserting you, racing back across the field. "What's going on? Do you see anything?" you ask Dr. Vivaldi. She shakes her head, seemingly as confused as you are. "It must be the ghost wolf. What we are witnessing may be more interesting than the diamond hills themselves. We may be in the presence of a life force that the Archpods can see but we can't Or maybe what they see is an illusion, and we are right in thinking nothing is there. This is something that has always interested me: different realities for different observers." "I don't think we have time to figure it out now," you say. "You may be right," Dr. Vivaldi admits. "In any event, I would guess that the Archpods have good reasons for their fears. Are you willing to risk continuing on to the Hills of Diamonds, or do you want to turn back?\"""")

    choice = input("Do you want to say to continue?: ")
    
    if choice == "yes" or choice == "Yes":
        page94()
    else:
        page97()

def page92():
    print("""\n\"I think I know why the Archpods and Rakas avoid this beautiful land," says Dr. Vivaldi. "They are conditioned to the dim red light of the Great River valley. The broad daylight here bothers Mopur as much as it would bother us to live in semidarkness." "Why is it so bright—?" You are interrupted by cries from Mopur. "Clera! The Flying Clera!" Craning your neck, you see several great birdlike creatures swooping across the sky. "They are like nothing that has ever lived on the surface," says Dr. Vivaldi. "They may have evolved on some other planet." You fall silent as the music of the Flying Clera begins—a great chorus you hear not only with your ears, but with your whole body. Like you, Dr. Vivaldi seems hypnotized. "They sound truly angelic," she says. But Mopur tugs at your sleeves. "This is not the place for us," he says. "We are not ready." "I have a strong feeling that we must turn back," says Dr. Vivaldi. "Yes," you say, "I have the same feeling. Some force is pulling us back." Dr. Vivaldi's gaze is fixed on the Shining Mountains. "The Flying Clera are a very advanced species," she explains. "They have the ability to project their feelings onto us. Their presence and purpose here is a mystery that I suspect we are not yet ready to understand, but I feel certain that they represent a force of good in the universe." "If the Flying Clera are so advanced," you say,""")
    input("Press Enter to Continue: ")
    page93()

def page93():
    print("""\n.................................................::VVVFV**VVF*********VVV**VFIVV*IVVV*V
.................................................**NVVIVV***IV*VV****VV****VVV**VV***V*
.................................................**$V*FV**:*II***VF**VV***VVIV***:*V**:
................................................:*VV**FF***VFMF**VVV**VV**VV****V:::***
................................................*:IF*VIFV***VVVVVV**:*FV*VV*****::****V
...............................................:*:I*V*VFV**VFF***VV**IFV*VF*V*:*VVVV***
...............................................*:*VV*VVV*****V***VFV*****VVV*:*V**VV*F*
..............................................:*:FV**VV****VVVVVV***VVV*VVV::VVVI***V**
.............................................:*.*F**VV*****VFV**VVVVV**FV***VVV*IV*V*V*
.............................................*::V**VVVVV***VFV**FFV*:*VVI*V*VIVV**VVV**
..................................:.........*:.VV*VVVMVVV*VVFV**VV**VV*FFI**VVVVFV*****
...........................:**VVVVV**:.:...::.*IVV***V**:*VV**VVV**VV**VFI*FV***VMV****
:........................:*VVFVVVVVVVV*V:.:*.*MV**VFV****VVV**:::*V**V*VVV*VVVV**V*V:..
VV*:*....................VVV*VVVV**VVIVFV**:*IVV***V***:*VV**VV*VVVFF*VMMV*VFF*:::.....
*VVV**::...............:***:*V*:*I:*VIFIV*:*FV**VVVV*VV**VIV***VIFVFV*VIM**:::.........
***VIF**:::............*VVV*VVMM*M**V*MV::*VV::*VF*:*IV*VMFV****VVVVVVV**:.............
VVFFVVVV**::::........:V*MI*IVMIVV:.:VM***V****VVV*VIFVIIVFV**::**VV:..................
V**VIVVV*VV**::::::...*FMI::*VVV**:*****VVV*:*VV****VIVV*VV::**IVF*....................
*FVM*V*VV*VVIVV**::****VM**:VV::VVV**:VVV*V***VV*:V:*V****VV***VIV.....................
*****VF*I*V*V*I*FVVVVVVV::VNVVV***VVV*****.::::**:**.::::::**IFVVV.....................
VVVVV*VVVFVVV:V*V*V:VVM*.MNVVNIVIVIIVV**:::..........:*VVVVVVV*VV*.....................
V**VVIVVVVV****F*VVVVVV:VFVVV*VVVV*VVVV******:*:****VFVMI*FFVMFV*......................
VVVVV*VVFM*VF**IVIV***VVVF**VVVMV*FVV***VMF*V***VVI*VFF*VVV*VFF*:....................::
*V***FVVVVV*V*II*V**V*FVVVV*F*****V***FMVV****V**.:*FF*VVVFVVVVV*..................:***
VVV*VVVV**VVV*VVVVVVV*V*V*V**VVVIVVVFVV**VVV*:..:*VFVVVVVVFVVVFIV:...............:*VVV*
.*V*:........:**VFVV**V*V*F*V**VV*****VV**::::*VVVFVVVVVIFFVVIVI*..............:*VVVIFI
.*V*V*::.........:::*VV***VVVV*V**::*:*V:.*VVVFVIVVVVV*VIFFFIFF*............:*VIVVMIMFF
.*VVVVVV**::...............:::.:.......VIVVVVVIVVFVV**VVVMFVV*:............*FVVMVVVVIV*
..*VFFFVVFVIVV**:......................*FVVVVVIVVV**IVVVFIFV*............:*V*VVVVVV*:.:
...::****VIIFIIMFV*:........:*VVVV***:**VFIIFFFFVVFVIVMIV*:.............:*FVFVVFV*.::V*
............::**VVMFV*:....*V***VVVIVVVVVFMFV*VV*:::**:................:VIIMIVVV*:*FVVV
..................**VMMV*:*V*MIVVVV**VVV******VFV*:...........::......*FIFIIVVV*VVFMIVF
......................:*IMMNFM$I****:.:**V*....:*VIF*:.....*VIVIV*:.:VMVFVVVVFVIINNMFVV
.........................:*VVIV*V*****VV*:........*VVV*:::VMIVV*VF*VFMMIMFFIMFVIMVVV*:.
..........................VVV*:.....................:*VMFFMN$II**VVFVF*VV*VFIV***:.....
..........................:............................:**I*IIM:****:::::VV**:.........
.........................................................:VFF::*******VV**:............
.........................................................::......:::::::...............""")
    print("""\"why don't they rule the Underground Kingdom?" Dr. Vivaldi smiles. "I don't know, but I would guess that not wanting to rule others is part of being advanced." At that moment you are overcome by a strong desire to return home, to the surface of the earth. You exchange glances with Dr. Vivaldi. "Do you have the same feeling I do?" you ask. She nods and motions you to follow.""")
    input("Press Enter to Continue: ")
    page94()

def page94():
    print("""\n\n"Let's get to those diamonds," you cry. And
you run toward the points of sparkling white light.
At the same time you begin choking on thick
sulphurous fumes. Behind you, thunder rumbles
from the ground!
Dr. Vivaldi has reached the first hill of diamonds. "They're the real thing!" she calls, sifting
them through her hands. "Within a few yards of
us are more diamonds than are worn by all the
people on earth!"
"Look!" you shout, for now the fields of white
clay are bubbling like boiling soup. Pale yellow
gases rise from cracks in the ground.
"We are trapped." Dr. Vivaldi's voice sounds
far away. "By the time the claybeds stop erupting,
these fumes will. . .put...us...to.. . sleep."
She coughs and staggers a few feet up a small hill
of diamonds. "Quick, over here!" she calls.
Gasping, you stumble up the hill and collapse
in a mound of diamonds. Dr. Vivaldi breathes
deeply. "We're safe for the moment This hill is
well above the toxic gases." Her voice is drowned
out by the ground thunder.""")
    input("Press Enter to Continue: ")
    page95()

def page95():
    print("""\"It looks like we're stuck here with all these millions of diamonds," you say. "Maybe not," replies Dr. Vivaldi. "The eruptions are quite localized. The gases are rising, but I think we can make it across the deadly strip of clay—it's less than a hundred feet, I'd guess. There's only one way to do it - take a deep breath and run as fast as you can. Don't breathe until you absolutely have to. Are you willing to try?\"""")

    print("""\n.:**................................................................................
.***................................................................................
.**:..*:...................................................................:........
.:V*::*::....................................................::.:**:......:*:..:....
.***.:*:*:.***:.:.*:.:*:.....................:::::*:...:VV:..:..::.::******:*****...
.***::*::*:*:.::*:::***:.................:****::****.....:******:.........::*...*...
***:***:.*:*........***..:*:::::**:.......:**:..:******.*.:VV*:..::::::**:*:*****...
**:::**:****::...**.****:..::VV:::.::*::::*:V**:*...*V*.*::**:...:V:..**:.*:***V.*..
.**..::::*..:***:...:**V****:.:.:::***::*:VV::*:*:..::*:V::*:.:*::*:.*:.*.:**::*:*..
.**...*:.::..:**:****V******:VV**:::::*:***V**::**VV***:V***:.V**:*.:*:.*::*:*****::
.**:.**:*:*...*:**:*****::***..........*:::*::.::**V***:*VVV:.*V*...:V***:*..:****::
FIV:.VIIV:**..:**:**V*V***:*:..:*********V***::*:**V**:.:*:**.:V:**:::*:***..******:
VV*:*IFV*:***..*IMMV*VVVF**:*V***..::::.:*V*I*:*V***V*..*IV**:::.VV*.*FVVV*.:VV*V*:.
***:*FI*V*VVM*:V*VVVFVVFV***VVVVVVVVVVV***FI*IVIIMFVV*F:***VM:*.:VV*:VI*.*::.::.VMV:
V**.***V******:*:**V**VV******V***:******VINM$$$$$$N*NI.*IFVV:V.*V**:*::*.*::**:*:..
I*VFVFIV*IVIMV:***VFVV*IF***V***V:***::::*V*FMNNMN$NM$I.*$$$VIN.*MM*:*VVV::.*V*:*...
VVVV*VV**FVV*V*:**:::*.*VV***:........::..:..:****:*VVF:*VVV*VV:*VV***VFI:..*V**V:..
:VV**.:*:*:::*::*VFVV:..**VV******....:..:***::**V**VIF*:V*VVVM*:**.V****...*V***...
:*VV*:**.*::*V:**:.:**:**....:::::..:**:***IMVV*V***:*.*********.VV:V***V...::::....
.**.*.:*::...*.***::*:VVVVVV**::.::....:.::::**:..:.....:*:***.*:**:*:*:*::.*****:::
:**.*.**:*:..*.*.*VV:*V*****::****VV*::V****:*:......::*******V*:V*:VV****::V**:*.:.
VIIV*.VV:MVVV*:V:.:*:*......:**:.....:.:.::::::*******::V**V:*VV:VV.V*VIV**VNMV:I*:.
MINNV.VV:FVV*:***:.*:*:*:.......:::............:***VV*VN$$$$VI$F:NN:VMIV*****V**:...
MIM$V:MV*$NF:*FVV*:**::**::::.:::::*:...:*::......:::::VIIM$VFMM:M$**$$$V*:FMM:VVV*:
*FM$V:M*V$NF.V$NMIV**:**:****V**V***::*....::::.**VVVVFMIVVVV*M$*I$M*$$$*V:I$N*M$I::
:*VNF*I:MNNM:*$$$$M:*::..::::*::....::::****************::*****VFMMM*N$F*V:I$V:M$V..
.:*NNMV:N$$M:*M$$N**VNM*VV**VV**VV**:::*VV*VVVV*VV*:**:....:..:*::***INMVNIN$MVN$M:.
::*M$NI:M$$M:*V$$**MV$MNM*.....::::*::*V**V****:::.......:*.:**********V**:V******:.
::VNNFV:VNFF::*I*.:MM$$NNNMFV*::::::.............................:*::...:*******V:..
..:::.:.::.........:*:::::*****VVV****::...............................:VV******:...
.................................::::*******:...........................::::::......""")
    choice = input("Are you willing to run for it? ")
    if choice == "yes" or choice == "Yes":
        page101()
    else:
        page102()

def page96():
    print("""\n...........:*:.......:::*.....***.::*:.......::*:.....*:.....V*:.........
...........::..:*.:.**:**.....:*::*.*........*::.....:**....:VV..........
........:......:V:*::V***.....:*:*:.*.....*:*::......*V:*..::*:....:.....
.......:*:.*:..:::*V***::::...:*:***:....::*****:...*F**..:*:*....:V.....
.......**.***..:***:*VV**:*....*::**..::*:**.***::***F:...**:....:::.....
.......::.:*V..:.****VIIV***VVV**:*::**:::*:.**VVVIV***:::**:...:*.....::
.......*:..**..:.**::VFN$V*V*VNNNV:*******V**VMV:IMF*:.*:.*.*...**.....**
.......**.**V*:.*V:.:FVFIIM*VMVVIIVVV*VVVMIM**I**$NVV*.*V****...**.....**
.....:***....***V*:..VMMV:******VMMFVMMM*:*VIV*.V**IIV.:VIV**:..:*:...:**
.....:*V:....V:*::..:*IMV******VVVV****::****VF***IMF*.:***:**..:V*..***.
.....:V*::...***.....*MMIMVVVFV*VVFV*.*V*VVV*VM:*IMFVV.***:..**.***.*:*..
....:*V:**...*V*:*:..*MM*V*..*MIVIMMVVIIVIMV:*V*:FIV*V::VIF:.*.:*::*::**.
.....**:*:.:::**.**..*MNVVNF*MM*FIF$$$$$$NIMFIFFVNIMV**::*V:::.***.:****.
.....:**:::::V*.*F***VMI*VMV******:VVM$MIV:*FIVV*:::**VV:****:.**:...*V:.
.....*******:*.:VIFIMMV*VIVVV**.*:*:.:V****VVVVVFV*:::*VVV*V*V::...:**:..
.....*:.::***V:*FFMMV*VIFVMVN**I****VFV$FMVMN*IMNM$I*:*IMI****V*:****:.::
.....:*::.:.**.*I*IV**VVNN$NN*FNV$VMV$I$N$NN$FI$$$NVV*FI*.******::*.:*:::
......**:.:**::FV*VF*:V*$$$$$VM$$$MNNN$N$$N$$VMNMIVV:VM*....*V**:*::*:...
......::.*.:*.:IM**IFVMVM$$MNMI$$NNN$IVMMVMN$MVVVF*.*MF*:...:V:**.*:.....
..*:....::*::.*V*:**V**:*VNFV$MNNNMFMNVMV*V*IV*MMV::VIV*:..::*:**:*...***
****:..::::*V.:*:..:*VVFV:*FVVNV***V:M*MV*:.**:MNFVV.:*.*....*:*:*::**:..
....::****.**..**V***:*:..:.**VVM$V:***MNM*.VM****NM*..*V.:V*:.*::..::...
..........::...:V*VVFIMI*V***V*VNNM::::MMMM:*V***MIFI..F**FNV:***..:**:.:
.........:IV:::::.:*::VMVVIIIMNVNF$M**.FMIV:V*.:*VVV::*MV**MV**:*..*:*:.*
***:::*..*NV*:M*:FV*:I*VV:::**VV::VM**:VVV*VI:.*M:*I:*MM**VV*V:*:.::::.::
...:*:...V**::MFVVV.*M:*NNIV**:...FN:.:MFV:*M*:IMV.***II:*::*::*..*:*:.::
...*:....:**.*F*..:.:V:*MMMMMN*.:VNMV.*MMM*.*M**M*.*VVFV**::V:::..**V:.**
..::.....:**.*::VI*.VMV.*VMFMM:.VMIFM:*IVFVV:V*VM*:*VVV**N*:F*::**:***.:*
..::::...*:*.*.*FM**MV*..*MFMV.:IIFMN..VVIVIF:.VI:*MM*VNVN**N:****:**..*V
...:*V.:**:******M:****:**MMV..*MMMM:.*FMM*FI**V**VMMMMMVM:*N*F$N*VV*:.*I
....:*:*:****:**:*.*.:*.**VV*...VVVV.:IV**VFIN$$NFFF*******II*VMF:*VIM**F
....:**:**V**:**.*:**V*.V*FI:..*MM**.:*:*VVV$$$NMI*V*V*******.**:*****:*V
....:**.:******:.V**.**:V::*...*:**:.***VI*FV***VV:VF******:*:******:*:**
...:**V**VVVVVV**V*:*:V**VV:.::*:*V::*VVFMMFVV*.....FNFVVV**:**V***VVVFMI
**VMVV*VINNIVNMV:*:...VV*FV..***.:**:*N*I$NNNM$*....VM:.*V*:V*VVFVVVFIMMM
******::*VFVVV**.*:..****V*V*V*******:VFNNNMIMMV:....*::***:******..:::::
.....:**VVVVVVVM**F:*V**V*:V**:*:***V.*VVFMVFMM*:....:IFVVVV*VV:***VVVV**
...:::****::***VV:V*VMV*V**M**I****:*:**::*IVMVI....:::***:::**.:........
.......::.:.:*VV:.**VV********:****.****:.***VFI:...*I*VV*:**V**V*:::.:::
....:**VVVVV**:*.:**VVV*******.*F*V**VM*FFV:VVIMVV**M$$$$NVVVVVV*VVVV::::
....::::...**:.::**VVMI$$:I$$I:FI*MMV$$MNNV::*VMN$$I**VMM$I:.::.:.:**V:.:
......::*****MMVV$$*INF$$VN$$$MNNM$NNNIV*:::****V$NV**:VM$$I:..:..:....::
:*VVIMMMMN$$V$$VV$$VMNI$$NN$$NMIIVVIMMIV*....:***$N*::*:VM$NVV*::****.:*.
:**:VN$$$$$$$N$$$$$NNMFV****....::..:::*VV*.:::*:*******VVIFF*......*:*..
.:*M$$$$$$$NNNN$$$$$$$MF*::*:.......:::*.*VV*:......****:*:V:*****VVVVV::
:V$$$$$$$$$$$NNMN$$$$N$$$NF*******::**V******VV*..****I*:FIV.VV*V:**V**::
M$$$$$$$$$$$$$$NNN$$$$$$$N$$V:..:*:..**...:.:*:*V**V:*V::**:.*:*:******::
$$$$$$NN$$$$$$NN$$$$$$$$N$$NN*....:***V*:***********V**.:V*.:**.***:**:.:
$$NN$$$NMN$$$$$NNN$$$$$$$$$$$M*V*****:*****.*****..VVV:..**.**:*V:***:...
$$$NMMNNMMMNN$$$$$$$$$$$$$$$$$*......::***:::*:.:::***.........*:VV:*.**V
$$NNMIIMNNNMMMN$$$NN$$$$$$$$$F*:........**:*:****..............V*:VV**VMM
N$NMNMNMMMNNMMMN$$$NN$NN$$$$$V.**::*:*****V*VVFVFV*:..........*V**:...::.
MN$NNMIMNMMMNMMMM$$$$$$NN$$$$V..VMMFV**VFIIV$$$NNNMIV:.......V$$VMMVFVVV*
NMN$$$NMIMNMNNNNN$$$$$$$NN$$$V..:FVVIMMNMM$N$MNNMNNNNF:.....*$MFV*::***:.
$$$NN$N$NNN$$NMNN$$$$$$$$NN$$M:..***V*:*****VII***:******VVVMIV*:.....:*:
$$$$$NN$$$NN$$$NNNN$$$$$$$$$$$I*..*:::.::...:*VV*:*VINNNNNMMNN$$NIV:*:..:
$$$$N$N$$NN$N$$$$$$N$$$$$$$$$$$$V..*:...:*::..*VMNNNNNMMMMIFIMNNN$N$M***V
$$$$$$$NNN$$$$$N$$$$$N$$$$$$$$$$$F**:....:*FVFNNNMMMNNMIFVVFVVMNNNN$$$V::
$$$$$$$$$$$$N$$$$$$$$$$NN$$$$$$$$N*VVIMIIMN$NMMMNMMNNNIFFIIIVVIMIMNN$$M**
F$$$$$$$$$$$$$$$N$$$$$$$$$$$$$$$$$$$NN$$$$NNNMMNNMMNMMMMMNNMIFIMMMN$N$$N*
VVVVN$$$$$$$$$$$$$N$$$$$$$$$$$$$$$N$$NM$NNNMNMN$MMMIMMNMFNMIMIIFFIFMMN$$M
....:VIM$$$$$$$$$$$$$$$$$$$$$$$$$$NMMMN$$NMMNNN$MMMIMNMNFIIIMFIFVVVINN$$$
.::****VVVVMN$$$$$$$$$$$$$$$$$$$$$NMNN$$NNNNMMNNMMNMMNNMIIMMMMMIVFVVM$$$$
.......:::**VIV****VIMVIN$$$$$$$$NMNMMN$MNNMMMMNMMMIIIIIMFIIFIFIIVVFIMIMN""")
    page97()

def page97():
    print("""\n"I don't believe the Archpods are running from
nothing," you say. "Let's get out of here!"
"OK!" Dr. Vivaldi starts back across the field of
white clay, and you are right behind her.
Running as fast as you can, still loaded down
by your pack, you feel a rumbling beneath your
feet. The ground begins to split apart. Great
slivers of clay are heaved up. Wide cracks open
around you. You think back to when you fell into
the Bottomless Crevasse in Greenland. This time
there may be no escape.
You see Dr. Vivaldi crawling on her hands and
knees, trying to work her way from the edge of a
crevice. The ground is shaking so hard you can
no longer stand. The air is filled with yellowish
haze as sulphurous fumes escape from beneath
the surface. Looking up, you see the blurred gray
form of a wolf looming as large as a mountain,
crowding out half the sky! Its bared, curving teeth
are like rows of elephant tusks. Its hot breath takes
your breath away, and the red world around you
goes black.
""")
    input("Press Enter to Continue: ")
    page103()

def page98():
    print("""\n"We mustn't waste time," says Dr. Vivaldi.
"The Bottomless Crevasse closes a bit more every
day."
Led by the Archpod guide, you begin the long
trek back to the Great River.
Six tides have passed before your party descends the mountain trail into the valley of the
Great River. You are eager to get back to the
Bottomless Crevasse—your only hope of returning to the surface of the earth and home. As you
strain your eyes, looking for the Raka village, you
see two figures headed toward you up the trail.
They're human!
"Can it be?" you cry.
Dr. Vivaldi stares through her mini-binoculars.
"No doubt about it," she says, "Larsen and
Sneed! They made it here alive!"
""")
    input("Press Enter to Continu\ne: ")
    page69()

def page99():
    print("""\nMIV**IN*.:*IMI***VVMV:VVFVVIIMM$NNNMFVINMVVNM*IM**VF*:IFVMMVFMMIMNIINMN$I**:*IV*IM**
V**MNN*:*:IMMV*VNI*MI*MVVFIVVIVVN$$MM$NI*VMV*VFIV**M**VMFIMIIN$N$NNNNNMVVVVFMNNIIF*V
**F$M**M**VFV:VM$NMNMV$MVFIIV*VVVIN$$$$MMNV**IMMFMN$MM$NMMIIMMMMMMMN****VVVFNMMIIMII
*IMNV:INI*FNMMMNMNMMMMMMIIMMMMV**VIMM$NM$NMVN$$NMMIM$MV*VFMMVVVV:.*V*M*VVVMVVVIIIFVV
IINFVMNNMNMMIFMMMMMM*..***FV*MNNFV*VIM$$$$NMMMIFVFVIMMIFFFVVVIFVVVVMNV.*V:*V*VIIVVVM
NNNN$NMMMIFMMIVFFN$V***F**V*V**V$NN$$$$$MIIMIVVVMFVVVVVVVVMMVVIMMFMNV:IF*:**VF*:*VIM
$$NNMMNNIV****N$NFV*VIN**I*FFMV**IM$$$NMMMN$MIMIVVFVVVIMMMVVV**VMNNV:VNV*INF**MVV*:*
MNNNIV*VVFMNFMFV**VFNMV*M**N:*NF:***VFFIN$$IM$NNNMMI****VVVVV**M$MVVVVNFVFNMN**VFFFV
MV***FNNV*MMMV***VMNF:VM*.:I*.*MF*****V*:*FFVVVIVFNNN$NM$NNF*:MNM*INMMNNNMMNNNV**VFM
**IMVVF**FNNF*.VN$NM:*MIV**FI**VIMIMFVVVVVVINIVVVV*VVV*VMNNNIMNIVN$$MM$NFFFIIMN$NIVI
N$NIMMVVNN$MVFIMNN$V*MMIMVV*MI*VVVMNIMIIMIMIVMNVV**VV*VNNNNN$$$N$$NI***V:*::.:*FIIN$
MMNIVINN$$$N$N$MIIVM$$NIIMMNN$$MNMM$$NMFFVVMMMIINMVVIMNNFV**V*MN$IMVVV:**VVVV*VFVVIM
VMMMNMMMNNMM*VV*::.*FII****V*VMNV*V*:*:::.**FM$NN$$$MVVV*:...:*:*:...:V*VMMIFVFMMIV*
**VIFVFIV*:**:VV....:****V*VVVVV*.:*..:V**:***FMMMNM*V:*VV::**:...:***VV**VV:.::V**I
.::**VIMV***:.::..*****::**:**:........::*VV*:****V***::*VIIV*:.......:*:..:.****V*:
VVVVVMMMMMIFV*VV***IFV:.*V:::........:****VV*****V****VVV*:*:...:::*.:.....:.:::..**
VV****VVVFMNNN$$NNVV*:.**V:......:*:VVV*..:FIV**IVV*::*VV*:**VMFVVV*.*...**V****:...
VVVMMFVFVFVFIINN$MVV:**:::..::::*IV****:..::*::*****...**VMNNN$M*:**:**VFV:V**:**:*:
:::::.***::..*VVIMIIMMVVV****V*:**:*::*VV.....::.:*..:*FIM$V*VVMVV*VV*V*.:*V*FVVMV**
VVVV*::***VV**V*VFVVVFNMMMNNIFV**:.::::::........:****:.:VFFVVM$$$$$$MIMFIN$$$$N$NNN
::*V*V:*::.::::***V*:::*VMN$NNNMIVVV******::****::**::****VMMVVFN$$$NVNN$$MF*VF*VMIM
***::V**VFIIVVV***:***VFMIIN$$MVM$NMMMIMNMMMMFIFMIIMIFVINIVVV:***M$$MIVVI*:***VV::*V
:...*V***:*V**MMF*:::.:***:***:VIVVVVVVFMMFNMMNNN$N*:**VVN*V*M$MMN$$IMV*V***V*VVVV*:
.....*VV*.*V**VVVV**::**V****:**FVVFFFVIMMVIVF$NNNV:*:I$N$$NN$$NNMFVV**.:::.:V**.*V:
*....:::...:*.:***MVVMMIV**VI**:::**VIVVVVFFIIFIFFM$NNNNNMMV**V**::V:::......:::*IV:
..:*..:V::*.:*::*VNMIFVFVVVVV*:...::*FVV**FFVFVVVIIIMNMII***.:V:...::.:::*.:.***:::.
MFIVIVNNNNMM**FVVINMIVV*:::*VVV****:*V****VFVIMMMIIMV*V***:V***:**::::***V*V::*.:..:
NIMNNM$NNNNMM$$$$MMFMMMMMMNNFVMNN$MVIMMVFVIMMNNMMN$MFVVVVI*:VFV*VIMIFIV*VMNNFFIIMVVI
N$$$$MMNN$N$MFM$MN$$$VVFFMMNFIMMNNNNNF*VFVFMNNNNNMMM$$MNNIMN$$$NMNMNVMNNN$$$$$$$N$$$
VF$$MINVMMNMVV*VMVVV**::*::*:*VVV*VVVVVVVVIMMIIMV*V*VMMMVMNN$$$$$NMNNMMNNMM$$NMMMMMN
VV*VVV****:*******:***:...::::::::::**:***V***VVV**VV**V***VVMMIVMNNNMVVVVINNNNMIFFV
***::::***::::**********::::::::....*****V*****VV***V*:*:::*********VVVV**VV******:.
...........::::**:**************::**:*********::***************:::************VVV*..
::*****:************VVV*************::*************************:*:**:*******VV****:.
::*::**:**::::::::::::::::...::::::***:******:::::::*::*******V*VVVV*VFVVVIIFVVVV:..
::*********:::**:**::*::**:::*:::::::.........::*..:*:::***V*******VVVVVVVV*V*:**::.
::***::::****VVV****VV****V*****VVVVVVV*************:..*:*****VVV**VV**:*****VFV*:::
*:*******************::::*******V*VVVVMVV*VV*V***VVVVFV**FV*V*::*:.:::::.:**:**VVVVV
F*VFVVVIIMMIIVVVVVV**VV**VIFVFVVVVVV*VIVVVMMMIVFMNN$MVFVVV**::***.::**.*M$I***:*:*VF
*****:**V*V***:*VVVMMNNVVMVIN$I*FIIVVM$MFVVMVIIIMFM**:V*::.*VV*V*:**:.*NNN$NV*..:.*F
V:..:.:.:.*F*::****FVFI**VVMN$MIM$$MVVVV**V*VMNMVV*...:..............:*VFV*::VV:****
................:*VV***INNNVNMMNMMNMMMIV*MIFNFFFV*:.....**...*:**VV**:.*:::*::..:.**
:......:**::*V*..:::.:V*MMIFNNNMVIMMNMFV*FFFMMV*V*:*::*VV::::::V:V**.*:::*.**:*VI*:*
:......*VV::*V::.****IV*FNIN$$MIMN$NIFV*VV***VIFV**VVVV*:.:*V:::**::**MMVVV*VFFN$$NM
.::....:::...:.V*:*V*VFFIN$$$$MM$$$$NIVV*.*****VVV**V***V***F:***VF*VINMN$NMNMV*VVMI
V*:.....:*.*:V*V*.*VFM$MVVM$N$MN$$NMII***V***:**VIMV**:*VM**VV:*::**IM*FIV***:V**.:*
:*:...*VV:**:*::VIIINMMVVI$FVV*:VMNIMMIV**V*FVVVVIMNMVVM$$MNNIVV**V*V*:*V:.::.**....
V**.::*IM$$MMMNNMVVMMIVVVFI*V****:*****VIFMIV*:*:**VIMMMIMIMMIV*::***:::*****.:.*:..
VMVFIVINNN$M$$$NIV:****.:***VVV::::.:*V**MIIMMVV***:**VIMN$FVVV:**..**V*:***..:.:.::
:**IMMNNN$$$MVMIVIVV***V*V**V*VV***...:**V*IMIMIV::***VIMM$$NMMFVV***:**..:*.*V:....
V**::*VVVFIIVVVVVVVVFIIV**:::****F:::..:*V****VVVVV*VVVMN$$$N$$$$$M:::...***.*V:::*:
:V***V*V**FNIV*:*VFMMVVFVV**:***:*VFV**...::::**IVV*V*I$N$$NN$$$$$$MV::::V*V*.*::***
.:***..:**VIV*:...:V*:********::*VVVMMV:*::::::VMNNIIIN$N$$M$$$$$$$$$V****FV**:..:**
:.:::..:**VMMVFIV***VFIM$NMMMIV*:::*:**VVVFIV*:**I$$N$$$MN$N$$$$$$$$$$MFMMN$MNV**FII
V*.*:.**VIVMMFVVFFN$$NINMVNNM$NNFVIVFFIMMMIV*VV**M$$$$$$MN$N$$$$N$$NN$$$$NMMI$NNIMN$
*:...:*V*VNI**VFNNMN$IVV*FVVMMFMN$NMNV*VVVFVVVVVVMN$$$$$MN$$$$$$$N$M$$$$$MM$MMVN$NMN
::***.:*VINNMIINMN$$NI*VF**VMMFINNMMNI:::*IMMINMN$$$N$$$NNN$$$$$NN$NN$$$$M**VN$$NFMV
.V*V**:V$NMIFMM$N$$$$MVMVVINNMIM$MMMNVFVVVVFVM$$$$$$NN$$$NN$N$$$N$$NM$$$$$$I*:*VIINM
**MNIVMMNMMMNN$$$$$$$FM$MMMIIMN$$$$NIVMFIIMMM$$$$$$$$$$N$MN$NM$$$$$$MN$$$$$$MV::***V
NN$$$NNNNMMMNN$$$$$$$MNNNMNN$$$NMNNIINNVVMFMMI$$$$N$$$$N$M$$$N$$$$$$NN$$$$$$NN$$$NV*
MN$N$$MNNMMNN$$$$$$$N$$NNN$$$$F:.*IFINMNMMFNVM$$$$$$$$$N$NN$$$$$N$$$NN$$$$$MINI*V*..
$$$N$N$MNM$NM$$$$$$$$$$NN$$$$M:.:FFMMNFMIMM$VM$$$$$N$$$$$$N$$$$$$$$$$$$$NVV*.:*.....
M$M$$N$$$NNNNN$$$$$N$$$$$$$$M*..*MVMMVIVMNM$IM$$$$$$$$$$$$$$$$$$$$$$$$$NI:.:.......:
FNI$$$$MM$$F*IN$$$$$$$$$$$NI*:.*NMV$FVVMINM$IM$$$$$$$MNN$$$$$$$$$$$$$$IVV:....::***V
F$IMIM$MNMV*VMN$$$$$$$$$$F**NMMINNIMFFFMMMINNM$$$MVFM***V$$$$$$$$$$MVV*::.::VVVVV*VV
IMVMNNNV:***VMIMNMMMVVMMMIMN$M$MMN$INVIMM$VFIN$MIV*IV:*:*VN$MFFVVV::......:V******VV
F$FNMNF*:****:*V**::.:*VFMIFVMMMN$MMNVVMINFNMNNM*I$M:...::IV:...:**..:.:*:******VVVF
M$$$IVVV***V*V*:..**:..***....***MN$M*VNNMI$$N*MV:**.....*V:**..:**:.:*.*V**V*VMNNNV
$$$MVVV*.**VVVV*:****.:*:..:.:**.:F$FVMNNMI$$V*VI*......VI*.:**:.*V:.:*:.*VV**V$$$NF
$$$IVV*::*V**********:***::V::VV*:.*VMNNNFI$N**VFV.....VVV:.*****V*:.:**.:****N$N$IF
$$NFF*..*****************::V*.*VV*..:V$$NMN$*.:VF*....*V**:.****VV*:..**:.***VM$MMMV
N$MIV..***:****:*********:.*V:VVV*:..:V$$$$V.:VIV....*FVVV::*******:..**:.:***VMMVNF
$$MFV:.******************:.:M*V****....V$$N:.*IM:....VV*V*..:******:..***..***VINIV*
$$MVV..*******************:*IVV*****....*$F*VMM*....*IV***:..******..:***:.****F$IV*
$$IV*..:*******************:VMV***VV:....VNNIF**:...FI**V:..:******..:***:.:***VNVVV
NNFV*.:********************:VIV******:...*$M*****..*NV***:..:******..:***:..***VM**F""")
    page100()
    
def page100():
    print("""\nA\n\nt the change of tide, Dr. Vivaldi leaves for her
interview with the Grand Akpar. Only one Raka is
left to guard you. You hand him the gold bracelet.
Taking it, he smiles broadly. You hurry past him,
but another guard is standing outside the agon.
You wheel past him and run for it. The surprised
Archpod yells; you soon hear others chasing you.
But in a few moments you reach the shelter of the
cluster-leaf groves, and as you go deeper into the
woods, you are relieved that you no longer hear
the Archpods behind you. It's strange,though,
that they didn't follow you into the woods.""")
    input("Press Enter to Continue: ")
    page72()


def page101():
    print("""\nAt the change of tide, Dr. Vivaldi leaves for her
interview with the Grand Akpar. Only one Raka is
left to guard you. You hand him the gold bracelet.
Taking it, he smiles broadly. You hurry past him,
but another guard is standing outside the agon.
You wheel past him and run for it. The surprised
Archpod yells; you soon hear others chasing you.
But in a few moments you reach the shelter of the
cluster-leaf groves, and as you go deeper into the
woods, you are relieved that you no longer hear
the Archpods behind you. It's strange,though,
that they didn't follow you into the woods.
""")
    input("Press Enter to Continue: ")
    page108()

def page102():
    print("""\n....................................::**:::.....:...............................
.............................::**VVFV**::..:::::*:*:............................
..........................:*****VINNFMMIFVV***V*V***:::.:.......................
......................::*****::.*N$M$$$$$$$MV*:*VIVV::****::....................
....................:***::....:*M$$$$$$MMMMNNNNF*:*VV*::***:::.:....:.:.........
..................:**:.....:*VI$$$$NNNMMMMIFINNNNV:.:*:*V*******:.::*:**........
..............:**:...::::VFMN$$$$$$$NNNNMIMNMMIMMNM*....*IF***:::::*****::::**::
..........:::***::****IINN$$MN$$$$$$NI$$$$$NNMMIMM$NF*.::.**VV*****:::***:::*:**
........::**::::*VM$$NIFN$$NM$$$NII*VVFMN$$NNNMMMMMNNNIV***::***MV*************:
.....::*:******:.*VIINV::I$$$$NI*:......*FM$$NNMIIMN$$$$MV**....VV*VVVV***V::**:
..:::::********:..:::*FMV:VMV**:...........*M$$$N$NN$$$$$N*:....::*V$IIV:*****..
**:***********:.......:*MMFI:.*.........*.::**VFN$$$$$$NIF..:*:*..:*MM**VV**....
*********:::::......:***MNFI*F*........:VV*:*:..:*$$$$$NMM*.FNMINMV:V$$MV*****:.
***::::::::::........:::VMMNNN:....:..*..::**V**VM$$$NI*IM**NV**MIM*VNMV:****:..
**::::..................:*VFN$*...:V:.**:VNMMNMIN$$MIIV***VVVV**FFMVI$IV*:***:..
::..................:...:***VVV*****V*VMMVI$$IIMMVMM:*V:::**:::*V:VV****V*V**::.
...............:****VV*::::::**VIV*VMMMVFMVVIVVVFVV***::**V::******:*::*:***....
...........:*VVMMVMNI*.....:****MMIVVVFVF*********:::::**:***:::*V**V*..:.......
........::**VINMV*::.......:.:::VVMMFVVVV**V:...:::**::.:***..::*V:*:...........
***::::*VIMFMV:.............:*:*MVFM*V****V*:*.::*:*****:.::::*:***:............
::::**VVVNMV:...............***M$****V**:***..:*****::....::**:*****............
*****VVMFF*..**:...........***MMNV*****:.:::.:::.***:.....::*.:.:...............
**VMFMMMF:**V*:..........:VVVV*VVV****:::........:..............................
VFMN$$M***IVV*.:..::....:IMMI***V*V:..*.........................................
VNNIV**:*VFVV::::**:...:**IIM****VV**.**:.......................................
I**:::.....:*:**VV*:**VVFIIFV*V*******:.........................................
M*****:...*VV***V*:*VM$M******V::*::**..........................................
NIM*.:****VVVVVIIVVVF*V**:*V**V::***:...........................................
M$*.......:*VVVIVVIMF***:.**:::*....:*..........................................
$$V:........**FV*MNV*:*:.::.....................................................
FIM*:.......:V*VNMV:.:..........................................................
IVNV*.......:MNV**:.............................................................
:*VM*........VNV::..............................................................
..:*V:.......****:..............................................................""")
    print("""\n"I'm worried we won't make it," you say.
"Maybe the eruptions will end soon, if we just
wait here awhile."
"Maybe so," Dr. Vivaldi observes without looking at you. "And maybe it will get worse."
The two of you sit, waiting. Soon a breeze
begins to blow. A minute later you are coughing
and sputtering as the toxic gases rise over your
hill. You try not to breathe more than you can
help, but your vision blurs and your head spins.
You can't even sit up. .. .
It's strange. Diamonds are the hardest substance in the world; yet, if they are several feet
deep and you lie down on them, they make a soft
bed. And so the end comes easily for you.""")
    the_end()

def page103():
    print("""\nYou are lying on a hammock woven of fine
clima vines. You feel flushed and feverish, yet
happy: you're alive! Dr. Vivaldi is beside you. She
brushes a cool, wet cloth across your forehead.
"Where are we?" you ask. "How did we get
out of there? Did you see the ghost wolf?"
"We're back with the Archpods," Dr. Vivaldi
says, smiling. "And I did see a great beast with
tongues of fire, but in truth there was no wolf, nor
any other beast And the cracks in the field were
only a few inches wide, just wide enough to
release a poisonous gas from beneath the
ground. A few whiffs of it was enough to make us
hallucinate and have the most horrible nightmares. It's fascinating that the gas causes such a
specific common vision—I'd like to research this
some more. In any event, we were lucky to be
close to the edge when I realized what was happening, I was able to pull you away so you could
get fresh air."
"Thanks," you say. "After this I'm not going to
be afraid of anything in the Underground Kingdom."
"That's good," she replies, "because we still
have a whole new world to explore!"
""")
    the_end()
    
def page104():
    print("""\n"I won't help you fight the Rakas," you tell the
Grand Akpar. "War is a terrible thing. Your villages will be destroyed and your people will be
killed. Our wars have always brought grief."
The Grand Akpar is silent for a time. "Then it
would be like that here," he finally says. "But how
can we avoid war? If we do nothing, the Rakas
will destroy us."
"Talk to them," you say. "Work out a plan for
peace."
"No," he says, shaking his head. "We can't
trust them."
"And they think they can't trust you! You must
tell them what you fear from them, and ask what
they fear from you. You might discover that you
fear the same things. Once you've reached an
understanding, you can work out a plan that will
let the Rakas and the Archpods live in peace.""")
    input("Press Enter to Continue: ")
    page105()

def page105():
    print("""\nThe Grand Akpar paces from one side of the
agon to the other. Rnally he stops and stares into
your eyes. You shrink back from his stern gaze. "I
will try what you suggest," he says. "Meanwhile
you will be kept under guard with Dr. Vivaldi. If
all goes well, you shall be freed, and we will do
everything we can to make you happy here.
When you are ready to return to the Nether
World, we shall help you."
You start to thank the Grand Akpar, but he
holds up his hand. "Do not thank me until I tell
you this: If we are betrayed and the Rakas attack,
you and Dr. Vivaldi will die."
There is not much you can say, and you would
hardly have time anyway, for the guards quickly
lead you away""")
    input("Press Enter to Continue: ")
    page76()

def page106():
    print("""\nIt's an avalanche all right, but the boulders are
rolling up the mountain! Panicked, you run
toward Katu. The boulders are coming right at
you. At near zero gravity they're being pulled
toward the Black Sun.
"You've got to run down!" Dr. Vivaldi shouts.
But the boulders have cut off your escape. The
only thing you can do is run up the mountain,
trying to keep out of their path. You're running
higher and faster, leaping fifty feet at a time.
Ahead of you, Katu flies off the mountain. Before
you can stop yourself your feet lose touch with
the ground, and you're in the air, being swept
higher and higher, straight toward the Black Sun!
You've read that a black hole might somehow
be an entrance to another universe. If only that
were possible! It's your only chance once you
reach the Black Sun. A chance in a million
maybe, but still a chance . . .
""")
    the_end()

def page107():
    print("""\n.................................................................................
......................................:..........................................
............................:::****V*VVVV******::................................
.......................::****V***************VVVVV**::...........................
.....................:*****:***VIMN$$$$$$$$$MMFV*****V*::........................
..................:*******VM$$$$$$$$$$$$$$$$$$$$$$NF**:*VV*:.....................
................:*V*::*FN$$$$$$$$$$$$$$$$$$$$$$$$$$$$$MV***V*....................
..............:***::*M$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NF*:*V:..................
.............***::*M$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NV:***:................
...........:*V:.*M$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*.*V*...............
..........:*V*:F$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$V:*V*:.............
.........:*V::I$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$M**V*.............
........:VV::F$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$M:*V:............
........*VV.V$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$V:V*:...........
.......:VV::N$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$**V*...........
.......***.V$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$V:FV:..........
.......*V:.M$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$M:VI*..........
......:VV*:$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N:*V*..........
......:VV::$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$N$$$$$$$$$$$$$$$$$$$$$$$N:*V:..........
.......*V*:M$$$$$$$$$$$$$$$$$$$$$$$NN$$N$$N$$$$$$$$$$$$$$$$$$$$$$$I.*V:..........
.......*V*.V$$$$$$$$$$$$$$$$$$$$$$$$V**:VN$N$$$$$$$$$$$$$$$$$$$$$$*:FV...........
.......*V*::N$$$$$$$$$$$$$$$$$$$$$$V:**:VF$$$$$$$$$$$$$$$$$$$$$$$M:*F*...........
.....:::*V*:V$$$$$$$$$$$$$$MVVFMMVFI.:V*.FNMMMIMNIMNN$$$$$$$$$$$$*:VV:...........
.::::...:VVV:V$$$$$$$$$MV*V*VVV***VV**V**VFM::*IM*VV*M$$$$$$$$$$I*VV*............
::......:*VV*:FNNNN$$M*..*IFIMMV:*VIMMMIIVVFIMN$MM*V**F$$$$$$$$V:*V*.:...........
.......::.*VVV**M$$$F:.*FN$N$NNNV*****VV**I$$$$$$$NNI::*N$$NNN*:*V*:.............
.....:*:...:VIV**V*:*VM$$$$$$$$$MVIIMF**V$$$$$$$$$$$$NF:*FN$V**VV:...............
..:::::....:FIV**::VN$$$NN$$$$$$MM$$$NMNN$$$$$$$$$$$$$$V*::V*VV::.:..............
.:..........:V**VIV*:VNMM$$$$$$$MNN$$$$$$$$NNN$$$$N$$$$IVVVI**:..::::............
.............::.::*FVVV*F$$$$$$$NN$$$$$$$$$NNN$$MIMMNNV**FVV*....................
.....:.....:::..::.**VVVVNMN$$N$$$$$$$$$$$$NN$NMMNMVVF*VIV::.....................
.....:.....:...::.:*V*VIVMFM$$$$$$$$N$NNM$$$NNMVVIVVIVV***...:...::..............
:::.........:....***:.*V*VINM$$N$$$NIMVMV$$NIINMV*VF*:::::...**:..:**:...........
..........:::...:::..:.::VNMMNNN$$NFVFVVVNN$NM$MV*:VV:.........*:...:::..........
......:...:.............***MNNNN$N*:...*.*FMV**VV*:.*V:......::........:::.......
....:*:..............:.*V:.:VIIMMV**...:.:*F::**:.::.:V:......::.........:::.....
.:::........:.......:::V*.::**:***::..::..*F:......*:.:*.......:......:....::....
::........::.......::.:::::.*.:V*.....::...*:::....:*.....:...........:..........
.........:..............:**::::V:.....**...**.......::.....::....................
.....................:..*V:..:**......:*...:*:*:............::...................
..::...........::....::.**..::*:.*..........::::..........::.*:..................
::.......::.........:*.:*....::..*.....:.....:.............:.:*:.................""")

def page108():
    print("""\n............................*................................
...........................:*................................
...........:...............:*................................
............::.............:*..........:.....................
............:*:............:*.........::.....................
...............*:..........:*.......:*.......................
...............:**:........:*:......:..........:.............
............:....**:.......:**....:*........:*:..............
.............::...:**:::*V***VV*VVVV*:...:**:................
................::VMV**:*VMV*V**FFVVV*::**:..................
......:::......:*VVVVF*FMMNM**VV*VIVI**F:....................
........:::::::VV*MV.*V*VVVMVVMVVIMFV*VV*.::.................
..............:VI:*V:VVV**FM*VVFFVFI**VVV::..................
...............VVV*:*VIIV*:V::**VIIIV*MI:....................
****************VVVVVVVVVVV:..:***VIMVIV**::::*****::::::.:::
................:VNNINIVVV*:..*VVVVVVI*......................
.................:VV*IVVFV**.***VVIVV*:::....................
............:::.:..***FMI:*F:VV*VFV*V:...:::::...............
.........:.......:***VVV*VVM:VVIF*MV:........................
...............:*::..IF*VFMN*IMMFIV:.:::.....................
.............:::.....*VNFVN$*FMFMN***:.:::...................
..........:::.......:..V*VFI*VV*V*..:*:......................
........:::........::..:VI*******....:*:.....................
......:::.........::.....**V*V*:.......::....................
..................:......:*$VVV.........::...................
..........................:MFV:...........*:.................
...........................*V*.............::................
...........................:*:...............:...............
............................:................................
............................*................................""")
    print("""\nYou made it!
Across the fields of white clay and safely back
to the land of the Archpods.
And, if you remembered to fill your pockets
with diamonds before you ran across the field of
white clay, you're very rich!""")
    the_end()

# Start of game
title_page()
time.sleep(1)
warning_page()
time.sleep(1)
buckners_theory()
time.sleep(1)
page1()
