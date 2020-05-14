# -----------------------------------------------------------
# File:   easytax.py
# Author: Luke Melto  User ID: lmelt914   Class: CPS 110
# Desc:   This program calculates the user's taxes.
# ----------------------------------------------------------- 


#INPUT 


print("CPS110 Program 1: Tax Calculator, by Luke Melto (lmelt914)\n")
taxpayerName = input("Enter Taxpayer Name: ")
status = input("Enter Filing Status (S - Single, M - Married, H - Head of Household): ")

while not (status == "S" or status == "M" or status == "H"):
  print("Invalid filing status selected. Please enter S, M, or H.")
  status = input("Enter Filing Status (S - Single, M - Married, H - Head of Household): ")

grossIncome  = float(input("Enter gross income amount: "))
numKids      = input("Enter number of children: ")


#CALCULATION


if status == "S":
  deduction = 5000
else:
  deduction = 8000

childBonus = int(numKids) * 1000
agi = grossIncome - int(deduction)

if agi < 0:
  agi = 0

if int(agi) <= 20000:
  taxAmt = 0.0
else:
  taxAmt = (agi - 20000) * .2

refund = 0
owed   = 0

if taxAmt - childBonus >= 0:
  owed = taxAmt - childBonus
else:
  refund = taxAmt - childBonus


#OUTPUT


print("Tax for", taxpayerName)
print("------------------------------------")

if status == "S":
  print("Filing status:           Single")
  status = "Single"
elif status == "M":
  print("Filing status:           Married")
  status = "Married"
else:
  print("Filing status:           Head of Household")
  status = "Head of Household"

print("Children:               ", numKids)
print("\nGross income:            ${0:.2f}".format(float(grossIncome)))
print("Standard deduction:      ${0:.2f}".format(float(deduction)))
print("                         -----------")
print("Adjusted Gross Income:   ${0:.2f}".format(float(agi)))
print("\nBase Tax:                ${0:.2f}".format(float(taxAmt)))
print("Child credit:            ${0:.2f}".format(float(childBonus)))
print("                         -----------")
print("Refund Amount:           ${0:.2f}".format(float(abs(refund))))
print("Amount You Owe:          ${0:.2f}".format(float(owed)))


#HTML OUTPUT


outfile = open('output.html', 'w')
outfile.write("""
   

<html>
    <head>
      <style>
          table, td, th {
              border: thin solid black;
              margin: 0px;
              padding: 10px;
              border-collapse: collapse;
              text-align: right;
          }
          th {
            background-color: lightblue;
          }
      </style>
    </head>
    <body>
    <h1>Tax for """ + str(taxpayerName) + """</h1>
    <table>
      <tr>
        <th>Filing status:</th>
        <td>""" + str(status) + """</td>
      </tr>
      <tr>
          <th>Children:</th>
          <td>""" + str(numKids) + """</td>
      </tr>
      <tr>
          <th>Gross income:</th>
          <td>$""" + """{0:.2f}""".format(float(grossIncome)) + """</td>
      </tr>
      <tr>
          <th>Standard deduction:</th>
          <td>$""" + """{0:.2f}""".format(float(deduction)) + """</td>
      </tr>
      <tr>
          <td></td>
          <td><hr/></td>
      </tr>
      <tr>
          <th>Adjusted Gross Income:</th>
          <td>$""" + """{0:.2f}""".format(float(agi)) + """</td>
      </tr>
      <tr>
          <td></td>
          <td></td>
      </tr>
      <tr>
          <th>Base Tax:</th>
          <td>$""" + """{0:.2f}""".format(float(taxAmt)) + """</td>
      </tr>
      <tr>
          <th>Child credit:</th>
          <td>$""" + """{0:.2f}""".format(float(childBonus)) + """</td>
      </tr>
      <tr>
          <td></td>
          <td><hr/></td>
      </tr>
      <tr>
          <th>Refund Amount:</th>
          <td>$""" + """{0:.2f}""".format(abs(float(refund))) + """</td>
      </tr>
      <tr>
          <th>Amount You Owe:</th>
          <td>$""" + """{0:.2f}""".format(float(owed)) + """</td>
      </tr>
    </table>



</body></html>
   """)
outfile.close()
