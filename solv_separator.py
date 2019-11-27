

def sep(N_atoms, N_snaps, N_species, d, lines):
    for j in range(int(N_species)):
        m = 0
        for i in range(N_atoms+2):
            if i == 0 or i == 1:
                continue
            elif lines[i].split()[0] == d[f'atom_label_{j+1}']:
                m += 1
    #            print(m)
            d["N_atom_label_{0}".format(j+1)] = m
    return d
 
def get_N_atoms(fpath, fname):
    with open(fpath + fname, 'r') as file: 
        N_atoms = int(file.readline().rstrip())
    return N_atoms

def read_xyz(fpath, fname):
    with open(fpath + fname, 'r') as file:
        lines = file.readlines()
        #N_atoms = int(lines[0])
    return lines

def write_xyz(fpath,fname, N_atoms, N_snaps, N_species, d, lines):
    t = 0
    for j in range(N_snaps):
        for k in range(int(N_species)):
            for i in range(N_atoms+2):
                if i == 0:
                    with open(fpath + "Atom_" + d[f'atom_label_{k+1}'] + "_" + f"snap_{j+1}" +".xyz", 'w') as f:
                        f.write(str(d[f'N_atom_label_{k+1}'])+"\n")
                elif i == 1:
                    with open(fpath + "Atom_" + d[f'atom_label_{k+1}'] + "_" + f"snap_{j+1}" +".xyz", 'a') as f:
                        f.write(lines[j*(N_atoms+2)+1])
                elif lines[i].split()[0] == str(d[f'atom_label_{k+1}']):
                    with open(fpath + "Atom_" + d[f'atom_label_{k+1}'] + "_" + f"snap_{j+1}" +".xyz", 'a') as f:
                        f.write(lines[j*(N_atoms+2)+i])
                else:
                    continue

def main():
    lines = read_xyz(fpath, fname)
    data = sep(N_atoms, N_snaps, N_species, d, lines)
    write_xyz(fpath, fname, N_atoms, N_snaps, N_species, data, lines) 

if __name__ == "__main__":
    import sys, os
  
    fpath = '/Users/ernesto/Main/Codes/solv_separator/test/'
    fname = 'h3o_64w-1-MD_1000snap.xyz'

    N_atoms = get_N_atoms(fpath, fname)
    print(f"There are {N_atoms} atoms in your trajectory file", "\n")
    
    print("How many snapshots to analyse ", "\n", "type: 'All' or 'An interger number' ", "\n")
    value = input()
    if value == "All":
        lines = read_xyz(fpath, fname)
        N_snaps = int(len(lines)/int(N_atoms+2))
    else:
        N_snaps = int(value)
    
    print("How many different species you will run PR on (put an integer number): ")
    N_species = input()
    
    d = {}
    for i in range(int(N_species)):
        print(f"Enter the Atom label of the species number {i+1}")
        d["atom_label_{0}".format(i+1)] = input() 

    main()

