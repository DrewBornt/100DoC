def formatName(fName, lName):
    formatedFNAME = fName.title()
    formatedLNAME = lName.title()

    return f"{formatedFNAME} {formatedLNAME}"

print(formatName("andrew", "bornt"))