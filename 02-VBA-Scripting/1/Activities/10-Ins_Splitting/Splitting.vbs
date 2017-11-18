Sub SimpleArrays():
    
    ' String Splitting Example
    ' ------------------------------------------
    ' Note that we don't have an integer inside of the parentheses here
    ' This is a variable-length array
    dim Words() as String
    dim Shakespeare as String
    Shakespeare = "To be or not to be. That is the question"

    ' Break apart the Shakespeare quote into individual words  
    Words = Split(Shakespeare, " ")

    ' Print individual word
    MsgBox(Words(5))

End Sub
