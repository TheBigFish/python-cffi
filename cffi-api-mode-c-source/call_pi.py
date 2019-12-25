from _pi.lib import pi_approx

approx = pi_approx(10)
assert str(approx).startswith("3.")
print(approx)

approx = pi_approx(10000)
assert str(approx).startswith("3.1")
print(approx)
