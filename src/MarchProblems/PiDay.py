# 3/14:

""" Directions: Happy pi (π) day!

Given an integer (n), where n is between 1 and 1000 (inclusive), return the nth decimal of π.

Make sure to return a number not a string.
π with its first five decimals is 3.14159. So given 5 for example, return 9, the fifth decimal.

You may have to find the first 1000 decimals of π somewhere.
"""

""" Time Complexity: O(1) -> Retrieving a character in a string is O(1), there are not computations or loops that scale with n.
Space Complexity: O(1) relative to the input n -> The pi_digits string consists of 1000+ characters, which exists in memory regardless
of n. The space taken up is proportional to the size of the string, so O(1000) -> O(1) with respect to n. If the storage of the string
itself is the "input" then technically space complexity would be O(1000) -> constant, since it doesn't grow as n grows. The pi_digits
string has a fixed length, so space complexity is constant.
"""

def get_pi_decimal(n):

    # check to make sure n is in between 1 and 1000 (inclusive)
    if n < 1 or n > 1000:
        print("n is not between 1 and 1000")
        return None

    # store the first 1000 decimals of pi
    pi_digits = ("3.14159265358979323846264338327950288419716939937510"
        "58209749445923078164062862089986280348253421170679"
        "82148086513282306647093844609550582231725359408128"
        "48111745028410270193852110555964462294895493038196"
        "44288109756659334461284756482337867831652712019091"
        "45648566923460348610454326648213393607260249141273"
        "72458700660631558817488152092096282925409171536436"
        "78925903600113305305488204665213841469519415116094"
        "33057270365759591953092186117381932611793105118548"
        "07446237996274956735188575272489122793818301194912"
        "98336733624406566430860213949463952247371907021798"
        "60943702770539217176293176752384674818467669405132"
        "00056812714526356082778577134275778960917363717872"
        "14684409012249534301465495853710507922796892589235"
        "42019956112129021960864034418159813629774771309960"
        "51870721134999999837297804995105973173281609631859"
        "50244594553469083026425223082533446850352619311881"
        "71010003137838752886587533208381420617177669147303"
        "59825349042875546873115956286388235378759375195778"
        "18577805321712268066130019278766111959092164201989"
    )

    # Index uses + 1 because of the '3.' at the start of pi
    index = n + 1

    # type cast to an int to return an int
    return int(pi_digits[index])

# main test cases
if __name__ == "__main__":
    print(get_pi_decimal(5))        # 9
    print(get_pi_decimal(10))       # 5
    print(get_pi_decimal(22))       # 6
    print(get_pi_decimal(39))       # 7
    print(get_pi_decimal(76))       # 2
    print(get_pi_decimal(384))      # 4
    print(get_pi_decimal(601))      # 0
    print(get_pi_decimal(1000))     # 9