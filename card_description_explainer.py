
# cards variable explanations
# #y, #r, #g, #b, #p. These colors are Gold, Red, Green, Blue, Purple (Only in events)
    # -Text is colored to highlight keywords and other important concepts. Colors are as follows: #y, #r, #g, #b, #p. These colors are Gold, Red, Green, Blue, Purple (Only in events)
    # EXAMPLE: "#yI'm #yGolden!"

    # -For events and dialogs, if a word is surrounded by ~ or @, they are wavy or shaky in game. 
    # EXAMPLE: "@This@ @is@ @shaky.@" "~This~ ~is~ ~wavy.~""

    # -Colors and text effects can be combined. However, the color must always come before the effect.
    # EXAMPLE: "#y@CLANG@ #y@CLANG@"

    # -Cards utilize dynamic values. These are !D!, !B!, !M!. They stand for Damage, Block, and Misc.
    # EXAMPLE: "Deal !D! damage."
    # EXAMPLE: "Gain !B! Block."
    # EXAMPLE2: "Draw !M! cards."

    # -Keywords found in keywords.json must be capitalized when they are shown on a card, power, or relic description.
    # EXAMPLE: "Apply 2 Vulnerable."

    # -NL stands for new line. New lines are added to make the text feel easier to read or separates two distinct sentences or quotes. There must be a space on either side for the new line to be appended.
    # EXAMPLE: "Hello. NL I am Bob."

    # -Sometimes descriptions will be disjointed. This is because we need to insert dynamic values into some text.
    # EXAMPLE:
    # "I ate #b",
    # " pies."
    # Would look like: "I ate #b6 pies." in the game