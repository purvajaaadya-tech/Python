def tc(ba, tp):
    total = ba * (1 + 0.01 * tp)
    total = round(total, 2)
    print(f"Please pay $ {total}")

tc(150, 20)