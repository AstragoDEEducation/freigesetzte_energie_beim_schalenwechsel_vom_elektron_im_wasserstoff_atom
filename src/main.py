from rich import print


# === Main Function ===
def main():
    for n in range(1, 8):
        for m in range(1, 8):
            if m == n:
                continue
            delta_e_in_ev = 13.6 * ((1 / n**2) - (1 / m**2))
            delta_e_in_j = delta_e_in_ev * 1.602e-19
            frequenz = delta_e_in_j / 6.626e-34
            wellenlaenge = (2.997e8) / frequenz
            print(
                f"m={m}; n={n}; E={delta_e_in_ev} eV; E= {delta_e_in_j} J; f={frequenz}; lambda={wellenlaenge}\n"
            )


if __name__ == "__main__":
    main()
