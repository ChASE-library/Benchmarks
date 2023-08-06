#!/bin/bash -x

cd NaCl-9k

sbatch OptN.sh

sbatch Opt.sh

cd ..


cd TiO2-29k

sbatch OptN.sh

sbatch Opt.sh

cd ..

cd AuAg-13k

sbatch OptN.sh

sbatch Opt.sh

cd ..

cd In2O3-76k

sbatch OptN.sh

sbatch Opt.sh

cd ..

cd In2O3-115k

sbatch OptN.sh

sbatch Opt.sh

cd ..

cd HfO2-76k

sbatch OptN.sh

sbatch Opt.sh

cd ..


