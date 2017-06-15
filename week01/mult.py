class BigNumber:
    def __init__(self, digits="", mult_type='katsuba'):
        self.digits = []
        self.mult_type = mult_type
        i = 0
        while i < len(digits) and int(digits[i]) == 0:
            i += 1
        while i < len(digits):
            self.digits.append(int(digits[i]))
            i += 1
        if len(self.digits) == 0:
            self.digits.append(0)

    def __mul__(self, other):
        if self.mult_type == 'katsuba':
            return self.katsuba_mult(other)
        else:
            return self.naive_mult(other)

    __rmul__ = __mul__

    def __str__(self):
        return ''.join([str(i) for i in self.digits])

    def __add__(self, other):
        carry = 0
        out = []
        max_len = 0
        A = self.digits
        B = other.digits
        if len(A) < len(B):
            for i in range(len(B)-len(A)):
                A.insert(0, 0)
        elif len(B) < len(A):
            for i in range(len(A)-len(B)):
                B.insert(0, 0)
        for a, b in zip(A[::-1], B[::-1]):
            cum_sum = carry + a + b
            out.append(cum_sum % 10)
            carry = int(cum_sum / 10)
        out.append(carry)
        out = out[::-1]
        while len(out) > 0 and out[0] == 0:
            del out[0]
        return BigNumber(out, self.mult_type)

    __radd__ = __add__

    def __neg__(self):
        return BigNumber([-1*i for i in self.digits], self.mult_type)

    def __sub__(self, other):
        return self.__add__(-other)

    __rsub__ = __sub__

    def naive_mult(self, other):
        """
        Performs naive multiplication of two integer lists, A and B, which
        contain each of the digits of A and B in normal decimal order.
        Outputs an integer list of digits.
        """
        carry = 0
        out = []
        for j in range(len(other.digits))[::-1]:
            out.append([])
            row = len(other.digits)-1-j
            for k in range(row):
                out[row].append(0)
            for i in range(len(self.digits))[::-1]:
                temp_out = (self.digits[i] * other.digits[j]) + carry
                out_digit = temp_out % 10
                carry = int(temp_out / 10)
                out[row].append(out_digit)
            if carry != 0:
                out[row].append(carry)
            out[row] = BigNumber(out[row][::-1], self.mult_type)
            carry = 0
        
        big_out = BigNumber('0', self.mult_type)
        for i in range(len(out)):
            big_out = big_out + out[i]
        return big_out

    def katsuba_mult(self, other):
        """
        Performs Katsuba multiplication of two integer lists, A and B, which
        contain each of the digits of A and B in normal decimal order. Outputs
        an integer list of digits.
        """
        if len(self.digits) < 2 and len(other.digits) < 2:
            mult = self.digits[0] * other.digits[0]
            val = mult % 10
            carry = int(mult / 10.0)
            out = BigNumber([carry, val])
            return out
        A = self.digits
        B = other.digits
        if len(A) < len(B):
            for i in range(len(B)-len(A)):
                A.insert(0, 0)
        elif len(B) < len(A):
            for i in range(len(A)-len(B)):
                B.insert(0, 0)
        mid = int(len(A)/2.0)
        m = len(A) - mid
        a = BigNumber(A[:mid])
        b = BigNumber(B[:mid])
        c = BigNumber(A[mid:])
        d = BigNumber(B[mid:])
        ab = a*b
        cd = c*d
        apb_cpd = ((a+c)*(b+d)) - ab - cd
        for i in range(m*2):
            ab.digits.append(0)
        for i in range(m):
            apb_cpd.digits.append(0)
        added_lists = ab + cd + apb_cpd
        return added_lists

def rem_lead_zeros(n):
    m = n
    while m[0] == 0 and len(m) > 1:
        del m[0]
    return m

def compare_karatsuba_naive():
    iops = []
    kops = []
    for i in range(20):
        for k in range(20):
            ni = str(i)
            nk = str(k)
            km = BigNumber(ni)*BigNumber(nk)
            nm = BigNumber(ni, 'naive')*BigNumber(nk, 'naive')
            if str(km) != str(nm):
                iops.append(ni)
                kops.append(nk)
                print 'Karatsuba', km
                print 'Naive    ', nm
    print iops
    print kops

    long1 = BigNumber("3141592653589793238462643383279502884197169399375105820974944592")
    long2 = BigNumber("2718281828459045235360287471352662497757247093699959574966967627")
    long1n = BigNumber("3141592653589793238462643383279502884197169399375105820974944592",\
            'naive')
    long2n = BigNumber("2718281828459045235360287471352662497757247093699959574966967627",\
            'naive')

    print long1n*long1n
    print long1*long1
    print str(long1n*long1n)==str(long1*long1)

    print long1n*long2n
    print long1*long2
    print str(long1n*long2n)==str(long1*long2)

def main():
    print 'Karatsuba Long Multiplication'

    long1 = BigNumber("3141592653589793238462643383279502884197169399375105820974944592")
    long2 = BigNumber("2718281828459045235360287471352662497757247093699959574966967627")

    print long1*long2

    print BigNumber("12345679")*BigNumber("81")

if __name__ == "__main__":
    main()
