#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^#A::
clipboard := ""   ; Empty the clipboard.
clipboard := "clipboarda"   ; Give the clipboard entirely new contents.
Return

^#B::
clipboard := ""   ; Empty the clipboard.
clipboard := "https://comscore.zoom.us/my/psmith"   ; Give the clipboard entirely new contents.
Return

^#C::
clipboard := ""   ; Empty the clipboard.
clipboard := "☝️"   ; Give the clipboard entirely new contents.
Return

