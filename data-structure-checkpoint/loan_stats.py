import numpy as np

# `with` closes the file automatically once reading is done
with open("Loan_prediction_dataset.csv") as f:
    loan_amount = np.genfromtxt(f, delimiter=",", skip_header=1, usecols=8)

# missing LoanAmount cells come back as nan, so use the nan-aware versions
print("Mean:  ", np.nanmean(loan_amount))
print("Median:", np.nanmedian(loan_amount))
print("Std:   ", np.nanstd(loan_amount))
