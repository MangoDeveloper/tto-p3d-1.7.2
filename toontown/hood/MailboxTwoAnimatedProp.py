# 2013.08.22 22:20:55 Pacific Daylight Time
# Embedded file name: toontown.hood.MailboxTwoAnimatedProp
from toontown.hood import ZeroAnimatedProp
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

class MailboxTwoAnimatedProp(ZeroAnimatedProp.ZeroAnimatedProp):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('MailboxTwoAnimatedProp')
    PauseTimeMult = base.config.GetFloat('zero-pause-mult', 1.0)
    PhaseInfo = {0: ('tt_a_ara_dod_mailbox_firstMoveFlagSpin1', 40 * PauseTimeMult),
     1: (('tt_a_ara_dod_mailbox_firstMoveStruggle', 'tt_a_ara_dod_mailbox_firstMoveJump'), 20 * PauseTimeMult),
     2: ('tt_a_ara_dod_mailbox_firstMoveFlagSpin2', 10 * PauseTimeMult),
     3: ('tt_a_ara_dod_mailbox_firstMoveFlagSpin3', 8 * PauseTimeMult),
     4: ('tt_a_ara_dod_mailbox_firstMoveJumpSummersault', 6 * PauseTimeMult),
     5: ('tt_a_ara_dod_mailbox_firstMoveJumpFall', 4 * PauseTimeMult),
     6: ('tt_a_ara_dod_mailbox_firstMoveJump3Summersaults', 2 * PauseTimeMult)}
    PhaseWeStartAnimating = 5

    def __init__(self, node):
        ZeroAnimatedProp.ZeroAnimatedProp.__init__(self, node, 'mailbox', self.PhaseInfo, ToontownGlobals.MAILBOX_ZERO_HOLIDAY)

    def startIfNeeded(self):
        try:
            self.curPhase = self.getPhaseToRun()
            if self.curPhase >= self.PhaseWeStartAnimating:
                self.request('DoAnim')
        except:
            pass

    def handleNewPhase(self, newPhase):
        if newPhase < self.PhaseWeStartAnimating:
            self.request('Off')
        else:
            self.startIfNeeded()
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\hood\MailboxTwoAnimatedProp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:20:55 Pacific Daylight Time
