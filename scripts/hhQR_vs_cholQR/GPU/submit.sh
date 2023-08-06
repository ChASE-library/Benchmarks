#!/bin/bash -x

cd NaCl-9k

sbatch hhQR.sh

sbatch cholQR.sh

cd ..


cd TiO2-29k

sbatch hhQR.sh

sbatch cholQR.sh

cd ..

cd AuAg-13k

sbatch hhQR.sh

sbatch cholQR.sh

cd ..

cd In2O3-76k

sbatch hhQR.sh

sbatch cholQR.sh

cd ..

cd In2O3-115k

sbatch hhQR.sh

sbatch cholQR.sh

cd ..

cd HfO2-76k

sbatch hhQR.sh

sbatch cholQR.sh

cd ..




