kwotabrutto = float(input('Wprowadź kwotę brutto:'))
vat3 = 0.03
vat8 = 0.08
vat23 = 0.23

print(round(kwotabrutto,2), "zł brutto to", round(kwotabrutto / (1 +vat3),2), "zł netto")
print(round(kwotabrutto,2), "zł brutto to", round(kwotabrutto / (1 +vat8),2), "zł netto")
print(round(kwotabrutto,2), "zł brutto to", round(kwotabrutto / (1 +vat23),2), "zł netto")


