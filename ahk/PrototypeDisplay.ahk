#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#Persistent
SetTimer, MM

MM:
If ( A_Hour <= 21 and A_Hour >= 7 )
	If ( A_TimeIdle > 59999 ) {
		MouseMove, 1 , 1,, R
		MouseMove, -1,-1,, R
	}
	Return

;another


;SetTimer, MMS, 60000 ; 
;
;MMS:
;    MouseMove, 1, 0, 1, R ;Move the mouse one pixel to the right
;    Sleep, 50 ; Wait 50 ms. Not realy required, but makes the move visible
;    MouseMove, -1, 0, 1, R ;Move the mouse back one pixel
;return



;another ideas is:

;autoexecute section
;pssv := false ; Boolean for label (subroutine). True = running/enabled.
;SetTimer, pss, 30000 ; launch label (subroutine), checks every 1 minute
 
 
;^5::
;global pssv := !pssv
;if (global pssv) {
;TrayTip, Pre, Enabled, 2, 17
;}
;else { TrayTip, Pre, Disabled, 2, 17 
;}
;return
; 
;;launch subroutine
;pss:
;if (global pssv) {
;    MouseMove, 1, 0, 1, R  ;Move the mouse one pixel to the right
;    MouseMove, -1, 0, 1, R ;Move the mouse back one pixel
;}
;return
