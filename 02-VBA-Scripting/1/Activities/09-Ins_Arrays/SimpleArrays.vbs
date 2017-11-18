Sub SimpleArrays():
    
    ' Basic Array Example
    ' ------------------------------------------
    ' Create the Ingredients Array - FIXED array, holds SIX elements
    Dim Ingredients(5) as String

    ' Add Ingredients to the Array 

    ' NOTE: the first element of the array is at index = 0!
    Ingredients(0) = "Chocolate Bar"
    Ingredients(1) = "Peanut Butter"
    Ingredients(2) = "Jelly"
    Ingredients(3) = "Macaroni"
    Ingredients(4) = "Potato Salad"
    Ingredients(5) = "Dragonfruit"

    ' Retrieve specific elements of the array
    MsgBox(Ingredients(4))
    MsgBox(Ingredients(0))

End Sub
