""" Directions: Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

Each blood type consists of:

A letter: "A", "B", "AB", or "O"
And an Rh factor: "+" or "-"
Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

Letter Rules:

"O" can donate to other letter type.
"A" can donate to "A" and "AB".
"B" can donate to "B" and "AB".
"AB" can donate only to "AB".
Rh Rules:

Negative ("-") can donate to both "-" and "+".
Positive ("+") can donate only to "+".
Both letter and Rh rule must pass for a donor to be able to donate to the recipient.
"""

''' O(1) time complexity, O(1) space complexity '''
# true of letter rules and rh rules both pass
def can_donate(donor, recipient):

    # Parsing
    # donor = "AB+" -> donor_letter = "AB" and the rh_factor is always the last character
    donor_letter = donor.split("+")[0].split("-")[0]
    donor_rh = donor[-1]

    recipient_letter = recipient.split("+")[0].split("-")[0]
    recipient_rh = recipient[-1]

    # letter rules
    letter_lookup = {
        "O": {"A", "B", "AB", "O"},
        "A": {"A", "AB"},
        "B": {"B", "AB"},
        "AB": {"AB"}
    }

    # rh rules
    rh_lookup = {
        "-": {"-", "+"},
        "+": {"+"}
    }

    return recipient_letter in letter_lookup[donor_letter] and recipient_rh in rh_lookup[donor_rh]

if __name__ == "__main__":
    print(can_donate("O-", "A+"))   # True
    print(can_donate("A-", "AB+"))  # True
    print(can_donate("B+", "AB-"))  # False
    print(can_donate("AB-", "AB+")) # True
    print(can_donate("O+", "O-"))   # False

''' I used an LLM to help me with my reasoning and logic, and what to ask myself, it didn't generate a full solution for me '''