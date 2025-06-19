import pandas as pd
import numpy as np

# Reik naudoti dvigubus pasviruosius rūkšnius! „\\“, nes viengubas mėgina padaryti veiksmus
df = pd.read_csv( "E:\\Numpy\\personality_dataset.csv")


# print ( df ) 
print ( df.head ()) 
print ( df.describe())


isfiltruota = df [[ "Personality", "Going_outside"]]
sugrupuota = isfiltruota.groupby (["Going_outside"])

isfiltruota_introvert = isfiltruota ["Personality" == "Introvert"]


isfiltruota.to_csv("test1.csv")
isfiltruota_introvert.to_csv("Introvert.csv")
# Šitaip neveikia, nes grupuojant paeičia tipą duomenų!
# sugrupuota.to_csv("test1.csv")


df["Musu_isvada"] = np.where(df["Eina_i_lauka"] > 2, "Ekstravertas", "Introvertas")