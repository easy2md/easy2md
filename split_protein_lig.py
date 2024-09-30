import os

def o(gmxOrder):
    try:
        print("输入命令："+gmxOrder)
        os.system(gmxOrder)
    except:
        print("wrong wrong wrong wrong wrong wrong wrong wrong wrong wrong")

o1="echo 1|gmx trjconv -s protein_md.tpr -f protein_md_1.xtc -n index.ndx -o complex_start_protein.pdb -b 0 -e 0"
o(o1)
o1="echo 13|gmx trjconv -s protein_md.tpr -f protein_md_1.xtc -n index.ndx -o complex_lig.pdb -b 0 -e 0"
o(o1)
