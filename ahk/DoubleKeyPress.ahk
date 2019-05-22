#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

~j::
if (A_PriorHotkey <> "~j" or A_TimeSincePriorHotkey > 150)
{
    ; Too much time between presses, so this isn't a double-press.
    KeyWait, j
    return
}
Send, {BS}{BS}g
return


;f::DoubleTap("g",250)
;
;DoubleTap(key,TimeVar=300) 
;{
;        If (A_ThisHotkey==A_PriorHotkey && A_TimeSincePriorHotkey < TimeVar)
;                Send %key%
;        else
;                Send {%A_ThisHotkey%}
;        return
;}
