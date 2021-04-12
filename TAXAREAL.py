
TaxaNominal = 0.0275 
TaxaInflação = 0.0610

valor_in = (((TaxaNominal+1)/(TaxaInflação+1)-1)*100)

print("Taxa Real: " + str(valor_in))