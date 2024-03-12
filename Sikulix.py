from datetime import datetime
import time
###REGIONS###
#REG_ELIMINA=
#REG_ELIMINATED=
#REG_X=
REG_UR_CORNER=Region(1667,4,253,156)
REG_CMD_CORNER=Region(1703,1003,217,77)
###PATTERNS###
#PLAY="PLAY.png"
#QUEUE="1697893023681.png"
#LOAD="SURVIVAL.png"
MATCH="1697892956167.png"
SURVIVAL_MATCH="1709903579967.png"
#LOST="ELIMINA.png"
#LOST2="1697894536838.png"
#XLOST="1697894643221.png"
EXIT="EXIT.png"
#CONFIRM_EXIT="EXIT2.png" #outside corner
#SKIP_REWARDS="SKIP.png"
#CONFIRM_LVLUP="1697892576216.png" #outside corner | sporadic
#FIN="CONFIRM.png"
###UNUSED###
def levelUp():
    return
def crownUp():
    return
def walkUntilEliminated():
    keyDown('w')
    while not exists(LOST):
        sleep(1)
    keyUp('w')
def play():
    isLobby=exists(LOBBY)
    print("isLobby:",isLobby)
    if(isLobby != None):
        type('w')
###FUNCTIONS###
def counts():
    global i
    i+=1
    #pop(i)
    print("#################################################",i)
    print('curtime:',hhmm())
    
def hhmm(timestamp=None):
    if(timestamp is None):
            timestamp=time.time()
    dt = datetime.fromtimestamp(timestamp)
    hh = dt.hour
    mm = dt.minute
    #print('dt',dt)
    #print("Current Hour:", hh)
    #print("Current Minute:", mm)
    return hh,mm
def pop(msg,timeout=1,title="FallGuys"):
    popat(0,0)
    return Do.popup(msg,title,timeout)
def quit():
    print('quit()')
    esc()
    enter()
def esc():
    type(Key.ESC)
def enter():
    type(Key.ENTER)
def enterUntilMatch():
    print('enterUntilMatch() ')
    start=time.time()
    #hhmm(start)
    #while not REG_CMD_CORNER.exists(MATCH):
    while not REG_UR_CORNER.exists(SURVIVAL_MATCH):
        isReloaded=reloadQ(start)
        if(isReloaded):
            enterUntilMatch()
        enter()
def walkUntilExit():
    print('walkUntilExit()')
    keyDown('w')
    while not REG_CMD_CORNER.exists(EXIT):
        sleep(.1)
    keyUp('w')
def reloadQ(startTime,elapsed=180):
    print('reloadQ()')
    isTime=time.time() - startTime > elapsed
    print('isTime:',hhmm())
    #pop("isTIme:"+str(hhmm()))
    if (isTime):
        esc()
        return True
    return False
###GAMEPLAY LOOP###
i=0
def loop():
    counts()
    enterUntilMatch() #need to know when to switch from spacespaming to Wspam
    sleep(1)
    walkUntilExit()
    quit()
while(True):
    loop()