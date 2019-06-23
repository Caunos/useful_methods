def crt(m, x):
    while True:
        temp1 = modinv(m[1], m[0]) * x[0] * m[1] + \
                modinv(m[0], m[1]) * x[1] * m[0]

        temp2 = m[0] * m[1]

        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x


        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m

        if len(x) == 1:
            break
    return x[0]
