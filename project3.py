import pandas as pd
import os
class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False
    def process_adoption(self):
        self.is_adopted = True
df1 = pd.read_csv("shelter_A.csv")
df2 = pd.read_csv("shelter_B.csv")
df = pd.concat([df1, df2], ignore_index=True)
df["Animal_Type"] = df["Animal_Type"].str.strip().str.lower()
dogs = df[df["Animal_Type"] == "dog"]
dog = dogs.iloc[0]
pet = RescuePet(dog["Pet_Name"], dog["Animal_Type"], dog["Age_Years"])
pet.process_adoption()
adopted_data = pd.DataFrame({
    "Pet_Name": [pet.name],
    "Animal_Type": [pet.species],
    "Age_Years": [pet.age], "Adopted": [pet.is_adopted]
})
file_name = "successful_adoptions.csv"
if os.path.exists(file_name):
    old_df = pd.read_csv(file_name)
    new_df = pd.concat([old_df, adopted_data], ignore_index=True)
    new_df.to_csv(file_name, index=False)
else:adopted_data.to_csv(file_name, index=False)
print("Adoption saved!")