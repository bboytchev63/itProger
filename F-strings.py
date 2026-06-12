# Formatted string
f_temp = 66
# t = f"Temperature is {f_temp} degrees Far"
# print(t)
# tc = f"Temperature is {(f_temp - 32) / 1.8} degrees Cel"
# print(tc)
# tc = f"Temperature is {(f_temp - 32) / 1.8:.2f} degrees Cel "
# print(tc)

f_suntemp = 28000000
# tc = f"Temperature of Sun is {(f_suntemp - 32) / 1.8:,.2f} degrees Cel"
# print(tc)

tc = f"Temperature is {(f_temp - 32) / 1.8:^15,.2f} degrees Cel"
print(tc)
tc = f"Temperature is {(f_suntemp - 32) / 1.8:^15,.2f} degrees Cel"
print(tc)
